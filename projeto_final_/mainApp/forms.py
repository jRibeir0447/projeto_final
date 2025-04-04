from django.forms import ModelForm, Textarea, TextInput, EmailInput, PasswordInput, NumberInput, SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import modelformset_factory
from django.forms.models import inlineformset_factory
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms import inlineformset_factory
from django.utils.translation import ugettext_lazy as _
#from PIL import *


class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'inputType1', 'type':'password', 'placeholder':_('Palavra-passe')}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'inputType1', 'type':'password', 'placeholder':_('Confirme a palavra-passe')})
    )

    error_messages = {
        'password_mismatch': _("As passwords não são iguais"),
    }
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

        widgets = {
            "username": TextInput(
                attrs={
                    "placeholder":_('Nome de Utilizador'),
                    'class': 'inputType1'
                }
            )
            ,"first_name": TextInput(
                attrs={
                    "placeholder":_('Primeiro nome'),
                    'class': 'inputType1'
                }
            )
            ,"last_name": TextInput(
                attrs={
                    "placeholder":_('Apelido'),
                    'class': 'inputType1'
                }
            )
            ,"email": EmailInput(
                attrs={
                    "placeholder":'E-mail',
                    'class': 'inputType1'
                }
            )
        }
    # def clean_email(self):
    #     # Get the email
    #     email = self.cleaned_data.get('email')

    #     # Check to see if any users already exist with this email as a username.
    #     try:
    #         match = User.objects.get(email=email)
    #     except User.DoesNotExist:
    #         # Unable to find a user, this is fine
    #         return email

    #     # A user was found with this as a username, raise an error.
    #     raise forms.ValidationError('This email address is already in use.')

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileForm(forms.ModelForm):

    class Meta:
        model = App_user
        fields = ['phoneNumber', 'birthDate','address','nif']

        widgets = {
            "phoneNumber": NumberInput(
                attrs={
                    "placeholder":_('Número de telefone'),
                    'class': 'inputType1'
                }
            )
            ,"birthDate": DateInput(
                attrs={
                    'class': 'inputType1',
                    'id': 'datefield'

                }
            )
            , "address" : TextInput(
                attrs={
                    'placeholder': _('Morada'),
                    'class': 'inputType1'
                }
            )
            , "nif" : NumberInput(
                attrs={
                    'placeholder': _('NIF'),
                    'class': 'inputType1'
                }
            )
        }

class ListingForm(forms.ModelForm):

    #listing_type = forms.CharField(required=True, max_length=25)
    allowed_gender = forms.CharField(required=True, max_length=25)
    monthly_payment = forms.IntegerField(required=True)
    availability_starts = forms.DateField()
    availability_ending = forms.DateField()
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=100)
    security_deposit = forms.IntegerField()
    max_occupancy = forms.IntegerField(required=True)

    class Meta:
        model = Listing
        fields = [
            'allowed_gender',
            'monthly_payment',
            'availability_starts',
            'availability_ending',
            'title',
            'description',
            'security_deposit',
            'max_occupancy']

class PropertyForm(forms.ModelForm):
    address = forms.CharField(required=True, max_length=100)
    bedrooms_num = forms.IntegerField(required=True) 
    bathrooms_num = forms.IntegerField(required=True)
    kitchens_num = forms.IntegerField(required=True)
    livingrooms_num = forms.IntegerField(required=True)
    latitude = forms.CharField(required=True, max_length=100)
    longitude = forms.CharField(required=True, max_length=100)
    listing_type = forms.CharField(required=True, max_length=25)
    floor_area = forms.IntegerField(required=True, initial=0)

    #booleans
    smoke = forms.BooleanField(required=False, initial=False)
    garden = forms.BooleanField(required=False, initial=False)
    garage = forms.BooleanField(required=False, initial=False)
    street_parking = forms.BooleanField(required=False, initial=False)
    internet = forms.BooleanField(required=False, initial=False)
    electricity = forms.BooleanField(required=False, initial=False)            
    water = forms.BooleanField(required=False, initial=False)   
    gas = forms.BooleanField(required=False, initial=False)
    pets = forms.BooleanField(required=False, initial=False)
    overnight_visits = forms.BooleanField(required=False, initial=False)
    cleaning_services = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = Property
        fields = [
            'listing_type',
            'latitude',
            'longitude',
            'address',
            'bedrooms_num',
            'smoke',
            'garden',
            'garage',
            'street_parking',
            'internet',
            'electricity',            
            'water',  
            'gas',
            'pets',
            'overnight_visits',
            'cleaning_services',
            'floor_area']


class BedroomForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BedroomForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if "num_" not in field_name and field_name != "max_occupancy":
                if field.widget.attrs.get('class'):
                    field.widget.attrs['class'] += 'custom-control-input'
                else:
                    field.widget.attrs['class']='custom-control-input'
            else:
                field.widget.attrs['min'] = '0'
                field.widget.attrs['value'] = 0
                

    be_chairs = forms.BooleanField(required=False, initial=False)
    be_sofa = forms.BooleanField(required=False, initial=False)
    be_sofa_bed = forms.BooleanField(required=False, initial=False)
    be_window = forms.BooleanField(required=False, initial=False)
    num_single_beds = forms.IntegerField(required=True)
    num_double_beds = forms.IntegerField(required=True)
    max_occupancy = forms.IntegerField(required=True)
    be_balcony = forms.BooleanField(required=False, initial=False)
    wardrobe = forms.BooleanField(required=False, initial=False)
    be_desk = forms.BooleanField(required=False, initial=False)
    lock = forms.BooleanField(required=False, initial=False)
    chest_of_drawers = forms.BooleanField(required=False, initial=False)
    tv = forms.BooleanField(required=False, initial=False)
    heater = forms.BooleanField(required=False, initial=False)
    air_conditioning = forms.BooleanField(required=False, initial=False)
    ensuite_bathroom = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = Bedroom
        fields = [
            "be_chairs",
            "be_sofa",
            "be_sofa_bed",
            "be_window",
            "num_single_beds",
            "num_double_beds",
            "max_occupancy",
            "be_balcony",
            "wardrobe",
            "be_desk",
            "lock",
            "chest_of_drawers",
            "tv",
            "heater",
            "air_conditioning",
            "ensuite_bathroom"]

        """ widget={
            'be_chairs' : forms.CheckboxInput(attrs={'class':'custom-control-input'})} """


class KitchenForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(KitchenForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += 'custom-control-input'
            else:
                field.widget.attrs['class']='custom-control-input'
    
    oven = forms.BooleanField(required=False, initial=False)
    fridge = forms.BooleanField(required=False, initial=False)
    k_table = forms.BooleanField(required=False, initial=False)
    laundering_machine = forms.BooleanField(required=False, initial=False)
    freezer = forms.BooleanField(required=False, initial=False)
    k_chairs = forms.BooleanField(required=False, initial=False)
    microwave = forms.BooleanField(required=False, initial=False)
    k_window = forms.BooleanField(required=False, initial=False)
    k_balcony = forms.BooleanField(required=False, initial=False)
    dish_washer = forms.BooleanField(required=False, initial=False)
    dishwasher_machine = forms.BooleanField(required=False, initial=False)
    dryer = forms.BooleanField(required=False, initial=False)
    pans_pots = forms.BooleanField(required=False, initial=False)
    dishes_cutlery = forms.BooleanField(required=False, initial=False)
    cooker = forms.BooleanField(required=False, initial=False)
    class Meta:
        model = Kitchen
        fields = [
            'oven',
            'fridge',
            'k_table',
            'laundering_machine',
            'freezer',
            'k_chairs',
            'microwave',
            'k_window',
            'k_balcony',
            'dish_washer',
            'dishwasher_machine',
            'dryer',
            'pans_pots',
            'dishes_cutlery',
            'cooker',]



class BathroomForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BathroomForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += 'custom-control-input'
            else:
                field.widget.attrs['class']='custom-control-input'

    shower = forms.BooleanField(required=False, initial=False)
    bathtub = forms.BooleanField(required=False, initial=False)
    bidet = forms.BooleanField(required=False, initial=False)
    toilet = forms.BooleanField(required=False, initial=False)
    sink = forms.BooleanField(required=False, initial=False)
    b_window = forms.BooleanField(required=False, initial=False)
    class Meta:
        model = Bathroom
        fields = [
            'shower',
            'bathtub',
            'bidet',
            'toilet', 
            'sink',
            'b_window']



class LivingroomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LivingroomForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += 'custom-control-input'
            else:
                field.widget.attrs['class']='custom-control-input'

    l_sofa = forms.BooleanField(required=False, initial=False)
    l_sofa_bed = forms.BooleanField(required=False, initial=False)
    l_chairs = forms.BooleanField(required=False, initial=False)
    l_window = forms.BooleanField(required=False, initial=False)
    l_table = forms.BooleanField(required=False, initial=False)
    l_desk = forms.BooleanField(required=False, initial=False)
    l_balcony = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = Livingroom
        fields = [
            'l_sofa',
            'l_sofa_bed',
            'l_chairs',
            'l_window',
            'l_table',
            'l_desk',
            'l_balcony']


"""class AgreementForm(forms.ModelForm):
    startsDate = forms.DateField()
    endDate = forms.DateField()
    
    class Meta:
        model = Agreement
        fields = [
            'startsDate',   
            'endDate'] """ #expandiu-se para dentro do agreement request #yolo

class Agreement_Request_Form(forms.ModelForm):

    startsDate = forms.DateField()
    endDate = forms.DateField()
    message = RichTextField(null=True, blank=True)


    class Meta:
        model = Agreement_Request
        fields = [
            'startsDate',
            'endDate',
            'message']

class ImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += 'imgfield form-control-file'
            else:
                field.widget.attrs['class']='imgfield form-control-file'
                
            if field.widget.attrs.get('onchange'):
                field.widget.attrs['onchange'] += 'upload_img(this);'
            else:
                field.widget.attrs['onchange']='upload_img(this);'

    images = forms.ImageField()

    class Meta:
        model = Image
        fields = ['images' ]

TYPE_CHOICES =( 
    ("", _("Tipo de Alojamento")), 
    ("Apartment", _("Apartamento")), 
    ("House", _("Casa")), 
    ("Studio", _("Estúdio")), 
    ("Bedroom", _("Quarto"))
) 
NUM_TENANTS_CHOICES =( 
    ("", _("Número de Inquilinos")), 
    ("1", _("1 inquilino")), 
    ("2", _("2 inquilinos")), 
    ("3", _("3 inquilinos")), 
    ("4", _("4 inquilinos")), 
    ("5", _("5+ inquilinos")), 
) 
NUM_BEDROOMS_CHOICES =( 
    ("", _("Número de Quartos")), 
    ("1", _("1 quarto")), 
    ("2", _("2 quartos")), 
    ("3", _("3 quartos")), 
    ("4", _("4 quartos")), 
    ("5", _("5+ quartos")), 
) 
class SearchForm(forms.Form):
    location = forms.CharField(required=False, max_length=100, 
        widget=forms.TextInput(
            attrs={
                "class":"form-control border-left-0 pl-0 border-info border-3 rounded-right",
                "placeholder":_("Localização"),
                "required":True
            }
        )
    )
    radius = forms.IntegerField(required=False,
        widget=forms.NumberInput(
            attrs={
                "class":"form-control border-info border-3 rounded-left",
                "placeholder":_("Raio"),
                "required":True
            }
        )
    )
    type = forms.ChoiceField(choices = TYPE_CHOICES, required=False,
        widget=forms.Select(
            attrs={
                "class":"form-select form-control border-info border-3 p-1"
            }
        )
    )
    num_tenants = forms.ChoiceField(choices = NUM_TENANTS_CHOICES, required=False,
        widget=forms.Select(
            attrs={
                "class":"form-select form-control border-info border-3 p-1"
            }
        )
    )
    num_bedrooms = forms.ChoiceField(choices = NUM_BEDROOMS_CHOICES, required=False,
        widget=forms.Select(
            attrs={
                "class":"form-select form-control border-info border-3 p-1"
            }
        )
    )
    date_in = forms.DateField(required=False,
        widget=forms.DateInput(
            attrs={
                "class":"form-control border-info border-3 textbox-n",
                "placeholder": _("Entrada"),
                "onfocus":"(this.type='date')",
                "onblur":"(this.type='text')"
            }
        )
    )
    date_out = forms.DateField(required=False,
        widget=forms.DateInput(
            attrs={
                "class":"form-control border-info border-3 textbox-n",
                "placeholder": _("Saída"),
                "onfocus":"(this.type='date')",
                "onblur":"(this.type='text')"
            }
        )
    )
    minPrice = forms.CharField(required=True,
        widget=forms.TextInput(
            attrs={
                "hidden":True,
                "id":"minPrice",
                "value":"450"
            }
        )
    )
    maxPrice = forms.CharField(required=True,
        widget=forms.TextInput(
            attrs={
                "hidden":True,
                "id":"maxPrice",
                "value":"1200"
            }
        )
    )


    
class UpdatePropertyForm(forms.ModelForm):
    address = forms.CharField(required=True, max_length=100)
    bedrooms_num = forms.IntegerField(required=False) 
    bathrooms_num = forms.IntegerField(required=False)
    kitchens_num = forms.IntegerField(required=False)
    livingrooms_num = forms.IntegerField(required=False)
    latitude = forms.CharField(required=True, max_length=100)
    longitude = forms.CharField(required=True, max_length=100)
    listing_type = forms.CharField(required=True, max_length=20)

    #booleans
    smoke = forms.BooleanField(required=False, initial=False)
    garden = forms.BooleanField(required=False, initial=False)
    garage = forms.BooleanField(required=False, initial=False)
    street_parking = forms.BooleanField(required=False, initial=False)
    internet = forms.BooleanField(required=False, initial=False)
    electricity = forms.BooleanField(required=False, initial=False)            
    water = forms.BooleanField(required=False, initial=False)   
    gas = forms.BooleanField(required=False, initial=False)
    pets = forms.BooleanField(required=False, initial=False)
    overnight_visits = forms.BooleanField(required=False, initial=False)
    cleaning_services = forms.BooleanField(required=False, initial=False)
    floor_area = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = Property
        fields = [
            'listing_type',
            'latitude',
            'longitude',
            'address',
            'smoke',
            'garden',
            'garage',
            'street_parking',
            'internet',
            'electricity',            
            'water',  
            'gas',
            'pets',
            'overnight_visits',
            'cleaning_services',
            'floor_area']

class UpdateUserForm(forms.Form):
    image = forms.ImageField(required=False)
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    address = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True, max_length=75)
    phoneNumber = forms.IntegerField(required=True, max_value= 999999999)
    nif = forms.IntegerField(required=True, min_value= 100000000, max_value= 999999999)
    birthDate = forms.DateField(required=True)
    university = forms.CharField(required=False, max_length=100)
    min_search = forms.IntegerField(required=False, max_value= 1000)
    max_search = forms.IntegerField(required=False, max_value= 2000)
    if image.widget.attrs.get('onchange'):
        image.widget.attrs['onchange'] += 'upload_img(this);'
    else:
        image.widget.attrs['onchange']='upload_img(this);'

