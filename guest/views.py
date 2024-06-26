import datetime
from django.utils import timezone
from django.http import HttpResponseRedirect, JsonResponse
from django.db import connection  # Needed to execute raw SQL queries
# from dateutil.parser import parse
from django.shortcuts import get_object_or_404, render
from guest.models import *
from django.contrib import messages


# from guest.models import contact
#Create your views here.
def state(request):
    return render(request,"admin/state.html")

def stateaction(request):
    if request.method=="POST":
       statename = request.POST.get('state')
       
       state_obj = states()
       state_obj.statename= statename
      
       state_obj.save()
       
       return render(request,"admin/state.html")  
   
 
   
def districts(request):
    stateview = states.objects.all()
    return render(request,"admin/district.html",{'states' :stateview })    

def districtaction(request):
    if request.method=="POST":
       stateid = request.POST.get('stateid')
       districtname = request.POST.get('district')
       
       district_obj = district()
       
       district_obj.state = stateid
       district_obj.districtname = districtname
      
       district_obj.save()
       
       return districtviews(request)
   
def districtviews(request):
    sql_query = "SELECT * FROM guest_states s inner join guest_district d on s.stateid=d.state;"
    results = district.objects.raw(sql_query)
    return render(request,"admin/districttable.html",{'district':results})   

def districtedit(request,id):
    print("hai")
    if request.method=="POST":
    #    print(id)
       stateid=request.POST.get('stateid')
       districtname =request.POST.get('district')
       print(stateid)
       print(districtname)

       districtedit_obj=district.objects.get(districtid=id)
              
       districtedit_obj.state=stateid
       districtedit_obj.districtname=districtname
      
       
       districtedit_obj.save()
       return districtviews(request)

    else:
        districtedit_obj=district.objects.get(districtid=id)
        
        stateview = states.objects.all()
        print(id)
        return render (request,"admin/districtedit.html",{"edit":districtedit_obj,'states' :stateview })
    

        
    
def districtdelete(request,id):
    districtdata=district.objects.get(districtid=id)
    districtdata.delete()
    messages.success(request,'deleted successfully')
    return districtviews(request)     



def location(request):
    stateview = states.objects.all()
    districtview = district.objects.all()
    return render(request,"admin/location.html",{'states' :stateview, 'district':districtview })  

def locationaction(request):
    if request.method=="POST":
       stateid = request.POST.get('stateid') 
       districtid = request.POST.get('districtid')
       locationname = request.POST.get('location')
       
    
       location_obj = locations()
       location_obj.state = stateid
       location_obj.district = districtid
       location_obj.locationname = locationname
      
       location_obj.save()
       
       return locationviews(request)  
   
def locationviews(request):
    # Define your SQL query
    sql_query = "SELECT * FROM `guest_district` d inner join guest_locations l on d.districtid=l.district inner join guest_states s on s.stateid=l.state;"

    # Execute the raw SQL query
    results = locations.objects.raw(sql_query)
    return render(request,"admin/locationtablee.html",{'location':results}) 

def locationedit(request,id):
    if request.method=="POST":
        
       stateid=request.POST.get('stateid')
       districtid = request.POST.get('districtid')
       locationname  =request.POST.get('location')
      

       locationedit_obj=locations.objects.get(locationid=id)
              
       locationedit_obj.state = stateid
       locationedit_obj.district = districtid
       locationedit_obj.locationname = locationname
      
       
       locationedit_obj.save()
       return locationviews(request)

    else:
        locationedit_obj=locations.objects.get(locationid=id)
        
        stateview = states.objects.all()
        districtview = district.objects.all()
        return render (request,"admin/locationedit.html",{"edit":locationedit_obj,'states' :stateview, 'district':districtview  })
    
def locationdelete(request,id):
    locationdata=locations.objects.get(locationid=id)
    locationdata.delete()
    messages.success(request,'deleted successfully')
    return locationviews(request)      
    

def category_view(request):
    return render(request,"admin/category.html")

def categoryaction(request):
    if request.method == "POST":
        categoryname = request.POST.get('categoryname')
        categoryimage = request.FILES.get('file')  # Corrected the field name
        
        category_obj = category()
        
        category_obj.category_name = categoryname
        category_obj.category_image = categoryimage
        
        print(category_obj.category_name)
        print(category_obj.category_image)
        category_obj.save()
        return categoryview(request) 
    
def categoryview(request):
    categoryview = category.objects.all()
    return render(request,"admin/categorytable.html",{'category':categoryview})

