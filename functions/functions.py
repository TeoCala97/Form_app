from google.cloud import pubsub_v1
from google.cloud import bigquery
from google.cloud import storage
from google.oauth2 import service_account
import time 
import json

import json
from poplib import CR
from google.cloud import pubsub_v1
from google.cloud import bigquery
from google.cloud import storage
from google.oauth2 import service_account
from google.oauth2 import credentials
from soditools import soditools as u
import pandas as pd
from datetime import date,datetime
from dateutil.relativedelta import relativedelta


class Credenciales:

    def __init__(self):
        self.dic = {'SOFT':'t_hrd_sllng_soft',
            'HARD':'t_hrd_sllng_hard',
            'ACABADOS':'t_hrd_sllng_acab',
            'MIX':'T_HRD_SLLNG_MARKPLC',
            'ONLINE':'T_CLI_ONLI'
            }

        self.nombre_proyecto = "sod-co-bi-sandbox"
        self.data_set = "test_camp_os_app"
        # self.data_set = "trf_sod_co_bi_sod_prd"
        self.data_set_seg_hist = "BI"
        self.table_hist_camp = 'tbl_log_hist_oneshot'
        self.table_seg_hist = 'tbl_clientes_segmento_hist_co'
        self.proceso_id = 'HRD_SLLG'
        self.proc_alm = 'sp_one_shot_audiencia_sod_sku'
        self.file_Json = "cfg_sp_one_shot_audiencia_sod_sku.json"
        self.bucket1 = 'dm_sod_conf_co'
        self.bucket2 = 'sod-co-bi-sandbox-campanhas'
        fecha_actual = date.today()
        if fecha_actual.day <=10:
            fecha_periodo = date.today() - relativedelta(months=+2)
            self.periodo = int(fecha_periodo.strftime('%Y%m'))
        else:
            fecha_periodo = date.today() - relativedelta(months=+1)
            self.periodo = int(fecha_periodo.strftime('%Y%m'))
        


