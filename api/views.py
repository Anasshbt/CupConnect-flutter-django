from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
import base64
from io import BytesIO
from PIL import Image, ImageOps
import json
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .utils import hotels

t = {
    "main": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Ftangier%2Fmain.jpg?alt=media&token=2fc78682-0748-4494-adca-2ecf5e5e0601",
    "s1": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Ftangier%2Fs1.jpg?alt=media&token=fa5d74dc-a14f-4572-a9f7-51d005611b16",
    "s2": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Ftangier%2Fs2.jpg?alt=media&token=ebc6d239-bbde-40b2-b658-2e253dcb7931",
    "s3": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Ftangier%2Fs3.jpg?alt=media&token=a679aacc-0d6a-4ac2-bd60-da09d143b261",
    "s4": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Ftangier%2Fs4.jpg?alt=media&token=3bb2b4fd-ad8c-4b31-afe3-e869ac58e72a",
}
c = {
    "main": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fcasa%2Fmain.jpg?alt=media&token=8ec0d752-cee4-455c-be63-4472af6e9fce",
    "s1": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fcasa%2Fs1.jpg?alt=media&token=301c9208-f684-41d6-8ee9-ddd79178d160",
    "s2": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fcasa%2Fs2.jpg?alt=media&token=85397cc7-5aa2-44f3-8aa3-4623c451d06b",
    "s3": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fcasa%2Fs3.jpg?alt=media&token=c4ea3e64-d2f5-4842-a80f-0d23a97bdde0",
    "s4": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fcasa%2Fs4.jpg?alt=media&token=aff44da0-8055-409a-8bfe-94d91128854c",
}
r = {
    "main": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Frabat%2Fmain.jpeg?alt=media&token=6139a3d9-f4f8-4daf-8dd9-dd5f5a7ea265",
    "s1": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Frabat%2Fs1.jpg?alt=media&token=7b0bacf0-84a1-42b1-bcfe-d793104c94e5",
    "s2": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Frabat%2Fs2.jpg?alt=media&token=4c33efc1-fd23-4b1f-89a5-72f4d43593f4",
    "s3": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Frabat%2Fs3.jpg?alt=media&token=39723de8-40d9-4ed8-9339-8e3c9893b14e",
    "s4": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Frabat%2Fs4.jpg?alt=media&token=962b8175-e881-41cf-a7a8-5021bcc7c2f5",
}
m = {
    "main": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fmarakech%2Fmain.jpg?alt=media&token=a011d92a-f2f2-44e9-8557-411aebc9f5e9",
    "s1": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fmarakech%2Fs1.jpg?alt=media&token=e14f26b6-d22c-4a26-99ff-0bc9865eca1f",
    "s2": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fmarakech%2Fs2.jpg?alt=media&token=2837db45-5cfb-483e-83f2-1bc8ecd4f446",
    "s3": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fmarakech%2Fs3.jpg?alt=media&token=2813c4e8-42b9-4544-89c0-ac7ea43d879c",
    "s4": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fmarakech%2Fs4.avif?alt=media&token=b4119d49-6301-4534-b9b2-1507b8caf1a6",
}
f = {
    "main": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Ffes%2Fmain.jpg?alt=media&token=bb003150-0ad4-4ea9-947f-42ecaead500d",
    "s1": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Ffes%2Fs1.jpg?alt=media&token=702d8bac-f20c-4ac8-865a-afc5a886554c",
    "s2": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Ffes%2Fs2.avif?alt=media&token=a0efdb81-7777-4362-b74d-75077d2bfff7",
    "s3": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Ffes%2Fs3.jpg?alt=media&token=65e71fa9-75e6-458f-83c7-f6d07795c65d",
    "s4": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Ffes%2Fs4.jpg?alt=media&token=5a92d94d-9c32-4018-b4f4-f3d7302e78a0",
}
a = {
    "main": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fagadir%2Fmain.jpg?alt=media&token=959c0346-d22e-4051-b317-6fd6cdb95b28",
    "s1": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fagadir%2Fs1.jpg?alt=media&token=626f992f-01e7-4d8b-8a30-51ba62b40713",
    "s2": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fagadir%2Fs2.jpg?alt=media&token=202d9d73-54cb-4213-b627-e09557106627",
    "s3": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fagadir%2Fs3.jpg?alt=media&token=688d2913-72f1-4641-9f7b-180274bc1dc0",
    "s4": "https://firebasestorage.googleapis.com/v0/b/devjamxcyberops.appspot.com/o/stadiums%2Fagadir%2Fs4.jpg?alt=media&token=afafae9c-2a88-4f32-bc92-679e2e2f5469",
}