def categoryedit(request,id):
    if request.method=="POST":
    
       categoryname=request.POST.get('categoryname')
       categoryimage = request.FILES.get('file')
    
       categoryedit_obj=category.objects.get(categoryid=id)
       
       if categoryimage:
           categoryedit_obj.category_image=categoryimage
           categoryedit_obj.category_name=categoryname
       
       categoryedit_obj.save()
       return categoryview(request)

    else:
        categoryedit_obj=category.objects.get(categoryid=id)
        return render (request,"admin/categoryedit.html",{"edit":categoryedit_obj })
    
def categorydelete(request,id):
    categorydata=category.objects.get(categoryid=id)
    categorydata.delete()
    messages.success(request,'deleted successfully')
    return categoryview(request)  

def subcategory(request):
    categoryview = category.objects.all()
    return render(request,"admin/subcategory.html",{"category":categoryview})

def subcategoryaction(request):
    if request.method == "POST":
        categoryid = request.POST.get('categoryid')
        subcategoryname = request.POST.get('subcategoryname') 
        subcategoryimage  = request.FILES.get('file')
        
        # category = get_object_or_404(category, pk=categoryid)
        # print(category)
        
        subcategory_obj = sub_category()
        
        subcategory_obj.category_id = categoryid
        subcategory_obj.subcategory_name = subcategoryname
        subcategory_obj.subcategory_image = subcategoryimage
       
        subcategory_obj.save()
        return subcategory_view(request)


def subcategory_view(request):
    sql_query = "SELECT * FROM guest_category c inner join guest_sub_category s on c.categoryid=s.category_id;"
    results = sub_category.objects.raw(sql_query)
    return render(request,"admin/subcategorytable.html",{'subcategory':results}) 

def subcategoryedit(request,id):
    if request.method=="POST":
       categoryid=request.POST.get('categoryid')
       subcategoryname =request.POST.get('subcategoryname')
       subcategoryimage  = request.FILES.get('file')
       print(subcategoryimage)
     
       subcategoryedit_obj=sub_category.objects.get(sub_categoryid=id)
              
       subcategoryedit_obj.category_id=categoryid
       subcategoryedit_obj.subcategory_name=subcategoryname
       subcategoryedit_obj.subcategory_image=subcategoryimage
      
       subcategoryedit_obj.save()
       return subcategory_view(request)

    else:
        subcategoryedit_obj=sub_category.objects.get(sub_categoryid=id)
        #print(subcategoryedit_obj)
        categoryview = category.objects.all()
        return render (request,"admin/subcategoryedit.html",{"edit":subcategoryedit_obj,'category' :categoryview })
    
def subcategorydelete(request,id):
    subcategorydata=sub_category.objects.get(sub_categoryid=id)
    subcategorydata.delete()
    messages.success(request,'deleted successfully')
    return subcategory_view(request)    

def products(request):
    categoryview = category.objects.all()
    sql_query = "SELECT * FROM guest_category c inner join guest_sub_category s on c.categoryid=s.category_id;"
    results = sub_category.objects.raw(sql_query)
    return render(request,"admin/product.html",{"category":categoryview,"subcategory":results})  

def productaction(request):
    if request.method=="POST":
       productname = request.POST.get('name')
       categoryid = request.POST.get('categoryid')
       subcategoryid = request.POST.get('subcategoryid')
       productrate = request.POST.get('rate')
       quantity = request.POST.get('quantity')
       productimage1 = request.FILES.get('file1')
       productimage2 = request.FILES.get('file2')
       productimage3 = request.FILES.get('file3')
       description = request.POST.get('description')
       productstatus = "Active"
       registerdate = timezone.now().date()
       print(categoryid)
       
       product_obj = product()
       
       product_obj.productname = productname
       product_obj.category_id = categoryid
       product_obj.sub_category_id = subcategoryid
       product_obj.product_rate = productrate
       product_obj.quantity = quantity
       product_obj.productimage_1 = productimage1
       product_obj.productimage_2 = productimage2
       product_obj.productimage_3=productimage3 
       product_obj.description=description
       product_obj.product_status=productstatus
       product_obj.registered_date=registerdate
       
       product_obj.save()
       
       return  productview(request)  
      
    
  
