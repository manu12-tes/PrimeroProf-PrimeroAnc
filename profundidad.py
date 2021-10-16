import sys as sys
pila_ciudades=[] #pila donde se guardar el recorrido
origen='Salina Cruz' #ciudad de orig
final='Reynosa' #ciudad destino
profundidad_maxima=5 #pprofundidad maxima
sys.setrecursionlimit(10000000)
def busqueda_profundidad(N,M,prof):
  pila_ciudades.append(N)
  if N==M:
    return True
  else:
    if prof<profundidad_maxima:
      if N=='Salina Cruz':
        if busqueda_profundidad('Huatulco',M,prof+1):
          return True
        if busqueda_profundidad('Tehuantepec',M,prof+1):
          return True
      if N=='Tehuantepec':
        if busqueda_profundidad('Oaxaca',M,prof+1):
          return True
        if busqueda_profundidad('Juchitan',M,prof+1):
          return True
        if busqueda_profundidad('Salina Cruz',M,prof+1):
          return True
      if N=='Juchitan':
        if busqueda_profundidad('Ixtepec',M,prof+1):
          return True
        if busqueda_profundidad('Tonala',M,prof+1):
          return True
        if busqueda_profundidad('Tehuantepec',M,prof+1):
          return True
        if busqueda_profundidad('Acayucan',M,prof+1):
          return True
      if N=='Ixtepec':
        if busqueda_profundidad('Ixtaltepec',M,prof+1):
          return True
        if busqueda_profundidad('Juchitan',M,prof+1):
          return True
      if N=='Tonala':
        if busqueda_profundidad('Pijijiapan',M,prof+1):
          return True
        if busqueda_profundidad('Tuxtla Gutierrez',M,prof+1):
          return True
        if busqueda_profundidad('Juchitan',M,prof+1):
          return True
      if N=='Pijijiapan':
        if busqueda_profundidad('Huixtla',M,prof+1):
          return True
        if busqueda_profundidad('Tonala',M,prof+1):
          return True
      if N=='Huixtla':
        if busqueda_profundidad('Tapachula',M,prof+1):
          return True
        if busqueda_profundidad('Pijijiapan',M,prof+1):
          return True
      if N=='Tuxtla Gutierrez':
        if busqueda_profundidad('Villahermosa',M,prof+1):
          return True
        if busqueda_profundidad('Tonala',M,prof+1):
          return True
      if N=='Comitan':
        if busqueda_profundidad('San Cristobal',M,prof+1):
          return True
      if N=='San Cristobal':
        if busqueda_profundidad('Ocosingo',M,prof+1):
          return True
        if busqueda_profundidad('Comitan',M,prof+1):
          return True
      if N=='Ocosingo':
        if busqueda_profundidad('Palenque',M,prof+1):
          return True
        if busqueda_profundidad('San Cristobal',M,prof+1):
          return True
      if N=='Palenque':
        if busqueda_profundidad('Villahermosa',M,prof+1):
          return True
        if busqueda_profundidad('Ocosingo',M,prof+1):
          return True
      if N=='Huatulco':
        if busqueda_profundidad('Puerto Escondido',M,prof+1):
          return True
        if busqueda_profundidad('Salina Cruz',M,prof+1):
          return True
      if N=='Oaxaca':
        if busqueda_profundidad('Puebla',M,prof+1):
          return True
        if busqueda_profundidad('Tehuantepec',M,prof+1):
          return True
      if N=='Villahermosa':
        if busqueda_profundidad('Cardenas',M,prof+1):
          return True
        if busqueda_profundidad('Ciudad del Carmen',M,prof+1):
          return True
        if busqueda_profundidad('Tuxtla Gutierrez',M,prof+1):
          return True
        if busqueda_profundidad('Palenque',M,prof+1):
          return True
      if N=='Ciudad del Carmen':
        if busqueda_profundidad('Campeche',M,prof+1):
          return True
        if busqueda_profundidad('Villahermosa',M,prof+1):
          return True
      if N=='Campeche':
        if busqueda_profundidad('Merida',M,prof+1):
          return True
        if busqueda_profundidad('Chetumal',M,prof+1):
          return True
        if busqueda_profundidad('Ciudad del Carmen',M,prof+1):
          return True
      if N=='Merida':
        if busqueda_profundidad('Cancun',M,prof+1):
          return True
        if busqueda_profundidad('Campeche',M,prof+1):
          return True
      if N=='Cancun':
        if busqueda_profundidad('Playa del Carmen',M,prof+1):
          return True
        if busqueda_profundidad('Merida',M,prof+1):
          return True
      if N=='Playa del Carmen':
        if busqueda_profundidad('Chetumal',M,prof+1):
          return True
        if busqueda_profundidad('Cancun',M,prof+1):
          return True
      if N=='Cardenas':
        if busqueda_profundidad('Coatzacoalcos',M,prof+1):
          return True
        if busqueda_profundidad('Villahermosa',M,prof+1):
          return True
      if N=='Coatzacoalcos':
        if busqueda_profundidad('Minatitlan',M,prof+1):
          return True
        if busqueda_profundidad('Cardenas',M,prof+1):
          return True
      if N=='Minatitlan':
        if busqueda_profundidad('Acayucan',M,prof+1):
          return True
        if busqueda_profundidad('Coatzacoalcos',M,prof+1):
          return True
      if N=='Acayucan':
        if busqueda_profundidad('Cordoba',M,prof+1):
          return True
        if busqueda_profundidad('Juchitan',M,prof+1):
          return True
        if busqueda_profundidad('Veracruz',M,prof+1):
          return True
        if busqueda_profundidad('Minatitlan',M,prof+1):
          return True
      if N=='Cordoba':
        if busqueda_profundidad('Orizaba',M,prof+1):
          return True
        if busqueda_profundidad('Acayucan',M,prof+1):
          return True
      if N=='Orizaba':
        if busqueda_profundidad('Puebla',M,prof+1):
          return True
        if busqueda_profundidad('Cordoba',M,prof+1):
          return True
      if N=='Puebla':
        if busqueda_profundidad('Ciudad de Mexico',M,prof+1):
          return True
        if busqueda_profundidad('Orizaba',M,prof+1):
          return True
      if N=='Veracruz':
        if busqueda_profundidad('Xalapa',M,prof+1):
          return True
        if busqueda_profundidad('Poza Rica',M,prof+1):
          return True
        if busqueda_profundidad('Acayucan',M,prof+1):
          return True
    if N=='Poza Rica':
      if busqueda_profundidad('Tuxpan',M,prof+1):
        return True
      if busqueda_profundidad('Veracruz',M,prof+1):
        return True
    if N=='Tuxpan':
      if busqueda_profundidad('Tampico',M,prof+1):
        return True
      if busqueda_profundidad('Poza Rica',M,prof+1):
        return True
    if N=='Tampico':
      if busqueda_profundidad('Matamoros',M,prof+1):
        return True
      if busqueda_profundidad('Tuxpan',M,prof+1):
        return True
    if N=='Matamoros':
      if busqueda_profundidad('Reynosa',M,prof+1):
        return True
      if busqueda_profundidad('Tampico',M,prof+1):
        return True
    if N=='Ixtaltepec':
      if busqueda_profundidad('Ixtepec',M,prof+1):
        return True
    if N=='Tapachula':
      if busqueda_profundidad('Huixtla',M,prof+1):
        return True
    if N=='Puerto Escondido':
      if busqueda_profundidad('Huatulco',M,prof+1):
        return True
    if N=='Chetumal':
      if busqueda_profundidad('Playa del Carmen',M,prof+1):
        return True
      if busqueda_profundidad('Campeche',M,prof+1):
        return True
    if N=='Ciudad de Mexico':
      if busqueda_profundidad('Puebla',M,prof+1):
        return True
    if N=='Xalapa':
      if busqueda_profundidad('Veracruz',M,prof+1):
        return True
    if N=='Reynosa':
      if busqueda_profundidad('Matamoros',M,prof+1):
        return True
  pila_ciudades.pop()
  return False

print(busqueda_profundidad(origen,final,0))
for ciudad in pila_ciudades:
  print(ciudad) 