s1 = {"name":"Stade Ibn Batouta","capacity":65000,"city":"tangier","country":"morocco","desc":"The newly built stadium in south-western outskirts of Tangier (by the N1 national road) isn't only the city's largest sports facility, but the largest building overall. Construction was marred with delays and lasted almost 9 years in the end. Began in 2002, it wasn't delivered until 2011. And it may still seem look unfinished to some, not without purpose. Both end zones were left single-tiered, but with the footing for an upper tier to be added in the future. Similarly, the east stand already has support structures for its future roof, should funds be allocated to build one.","cost":844,"picture":t,"map":"https://maps.app.goo.gl/aTUaf4hKfcCLAgAF9","longitude": -5.8580531, "latitude": 35.741152}
s1_path=["C:/Users/pp/Desktop/devjam/api/images/tangier/main.jpg","C:/Users/pp/Desktop/devjam/api/images/tangier/s1.jpg","C:/Users/pp/Desktop/devjam/api/images/tangier/s2.jpg","C:/Users/pp/Desktop/devjam/api/images/tangier/s3.jpg","C:/Users/pp/Desktop/devjam/api/images/tangier/s4.jpg"]

s2 = {"name":"Stade Mohamed V","capacity":67000,"city":"Casablanca","country":"morocco","desc":"The stadium first opened in 1955, celebrating a famous French boxer Marcel Serdan. But just one year later, as Morocco became independent from France, the name was changed to Stade D'Honneur (which is used by many to this day). Final name came in 1981, when Sultan Mohammed V became the venue's patron. Initial capacity was set at 30,000, but before 1983 Mediterranean Games the stadium was completely rebuilt to hold even 80,000 people, most of them standing (along were built an indoor hall, natatorium and a secondary stadium around the venue). And despite capacity fell to  67,000 with some sections conversed to seating, no other stadium in Morocco ever saw crowds like this one.","cost":0,"picture":c,"map":"https://maps.app.goo.gl/LR3GMUfkRjhiP8nX6", "latitude": 33.5831602, "longitude": -7.6501012}
s2_path=["C:/Users/pp/Desktop/devjam/api/images/casa/main.jpg","C:/Users/pp/Desktop/devjam/api/images/casa/s1.jpg","C:/Users/pp/Desktop/devjam/api/images/casa/s2.jpg","C:/Users/pp/Desktop/devjam/api/images/casa/s3.jpg","C:/Users/pp/Desktop/devjam/api/images/casa/s4.jpg"]

s3 = {"name":"Moulay Abdellah Stadium","capacity":50000,"city":"Rabat","country":"morocco","desc":"It was built in 1983 and was the home ground of AS FAR. It was used mostly for football matches and it also staged athletics. The stadium had a capacity of 50,000 people. From 2008 until 2023, it has hosted the Meeting International Mohammed VI d'Athlétisme de Rabat. It was a confirmed venue for the 2015 Africa Cup of Nations until Morocco was stripped of its hosting rights. Morocco asked for the Africa Cup of Nations to be postponed because of fear of the Ebola pandemic that was affecting several African countries at the time. The country was then ruled out as a host of the international competition.","cost":0,"picture":r,"map":"https://maps.app.goo.gl/4eXq1ZLe17Q6siYUA", "latitude": 33.9598463, "longitude": -6.8890037}
s3_path=["C:/Users/pp/Desktop/devjam/api/images/rabat/main.jpeg","C:/Users/pp/Desktop/devjam/api/images/rabat/s1.jpg","C:/Users/pp/Desktop/devjam/api/images/rabat/s2.jpg","C:/Users/pp/Desktop/devjam/api/images/rabat/s3.jpg","C:/Users/pp/Desktop/devjam/api/images/rabat/s4.jpg"]