def productview(request):
    # Define your SQL query
    sql_query = "SELECT * FROM guest_category c inner join guest_sub_category s on c.categoryid=s.category_id inner join guest_product p on s.sub_categoryid=p.sub_category_id;"

    # Execute the raw SQL query
    results = product.objects.raw(sql_query)
   
    return render(request,"admin/producttable.html",{'product':results})   

def productedit(request,id):
    if request.method=="POST":  
       print(id)
       productname = request.POST.get('name')
       categoryid = request.POST.get('categoryid')
       print(categoryid)
       subcategoryid = request.POST.get('subcategoryid')
       productrate = request.POST.get('rate')
       quantity = request.POST.get('quantity')
       productimage1 = request.POST.get('file1')
       productimage2 = request.POST.get('file2')
       productimage3 = request.POST.get('file3')
       description = request.POST.get('description')
       productstatus = "Active"
       registerdate = timezone.now().date()
     
       productedit_obj=product.objects.get(productid=id)
              
       productedit_obj.productname= productname 
       productedit_obj.category_id = categoryid
       productedit_obj.sub_category_id = subcategoryid
       productedit_obj.product_rate= productrate
       productedit_obj.quantity=quantity 
       if productimage1:
          productedit_obj.productimage_1=productimage1      
       if productimage2:
          productedit_obj.productimage_2=productimage2
       if productimage3:
          productedit_obj.productimage_3=productimage3 
       productedit_obj.description=description
       productedit_obj.product_status=productstatus
       productedit_obj.registered_date=registerdate
       
       productedit_obj.save()
       
       return  productview(request) 

    else:
        print(id)
        productedit_obj=product.objects.get(productid=id)
        print(productedit_obj)
        
        categoryview = category.objects.all()
        subcategory_view = sub_category.objects.all()
        return render (request,"admin/productedit.html",{"edit":productedit_obj,'category' :categoryview, 'subcategory' :subcategory_view})
    
     
def productdelete(request,id):
    productdata=product.objects.get(productid=id)
    productdata.delete()
    messages.success(request,'deleted successfully')
    return productview(request)    



     
def cusregforms(request):
     stateview = states.objects.all()
     districtview = district.objects.all()
     return render(request,"guest/cusregform.html", {'states' :stateview, 'district':districtview })      
        
def login(request):
     return render(request,"guest/login.html") 
     
def cusregformaction(request):
    if request.method=="POST":
       print("hai")
       customername = request.POST.get('name')
       emailid = request.POST.get('emailid')
       contactno = request.POST.get('number')
       state = request.POST.get('stateid')
       district = request.POST.get('districtid')
       location = request.POST.get('location')
       address = request.POST.get('address')
       username = request.POST.get('username')
       password = request.POST.get('password')
       
      
       
       cusregform_obj = cusregform()
       
       cusregform_obj.customer_name= customername 
       cusregform_obj.email_id = emailid
       cusregform_obj.contact_no = contactno
       cusregform_obj.state= state
       cusregform_obj.district=district
       cusregform_obj.location=location
       cusregform_obj.address=address
       cusregform_obj.username=username
       cusregform_obj.password=password
       
      
       
       
       cusregform_obj.save()
       
       return login(request)
   

def cusregformview(request):
        cusregformview = cusregform.objects.all()
        return render(request,"guest/cusregformtable.html",{'cusregform': cusregformview}) 
 
def loginaction(request):
    if request.method=="POST":
        print("hai")
        username = request.POST.get('username')
        password = request.POST.get('password')
        customerid = request.session.get('loginid')
        sql_query= "SELECT COUNT(*) AS TOTAL FROM guest_cart WHERE customer_id=%s"
        with connection.cursor() as cursor:
           cursor.execute(sql_query,[customerid])
           result=cursor.fetchone()
           count=result[0]
           print(count)
        print(username)
        print(password)
        if cusregform.objects.filter(username=username , password=password).exists():
            loginobj = cusregform.objects.get(username=username , password=password)
            request.session['username'] = loginobj.username
            request.session['loginid'] = loginobj.customerid
            request.session['name'] = loginobj.customer_name
            # print(session['loginid'])
            print("hai")
            categoryview = category.objects.all()
            productview = product.objects.all()
            context = {'username' : username,'name':loginobj.customer_name,'category' :categoryview, 'product' :productview,'count':count}
            if 'loginid' in request.session:
                return render(request, 'customer/cusindex.html',context)
            return render(request,"guest/login.html")
                
        elif admin.objects.filter(admin_username=username , admin_password=password).exists():
            return render(request, 'admin/index.html')
        
        else :
            messages.success(request,"CHECK USERNAME OR PASSWORD")
            return render(request,"guest/login.html")
           
          
        
    
