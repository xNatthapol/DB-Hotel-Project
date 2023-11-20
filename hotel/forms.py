from django import forms
from django.utils import timezone

import hotel
from  .models import Customer, Payment, Facility, Room, ReservedRoom, ReservedFacility, Stock, Ingredient, MealList, Recipe, Employee, Role

class DynamicForm(forms.Form):
    def __init__(self, fields, *args, **kwargs):
        super(DynamicForm, self).__init__(*args, **kwargs)

        for field_name, field_type in fields.items():
            if field_type == 'char':
                self.fields[field_name] = forms.CharField(label=field_name)
            elif field_type == 'integer':
                self.fields[field_name] = forms.IntegerField(label=field_name)
            elif field_type == 'email':
                self.fields[field_name] = forms.EmailField(label=field_name)
            elif field_type == 'decimal':
                self.fields[field_name] = forms.DecimalField(label=field_name)
            elif field_type == 'datetime':
                self.fields[field_name] = forms.DateTimeField(label=field_name)
            elif field_type == 'boolean':
                self.fields[field_name] = forms.BooleanField(label=field_name)
            elif field_type == 'date':
                self.fields[field_name] = forms.DateField(label=field_name)
            elif field_type == 'time':
                self.fields[field_name] = forms.TimeField(label=field_name)
            elif field_type[0] == 'foreignkey':
                self.handle_foreign_key(field_name)

    def handle_foreign_key(self, field_name):
        model_mapping = {
            'customer': Customer,
            'payment': Payment,
            'facility': Facility,
            'room': Room,
            'reservedroom': ReservedRoom,
            'reservedfacility': ReservedFacility,
            'stock': Stock,
            'ingredient': Ingredient,
            'meallist': MealList,
            'recipe': Recipe,
            'employee': Employee,
            'role': Role,
            # Add more models as needed
        }
        related_model = model_mapping.get(field_name.lower())

        if related_model:
            # Generate the dynamic form field for the foreign key
            self.fields[field_name] = forms.ModelChoiceField(
                queryset=related_model.objects.all(),
                label=field_name.capitalize()
                # Capitalize the field name for better display
            )


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'checkin_time',
            'checkout_time'
        ]

    def clean(self):
        cleaned_data = super().clean()
        checkin_time = cleaned_data.get("checkin_time")
        checkout_time = cleaned_data.get("checkout_time")

        # Ensure checkin_time and checkout_time are not None before comparison
        if checkin_time is not None and checkout_time is not None:
            if checkin_time > checkout_time:
                raise forms.ValidationError(
                    "Checkin time should be before checkout time"
                )

        # Additional validation logic if needed

        return cleaned_data

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'amount',
            'money_type',
            'transaction_type',
            'description',
        ]

    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get("amount")

        if amount is not None and amount < 0:
            raise forms.ValidationError(
                "Amount should be positive"
            )

        return cleaned_data

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = [
            'name',
            'cost_per_hour',
        ]

    def clean(self):
        cleaned_data = super().clean()
        cost_per_hour = cleaned_data.get("cost_per_hour")
        if cost_per_hour is not None and cost_per_hour < 0:
            raise forms.ValidationError(
                "Cost per hour should be positive"
            )
        return cleaned_data


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = [
            'floor',
            'room_type',
            'accommodates',
            'is_available',
        ]

    def clean(self):
        cleaned_data = super().clean()
        accommodates = cleaned_data.get("accommodates")
        if accommodates is not None and accommodates < 0:
            raise forms.ValidationError(
                "Accommodates should be positive"
            )
        return cleaned_data


class ReservedRoomForm(forms.ModelForm):
    class Meta:
        model = ReservedRoom
        fields = [
            'customer',
            'room',
            'room_number',
            'checkin_time',
            'checkout_time',
        ]

    def clean(self):
        cleaned_data = super().clean()
        checkin_time = cleaned_data.get("checkin_time")
        checkout_time = cleaned_data.get("checkout_time")
        if checkin_time is not None and checkout_time is not None:
            if checkin_time > checkout_time:
                raise forms.ValidationError(
                    "Checkin time should be before checkout time"
                )
        return cleaned_data

class ReservedFacilityForm(forms.ModelForm):
    class Meta:
        model = ReservedFacility
        fields = [
            'customer',
            'facility',
            'checkin_time',
            'checkout_time',
        ]

    def clean(self):
        cleaned_data = super().clean()
        checkin_time = cleaned_data.get("checkin_time")
        checkout_time = cleaned_data.get("checkout_time")
        if checkin_time is not None and checkout_time is not None:
            if checkin_time > checkout_time:
                raise forms.ValidationError(
                    "Checkin time should be before checkout time"
                )
        return cleaned_data

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [
            'ingredient_name',
            'quantity',
            'type',
        ]

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get("quantity")
        if quantity is not None and quantity < 0:
            raise forms.ValidationError(
                "Quantity should be positive"
            )
        return cleaned_data

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'recipe',
            'stock',
            'ingredients_measure',
            'measure_type',
        ]

    def clean(self):
        cleaned_data = super().clean()
        ingredients_measure = cleaned_data.get("ingredients_measure")
        if ingredients_measure is not None and ingredients_measure < 0:
            raise forms.ValidationError(
                "Ingredients measure should be positive"
            )
        return cleaned_data

class MealListForm(forms.ModelForm):
    class Meta:
        model = MealList
        fields = [
            'recipe',
            'quantity_ordered',
            'date',
        ]

    def clean(self):
        cleaned_data = super().clean()
        quantity_ordered = cleaned_data.get("quantity_ordered")
        if quantity_ordered is not None and quantity_ordered < 0:
            raise forms.ValidationError(
                "Quantity ordered should be positive"
            )
        return cleaned_data

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'menu_name',
            'portion_size',
            'price',
        ]

    def clean(self):
        cleaned_data = super().clean()
        portion_size = cleaned_data.get("portion_size")
        price = cleaned_data.get("price")
        if portion_size is not None and price is not None:
            if portion_size < 0:
                raise forms.ValidationError(
                    "Portion size should be positive"
                )
            if price < 0:
                raise forms.ValidationError(
                    "Price should be positive"
                )
        return cleaned_data

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'role',
            'first_name',
            'last_name',
            'phone_number',
            'email',
        ]

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get("phone_number")
        if phone_number is not None and phone_number < 0:
            raise forms.ValidationError(
                "Phone number should be positive"
            )
        return cleaned_data

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = [
            'role_name',
            'base_salary',
        ]

    def clean(self):
        cleaned_data = super().clean()
        base_salary = cleaned_data.get("base_salary")
        if base_salary is not None and base_salary < 0:
            raise forms.ValidationError(
                "Base salary should be positive"
            )
        return cleaned_data
