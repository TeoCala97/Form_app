from copyreg import dispatch_table
from dis import dis
from urllib import response
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from Form.forms import Formulario, Provisiones
from functions.functions import Proyecto
from django.views.generic.edit import FormView


#%% Formulario Campañas
class FormView(FormView):
    template_name = 'Form/form.html'
    form_class = Formulario
    success_url = reverse_lazy('campaña')

    def post(self,request,*args,**kwargs):
        formulario = Formulario()
        if request.method == 'POST':
            formulario = Formulario(data=request.POST)
            if formulario.is_valid():
                print(request.POST)
                formulario.save()
                formu = dict(request.POST)
                print(formu)
                # camp = Proyecto(formu)
                # camp.connect()
                # salida = camp.call_proc()
                # if salida.empty:
                #     print("No hay datos")
                #     response = "No hay datos"
                # else:
                #     camp.Update_Json()
                #     print(">>>>> ok Update json <<<<<")
                #     camp.Publisher_topic()
                #     print(">>>>> ok Publisher_topic <<<<<")
            return render(request,'Form/camp.html')
            # return reverse_lazy('campaña')

    def form_valid(self, form):
        return super().form_valid(form)

#%%Formulario Big Query
class QueryView(FormView):
    template_name = 'Form/query.html' # enlaza ek html a la clase
    form_class = Provisiones # llama el formulario dentro de la clase vista template

    def post(self,request,*arg,**kwargs): # se crea un metodo POST generar la consulta al darle inseertar
        form = Provisiones() # se inicializa el formulario
        # client = bigquery.Client(project='sod-co-bi-sandbox') # proyecto de GCP
        if request.method == 'POST': # ingresa el metodo a ejecutar al presionar el submit
            form = Provisiones(data=request.POST) # inicializa los datos en el modleo db
            if form.is_valid(): # si hay datos
                form.save() # se guardan en la tabla de DB
            #     formu = dict(request.POST) # se convierte los datos a diccionario
            #     formu = [{'qname': formu['qname'][0],'select': formu['select'][0],'fecha': formu['fecha'][0]}]  # se organiza los campos 
            #     print(formu)
            #     errors = client.insert_rows_json("Nombre de la tabla", formu)  # nombre de la tabla a insertar y formu( los campos a insertar)
            #     if errors == []:# si esta vacia
            #         print("New rows have been added.")
            #     else:
            #         print("Encountered errors while inserting rows: {}".format(errors))
        return render(request,self.template_name)
    
    def form_valid(self, form):
        return super().form_valid(form)