def guestindex(request):
    if 'loginid' in request.session:
       categoryview = category.objects.all()
       productview = product.objects.all()
       
       return render(request,"customer/cusindex.html",{'category' :categoryview, 'product' :productview}) 
    categoryview = category.objects.all()
    productview = product.objects.all()
    return render(request,"guest/index.html",{'category' :categoryview, 'product' :productview})

def getsubcategoryview(request,id):
    categoryview = category.objects.all()
    print(id)
    username = request.session.get('username')
    customerid = request.session.get('loginid')
    
    # Define your SQL query
    sql_query = "SELECT * FROM guest_sub_category where category_id= %s;"
    # Execute the raw SQL query
    subcategory_view = sub_category.objects.raw(sql_query, [id])
    if customerid:
        return render(request,"customer/getsubcategoryview.html",{'subcategory_view': subcategory_view, 'category' :categoryview,'username':username})
    return render(request,"guest/getsubcategoryview.html",{'subcategory_view': subcategory_view, 'category' :categoryview,'username':username})     
       
def cusdesigns(request):
    categoryview = category.objects.all()
    return render(request,"customer/cusdesign.html",{'category': categoryview}) 
   
def cusdesignaction(request):
    if request.method=="POST":
       print("hi")
       category = request.POST.get('categoryid')
       customerid = request.session.get('loginid')
       modelimage = request.FILES.get('modelimage')
       description = request.POST.get('description')
       name = request.POST.get('name')
       emailid = request.POST.get('emailid')
       contactnumber = request.POST.get('contactnumber')
       address = request.POST.get('address')
       
       cusdesign_obj = cusdesign()
       
       cusdesign_obj.category = category 
       cusdesign_obj.customer_id = customerid
       cusdesign_obj.model_image = modelimage
       cusdesign_obj.description = description
       cusdesign_obj.name= name
       cusdesign_obj.email_id = emailid
       cusdesign_obj.contact_number = contactnumber
       cusdesign_obj.address = address
       
       cusdesign_obj.save()
       return render(request,"customer/cusdesign.html")
   
def cusdesignview(request):
       sql_query = "SELECT * FROM guest_category c inner join guest_cusdesign cu on c.categoryid=cu.category;"
       results = cusdesign.objects.raw(sql_query)
       return render(request,"admin/categorytable.html",{'cusdesign':results}) 
   
def contacts(request):
    categoryview = category.objects.all()
    return render(request,"guest/contact.html",{'category' :categoryview}) 

def contactaction(request):
    if request.method=="POST":
       name = request.POST.get('name')
       emailid = request.POST.get('email')
       subject = request.POST.get('subject')
       message = request.POST.get('message')
       
       contact_obj = contacts()
       
       contact_obj.name= name
       contact_obj.email_id = emailid
       contact_obj.subject = subject
       contact_obj.message = message
       
       contact_obj.save()
       return render(request,"guest/contact.html")
 

def cartview(request):
    username = request.session.get('username')
    categoryview = category.objects.all()
    # Define your SQL query
    customerid = request.session.get('loginid')
    sql_query= "SELECT COUNT(*) AS TOTAL FROM guest_cart WHERE customer_id=%s"
    with connection.cursor() as cursor:
        cursor.execute(sql_query,[customerid])
        result=cursor.fetchone()
        count=result[0]
    # print(customerid)
    sql_query = """  SELECT c.cart_id, c.product, c.quantity,p.productname, c.price, (c.quantity * c.price) as total_price FROM guest_cart c INNER JOIN guest_product p ON p.productid = c.product WHERE c.customer_id = %s; """
    # Execute the raw SQL query
    with connection.cursor() as cursor:
        cursor.execute(sql_query, [customerid])
        results = cursor.fetchall()
   # Calculate the total sum
    total_sum = sum(row[5] for row in results)  # total_price is in the 5th column (index 4)
    print(total_sum)
    # Prepare results for template
    cart_items = []
    for row in results:
        item = {
            'cartid':row[0],
            'productname':row[3],
            'product': row[1],
            'quantity': row[2],
            'price': row[4],
            'total_price': row[5]
        }
        cart_items.append(item)
        
     # Calculate the expected delivery date
    current_date = timezone.now().date()
    print(current_date)
    expected_delivery_date = current_date + datetime.timedelta(days=5)
    print(expected_delivery_date)
    if total_sum>999:
        shipping_charge = 0
    else:
        shipping_charge = 40
    request.session['shipping_charge'] = shipping_charge
    subtotal = total_sum + shipping_charge
    print(subtotal)
    delivery_date = expected_delivery_date.strftime("%B %d")
    print(delivery_date)
   
    
    
    return render(request,"customer/cart.html",{'cart':cart_items,"total_sum":total_sum,'delivery_date':delivery_date,'shipping_charge':shipping_charge,'subtotal':subtotal,'category' :categoryview,'count':count, 'username':username})  
    