s4 = {"name":"Stade de Marrakech","capacity":45240,"city":"Marrakech","country":"morocco","desc":"Built some 11km from the centre of Marrakech this stadium stands in a rather deserted area. With few landmarks around it seems almost like an ancient fort and that's not a coincidence. The form was supposed to refer to fortifications on one hand and to local architecture in general. That's why massive elements dominate, geometrical forms give it rhythm and the colours are all natural, from white to brown. The vision of Morrocan-Italian design team was criticized however for the resemblance this ground has to Stadio Luigi Ferraris created by the same architects in Italy.","cost":890,"picture":m,"map":"https://maps.app.goo.gl/T37AopaHJXMhFPHC7", "latitude": 31.706055, "longitude": -7.9808083}
s4_path=["C:/Users/pp/Desktop/devjam/api/images/marakech/main.jpg","C:/Users/pp/Desktop/devjam/api/images/marakech/s1.jpg","C:/Users/pp/Desktop/devjam/api/images/marakech/s2.jpg","C:/Users/pp/Desktop/devjam/api/images/marakech/s3.jpg","C:/Users/pp/Desktop/devjam/api/images/marakech/s4.avif"]

s5 = {"name":"Stade Adrar","capacity":45480,"city":"Agadir","country":"morocco","desc":"The competition for design of a new major stadium in Agadir was launched back in the twentieth century, when Morocco was bidding to become the first ever African host of the FIFA World Cup. Already then the Italian-Moroccan consortium of Gregotti and Benkirane were awarded the job. That same design, though upgraded, was submitted as Morocco's bid for the 2010 World Cup, having failed for the 2006 edition. To increase Morocco's chances ground clearing began in 2003. That may have been enough to win some votes and get Morocco to the final vote, but in May 2004 FIFA chose South Africa over Morocco by 14 votes to 10. This effectively ruined the Maghreb country's chances for at least two decades as continental rotation of the World Cup was dropped soon after (in 2007) and bringing it back to Africa became a dim prospect.","cost":860,"picture":a,"map":"https://maps.app.goo.gl/juMDPN1BSyojqkNJ6", "latitude":30.427483, "longitude":-9.54025 }
s5_path=["C:/Users/pp/Desktop/devjam/api/images/agadir/main.jpg","C:/Users/pp/Desktop/devjam/api/images/agadir/s1.jpg","C:/Users/pp/Desktop/devjam/api/images/agadir/s2.jpg","C:/Users/pp/Desktop/devjam/api/images/agadir/s3.jpg","C:/Users/pp/Desktop/devjam/api/images/agadir/s4.jpg"]

s6 = {"name":"Complexe Sportif de Fès","capacity":45000,"city":"Fes","country":"morocco","desc":"According to initial plans, works on the new central stadium for Fez were to start in early 1990s, but groundbreaking was delayed for almost 2 years, starting eventually in 1994. As if this wasn't enough, the delays were growing further as time went by, resulting by the stadium not being ready for the 1997 Cup of Nations, as was planned. It wasn't until 2003 that the construction ended, being expanded in the process by 5,000 additional seats compared to the 1992 design. Still, even after delivery it waited four years to be opened. The free-for-all exhibition game between FAR Rabat and Rachad Bernoussi was played in front of full stands in November 2007.","cost":0,"picture":f,"map":"https://maps.app.goo.gl/SdNbXR3QpWqsjNtd7", "longitude":-5.0410351, "latitude":34.0290527}
s6_path=["C:/Users/pp/Desktop/devjam/api/images/fes/main.jpg","C:/Users/pp/Desktop/devjam/api/images/fes/s1.jpg","C:/Users/pp/Desktop/devjam/api/images/fes/s2.avif","C:/Users/pp/Desktop/devjam/api/images/fes/s3.jpg","C:/Users/pp/Desktop/devjam/api/images/fes/s4.jpg"]

CACHE_TTL = 60 * 15




