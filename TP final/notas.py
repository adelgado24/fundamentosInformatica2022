from datetime import date,datetime

#IDEA ANTIGUA

def chequeo(self):
    defectos = 0
    if self.ruedas == True:
        defectos += 1
    if self.frenos == True:
        defectos += 1
    if self.gases == True:
        defectos += 1
    if self.luces == True:
        defectos += 1
    if self.identificacion_vehiculo == True:
        defectos += 1
    if self.suspension == True:
        defectos += 1
    if self.sistema_direccion == True:
        defectos += 1
    if self.seguridad == True:
        defectos += 1
    if self.chasis == True:
        defectos += 1
    if defectos == 0:
        return "SIIIIIII"
    else:
        return 'Volve en unos dias campeon'


fecha = str(date.today().day) +"/"+ str(date.today().month) +"/"+ str(date.today().year + 1)
#print(fecha)

"""date_time_obj = '18/09/19'

date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y')
fecha_final = datetime.strptime(date_time_obj, '%d-%m-%y')

print ("The date is", date_time_obj)"""

date_str = '10/27/2020'

dto = datetime.strptime(date_str, '%m/%d/%Y').date()
print(type(dto))
print(dto)