def cartaction(request):
    if request.method=="POST":
        if 'loginid' in request.session:
            print("hai")
            
            customerid= request.session.get('loginid')
            #    print(customerid)
            product = request.POST.get('product')
            product
            quantity = request.POST.get('quantity')
            print(quantity)
            price = request.POST.get('price')
            print(price)
            cartdate = timezone.now().date()
            cartstatus = "Carted"
            
            cart_obj = cart()
                
            cart_obj.customer_id = customerid
            cart_obj.product =  product
            cart_obj.quantity = quantity
            cart_obj.price = price 
            cart_obj.cart_date = cartdate 
            cart_obj.cart_status = cartstatus
                    
            cart_obj.save()
            
            
            return cartview(request) 
        return render(request,"guest/login.html")


def cartdelete(request,id):
    cartdata=cart.objects.get(cart_id=id)
    cartdata.delete()
    messages.success(request,'deleted successfully')
    return cartview(request)    

def productviewmore(request,id):
    categoryview = category.objects.all()    
    # Define your SQL query
    sql_query = "SELECT * FROM guest_category c inner join guest_sub_category s on c.categoryid=s.category_id inner join guest_product p on s.sub_categoryid=p.sub_category_id where p.productid = %s;"

    # Execute the raw SQL query
    results = product.objects.raw(sql_query,[id])
    
    customerid = request.session.get('loginid')
    username = request.session.get('username')
    sql_query= "SELECT COUNT(*) AS TOTAL FROM guest_cart WHERE customer_id=%s"
    with connection.cursor() as cursor:
        cursor.execute(sql_query,[customerid])
        result=cursor.fetchone()
        count=result[0]
    return render(request,"customer/productviewmore.html",{'product':results,'category' :categoryview,'username':username, "count":count})  

def productviewmoreguest(request,id):
    categoryview = category.objects.all()    
    # Define your SQL query
    sql_query = "SELECT * FROM guest_category c inner join guest_sub_category s on c.categoryid=s.category_id inner join guest_product p on s.sub_categoryid=p.sub_category_id where p.productid = %s;"

    # Execute the raw SQL query
    results = product.objects.raw(sql_query,[id])
    
    customerid = request.session.get('loginid')
    username = request.session.get('username')
    sql_query= "SELECT COUNT(*) AS TOTAL FROM guest_cart WHERE customer_id=%s"
    with connection.cursor() as cursor:
        cursor.execute(sql_query,[customerid])
        result=cursor.fetchone()
        count=result[0]
    return render(request,"guest/productviewmore.html",{'product':results,'category' :categoryview,'username':username, "count":count})  


    
def subcatwiseproduct(request,id):
    print(id)
    customerid = request.session.get('loginid')
    username = request.session.get('username')
    # Fetch products that belong to the specified subcategory ID
    product_data = product.objects.filter(sub_category_id=id)
    categoryview = category.objects.all()
    
    
    sql_query= "SELECT COUNT(*) AS TOTAL FROM guest_cart WHERE customer_id=%s"
    with connection.cursor() as cursor:
        cursor.execute(sql_query,[customerid])
        result=cursor.fetchone()
        count=result[0]
    if customerid:
        return render(request, "customer/subcatwiseproduct.html", {"product_data": product_data,"category": categoryview, 'username':username,"count":count})
    return render(request, "guest/subcatwiseproduct.html", {"product_data": product_data,"category": categoryview, 'username':username,"count":count})
    # else:
    #     print("pettu")
    #     # Fetch products that belong to the specified subcategory ID
    #     product_data = product.objects.filter(sub_category_id=id)
    #     categoryview = category.objects.all()
        
    #     customerid = request.session.get('loginid')
    #     username = request.session.get('username')
    #     sql_query= "SELECT COUNT(*) AS TOTAL FROM guest_cart WHERE customer_id=%s"
    #     with connection.cursor() as cursor:
    #         cursor.execute(sql_query,[customerid])
    #         result=cursor.fetchone()
    #         count=result[0]
    #     return render(request,"guest/subcatwiseproduct.html",{"product_data": product_data,"category": categoryview, 'username':username,"count":count})
    
