from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

from django.contrib.auth.models import User
from manager_messages.models import Role, Profile

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name') #Columnas en el listar en el administrador
    list_display_links = ('pk',) #Que al precionar el elemento nos lleva al detalle
    list_editable = ('name',) #Que sea editable el valor
    search_fields = ('name',) #filtrar por este campo

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'role', 'user','first_name', 'last_name','picture') #Columnas en el listar en el administrador
    list_display_links = ('pk',) #Que al precionar el elemento nos lleva al detalle
    list_editable = ('first_name','last_name') #Que sea editable el valor
    search_fields = ('role__name','user__username','first_name','last_name') #filtrar por este campo
    list_filter = ('role__name','user__username','first_name','last_name') #filtrar por este campo de forma parcial

    fieldsets = ( 
        ('Información del usuario y tipo', { #Titilo de la seccion
            "fields": ( #ubicacion de los filed en el formulario de crear y modificar
                ('user', 'role'),
            ) 
        }),
        ('Informacion de nombres', { #Titilo de la seccion
            "fields": ( #ubicacion de los filed en el formulario de crear y modificar
                ('first_name','last_name'),
            ) 
        }),
        ('Informacion de la bibliografia', { #Titilo de la seccion
            "fields": ( #ubicacion de los filed en el formulario de crear y modificar
                ('bibliography',),
            ) 
        }),
        ('Otros', { #Titilo de la seccion
            "fields": ( #ubicacion de los filed en el formulario de crear y modificar
                ('birthdate','picture'),
            ) 
        }),
        ('Creacion y ultima del perfil', { #Titilo de la seccion
            "fields": ( #ubicacion de los filed en el formulario de crear y modificar
                ('created','modified'),
            ) 
        })
    )
    readonly_fields = ('created','modified', 'role', 'user') #Solo visible no se puede editar


#Vincular varios formularios en uno

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Perfil'
    fieldsets = ( 
        ('Información del usuario y tipo', { #Titilo de la seccion
            "fields": ( #ubicacion de los filed en el formulario de crear y modificar
                ('role',),
            ) 
        }),
        ('Informacion de nombres', { #Titilo de la seccion
            "fields": ( #ubicacion de los filed en el formulario de crear y modificar
                ('first_name','last_name'),
            ) 
        }),
        ('Informacion de la bibliografia', { #Titilo de la seccion
            "fields": ( #ubicacion de los filed en el formulario de crear y modificar
                ('bibliography',),
            ) 
        }),
        ('Otros', { #Titilo de la seccion
            "fields": ( #ubicacion de los filed en el formulario de crear y modificar
                ('birthdate','picture'),
            ) 
        }),
        ('Creacion y ultima del perfil', { #Titilo de la seccion
            "fields": ( #ubicacion de los filed en el formulario de crear y modificar
                ('created','modified'),
            ) 
        })
    )
    readonly_fields = ('created','modified', 'role') #Solo visible no se puede editar

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)