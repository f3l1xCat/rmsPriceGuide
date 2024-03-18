from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.contrib import messages
# Create your models here.

class stuff(models.Model):
    EQUIPMENT = 'E'
    USABLE = 'U'
    SET_UP = 'S'
    ETC = 'T'
    NX = 'N'
    type_choices = [
        (EQUIPMENT, 'Equipment'),
        (USABLE, 'Use'),
        (SET_UP, 'Set-up'),
        (ETC, 'Etc'),
        (NX, 'NX')
    ]

    stuff_name = models.CharField(max_length=60, unique=True, blank=False)
    category = models.CharField(max_length=1, choices=type_choices)
    stuff_image = models.ImageField(upload_to='stuff_images', blank=False)

    def __str__(self):
        return self.stuff_name
    
class equipInfo(models.Model):
    equip_name = models.ForeignKey(stuff,unique=True, on_delete=models.CASCADE, limit_choices_to={'category': 'E'})
    STR = models.PositiveIntegerField(validators=[MaxValueValidator(200)], default=0)
    DEX = models.PositiveIntegerField(validators=[MaxValueValidator(200)], default=0)
    INT = models.PositiveIntegerField(validators=[MaxValueValidator(300)], default=0)
    LUK = models.PositiveIntegerField(validators=[MaxValueValidator(200)], default=0)
    ACC = models.PositiveIntegerField(validators=[MaxValueValidator(150)], default=0)
    Avoid = models.PositiveIntegerField(validators=[MaxValueValidator(150)], default=0)
    att = models.PositiveIntegerField(validators=[MaxValueValidator(250)], default=0)
    Matt = models.PositiveIntegerField(validators=[MaxValueValidator(300)], default=0)
    slot = models.PositiveIntegerField(validators=[MaxValueValidator(100)],default=7)
    

    def __str__(self):
        return self.equip_name.stuff_name
    

class transaction_equip(models.Model):
    equip_name = models.ForeignKey(equipInfo, on_delete=models.CASCADE)
    # equip_name = models.CharField(max_length=60, blank=True)
    STR = models.PositiveIntegerField(validators=[MaxValueValidator(250)], default=0)
    DEX = models.PositiveIntegerField(validators=[MaxValueValidator(250)], default=0)
    INT = models.PositiveIntegerField(validators=[MaxValueValidator(250)], default=0)
    LUK = models.PositiveIntegerField(validators=[MaxValueValidator(250)], default=0)
    ACC = models.PositiveIntegerField(validators=[MaxValueValidator(150)], default=0)
    Avoid = models.PositiveIntegerField(validators=[MaxValueValidator(150)], default=0)
    att = models.PositiveIntegerField(validators=[MaxValueValidator(250)], default=0)
    Matt = models.PositiveIntegerField(validators=[MaxValueValidator(300)], default=0)
    slot = models.PositiveIntegerField(validators=[MaxValueValidator(90)], default=7)
    price = models.CharField(max_length=10)
    is_clean = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True, blank=True)

    # objects = TransactionEquipManager()
    def clean(self):
        # Cleanliness validation
        if self.is_clean:
            if (
                self.STR > self.equip_name.STR
                or self.DEX > self.equip_name.DEX
                or self.INT > self.equip_name.INT
                or self.LUK > self.equip_name.LUK
                or self.ACC > self.equip_name.ACC
                or self.Avoid > self.equip_name.Avoid
                or self.att > self.equip_name.att
                or self.Matt > self.equip_name.Matt
            ):
                raise ValidationError(
                    "Values cannot exceed corresponding values of equip"
                )
        #else:

        # Slot validation (always applies)
        if self.slot > self.equip_name.slot:
            raise ValidationError("Slot cannot exceed equip's maximum slot.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Call clean method for validation before saving
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.equip_name.equip_name.stuff_name
    
    # get foreign key related equipInfo's slot value
    # def get_slot(self):
    #     return self.equip_name.slot
    
    
    
class transaction_others(models.Model):
    others_name = models.ForeignKey(stuff, on_delete=models.CASCADE, limit_choices_to=Q(category='U') | Q(category='S') | Q(category='T') | Q(category='N'))
    # others_name = models.CharField(max_length=60, blank=True)
    price = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.others_name.stuff_name
    

@admin.register(stuff)
class stuffAdmin(admin.ModelAdmin):
    list_display = [field.name for field in stuff._meta.fields]
    list_filter = ('category',)
    search_fields = ('stuff_name',)


@admin.register(transaction_equip)
class transaction_equipAdmin(admin.ModelAdmin):
    list_display = [field.name for field in transaction_equip._meta.fields]
    list_filter = ('slot','is_clean',)
    search_fields = ('equip_name__equip_name__stuff_name', 'STR', 'DEX', 'INT', 'LUK', 'ACC', 'Avoid', 'att', 'Matt', )
    autocomplete_fields = ["equip_name"]

    def save_model(self, request, obj, form, change):
        try:
            obj.clean()
        except ValidationError as e:
            self.message_user(request, str(e), messages.ERROR)
            return

        # Save the object if no errors
        super().save_model(request, obj, form, change)


@admin.register(transaction_others)
class transaction_othersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in transaction_others._meta.fields]
    search_fields = ('others_name__stuff_name',)
    autocomplete_fields = ["others_name"]

@admin.register(equipInfo)
class equipInfoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in equipInfo._meta.fields]
    search_fields = ('equip_name__stuff_name', 'slot',)
    autocomplete_fields = ["equip_name"]
    list_filter = ('slot',)
