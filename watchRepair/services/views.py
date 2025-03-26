from django.shortcuts import render


# ===============================/ Pagina inicial home /======================== #
def home(request):
    return render(request, 'home.html') # Pagina de inicio


# ===============================/ Vista para la pagina servicios /======================== #
def services(request):
    return render(request, 'services.html') # Pagina de servicios

# ===============================/ Vista para la nosotros /======================== #
def aboutUs(request):
    return render(request, 'aboutUs.html') # Pagina de nosotros

# ===============================/ Vista para la contactanos /======================== #
def contacts(request):
    return render(request, 'contacts.html') # Pagina de nosotros

