from django import template
from quran.models import Sura

register = template.Library()
@register.filter
def zfill(value, arg):
    return str(value).zfill(arg) 

@register.filter
def sura_dropdown(value):
	suras = Sura.objects.all()
	nav_dropdown = """		
    <select onChange="document.location.href=this.value">
      {% for sura in suras %}
      <option value="{% url 'quran_sura' sura.pk %}"{% if sura.pk == cur_sura %} selected{% endif %}>{{sura.pk}}. {{sura.tname}}</option>
      {%endfor%}
    </select>		  
	"""
	t = template.Template(nav_dropdown)
	c = template.Context({'suras': suras,'cur_sura':value})
	return t.render(c)
