from django import template
from quran.models import Sura,QuranTranslation

register = template.Library()
@register.filter
def zfill(value, arg):
    return str(value).zfill(arg) 

@register.filter
def suras_list(value=1):
	suras = Sura.objects.all()
	nav_suras = """		
	<ul style="list-style-type: none; ">
	{% for sura in suras %}
		{% if sura.pk == cur_sura %}
		<li><strong>{{sura.pk}}. {{sura.tname}}</strong></li>
		{% else %}
		<li><a href="/{{sura.pk}}/">{{sura.pk}}. {{sura.tname}}</a></li>
		{% endif %}		
	{%endfor%}
    </ul>  
	"""
	t = template.Template(nav_suras)
	c = template.Context({'suras': suras,'cur_sura':value})
	return t.render(c)



@register.filter
def trans_list(value):
	trans = QuranTranslation.objects.all()
	opt_trans = """		
	<select onChange="document.location.href = document.location.href.split('?')[0]+'?trans='+this.value">
      {% for translation in trans %}
        <option value="{{translation.pk}}"{% if translation.pk == cur_trans %} selected{% endif %}>{{translation.name}}</option>
      {%endfor%}
      </select>
	"""
	t = template.Template(opt_trans)
	c = template.Context({'trans': trans,'cur_trans':value})
	return t.render(c)
