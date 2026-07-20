from django.core.management import BaseCommand
from app.kuma.models import Producto, Categoria
from django.core.files import File 
from django.conf import settings
import datetime
import os

import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name = "gcpljpzi",
    api_key = os.environ.get("API_KEY"),
    api_secret = os.environ.get("API_SECRET"),
    secure = True
)

class Command(BaseCommand):

    help = "Crea productos y categorias"

    def handle(self, *args, **kwargs):
        categorias = [
            {"categoria_id": 1, "nombre": "Perro", "descripcion": "Productos para tu amigo canino"},
            {"categoria_id": 2, "nombre": "Gato", "descripcion": "Productos para tu amigo felino"},
            {"categoria_id": 3, "nombre": "Todos", "descripcion": "Todo lo que buscas está aquí"},
            {"categoria_id": 4, "nombre": "Bandanas", "descripcion": "¡Bandanas de todo tipo!"},
            {"categoria_id": 5, "nombre": "Correas", "descripcion": "Correas para todo proposito"},
            {"categoria_id": 6, "nombre": "Colgantes", "descripcion": "Colgantes e identificadores para toda necesidad"},
            {"categoria_id": 7, "nombre": "Juguetes", "descripcion": "Variedad de juguetes para que tu mascota no se aburra"},
            {"categoria_id": 8, "nombre": "Comida", "descripcion": "Comidas de todo tipo para las necesidades de tus mascotas"}
        ]

        for data in categorias:
            Categoria.objects.update_or_create(categoria_id = data["categoria_id"], defaults={"nombre": data["nombre"], "descripcion": data["descripcion"]})
        
        self.stdout.write(self.style.SUCCESS("Categorias procesadas..."))

        productos = [
            {"sku": 1, "nombre": "Acana", "descripcion": "Comida para perros de la marca Acana", "stock": 24, "precio": 5000, "fecha_vencimiento": "13/03/2028", "categoria_id": 8, "imagen_url": "imagenesProductos/Acana.webp"},
            {"sku": 2, "nombre": "Diamond natural", "descripcion": "Comida para perros de la marca Diamond natural", "stock": 50, "precio": 10000, "fecha_vencimiento": "13/04/2028", "categoria_id": 8, "imagen_url": "imagenesProductos/diamond-naturals-adult-small-breed.webp"},
            {"sku": 3, "nombre": "Prestige", "descripcion": "Comida para perros marca Prestige", "stock": 45, "precio": 20000, "fecha_vencimiento": "25/11/2029", "categoria_id": 8, "imagen_url": "imagenesProductos/Prestige.webp"},
            {"sku": 4, "nombre": "Bandana Escocesa", "descripcion": "Bandana para mascotas con patron Escoces", "stock": 24, "precio": 5000, "categoria_id": 4, "imagen_url": "imagenesProductos/bandanaescocesa_300x.webp"},
            {"sku": 5, "nombre": "Bandana Playera", "descripcion": "Bandana con diseño playero", "stock": 15, "precio": 7000, "categoria_id": 4, "imagen_url": "imagenesProductos/bandanaplayera.avif"},
            {"sku": 6, "nombre": "Bandana Popcorn", "descripcion": "Bandana con divertido diseño de PopCorn", "stock": 35, "precio": 2500, "categoria_id": 4, "imagen_url": "imagenesProductos/popcorn-bandana.avif"},
            {"sku": 7, "nombre": "Peluche", "descripcion": "Peluche felpudo para jugar", "stock": 30, "precio": 7500, "categoria_id": 7, "imagen_url": "imagenesProductos/Peluche_de_animal.jpg"},
            {"sku": 8, "nombre": "Pantufla", "descripcion": "Peluche con forma de pantufla para aquellas mascotas que adoran destruirlas", "stock": 24, "precio": 5000, "categoria_id": 7, "imagen_url": "imagenesProductos/Peluche_pantufla.jpg"},
            {"sku": 9, "nombre": "Juguete chillon", "descripcion": "Tipico juguete chillon para que tu mascota se entretenga", "stock":15, "precio": 6500, "categoria_id": 7, "imagen_url": "imagenesProductos/Juguete_Chillon.jpg"},
            {"sku": 10, "nombre": "Collar Stranger Things", "descripcion": "Collar con diseño de la famosa serie Stranger Things", "stock": 50, "precio": 15000, "categoria_id": 5, "imagen_url": "imagenesProductos/Collar_stranger_things.jpg"},
            {"sku": 11, "nombre": "Arnes de torso", "descripcion": "Arnes que cubre el torso de tu mascota y asegura un paseo sin ahorcamientos", "stock": 15, "precio": 10000, "categoria_id": 5, "imagen_url": "imagenesProductos/mascan-arnés-cruzado-acolchado.jpg"},
            {"sku": 12, "nombre": "Arnes acolchado", "descripcion": "Arnes con dos puntos de contacto acolchado", "stock": 30, "precio": 5000, "categoria_id": 5, "imagen_url": "imagenesProductos/Arnes_acolchado.jpg"},
            {"sku": 13, "nombre": "Colgante Safety Light", "descripcion": "Colgante con luz y sonido para encontrar a tu mascota en caso de emergencia", "stock": 20, "precio": 20000, "categoria_id": 6, "imagen_url": "imagenesProductos/Colgante_safety_light.jpg"},
            {"sku": 14, "nombre": "Colgante Antipulgas", "descripcion": "Colgante que ayuda a prevenir las pulgas", "stock": 24, "precio": 15000, "categoria_id": 6, "imagen_url": "imagenesProductos/Colgante_Antipulgas_y_garrapatas.png"},
        ]

        
        for data in productos:
            categoria_obj = Categoria.objects.get(categoria_id = data["categoria_id"])

            fecha_venc = None
            if "fecha_vencimiento" in data:
                fecha_venc = datetime.datetime.strptime(data["fecha_vencimiento"], "%d/%m/%Y").date()

            nombre_carpeta_limpio = data["imagen_url"].replace("imagenesProductos/", "ImagenesProductos/")
            ruta_fisica_local = os.path.join(settings.MEDIA_ROOT, nombre_carpeta_limpio)

            if os.path.exists(ruta_fisica_local):
                self.stdout.write(f"Subiendo imagen de {data['nombre']} a Cloudinary...")
                
                resultado_subida = cloudinary.uploader.upload(
                    ruta_fisica_local,
                    public_id = os.path.splitext(os.path.basename(nombre_carpeta_limpio))[0] 
                )
                
                url_en_la_nube = resultado_subida["secure_url"]

                defaults_producto = {
                    "nombre": data["nombre"],
                    "descripcion": data["descripcion"],
                    "stock": data["stock"],
                    "precio": data["precio"],
                    "categoria_id": categoria_obj,
                    "imagen_url": url_en_la_nube 
                }
                if fecha_venc:
                    defaults_producto["fecha_vencimiento"] = fecha_venc

                Producto.objects.update_or_create(sku=data["sku"], defaults=defaults_producto)
                self.stdout.write(self.style.SUCCESS(f"Producto SKU {data['sku']} creado con URL: {url_en_la_nube}"))
            else:
                self.stdout.write(self.style.WARNING(f"No se encontró el archivo local en: {ruta_fisica_local}"))

        self.stdout.write(self.style.SUCCESS("Datos base creados con éxito"))