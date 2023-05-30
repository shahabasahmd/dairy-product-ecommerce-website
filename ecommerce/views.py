from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product,Customer
from .forms import CustomerForm
from django.views import View
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.models import User, auth






# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")


class CategoryView(View):
    def get(self,request,val):
        products = product.objects.filter(category=val)
        title = product.objects.filter(category=val).values('title')
        return render(request,'category.html',locals() )
    

class CategoryTitle(View):
    def get(self,request,val):
        products = product.objects.filter(title=val)
        title = product.objects.filter(category=products[0].category).values('title')
        return render(request,'category.html',locals() )


class ProductDetail(View):
    def get(self,request,pk):
        products = product.objects.get(pk=pk)
        return render(request,'productdetail.html',locals())


class profileView(View):
   def get(self,request):
      return render(request,'profile.html',locals())

   def post(self,request):
      return render(request,'profile.html',locals())

    
def register(request): 
   if request.method == 'POST' : 
      first_name=request.POST['first_name'] 
      last_name=request.POST['last_name'] 
      username=request.POST['username'] 
      email=request.POST['email'] 
      password1=request.POST['password1'] 
      password2=request.POST['password2'] 
       
      
 
 
      if password1 == password2 : 
         if User.objects.filter(username=username).exists(): 
             messages.info(request,'username is taken') 
             return redirect('register') 
         elif User.objects.filter(email=email).exists()  : 
            messages.info(request,'email is taken') 
            return redirect('register') 
         else:      
            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name) 
            user.save(); 
            print('user created') 
            messages.success(request,"congratulation User Registered Successfully") 
      else: 
         messages.warning(request,'password is not matching  ') 
          
         return redirect('register') 
      return redirect('/')  
   else: 
      return render(request,'register.html')   
    
 
def  login(request): 
   if request.method == 'POST': 
      username=request.POST.get('username') 
      password=request.POST.get('password') 
       
     
 
      user =auth.authenticate(username=username,password=password) 
       
      if user is not None: 
         auth.login(request,user) 
         return redirect('/')  
      else: 
         messages.info(request,'invalid credentials') 
         return redirect('login') 
   else: 
      return render(request,'login.html') 
      
# def logout(request): 
#    auth.logout(request) 
#    return redirect('/')  

def CustomerProfile(request): 
   
   if request.method == 'POST' : 
      user= request.user
      name =request.POST['name']
      locality =request.POST['locality'] 
      city =request.POST['city'] 
      mobile =request.POST['mobile'] 
      zipcode =request.POST['zipcode'] 
      

      customer = Customer.objects.create(user=user, name=name, locality=locality, city=city, mobile=mobile, zipcode=zipcode)
      print(user)
      customer.save()
        
      messages.success(request,"congratulation ! your details are saved successfully ")
   return render(request, 'profile.html')

def address(request):
   add = Customer.objects.filter(user = request.user)
   return render(request,'address.html',locals())
    
def UpdateAddress(request, pk):
    if request.method == 'POST':
        user = request.user
        name = request.POST['name']
        locality = request.POST['locality']
        city = request.POST['city']
        mobile = request.POST['mobile']
        zipcode = request.POST['zipcode']

        customer = Customer.objects.get(user=user, pk=pk)
        customer.name = name
        customer.locality = locality
        customer.city = city
        customer.mobile = mobile
        customer.zipcode = zipcode
        customer.save()

        messages.success(request, "Congratulations! Your details have been updated successfully.")
        return redirect('profile')  # Redirect to the profile page or any other desired page

    return HttpResponse("Invalid request")  # Return a response in case of GET or other invalid requests



 