def cusindex(request):
    if 'loginid' in request.session:
       categoryview = category.objects.all()
       productview = product.objects.all()
       for data in productview:
          quantity = data.quantity
          print(quantity)
            
       username = request.session.get('username')
       customerid = request.session.get('loginid')
       sql_query= "SELECT COUNT(*) AS TOTAL FROM guest_cart WHERE customer_id=%s"
       with connection.cursor() as cursor:
           cursor.execute(sql_query,[customerid])
           result=cursor.fetchone()
           count=result[0]
           print(count)
       # Redirect to the home page if the value doesn't exist
       return render(request,"customer/cusindex.html",{'category' :categoryview, 'product' :productview,'username':username,"quantity":quantity,"count":count})
       # return render(request,"guest/login.html")
    return render(request,"guest/login.html")
     
 
# def guestsubcatproduct(request,id):
#     print(id)

#     # Fetch products that belong to the specified subcategory ID
#     product_data = product.objects.filter(sub_category_id=id)
#     categoryview = category.objects.all()
    
#     customerid = request.session.get('loginid')
#     # username = request.session.get('username')
#     sql_query= "SELECT COUNT(*) AS TOTAL FROM guest_cart WHERE customer_id=%s"
#     with connection.cursor() as cursor:
#           cursor.execute(sql_query,[customerid])
#           result=cursor.fetchone()
#           count=result[0]
#     return render(request, "guest/subcatwiseproduct.html", {"product_data": product_data,"category": categoryview, "count":count})  

def adminlogin(request):
     return render(request,"admin/adminlogin.html") 


def checkout(request,amt,shipping):
    username = request.session.get('username')
    categoryview = category.objects.all()
    stateview = states.objects.all()
    districtview = district.objects.all()
    customerid = request.session.get('loginid')
    sql_query = """SELECT * FROM guest_cart c INNER JOIN guest_product p ON c.product = p.productid WHERE c.customer_id = %s;"""
    with connection.cursor() as cursor:
        cursor.execute(sql_query, [customerid])
        results = cursor.fetchall()
      
    # # Calculate the total sum
    total_sum = amt
    shipping_charge = shipping
    # print(total_sum)
        # 
    # Calculate the expected delivery date
    current_date = timezone.now().date()
    # print(current_date)
    expected_delivery_date = current_date + datetime.timedelta(days=5)
    # print(expected_delivery_date) 
    # if total_sum>999:
    #     shipping_charge = 0
    # else:
    #     shipping_charge = 40
    # subtotal = total_sum + shipping_charge
    # print(subtotal)
    delivery_date = expected_delivery_date.strftime("%B %d")
    print(delivery_date)
        
    return render(request,"customer/checkout.html",{'states' :stateview, 'district':districtview,'result':results,'total_sum' :total_sum,'delivery_date':delivery_date,'category' :categoryview, 'shipping_charge':shipping_charge,'username':username})  

