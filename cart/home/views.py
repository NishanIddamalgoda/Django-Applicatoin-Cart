from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect

from django.contrib.postgres.search import SearchVector
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer

def home(request):
    itemList = []
    item = Item()
    item.id = "1.jpg"
    itemList.append(item)

    item2 = Item()
    item2.id = "2.jpg"
    itemList.append(item2)

    item3 = Item()
    item3.id = "3.jpg"
    itemList.append(item3)

    item4 = Item()
    item4.id = "4.jpg"
    itemList.append(item4)

    item5 = Item()
    item5.id = "5.jpg"
    itemList.append(item5)

    item6 = Item()
    item6.id = "6.jpg"
    itemList.append(item6)

    dbItemList = Item.objects.all()
    dbItemListTop = Item.objects.filter(top_selling=True)
    print(dbItemListTop)

    banner = True

    search_string=""

    return render(request, "home.html", {'itemListlatest': dbItemListTop, 'itemListTopSelling': itemList,'dbItems':dbItemList,'banner':banner,'search_string':search_string})


def register(request):
    return render(request,"register.html")

def registerAccount(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        user.save()
        return redirect('/')
    else:
        return redirect('register')

def login(request):
    return render(request,"login.html")

def loginto(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect("login")
    else:
        return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('/')

def searchITem(request):
    if request.method=='POST':
        your_search_query = request.POST['srch_item']
        dbItemList = Item.objects.annotate(search=SearchVector('item_name', 'descrp')).filter(search=your_search_query)   
        banner : bool = False  
        return render(request, "home.html", {'dbItems':dbItemList,'banner':banner,'search_string':your_search_query})
    
# REST ITEM ACCESS
class itemList(APIView):
    def get(self, request,pk=''):
        if pk=='':
            itemlist = Item.objects.all()
        else:
            itemlist = Item.objects.filter(id=pk)
        seriali = ItemSerializer(itemlist, many=True)
        return Response(seriali.data)

    def post(self,request):    
        serializer = ItemSerializer(data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def put(self,request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            item_obj = Item.objects.get(id = request.data['id'])
            item_obj.item_name = request.data['item_name']
            item_obj.img = request.data['img']
            item_obj.descrp = request.data['descrp']            
            item_obj.price = request.data['price']
            item_obj.top_selling = request.data['top_selling']
            item_obj.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self,request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            Item.objects.filter(id=request.data['id']).delete()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)