class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileImage, self).__init__(*args, **kwargs)
        '''for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += 'imgfield form-control-file'
            else:
                field.widget.attrs['class']='imgfield form-control-file'
                
            if field.widget.attrs.get('onchange'):
                field.widget.attrs['onchange'] += 'upload_img(this);'
            else:
                field.widget.attrs['onchange']='upload_img(this);'''

    images = forms.ImageField()

    class Meta:
        model = App_user
        fields = ['image' ]

class GetChat(forms.Form):
    chat_id = forms.IntegerField(required=True)

class SendMessage(forms.Form):
    chat_id = forms.IntegerField(required=True)
    content =  forms.CharField(required=True, max_length=200)

class CreateChat(forms.Form):
    receiver = forms.IntegerField(required=True)

class RichTextForm(ModelForm):
    class Meta:
        model = Rich_Text_Message
        fields = ['message']

BedroomFormSet = modelformset_factory(model = Bedroom, form = BedroomForm, extra=1)

KitchenFormSet = modelformset_factory(model = Kitchen, form = KitchenForm, extra=1)

BathroomFormSet = modelformset_factory(model = Bathroom, form = BathroomForm, extra=1)

LivingroomFormSet = modelformset_factory(model = Livingroom, form = LivingroomForm, extra=1)

ImgFormSet = modelformset_factory(model = Image, form = ImageForm, extra=1)

ListingFormSet = modelformset_factory(model = Listing, form = ListingForm, extra=1)
