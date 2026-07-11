from django.core.management import BaseCommand
from app.kuma.models import Producto, Categoria
import datetime

class Command(BaseCommand):

    help = "Crea productos y categorias"

    def handle(self, *args, **kwargs):
        categorias = [
            {"categoria_id": 1, "nombre": "Perro"},
            {"categoria_id": 2, "nombre": "Gato"},
            {"categoria_id": 3, "nombre": "Todos"},
            {"categoria_id": 4, "nombre": "Bandanas"},
            {"categoria_id": 5, "nombre": "Correas"},
            {"categoria_id": 6, "nombre": "Colgantes"},
            {"categoria_id": 7, "nombre": "Juguetes"},
            {"categoria_id": 8, "nombre": "Comida"}
        ]

        for data in categorias:
            Categoria.objects.get_or_create(categoria_id = data["categoria_id"], defaults={"nombre": data["nombre"]})
        
        self.stdout.write(self.style.SUCCESS("Categorias procesadas..."))

        productos = [
            {"sku": 1, "nombre": "Acana", "descripcion": "Comida para perros de la marca Acana", "stock": 24, "precio": 5000, "fecha_vencimiento": "13/03/2028", "categoria_id": 8, "imagen_url": "imagenesProductos/Acana.webp"},
            {"sku": 2, "nombre": "Diamond natural", "descripcion": "Comida para perros de la marca Diamond natural", "stock": 50, "precio": 10000, "fecha_vencimiento": "13/04/2028", "categoria_id": 8, "imagen_url": "imagenesProductos/diamond-natural-adult-small-breed.webp"},
            {"sku": 3, "nombre": "Prestige", "descripcion": "Comida para perros marca Prestige", "stock": 45, "precio": 20000, "fecha_vencimiento": "25/11/2029", "categoria_id": 8, "imagen_url": "imagenesProductos/Prestige.webp"},
            {"sku": 4, "nombre": "Bandana Escocesa", "descripcion": "Bandana para mascotas con patron Escoces", "stock": 24, "precio": 5000, "categoria_id": 4, "imagen_url": "imagenesProductos/bandanaescocesa_300x.webp"},
            {"sku": 5, "nombre": "Bandana Playera", "descripcion": "Bandana con diseño playero", "stock": 15, "precio": 7000, "categoria_id": 4, "imagen_url": "imagenesProductos/bandanaplayera.avif"},
            {"sku": 6, "nombre": "Bandana Popcorn", "descripcion": "Bandana con divertido diseño de PopCorn", "stock": 35, "precio": 2500, "categoria_id": 4, "imagen_url": "imagenesProductos/popcorn_bandana.avif"},
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
            
            defaults_producto = {
                "nombre": data["nombre"],
                "descripcion": data["descripcion"],
                "stock": data["stock"],
                "precio": data["precio"],
                "categoria_id": categoria_obj, # Aquí pasamos la relación al objeto
                "imagen_url": data["imagen_url"]       # Ajusta 'imagen' según el nombre exacto en tu modelo Producto
            }

            if fecha_venc:
                defaults_producto["fecha_vencimiento"] = fecha_venc

            Producto.objects.get_or_create(sku = data["sku"], defaults=defaults_producto)
        
        self.stdout.write(self.style.SUCCESS("Datos base creados"))