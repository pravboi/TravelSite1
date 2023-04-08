from io import BytesIO
from django.http import  HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def html2pdf(template_source, context={}):
    template = get_template(template_source)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("cp1252")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return None
