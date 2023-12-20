from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


# Create your models here.
class Car(models.Model):

    state_choice = (
        ('KZ', 'Qazaqstan'),
    )

    # year_choice = []
    
    # for r in range(2000, (datetime.now().year+1)):
    #     year_choice.append((r,r))

    features_choices = (
        ('Экологичные материалы', 'Экологичные материалы'),
        ('Поддержка местных производителей', 'Поддержка местных производителей'),
        ('Сезонные коллекции', 'Сезонные коллекции'),
        ('Эксклюзивные дизайны', 'Эксклюзивные дизайны'),
        ('Размерная сетка включает плюс-сайзы', 'Плюс-сайзы в размерной сетке'),
        ('Стремление к устойчивости', 'Устойчивость и этическое производство'),
        ('Бесплатная доставка', 'Бесплатная доставка при определенной сумме заказа'),
        ('Программа лояльности', 'Программа лояльности для постоянных клиентов'),
        ('Примерка перед покупкой', 'Возможность примерки перед покупкой'),
        ('Стилистические консультации', 'Индивидуальные стилистические консультации'),
        ('Электронные подарочные сертификаты', 'Электронные подарочные сертификаты'),
        ('Быстрый обмен и возврат', 'Удобная политика обмена и возврата'),
        ('Трендовые коллекции', 'Представление последних трендов в мире моды'),
        ('Электронные уведомления о новинках', 'Уведомления о новых поступлениях по электронной почте'),
    )

    # features_choices = (
        # ('Круиз-контроль', 'Круиз-контроль'),
        # ('Аудиоинтерфейс', 'Аудиоинтерфейс'),
        # ('Подушки безопасности', 'Подушки безопасности'),
        # ('Кондиционер', 'Кондиционирование воздуха'),
        # ('Подогрев сидений', 'Подогрев сидений'),
        # ('Сигнализация', 'Система охранной сигнализации'),
        # ("Парковщик", "Парковщик"),
        # ("Гидроусилитель руля", "Гидроусилитель рулевого управления"),
        # ("Камера заднего вида", "Камера заднего вида"),
        # ("Непосредственный впрыск топлива", "Непосредственный впрыск топлива"),
        # ('Автоматический запуск/остановка', "Автоматический запуск/остановка"),
        # ("Ветроотражатель", "Ветроотражатель"),
        # ('Bluetooth', 'Bluetooth'),
        # ('Cruise Control', 'Cruise Control'),
        # ('Audio Interface', 'Audio Interface'),
        # ('Airbags', 'Airbags'),
        # ('Air Conditioning', 'Air Conditioning'),
        # ('Seat Heating', 'Seat Heating'),
        # ('Alarm System', 'Alarm System'),
        # ('ParkAssist', 'ParkAssist'),
        # ('Power Steering', 'Power Steering'),
        # ('Reversing Camera', 'Reversing Camera'),
        # ('Direct Fuel Injection', 'Direct Fuel Injection'),
        # ('Auto Start/Stop', 'Auto Start/Stop'),
        # ('Wind Deflector', 'Wind Deflector'),
        # ('Bluetooth Handset', 'Bluetooth Handset'),
    # )












    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )

    # door_choices = (
        # ('2', '2'),
        # ('3', '3'),
        # ('4', '4'),
        # ('5', '5'),
        # ('6', '6'),
    # )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)

    # city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    # year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    # interior = models.CharField(max_length=100)
    # miles = models.IntegerField()
    # doors = models.CharField(choices=door_choices, max_length=10)
    # passengers = models.IntegerField()
    # vin_no = models.CharField(max_length=100)
    # milage = models.IntegerField()
    # fuel_type = models.CharField(max_length=50)
    # size = models.CharField(max_length=50)
    # no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    # status=models.CharField(max_length=50,null=True,choices=STATUS)


# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    def __str__(self):
        return self.name












class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    car=models.ForeignKey('Car', on_delete=models.CASCADE,null=True)
    # product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    # email = models.CharField(max_length=50,null=True)
    # address = models.CharField(max_length=500,null=True)
    # mobile = models.CharField(max_length=20,null=True)
    # order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name




    def __str__(self):
        return self.car_title
