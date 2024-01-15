from django.db import models
from users.models import User

class Products(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products_image',null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'Название: {self.name}'

class Purchase(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Пользователь: {self.user.username} | Товар: {self.product.name}'

class Return(models.Model):
    purchase = models.ForeignKey(to=Purchase, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Пользователь: {self.purchase.user.username} | Товар: {self.purchase.product.name}'