def checkoutaction(request):
    if request.method=="POST":
       print("hi")
       customerid= request.session.get('loginid')
       fullname = request.POST.get('name')
       emailid = request.POST.get('email')
       mobileno = request.POST.get('mobileno')
       address = request.POST.get('address')
       street = request.POST.get('street')
       landmark = request.POST.get('landmark')
       pincode = request.POST.get('pincode')
       city = request.POST.get('city')
       state = request.POST.get('stateid')
       total_amount = request.POST.get('total_sum')
       payments = request.POST.get('payment')
       order_date = timezone.now().date()
       order_status = "Ordered"
 
       billing_address_obj = billing_address()
         
       billing_address_obj.customer_id = customerid
       billing_address_obj.full_name =  fullname
       billing_address_obj.email_id = emailid
       billing_address_obj.mobile_no = mobileno 
       billing_address_obj.address =  address 
       billing_address_obj.street =  street
       billing_address_obj.landmark = landmark
       billing_address_obj.pincode = pincode
       billing_address_obj.city =  city
       billing_address_obj.state = state
       
       billing_address_obj.save()    
           
       if payments == "COD":
            order_master_obj = order_master()
            order_master_obj.customer_id=customerid
            order_master_obj.order_date= order_date
            order_master_obj.total_amount= total_amount
            order_master_obj.order_status=order_status
            order_master_obj.payment_method=payments
            
            order_master_obj.save()
            
            # Get the last inserted ID
            last_inserted_id = order_master_obj.order_master_id
            print(last_inserted_id)
            cart_data = cart.objects.filter(customer_id=customerid)
            order_data = []
            order_data.append(cart_data)
            context = {'subtotal':total_amount,"order_data":order_data}
            for cart_item in cart_data:
                order_detail.objects.create(
                bill_no=last_inserted_id,
                customer_id=customerid,
                product_id=cart_item.product,
                product_price=cart_item.price*cart_item.quantity,
                quantity=cart_item.quantity,
                order_date = timezone.now().date(),
                order_status = "Ordered",
                payment_method = payments
            )
                
            cart_data.delete()

            return orderconfirmation(request)
       
       elif payments == "CARD PAYMENT":
            # Get the last inserted ID
           cart_data = cart.objects.filter(customer_id=customerid)
        #    payment_data = []
           context = {'subtotal':total_amount}
           for cart_item in cart_data:
               print(cart_item.product)
            #    payment_data.append(cart_item.product)
            #    payment_data.append(cart_item.quantity)
            #    payment_data.append(cart_item.price)
            #    payment_data.append(payments)
            #    payment_data.append(total_amount)
               
               context = {"payments":payments,'subtotal':total_amount}
               return render(request,"customer/payment.html",context) 
        
       return cartview(request) 
 
def paymentaction(request):
    if request.method=="POST":
        customerid= request.session.get('loginid')
        payments = request.POST.get('payments')
        total_amount = request.POST.get('total_amount')
        
        order_date = timezone.now().date()
        order_status = "Ordered"
        
        context = {'subtotal':total_amount}
        
        order_master_obj = order_master()
        order_master_obj.customer_id=customerid
        order_master_obj.order_date= order_date
        order_master_obj.total_amount= total_amount
        order_master_obj.order_status=order_status
        order_master_obj.payment_method=payments
        
        order_master_obj.save()
        
        # Get the last inserted ID
        last_inserted_id = order_master_obj.order_master_id
        
        cart_data = cart.objects.filter(customer_id=customerid)
        for cart_item in cart_data:
            order_detail.objects.create(
            bill_no=last_inserted_id,
            customer_id=customerid,
            product_id=cart_item.product,
            product_price=cart_item.price*cart_item.quantity,
            quantity=cart_item.quantity,
            order_date = timezone.now().date(),
            order_status = "Ordered",
            payment_method = payments
            )
                
            cart_data.delete()
            return orderconfirmation(request)
  
def orderview(request):
     # Define your SQL query
    sql_query ="SELECT * FROM guest_order_master om INNER JOIN guest_cusregform c ON om.customer_id = c.customerid;"
    
     # Execute the raw SQL query
    results = order_master.objects.raw(sql_query)
    
    return render(request,"admin/orderdetail.html",{'order_master':results}) 

def getorderview(request,id,subtotal):
     # Define your SQL query
    sql_query = "SELECT * FROM guest_order_detail o inner join guest_product p on p.productid=o.product_id where o.order_detail_id= %s;"
    print(sql_query)
    # Execute the raw SQL query
    orderdetailsview = order_detail.objects.raw(sql_query, [id]) 
    # print(orderdetailsview.product_price)
    for order in orderdetailsview:
        order_status = order.order_status
        print(order_status)
    
    return render(request,"admin/getorderdetail.html",{'order_detailsview': orderdetailsview,'sub_total':subtotal,'master_id':id,'order_status':order_status})
     
def addtoshipping(request,id): 
        # Updating order_master table
       order_status = "Shipped"
       order_master_obj = order_master.objects.get(order_master_id=id)
       order_master_obj.order_status = order_status
       order_master_obj.save() 
       
        # Updating order_detail table
       order_detail_obj = order_detail.objects.filter(order_detail_id=id)
       
       for detail_obj in order_detail_obj:
           detail_obj.order_status = order_status 
           detail_obj.save()
           
       return orderview(request)
       
def searchorder(request):   
    if request.method=="POST":
       search_date = request.POST.get('searchDate')
       #print(search_date)
       sql_query ="SELECT * FROM guest_order_master om INNER JOIN guest_cusregform c ON om.customer_id = c.customerid where om.order_date=%s;"
      # Execute the raw SQL query
       order_details = order_master.objects.raw(sql_query,[search_date])
       # Execute the raw SQL query
       context = {'order_detail':order_details}
       return render(request,"admin/orderdetail.html",context)
   
