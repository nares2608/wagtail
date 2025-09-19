from .models.snippets import Menus, FooterMenu
from .models.blocks import *
from .models.settings import *
def global_settings(request):
    return {
        "menus": Menus.objects.all(),
        "footermenus": FooterMenu.objects.all(),
        

    }
        