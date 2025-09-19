from core.models.snippets import Menus, FooterMenu, FAQ, Service, Package, Testimonial
 
def global_context(request):
    return {
        "menus": Menus.objects.all(),
        "footermenus": FooterMenu.objects.all(),
        

    }
