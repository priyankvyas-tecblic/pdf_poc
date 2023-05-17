from django.http import HttpResponse
from django.views.generic import View
from myapp.utilities import render_to_pdf

def home(request):
    data = {'id': 64, 'package_name': 'string', 'description': 'string', 'days': 2147483647, 'nights': 2147483647, 'price_per_people': 0.0, 'package_range': 'string', 'season': 'sum', 'rating': 0.0, 'is_active': True}
    pdf = render_to_pdf.render_to_pdf('invoice.html', data)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + "package_detail.pdf"
    return response