def migrate():
    all = [(s1,s1_path),(s2,s2_path),(s3,s3_path),(s4,s4_path),(s5,s5_path),(s6,s6_path)]
    for j in all:

        d = {}
        names = ["main","p1","p2","p3","p4"]
        
        
        
        t = stadiums(
                     name = j[0]["name"],
                     capacity = j[0]["capacity"],
                     city = j[0]["city"],
                     country = j[0]["country"],
                     desc = j[0]["desc"],
                     cost = j[0]["cost"],
                     picture = j[0]["picture"],
                     map = j[0]["map"],
                     latitude = j[0]["latitude"],
                     longitude = j[0]["longitude"]
                     )
        t.save()

        try:
            nearby_hotels = hotels.get_nearcoords(t.latitude, t.longitude)
            for h in nearby_hotels:
                print(h)
                h = hotels.get_hotel_info(h)
                hotel = Hotel(
                    name = h["name"],
                    map = h["map"],
                    longitude = h["longitude"],
                    latitude = h["latitude"],
                    properties= h["properties"],
                    min_price = h["min_price"],
                    max_price = h["max_price"],
                    address = h["address"],
                    review = h["review"],
                    image = h["image"],
                    hotel_id = h["hotel_id"],
                    stad = t
                )
    
                hotel.save()
    
            print("[+] Migration complete")
        except Exception as e:
            print(e)
            




def image_to_base64(img):
    image = open(img, "rb")
    b64 = base64.b64encode(image.read()).decode("utf-8")
    return b64


def base64_to_image(b64):
    imagebyte = base64.b64decode(b64)
    image = Image.open(BytesIO(imagebyte))
    rgb_image = image.convert("RGB")
    imaged = ImageOps.invert(rgb_image)
    imaged.save("hello.png")
    return image


def home(request):
    migrate()
    return render(request, "home.html")


class stadiums_view(APIView):
    serializer_class = stadiumsseria

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request):
        out = [
            {
                "id": o.id,
                "name": o.name,
                "capacity": o.capacity,
                "city": o.city,
                "country": o.country,
                "desc": o.desc,
                "cost": o.cost,
                "picture": o.picture,
                "map": o.map,
                "latitude": o.latitude,
                "longitude": o.longitude,
            }
            for o in stadiums.objects.all()
        ]
        return Response(out)


class user_view(APIView):
    serializer_class = userseria

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request):
        out = [
            {
                "id": o.id,
                "username": o.username,
                "email": o.email,
                "password": o.password,
                "gender": o.gender,
                "phone": o.phone,
                "country": o.country,
            }
            for o in user.objects.all()
        ]
        return Response(out)

class hotel_view(APIView):
    serializer_class = hotelseria

    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, stad_id):
        out = [
            {
                "id": o.id,
                "name": o.name,
                "properties": o.properties,
                "min_price": o.min_price,
                "max_price": o.max_price,
                "latitude": o.latitude,
                "longitude": o.longitude,
                "review": o.review,
                "address": o.address,
                "image": o.image,
                "map": o.map,
                "hotel_id": o.hotel_id
            }
            for o in Hotel.objects.filter(stad=stad_id).all()
        ]
        return Response(out)


@api_view(
    [
        "POST",
    ]
)
def create_user(request):
    if request.method == "POST":
        serializer = userseria(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("failed", status=status.HTTP_400_BAD_REQUEST)


@api_view(
    [
        "GET",
    ]
)
def get_user(request, email):
    if request.method == "GET":
        userthis = user.objects.all().filter(email=email)

        try:
            d = {
                "id": userthis[0].id,
                "username": userthis[0].username,
                "email": userthis[0].email,
                "password": userthis[0].password,
                "gender": userthis[0].gender,
                "phone": userthis[0].phone,
                "country": userthis[0].country,
            }
            return Response(d)
        except:
            return Response("user not exist", status=status.HTTP_404_NOT_FOUND)
        # serializer = userseria



def update_user(request,attribute,id,new_value):
   
    userinfo = user.objects.all().filter(id=id)[0] 
    
    if attribute == "username":
        userinfo.username=new_value
        
    if attribute == "phone":
        userinfo.phone = new_value
    if attribute == "password":
        userinfo.password = new_value
    userinfo.save()

    return JsonResponse({"message":"done"})
        
