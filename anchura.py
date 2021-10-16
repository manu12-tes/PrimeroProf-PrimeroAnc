#primero en anchura
cola_ciudades=[] #cola donde se guardara nuestro recoorrido
origen='Salina Cruz'
final='Reynosa'
def generaHijos(N): #dependiendo de N se generar una lista de hijos 
  ListaCiudades=[]
  if N=='Salina Cruz':
    ListaCiudades.append('Huatulco')
    ListaCiudades.append('Tehuantepec')
  if N=='Tehuantepec':
    ListaCiudades.append('Oaxaca')
    ListaCiudades.append('Juchitan')
    ListaCiudades.append('Salina Cruz')
  if N=='Juchitan':
    ListaCiudades.append('Ixtepec')
    ListaCiudades.append('Tonala')
    ListaCiudades.append('Tehuantepec')
    ListaCiudades.append('Acayucan')
  if N=='Ixtepec':
    ListaCiudades.append('Ixtaltepec')
    ListaCiudades.append('Juchitan')
  if N=='Tonala':
    ListaCiudades.append('Pijijiapan')
    ListaCiudades.append('Tuxtla Gutierrez')
    ListaCiudades.append('Juchitan')
  if N=='Pijijiapan':
    ListaCiudades.append('Huixtla')
    ListaCiudades.append('Tonala')
  if N=='Huixtla':
    ListaCiudades.append('Tapachula')
    ListaCiudades.append('Pijijiapan')
  if N=='Tuxtla Gutierrez':
    ListaCiudades.append('Villahermosa')
    ListaCiudades.append('Tonala')
  if N=='Comitan':
    ListaCiudades.append('San Cristobal')
  if N=='San Cristobal':
    ListaCiudades.append('Ocosingo')
    ListaCiudades.append('Comitan')
  if N=='Ocosingo':
    ListaCiudades.append('Palenque')
    ListaCiudades.append('San Cristobal')
  if N=='Palenque':
    ListaCiudades.append('Villahermosa')
    ListaCiudades.append('Ocosingo')
  if N=='Huatulco':
    ListaCiudades.append('Puerto Escondido')
    ListaCiudades.append('Salina Cruz')
  if N=='Oaxaca':
    ListaCiudades.append('Puebla')
    ListaCiudades.append('Tehuantepec')
  if N=='Villahermosa':
    ListaCiudades.append('Cardenas')
    ListaCiudades.append('Ciudad del Carmen')
    ListaCiudades.append('Tuxtla Gutierrez')
    ListaCiudades.append('Palenque')
  if N=='Ciudad del Carmen':
    ListaCiudades.append('Campeche')
    ListaCiudades.append('Villahermosa')
  if N=='Campeche':
    ListaCiudades.append('Merida')
    ListaCiudades.append('Chetumal')
    ListaCiudades.append('Ciudad del Carmen')
  if N=='Merida':
    ListaCiudades.append('Cancun')
    ListaCiudades.append('Campeche')
  if N=='Cancun':
    ListaCiudades.append('Playa del Carmen')
    ListaCiudades.append('Merida')
  if N=='Playa del Carmen':
    ListaCiudades.append('Chetumal')
    ListaCiudades.append('Cancun')
  if N=='Cardenas':
    ListaCiudades.append('Coatzacoalcos')
    ListaCiudades.append('Villahermosa')
  if N=='Coatzacoalcos':
    ListaCiudades.append('Minatitlan')
    ListaCiudades.append('Cardenas')
  if N=='Minatitlan':
    ListaCiudades.append('Acayucan')
    ListaCiudades.append('Coatzacoalcos')
  if N=='Acayucan':
    ListaCiudades.append('Cordoba')
    ListaCiudades.append('Juchitan')
    ListaCiudades.append('Veracruz')
    ListaCiudades.append('Minatitlan')
  if N=='Cordoba':
    ListaCiudades.append('Orizaba')
    ListaCiudades.append('Acayucan')
  if N=='Orizaba':
    ListaCiudades.append('Puebla')
    ListaCiudades.append('Cordoba')
  if N=='Puebla':
    ListaCiudades.append('Ciudad de Mexico')
    ListaCiudades.append('Orizaba')
  if N=='Veracruz':
    ListaCiudades.append('Xalapa')
    ListaCiudades.append('Poza Rica')
    ListaCiudades.append('Acayucan')
  if N=='Poza Rica':
    ListaCiudades.append('Tuxpan')
    ListaCiudades.append('Veracruz')
  if N=='Tuxpan':
    ListaCiudades.append('Tampico')
    ListaCiudades.append('Poza Rica')
  if N=='Tampico':
    ListaCiudades.append('Matamoros')
    ListaCiudades.append('Tuxpan')
  if N=='Matamoros':
    ListaCiudades.append('Reynosa')
    ListaCiudades.append('Tampico')
  if N=='Ixtaltepec':
    ListaCiudades.append('Ixtepec')
  if N=='Tapachula':
    ListaCiudades.append('Huixtla')
  if N=='Puerto Escondido':
    ListaCiudades.append('Huatulco')
  if N=='Chetumal':
    ListaCiudades.append('Playa del Carmen')
    ListaCiudades.append('Campeche')
  if N=='Ciudad de Mexico':
    ListaCiudades.append('Puebla')
  if N=='Xalapa':
    ListaCiudades.append('Veracruz')
  if N=='Reynosa':
    ListaCiudades.append('Matamoros')
  return ListaCiudades


def busquedaAmplitud(N,M):
  cola_ciudades.append(N)
  actual=N
  while actual!=M and len(cola_ciudades)!=0:
    cola_ciudades.pop(0)
    hijos=generaHijos(actual)
    for nodo in hijos:
      cola_ciudades.append(nodo)
    actual=cola_ciudades[0]
  return cola_ciudades

busquedaAmplitud(origen,final)
cola_ciudades