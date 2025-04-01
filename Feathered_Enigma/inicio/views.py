from django.shortcuts import render, HttpResponse
from firebase_config import db
from django.http import JsonResponse



def principal(request):
  return render(request,'inicio/principal.html')
def historia(request):
    return render(request, "inicio/historia.html")

def personajes(request):
    try:
        # Referencia a la colección "Reseñas"
        personajesCollection = db.collection("Personajes")
        escenariosCollection = db.collection("Escenarios")

        # Obtener todos los documentos y convertir a listas de diccionarios
        personajes = [doc.to_dict() for doc in personajesCollection.stream()]
        escenarios = [doc.to_dict() for doc in escenariosCollection.stream()]
        
        
        return render(request, "inicio/personajes.html", {"personajes": personajes,"escenarios":escenarios})  # Pasar datos al template
    except Exception as e:
        return render(request, 'inicio/personajes.html')

def comentarios(request):
    return render(request, "inicio/comentarios.html")

def resenas(request):
    try:
        # Referencia a la colección "Reseñas"
        resenas_ref = db.collection("Reseñas")
        
        # Obtener todos los documentos
        documentos = resenas_ref.stream()
        
        # Convertir a lista de diccionarios
        resenas = []
        for doc in documentos:
            resena_data = doc.to_dict()
            resena_data["id"] = doc.id  # Opcional: incluir el ID del documento
            resenas.append(resena_data)
        
        return render(request, "inicio/resenas.html", {"resenas": resenas})  # Pasar datos al template
    except Exception as e:
        return render(request, 'inicio/resenas.html')








def obtener_resenas(request):
    try:
        # Referencia a la colección "Reseñas"
        resenas_ref = db.collection("Reseñas")
        
        # Obtener todos los documentos
        documentos = resenas_ref.stream()
        
        # Convertir a lista de diccionarios
        resenas = []
        for doc in documentos:
            resena_data = doc.to_dict()
            resena_data["id"] = doc.id  # Opcional: incluir el ID del documento
            resenas.append(resena_data)
        
        """return JsonResponse({"resenas": resenas}, safe=False)"""""
        return render(request, "resenas.html", {"resenas": resenas})  # Pasar datos al template

    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)