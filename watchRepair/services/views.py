from django.shortcuts import render


# ===============================/ Pagina inicial home /======================== #
def home(request):
    return render(request, 'home.html') # Pagina de inicio


# ===============================/ Pagina servicios /======================== #

def services(request):
    return render(request, 'services.html') # Pagina de servicios.

# ===============================/ Pagina Nosotros /======================== #

def aboutUs(request):
    return render(request, 'aboutUs.html') # Pagina de nosotros.

# ===============================/ Pagina Contactanos /======================== #

def contactUs(request):
    return render(request, 'contactUs.html') # Pagina de nosotros.