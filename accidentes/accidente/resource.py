
from import_export import resources  
from .models import Accidente, CasoAccidente, TipoAccidente
from personas.models import Personas, TipoVictima
from sitios.models import Lugar

class AccidenteResource(resources.ModelResource):  
   class Meta:  
     model =  Accidente 
class CasoAccidenteResource(resources.ModelResource):  
   class Meta:  
     model =  CasoAccidente 
class TipoAccidenteResource(resources.ModelResource):  
   class Meta:  
     model =  TipoAccidente 
class PersonasResource(resources.ModelResource):  
   class Meta:  
     model =  Personas 
class TipoVictimaResource(resources.ModelResource):  
   class Meta:  
     model =  TipoVictima 
class LugarResource(resources.ModelResource):  
   class Meta:  
     model =  Lugar      
