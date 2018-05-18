from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import bcrypt


# define the validator
def ValidatedEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

# Create your models here.
class UserManager(models.Manager):

    def regValidator(self, form):

        errors = []
    # ---- TEST ---- First Test
        # print("-"*25)
        # print('Form: ', form)
        # print("-"*25)
        # return redirect('/')

        if len(form['fname']) < 2:
            errors.append("First name field cannot be at least 2 characters")
        if len(form['lname']) < 2:
            errors.append("Last name field cannot be at least 2 characters")
        if not form['email']:
            errors.append("First name field cannot be at least 2 characters")
        elif not ValidatedEmail(form['email']):
            errors.append("Must be valid email")
        if len(form['password']) < 6:
            errors.append("Email must be at least 5 characters")

        if not errors:
            hash_gen = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(fname=form['fname'], lname=form['lname'], email=form['email'], password=hash_gen)
            return(True, user)
        else:
            return(False, errors)


class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User: {}|{} {} | {}>".format(self.id, self.fname, self.lname, self.email)

    objects = UserManager()


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isSold = models.BooleanField(default=False)
    seller = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)

    def __repr__(self):
        return "<Product: {}|{} - {} | {}>".format(self.id, self.name, self.price, self.isSold)

# ---- Many-to-Many Relationship SETUP -------
class Sales(models.Model):
    product = models.ForeignKey(Product, related_name="sales_product", on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name="sales_buyer", on_delete=models.CASCADE)
    date_sold = models.DateTimeField()

    # form is the req.POST dictionary
    # def validator(self, form):
    #     errors = []
    #
    #     # if len(form['fname']) <1:
    #     if not form['first_name']:
    #         errors.append("First name is required.")
    #     if not form['last_name']:
    #         errors.append("Last name is required.")
    #     if not form['email']:
    #         errors.append("Email is required.")
    #     elif not ValidateEmail(form['email']):
    #         errors.append("Must be valid email format.")
    #
    #     if not errors:
    #         user = User.objects.create(first_name=form['first_name'], last_name=form['last_name'], email=form['email'])
    #         return (True, user)
    #     else:
    #         return (False, errors)
