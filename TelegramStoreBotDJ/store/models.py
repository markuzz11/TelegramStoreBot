from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название товара')
    photo = models.ImageField(upload_to="photos/", verbose_name='Фото')
    is_available = models.BooleanField(default=False, verbose_name='Наличие')
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

class Order(models.Model):
    orderId = models.AutoField(primary_key=True, verbose_name='Номер заказа')
    goodsName = models.CharField(max_length=40, verbose_name='Название товара')
    goodsId = models.IntegerField(verbose_name='ID товара')
    size = models.CharField(max_length=40, verbose_name='Размер')
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')

    def __str__(self):
        return str(self.orderId)

    def cartInfo(self):
        orderInfo = f'Номер заказа: <b>{self.orderId}</b>\n'
        goodsInfo = f'Товар(ы): <b>{self.goodsName}</b>\n'
        sizeInfo = f'Размер(ы): <b>{self.size}</b>\n'
        priceInfo = f'Стоимость: <b>{self.price}</b>\n'
        textInfo = orderInfo + goodsInfo + sizeInfo + priceInfo
        return textInfo

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

class Users(models.Model):
    userId = models.PositiveIntegerField(verbose_name='Id покупателя')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

class Status(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    status = models.ForeignKey('StatusVariables', on_delete=models.PROTECT, verbose_name='Статус',
                               default=lambda: StatusVariables.objects.get(name='Не оплачено'))

    def __str__(self):
        return str(self.status)

    class Meta:
        verbose_name = 'Статусы заказов'
        verbose_name_plural = 'Статусы заказов'

class StatusVariables(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Выбор статуса'
        verbose_name_plural = 'Выбор статуса'