class Proyecto(Credenciales):

    def __init__(self,datos_campanha):
        super().__init__()
        self.canal = datos_campanha["Canal"][0]
        self.tipo_usuario = datos_campanha["Tipo_usuario"][0]
        self.marca = datos_campanha["Marca"][0]
        self.prioridad = int(datos_campanha["Prioridad"][0])
        self.name_camp =  datos_campanha["Nombre_campanha"][0]
        self.fecha_envio = datos_campanha["Fecha_envio"][0]
        self.Email = datos_campanha["Email"][0]
        self.Camp = datos_campanha["Valor_Campo"][0]
        self.N_campo = datos_campanha["Nombre_campo"][0]    
        self.Table_name = datos_campanha["Table_name"][0]
        
              

    def connect(self):
        try:
            self.client = bigquery.Client(project=self.nombre_proyecto)
            self.client_storage = storage.Client(project=self.nombre_proyecto)
            self.bucket1 = self.client_storage.get_bucket(self.bucket1)
            self.bucket2 = self.client_storage.get_bucket(self.bucket2)
            print("Conexión Activa")
        except:
            print("No sé logró conectar")
        
    
    def __normalize(self,_str):
        replacements = (
            ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("ñ", "n"),   
            ("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"), ("Ú", "U"), ("Ñ", "N"),
            (" -", ""), (" ", "_"), ("-", "")
        ) 
        for a, b in replacements:
            _str = _str.replace(a, b)
        return _str

    def __name_table(self):
        fecha_md = self.__normalize(self.fecha_envio)
        fecha_md = fecha_md[4:]
        name_table = f"{self.canal}_p{self.prioridad}_{fecha_md}"     
        if self.tipo_usuario == "":
            self.ruta_table = f"`{self.Table_name}`"
        else:
            self.ruta_table = f"`{self.nombre_proyecto}.{self.data_set}.{name_table}`"
        return self.ruta_table

    def __create_table_camp(self):
        if self.marca== "HC":
            perfil = 'HOGAR'
        else: 
            perfil = 'PROFESIONAL'

        if self.tipo_usuario == 'TODOS':
            filtro = ""
        else:
            filtro = f"INNER JOIN `{self.nombre_proyecto}.{self.data_set}.{self.dic[self.tipo_usuario]}` A ON A.NO_CEDULA = B.NO_CEDULA"
        consulta = f"""create or replace table {self.ruta_table}
                OPTIONS(expiration_timestamp=TIMESTAMP_ADD(current_timestamp(), INTERVAL 1 DAY))
                as
                SELECT B.NO_CEDULA, B.PERIODO  
                from `{self.nombre_proyecto}.{self.data_set_seg_hist}.{self.table_seg_hist}` B 
                INNER JOIN `sod-co-bi-sandbox.svw_sod_cp_sod_raw_dtgv_prd.vw_mv_optin_cliente_co` O ON B.NO_CEDULA = O.numero_documento 
                {filtro}              
                where B.perfil = '{perfil}'
                and B.periodo = {self.periodo}"""
        print(f"Consulta {consulta}.")
        print(self.ruta_table)
        u.query(consulta)
        ##return (u.query(f"SELECT COUNT(*) FROM {ruta_table}")).f0_[0]


    

    def call_proc(self):

        if self.tipo_usuario != "":
            print(">>>>> crear tabla <<<<<")
            self.__name_table()
            self.__create_table_camp() 
            print(">>>>> crear tabla: ok <<<<<")
            
        print('>>>>> '+'Nombre tabla: '+self.ruta_table+' <<<<<')
        
        print(f""" CALL `{self.nombre_proyecto}.{self.data_set}.{self.proc_alm}`
                ('{self.fecha_envio}','{self.ruta_table}','{self.name_camp}','{self.prioridad}','{self.canal.upper()}','{self.marca}', {self.periodo}); """)
        
        
        
        u.query(f"""  CALL `{self.nombre_proyecto}.{self.data_set}.{self.proc_alm}`
                ('{self.fecha_envio}','{self.ruta_table}','{self.name_camp}','{self.prioridad}','{self.canal.upper()}','{self.marca}', {self.periodo}); """)
        
        id_camp = (u.query(f"""SELECT max(campaign_id) 
                            FROM `{self.nombre_proyecto}.{self.data_set}.{self.table_hist_camp}` where PARTITIONTIME = "{self.fecha_envio}";
                            """)).f0_[0]
        query = f""" SELECT
                    campaign_id AS Campanha_id,
                    nombre_campania AS Nombre_campania,
                    COUNT(*)N_registros
                    FROM
                    `sod-co-bi-sandbox.test_camp_os_app.tbl_log_hist_oneshot`
                    WHERE
                    PARTITIONTIME = "{self.fecha_envio}"--Parametro Fecha Envio
                    AND campaign_id = "{id_camp}" --Param Campaña
                    AND flag_grupocontrol ="GT:GRUPOTRATAMIENTO"
                    GROUP BY
                    campaign_id,
                    nombre_campania;
                    """
        
        salida = (u.query(query))
        return salida
    
    def Publisher_topic(self):
        publisher = pubsub_v1.PublisherClient()
        project_id = self.nombre_proyectoa
        #topic_id = "ps_dm_daily_load"
        #topic_id = "crm_symphoy_daily_load"
        # The `topic_path` method creates a fully qualified identifier
        # in the form `projects/{project_id}/topics/{topic_id}`    
        if self.canal == "EMAIL":
            topic_id = "ps_dm_daily_load"
            message='{"params": {"query": "CALL `sod-co-bi-sandbox.trf_sod_co_bi_sod_prd.sp_one_shot_audiencia_sod_sku`();"}}'
        else : #SMS
            topic_id = "ps_dm_sms_daily_load"
            message='{"params": {"query": "CALL `sod-co-bi-sandbox.trf_sod_co_bi_sod_prd.sp_one_shot_sms_audiencia`();"}}'
        
        topic_path = publisher.topic_path(project_id, topic_id)    
        data = message
        data = data.encode('utf-8')
            # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data)
        print(future.result())
        print(f"Published messages to {topic_path}.")

    def Update_Json(self):

        self.fecha_envio = self.fecha_envio.replace("-","")
        
        self.name_camp = self.__normalize(self.name_camp)
        
        x = datetime.now()
        x= x.strftime("%Y%m%d")
        nombre_archivocsv = self.fecha_envio + "_" + self.name_camp + "-" + x +".csv"
        print(f"Nombre Archivo: {nombre_archivocsv}")
        
        #Nombre_campania = Nombre_campania.replace(" -","")
        #Nombre_campania = Nombre_campania.replace(" ","_")

        if self.canal == "EMAIL":
            _Canal = "Email"
            _Campo = "email"

            with open(self.file_Json,"r") as j:
                datos=json.load(j)
                
            for index in datos:            
                if index == "LdgSftpAccount":
                    if self.canal == "HC":
                        datos[index] = "6235045"    
                    else:
                        datos[index] = "6235046"
                if index == "LdgYamlDecryptCol":
                    datos[index] = ["Cedula",""+_Canal+""]            
                    #datos[index] = ["Cedula"]
                if index == "LdgSendableAtt":
                    datos[index] = ""+_Canal+""            
                if index == "LdgMailAlerts":
                    datos[index] = self.Email
                if index == "LdgFileNamesCsv":
                    datos[index] = [self.fecha_envio + "_" + self.name_camp ]
                if index == "LdgFileNamesYml":
                    datos[index] = [self.fecha_envio + "_" + self.name_camp ]
                if index == "SrcBQueryBase":
                    if self.Camp == "None":
                        datos[index] = "SELECT tt1.no_cedula as Cedula, tt1."+_Campo+" as "+_Canal+" FROM `{0}.{1}.{2}` tt1 WHERE tt1.PARTITIONTIME = TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(),DAY) AND flag_grupocontrol = 'GT:GRUPOTRATAMIENTO';"    
                    else:
                        datos[index] = "SELECT tt1.no_cedula as Cedula, tt1."+_Campo+" as "+_Canal+", '"+self.Camp+"' "+self.name_camp +" FROM `{0}.{1}.{2}` tt1 WHERE tt1.PARTITIONTIME = TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(),DAY) AND flag_grupocontrol = 'GT:GRUPOTRATAMIENTO';"  
        
            with open(self.file_Json,'w') as j:
                json.dump(datos,j)    

            blob = self.bucket1.blob(self.file_Json)
            blob.upload_from_filename(self.file_Json)        
        else:
            file_Json = "cfg_sp_one_shot_sms_audiencia.json"
            with open(file_Json,"r") as j:
                datos=json.load(j)        
            for index in datos:
                if index == "LdgFileNamesCsv":
                    datos[index] = [self.fecha_envio + "_" + self.name_camp]
                if index == "LdgFileNamesYml":
                    datos[index] = [self.fecha_envio + "_" + self.name_camp]
            with open(file_Json,'w') as j:
                json.dump(datos,j)    

            blob = self.bucket1.blob(file_Json)
            blob.upload_from_filename(file_Json)
            #nombre archivo

    def get_form(self):
        blob_get = self.bucket2.get_blob('post_data_test.json')
        File= blob_get.download_as_string() 
        File = json.loads(File)
        return File

    def update_bucket(self,datos):    
    
        file_Json = "post_data_test.json"
        
        
        with open(file_Json,"r") as j:
            datosjson=json.load(j)
        
        if datos.empty:
            datosjson["Campanha_id"] = "None"
            datosjson["Nombre_campania"] = "None"
            datosjson["N_registros"] = int(0)
        else:
            datosjson["Campanha_id"] = datos["Campanha_id"][0]
            datosjson["Nombre_campania"] = datos["Nombre_campania"][0]
            datosjson["N_registros"] = int(datos["N_registros"][0])

        with open(file_Json,'w') as j:
            json.dump(datosjson,j)    
        
        blob = self.bucket2.blob(file_Json)
        blob.upload_from_filename(file_Json)


    


