from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from uuid import uuid4


class MyAccountManager(BaseUserManager):
     
    def create_user(self, first_name, last_name, phone_number, email, password = None):
        if not email:
            raise ValueError("Email address is mandatory")
        if not password:
            raise ValueError("password is mandatory")
            
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, first_name, last_name, phone_number, email, password = None):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number
        )
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using = self._db)
        return user
            

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    profile_pic = models.ImageField(upload_to='user/profile_pic/',null=True,blank=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'first_name', 'last_name', 'phone_number']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.email
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}' 
    
    def has_perm(self, perm, obj = None):
        return self.is_superadmin
    
    def has_module_perms(self, add_label):
        return True
class BaseModle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)   
    
    class Meta:
        abstract = True
        
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    name = models.CharField(max_length=100)
    user = models.OneToOneField("Account", on_delete=models.CASCADE, related_name='author', null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)  
    image_url = models.URLField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    fans_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Book(BaseModel):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name='books')
    description = models.TextField()
    work_id = models.CharField(max_length=100, unique=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    isbn13 = models.CharField(max_length=20, blank=True, null=True)
    asin = models.CharField(max_length=20, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    average_rating = models.FloatField(default=0)
    rating_dist = models.TextField(blank=True, null=True)  # Can be processed separately
    ratings_count = models.IntegerField(default=0)
    text_reviews_count = models.IntegerField(default=0)
    publication_date = models.DateField(blank=True, null=True)
    original_publication_date = models.DateField(blank=True, null=True)
    format = models.CharField(max_length=50, blank=True, null=True)
    edition_information = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    num_pages = models.IntegerField(blank=True, null=True)
    series_id = models.CharField(max_length=100, blank=True, null=True)
    series_name = models.CharField(max_length=255, blank=True, null=True)
    series_position = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title