def addtodelivered(request,id): 
        # Updating order_master table
       order_status = "Delivered"
       order_master_obj = order_master.objects.get(order_master_id=id)
       order_master_obj.order_status = order_status
       order_master_obj.save() 
       
        # Updating order_detail table
       order_detail_obj = order_detail.objects.filter(order_detail_id=id)
       
       for detail_obj in order_detail_obj:
           detail_obj.order_status = order_status 
           detail_obj.save()
           
       return orderview(request)
   
def logout_view(request):
   
    # Delete a custom cookie (replace 'custom_cookie_name' with your cookie's name)
    response = HttpResponseRedirect('/')  # Redirect to the homepage or any desired URL
    request.session.flush()  # Replace 'custom_cookie_name' with your cookie's name

    return response

def logout_viewadmin(request):
   
    # Delete a custom cookie (replace 'custom_cookie_name' with your cookie's name)
    response = HttpResponseRedirect('/')  # Redirect to the homepage or any desired URL
    request.session.flush()  # Replace 'custom_cookie_name' with your cookie's name

    return response

def myorders(request):
    customerid = request.session.get('loginid')
    categoryview = category.objects.all()
    sql_query = "SELECT * FROM `guest_order_detail` od INNER JOIN guest_product p ON od.product_id = p.productid WHERE customer_id = %s;"
    order_master = order_detail.objects.raw(sql_query,[customerid])
    
    return render(request,"customer/myorders.html",{"order_details":order_master,'category' :categoryview})
    
def ordersviewmore(request,id):
    customerid = request.session.get('loginid')
    
    categoryview = category.objects.all()
    sql_query = "SELECT * FROM `guest_order_detail` od INNER JOIN guest_product p ON od.product_id = p.productid WHERE customer_id = %s AND order_detail_id = %s;"
    result = order_detail.objects.raw(sql_query,[customerid,id])
    
    return render(request,"customer/ordersviewmore.html",{'category' :categoryview,"result":result})

def orderconfirmation(request):
    # print("hai mutta")
    customerid = request.session.get('loginid')
    # Retrieve the last inserted order for the customer
    order_master_obj = order_master.objects.filter(customer_id=customerid).order_by('-order_master_id').first()
    total_sum = order_master_obj.total_amount
    print(total_sum)
    if order_master_obj:
        # Get the last inserted ID
        last_inserted_id = order_master_obj.order_master_id
        # print(last_inserted_id)
        
        # SQL query to fetch all rows where bill_no matches the last inserted ID
        sql_query = """SELECT * FROM guest_order_detail od inner join guest_product p on p.productid = od.product_id WHERE od.bill_no = %s;"""
        
        with connection.cursor() as cursor:
            cursor.execute(sql_query, [last_inserted_id])
            results = cursor.fetchall()
            
        # Calculate the expected delivery date
        current_date = timezone.now().date()
        print(current_date)
        expected_delivery_date = current_date + datetime.timedelta(days=5)
        print(expected_delivery_date)
        shipping_charge = request.session['shipping_charge']
        delivery_date = expected_delivery_date.strftime("%B %d, %Y")
        print(delivery_date)
        
        # Process the results as needed
        for row in results:
            data = row[0]
        
        return render (request,"customer/orderconfirmation.html", {'result':results,'total_sum':total_sum,'delivery_date':delivery_date,'shipping_charge':shipping_charge} )
     
def monthlyreport(request):
    return render(request,"admin/monthlyreport.html")
def getmonthlyreport(request):
     if request.method=="POST":
        from_date = request.POST.get('FromDate')
        to_date = request.POST.get('ToDate')
        print(from_date)
        print(to_date)
        sql_query = "SELECT od.order_detail_id,sum(od.product_price) as product_price,p.productname,s.subcategory_name,c.category_name,sum(od.quantity) as quantity,p.product_rate FROM guest_order_detail od inner join guest_product p on od.product_id=p.productid inner join guest_sub_category s on s.sub_categoryid =p.sub_category_id inner join  guest_category c on c.categoryid=s.category_id WHERE od.order_date BETWEEN %s AND %s GROUP BY od.product_id ;"
    
        data = order_detail.objects.raw(sql_query,[from_date,to_date])
        context = {'order_detail':data}
         
        return render(request,"admin/monthlyreport.html",context)
    

