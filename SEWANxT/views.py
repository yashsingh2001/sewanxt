from django.http import HttpResponse
from django.shortcuts import render


# views.py
# views.py
import qrcode
from PIL import Image
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.crypto import get_random_string


import qrcode
from django.http import HttpResponse
from io import BytesIO
from PIL import Image
from homepage.models import Homepage
from noncrop.models import Noncrop

from django.shortcuts import render






from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from datetime import datetime


from django.db import migrations, models





from homesignup.models import Homesignup

from personaldetails.models import personaldetails



def personal_details(request):
    if request.method == "POST":
        # Get form data
        personal_details_state = request.POST.get('state1')
        personal_details_product = request.POST.get('product1')
        personal_details_aadhaarNumber = request.POST.get('aadhar')
        personal_details_farmername = request.POST.get('farmerName1')
        personal_details_GuardianName = request.POST.get('guardian')
        personal_details_age = request.POST.get('age')
        personal_details_mobilenumber = request.POST.get('number1')
        personal_details_gender = request.POST.get('Gender')
        personal_details_category = request.POST.get('caste')
        personal_details_residencestate = request.POST.get('resState1')
        personal_details_residencedistrict = request.POST.get('District')
        personal_details_residenceblock = request.POST.get('block1')
        personal_details_grampanchayatofresidence = request.POST.get('grampanch')
        personal_details_residencevillage = request.POST.get('Village')
        personal_details_housenumber = request.POST.get('H_no')
        personal_details_pincode = request.POST.get('Pin')
        personal_details_farmercategory = request.POST.get('category1')
        personal_details_natureoffarmer = request.POST.get('nature1')
        personal_details_mandi = request.POST.get('Mandi')
        personal_details_seedpurchase = request.POST.get('invoice')
        personal_details_retailstore = request.POST.get('retailstore1')
        personal_details_bankname = request.POST.get('bankname')
        personal_details_branch = request.POST.get('branchname')
        personal_details_ifsc = request.POST.get('ifsc1')
        personal_details_bankaccountnumber = request.POST.get('account_no')
        personal_details_nomineename = request.POST.get('nominee_name')
        personal_details_nomineerelation = request.POST.get('nominee_relation')
        nomineeage = request.POST.get('nominee_age')

        # Check if an entry with similar attributes already exists
        existing_entry = personal_details.objects.filter(
            personal_details_typeofrisk=personal_details_state,
            personal_details_product=personal_details_product,
            personaldetails_aadhaarNumber=personal_details_aadhaarNumber,
            personaldetails_farmername=personal_details_farmername,
            personaldetails_GuardianName=personal_details_GuardianName,
            personaldetails_age=personal_details_age,
            personaldetails_mobilenumber=personal_details_mobilenumber,
            personaldetails_gender=personal_details_gender,
            personaldetails_category=personal_details_category,
            personaldetails_residencestate=personal_details_residencestate,
            personaldetails_residencedistrict=personal_details_residencedistrict,
            personaldetails_residenceblock=personal_details_residenceblock,
            personaldetails_grampanchayatofresidence=personal_details_grampanchayatofresidence,
            personaldetails_residencevillage=personal_details_residencevillage,
            personaldetails_housenumber=personal_details_housenumber,
            personaldetails_pincode=personal_details_pincode,
            personaldetails_farmercategory=personal_details_farmercategory,
            personaldetails_natureoffarmer=personal_details_natureoffarmer,
          
            personaldetails_seedpurchase=personal_details_seedpurchase,
            personaldetails_retailstore=personal_details_retailstore,
            personaldetails_bankname=personal_details_bankname,
            personaldetails_branch=personal_details_branch,
            personaldetails_ifsc=personal_details_ifsc,
            personaldetails_bankaccountnumber=personal_details_bankaccountnumber,
            personaldetails_nomineename=personal_details_nomineename,
            personaldetails_nomineerelation=personal_details_nomineerelation,
            personaldetails_nomineeage=nomineeage,
        ).exists()

        if existing_entry:
            # Handle case where similar entry already exists
            return render(request, ".html", {'error': 'Similar entry already exists in the database.'})

        # Save to database
        new_entry = personaldetails(
            personal_details_state=personal_details_state,
            personal_details_product=personal_details_product,
            personal_details_aadhaarNumber=personal_details_aadhaarNumber,
            personal_details_farmername=personal_details_farmername,
            personal_details_GuardianName=personal_details_GuardianName,
            personal_details_age=personal_details_age,
            personal_details_mobilenumber=personal_details_mobilenumber,
            personal_details_gender=personal_details_gender,
            personal_details_category=personal_details_category,
            personal_details_residencestate=personal_details_residencestate,
            personal_details_residencedistrict=personal_details_residencedistrict,
            personal_details_residenceblock=personal_details_residenceblock,
            personal_details_grampanchayatofresidence=personal_details_grampanchayatofresidence,
            personal_details_residencevillage=personal_details_residencevillage,
            personal_details_housenumber=personal_details_housenumber,
            personal_details_pincode=personal_details_pincode,
            personal_details_farmercategory=personal_details_farmercategory,
            personal_details_natureoffarmer=personal_details_natureoffarmer,
            personal_details_mandi=personal_details_mandi,
            personal_details_seedpurchase=personal_details_seedpurchase,
            personal_details_retailstore=personal_details_retailstore,
            personal_details_bankname=personal_details_bankname,
            personal_details_branch=personal_details_branch,
            personal_details_ifsc=personal_details_ifsc,
            personal_details_bankaccountnumber=personal_details_bankaccountnumber,
            personal_details_nomineename=personal_details_nomineename,
            personal_details_nomineerelation=personal_details_nomineerelation,
            personal_details_nomineeage=nomineeage,
        )
        new_entry.save()

        return redirect('insurancedetails.html')  # Redirect to a success page after saving

    return render(request, "insurancedetails.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Check if a user with the same username or email already exists
        existing_user = Homesignup.objects.filter(homesignup_username=username).exists()
        existing_email = Homesignup.objects.filter(homesignup_email=email).exists()

        if not existing_user and not existing_email:
            # If user and email are unique, save data to the database
            Homesignup.objects.create(homesignup_username=username, homesignup_password=password, homesignup_email=email)

            # Redirect to a thank you page or any other page
            return redirect('thank_you_signup')

    return render(request, "thankssignuppage.html")




class Migration(migrations.Migration):

    dependencies = [
        # Define your dependencies here
    ]

    operations = [
        migrations.AlterField(
            model_name='noncrop',
            name='noncrop_hypothecated',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='noncrop',
            name='noncrop_vaccination',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]





def savenoncrop(request):
    if request.method == "POST":
        # Get form data
        type_risk = request.POST.get('typerisk')
        gender = request.POST.get('Gender')
        risk_age_year = request.POST.get('riskAgeYear')
        risk_age_months = request.POST.get('riskAgeMonths')
        breed = request.POST.get('Breed')
        vaccination = request.POST.get('option')
        hypothecation = request.POST.get('options')
        hypothecatee_name = request.POST.get('hypothecatee_name', '')
        hypothecatee_contact = request.POST.get('hypothecatee_contact', '')
        tagging_date = request.POST.get('Taggingdate', None)
        sum_insured = request.POST.get('Insured')
        market_value = request.POST.get('Market_value')
        pregnancy_status = request.POST.get('Pregnancy-status')
        calving_cycle = request.POST.get('calving')
        animal_color = request.POST.get('optio')
        animal_tail_color = request.POST.get('color')
        animal_left_horn_shape = request.POST.get('shape')
        animal_right_horn_shape = request.POST.get('shape')

        # Handle file uploads
        ear_tag_image = request.FILES.get('tag-img')
        left_side_image = request.FILES.get('tag-leftimg')
        right_side_image = request.FILES.get('tag-rightimg')
        tail_image = request.FILES.get('tail-img')
        with_owner_image = request.FILES.get('with-owner-img')

        # Check if an entry with similar attributes already exists
        existing_entry = Noncrop.objects.filter(
            noncrop_typeofrisk=type_risk,
            noncrop_gender=gender,
            noncrop_ageyears=risk_age_year,
            noncrop_agemonths=risk_age_months,
            noncrop_breed=breed,
            noncrop_vaccination=vaccination,
            noncrop_hypothecated=hypothecation,
            noncrop_taggingdate=datetime.strptime(tagging_date, '%Y-%m-%d') if tagging_date else None,
            noncrop_suminsured=sum_insured,
            noncrop_marketvalue=market_value,
            noncrop_pregnancystatus=pregnancy_status,
            noncrop_calvingcycle=calving_cycle,
            noncrop_animalcolor=animal_color,
            noncrop_tailswitchcolour=animal_tail_color,
            noncrop_lefthornshape=animal_left_horn_shape,
            noncrop_righthornshape=animal_right_horn_shape,
        ).exists()

        if existing_entry:
            # Handle case where similar entry already exists
            return render(request, "personaldetails.html", {'error': 'Similar entry already exists in the database.'})

        # Save to database
        en = Noncrop(
            noncrop_typeofrisk=type_risk,
            noncrop_gender=gender,
            noncrop_ageyears=risk_age_year,
            noncrop_agemonths=risk_age_months,
            noncrop_breed=breed,
            noncrop_vaccination=vaccination,
            noncrop_hypothecated=hypothecation,
            noncrop_taggingdate=datetime.strptime(tagging_date, '%Y-%m-%d') if tagging_date else None,
            noncrop_suminsured=sum_insured,
            noncrop_marketvalue=market_value,
            noncrop_pregnancystatus=pregnancy_status,
            noncrop_calvingcycle=calving_cycle,
            noncrop_animalcolor=animal_color,
            noncrop_tailswitchcolour=animal_tail_color,
            noncrop_lefthornshape=animal_left_horn_shape,
            noncrop_righthornshape=animal_right_horn_shape,
        )
        en.save()

    return render(request, "personaldetails.html")




# def savenoncrop(request):
#     if request.method == "POST":
#         # Get form data
#         type_risk = request.POST.get('typerisk')
#         gender = request.POST.get('Gender')
#         risk_age_year = request.POST.get('riskAgeYear')
#         risk_age_months = request.POST.get('riskAgeMonths')
#         breed = request.POST.get('Breed')
#         vaccination = request.POST.get('option')
#         hypothecation = request.POST.get('options')
#         hypothecatee_name = request.POST.get('hypothecatee_name', '')
#         hypothecatee_contact = request.POST.get('hypothecatee_contact', '')
#         tagging_date = request.POST.get('Taggingdate', None)
#         sum_insured = request.POST.get('Insured')
#         market_value = request.POST.get('Market_value')
#         pregnancy_status = request.POST.get('Pregnancy-status')
#         # milking_status = request.POST.get('milking')
#         calving_cycle = request.POST.get('calving')
#         animal_color = request.POST.get('optio')
#         animal_tail_color = request.POST.get('color')
#         animal_left_horn_shape = request.POST.get('shape')
#         animal_right_horn_shape = request.POST.get('shape')

#         # Handle file uploads
#         ear_tag_image = request.FILES.get('tag-img')
#         left_side_image = request.FILES.get('tag-leftimg')
#         right_side_image = request.FILES.get('tag-rightimg')
#         tail_image = request.FILES.get('tail-img')
#         with_owner_image = request.FILES.get('with-owner-img')

#         # Save to database
#         en = Noncrop(
          
#             noncrop_typeofrisk=type_risk,
#             noncrop_gender=gender,
#             noncrop_ageyears=risk_age_year,
#             noncrop_agemonths=risk_age_months,
#             noncrop_breed=breed,
#             noncrop_vaccination=vaccination,
#             noncrop_hypothecated=hypothecation,
#             # hypothecatee_name=hypothecatee_name,
#             # hypothecatee_contact=hypothecatee_contact,
#             noncrop_taggingdate=datetime.strptime(tagging_date, '%Y-%m-%d') if tagging_date else None,
#             noncrop_suminsured=sum_insured,
#             noncrop_marketvalue=market_value,
#             noncrop_pregnancystatus=pregnancy_status,
#             # noncrop_milkingstatus=milking_status,
#             noncrop_calvingcycle=calving_cycle,
#             noncrop_animalcolor=animal_color,
#             noncrop_tailswitchcolour=animal_tail_color,
#             noncrop_lefthornshape=animal_left_horn_shape,
#             noncrop_righthornshape=animal_right_horn_shape,
#             # ear_tag_image=ear_tag_image,
#             # left_side_image=left_side_image,
#             # right_side_image=right_side_image,
#             # tail_image=tail_image,
#             # with_owner_image=with_owner_image,
#         )
#         en.save()

       

#     return render(request, "personaldetails.html")





def generate_qr(request):
    # Generate a unique ID
    unique_id = get_random_string(length=10)

    # URL to the image
    image_url = "http://127.0.0.1:8000/login/recipt=(promo_code=SDIET-SAVE20)" 
      # Replace with the actual URL of your image

    # Generate QR code with the unique ID and the image URL
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(image_url)
    qr.make(fit=True)

    # Create the QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Get the image data of the QR code
    img_byte_array = BytesIO()
    qr_img.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)

    # Return the QR code image as an HTTP response
    response = HttpResponse(img_byte_array, content_type='image/png')
    return response




# def savelogin(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         print(f"Username: {username}")
#         password = request.POST.get('password')
#         print(f"Password: {password}")

#         en = Homepage(homepage_username=username, homepage_password=password)
#         en.save()
        
#     return render(request, "login.html")




def savelogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username already exists in the database
        existing_user = Homepage.objects.filter(homepage_username=username).exists()

        if existing_user:
            # Handle case where username already exists
            return render(request, "login.html", {'error': 'Username already exists'})
        

        if Homesignup.objects.filter(homesignup_username=username).exists():
            # Authenticate the user
            if Homepage.objects.filter(homepage_username=username, homepage_password=password).exists():
                # Handle successful login
                # Redirect the user to their profile page or any other desired page
                return redirect('login.html')
            
            
            # else:
            #     # Handle incorrect password
            #     return render(request, "aichomepage.html", {'error': 'Incorrect password'})
        else:
            # Handle non-existing username
            return render(request, "aichomepage.html", {'error': 'User is not registered'})


        # Save to database
        # en = Homepage(homepage_username=username, homepage_password=password)
        # en.save()
        
    return render(request, "login.html")





def home(request):


 Data={
'title':'sewanxt portal',

# 'fns':'1',
# 'fna':'1',
# 'fnr':'0'


}
 return render(request,"aichomepage.html",Data)

def help(request):


 Data={
'title':'sewanxt portal',

# 'fns':'1',
# 'fna':'1',
# 'fnr':'0'


}
 return render(request,"help.html",Data)





def thankssignuppage(request):


 Data={
'title':'thanks page',

# 'fns':'1',
# 'fna':'1',
# 'fnr':'0'


}
 return render(request,"thankssignuppage.html",Data)



def login(request):


 Data={
'title':'login',




}
 return render(request,"login.html",Data)





def recipt(request):


 Data={
'title':'recipt',




}
 return render(request,"reciptpage.html",Data)




def noncrop(request):


 Data={
'title':'noncrop',




}
 return render(request,"noncrop.html",Data)




def Crop(request):


 Data={
'title':'crop',




}
 return render(request,"crop.html",Data)



def policydetails(request):


 Data={
'title':'policydetails',




}
 return render(request,"policydetails.html",Data)


def personaldetails(request):


 Data={
'title':'personaldetails',




}
 return render(request,"personaldetails.html",Data)




def planselection(request):


 Data={
'title':'plan-selection',




}
 return render(request,"planselection.html",Data)



def insurancedetails(request):


 Data={
'title':'insurance details',




}
 return render(request,"insurancedetails.html",Data)


def trainingppt(request):


 Data={
'title':'trainingppt',




}
 return render(request,"trainingppt.html",Data)





def certificate(request):


 Data={
'title':'trainingppt',




}
 return render(request,"certificate.html",Data)





 