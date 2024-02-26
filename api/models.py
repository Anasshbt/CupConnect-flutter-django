from django.db import models


# lets creat a json to return data = ['name','capacity','city','country','desc','cost','picturesx7']

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

class stadiums(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    desc = models.TextField()
    cost = models.IntegerField()
    picture = models.JSONField()
    map = models.CharField(max_length=300)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)

class Hotel(models.Model):
    """
    Hotels near stadiums
    """
    name = models.CharField(max_length=50)
    properties = models.TextField()
    min_price = models.IntegerField(null=True)
    max_price = models.IntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    review = models.FloatField(null=True)
    image = models.TextField(null=True)
    map = models.TextField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    hotel_id = models.IntegerField(null=True) # Booking.com Id
    stad = models.ForeignKey(stadiums, on_delete=models.CASCADE)



    


class user(models.Model):
    username = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=1)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
