"""
ENUNCIADO:
Hacer un script en python para convertir un archivo XML en un archivo JSON.
El script deberia tener dos parameter --input --output
El archivo de salida tiene que tener el siguiente formato:
{
“hosts_count”: cantidad_de_hosts,
“services_count”: cantidad_de_servicios,
“website_count”: cantidad_de_websites,
“web_vulns_count”: cantidad_de_vulns_web,
“vulns_count”: cantidad_de_vulns_not_web,
“vulns”: lista_con_vulns
}
Donde:
Cantidad_de_hosts: total de hosts contenidas en el archivo XML
Contidad_de_servicios: total de servicios contenidas en el XML
Cantidad_de_websites: cantidad de websites contenidas en el XML
Cantidad_de_vulns_web: cantidad de vulns web contenidas en el XML
Cantidad_de_vulns_not_web: cantidad de vulns no web contenidas en el XML (La diferencia es que no tienen servicio asignado)
Lista_con_vulns: es una lista de las vulnerabilidades que hay en el archivo xml

Para la lista de vuln, usar un formato adecuado (diccionario) sin perder información.
Nota: Las cantidades deberían evitar contar elementos duplicados
El generador de XML está adjunto.
Aclaraciones:
Las únicas dependencias de python no stdlib para el generador, son click y lxml.
La idea es resolver el conteo iterando sobre el archivo xml, no utilizar algo externo que te de la cuenta.
"""

import json
import xml.etree.ElementTree as et 

entrada= str(input("Ingrese ruta del archivo XML: "))
xtree = et.parse(entrada)
xroot = xtree.getroot() 

s_hosts,s_service,s_vulns,s_vulns_web,s_vulns_not_web,s_websites=0,0,0,0,0,0
s_vulns_list=[]
for node in xroot.iter("hosts"): 
    s_hosts +=1
    for elements in node.iter("services"):
        s_service+= len(elements.findall("service"))
    for elements in node.iter("vulns"):
        s_vulns+= len(elements.findall("vuln"))
        for vuln in elements.iter("vuln"):
            dicc={}
            for item in vuln:
                dicc[item.tag]= item.text
                if item.tag== 'web-site-id':
                    s_vulns_web+=1

            s_vulns_list.append(dicc)

s_vulns_not_web=s_vulns-s_vulns_web


diccionario= {"hosts_count": s_hosts,"services_count": s_service,"website_count": s_websites,"web_vulns_count": s_vulns_web,
    "vulns_count": s_vulns_not_web,"vulns": s_vulns_list}
with open('data.json', 'w') as fp:
    json.dump(diccionario, fp)
