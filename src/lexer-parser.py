import tkinter as tk
import ply.lex as lex
from ply.lex import LexError
import ply.yacc as yacc
from tkinter import filedialog, scrolledtext, messagebox
from decimal import Decimal, ROUND_DOWN
import os, webbrowser

#definición de tokens
tokens = (
    'LLAVEI', 'LLAVED', # { }
    'CORCHETEI', 'CORCHETED', # [ ]
    'COMA', 'TOK_EQUIPOS', 'TOK_VERSION', 'TOK_FIRMA_DIG',
    'TOK_NOMBRE_EQUIPO', 'TOK_IDENTIDAD_EQ', 'TOK_LINK',
    'TOK_ASIGNATURA', 'TOK_CARRERA', 'TOK_UNIVERSIDAD', 'TOK_DIRECCION',
    'TOK_CALLE', 'TOK_CIUDAD', 'TOK_PAIS', 'TOK_ALIANZA', 'TOK_INTEGRANTES',
    'TOK_NOMBRE', 'TOK_EDAD', 'TOK_CARGO', 'TOK_FOTO', 'TOK_EMAIL', 'TOK_HABILIDADES',
    'TOK_SALARIO', 'TOK_ACTIVO', 'TOK_PROYECTOS', 'TOK_ESTADO', 'TOK_RESUMEN',
    'TOK_TAREAS', 'TOK_FECHA_INICIO', 'TOK_FECHA_FIN', 'TOK_VIDEO', 'TOK_CONCLUSION',
    'DATE', 'EMAIL', 'URL', 'STRING', 'NUMERO', 'FLOAT',
    'TRUE', 'FALSE', 'NULL', 'VACIO', 'TO_DO', 'INPROGRESS', 'CANCELED', 'DONE', 'ONHOLD',
    'PRODUCTANALYST', 'PROJECTMANAGER', 'UXDESIGNER', 'MARKETING', 'DEVELOPER', 'DEVOPS', 'DBADMIN'    
)

t_LLAVEI = r'\{'
t_LLAVED = r'\}'
t_CORCHETEI = r'\['
t_CORCHETED = r'\]'
t_COMA = r'\,'


def t_TOK_EQUIPOS(t):
    r'\"equipos\":'
    return t

def t_TOK_VERSION(t):
    r'\"versi(o|ó)n\":'
    return t

def t_TOK_FIRMA_DIG(t):
    r'\"firma_digital\":'
    return t

def t_TOK_NOMBRE_EQUIPO(t):
    r'\"nombre_equipo\":'
    return t

def t_TOK_IDENTIDAD_EQ(t):
    r'\"identidad_equipo\":'
    return t

def t_TOK_LINK(t):
    r'\"link\":'
    return t

def t_TOK_ASIGNATURA(t):
    r'\"asignatura\":'
    return t

def t_TOK_CARRERA(t):
    r'\"carrera\":'
    return t

def t_TOK_UNIVERSIDAD(t):
    r'\"universidad_regional\":'
    return t

def t_TOK_DIRECCION(t):
    r'\"direcci(o|ó)n\":'
    return t

def t_TOK_CALLE(t):
    r'\"calle\":'
    return t

def t_TOK_CIUDAD(t):
    r'\"ciudad\":'
    return t

def t_TOK_PAIS(t):
    r'\"pa(i|í)s\":'
    return t

def t_TOK_ALIANZA(t):
    r'\"alianza_equipo\":'
    return t

def t_TOK_INTEGRANTES(t):
    r'\"integrantes\":'
    return t

def t_TOK_NOMBRE(t):
    r'\"nombre\":'
    return t

def t_TOK_EDAD(t):
    r'\"edad\":'
    return t

def t_TOK_CARGO(t):
    r'\"cargo\":'
    return t

def t_TOK_FOTO(t):
    r'\"foto\":'
    return t

def t_TOK_EMAIL(t):
    r'\"email\":'
    return t

def t_TOK_HABILIDADES(t):
    r'\"habilidades\":'
    return t

def t_TOK_SALARIO(t):
    r'\"salario\":'
    return t

def t_TOK_ACTIVO(t):
    r'\"activo\":'
    return t

def t_TOK_PROYECTOS(t):
    r'\"proyectos\":'
    return t

def t_TOK_ESTADO(t):
    r'\"estado\":'
    return t

def t_TOK_RESUMEN(t):
    r'\"resumen\":'
    return t

def t_TOK_TAREAS(t):
    r'\"tareas\":'
    return t

def t_TOK_FECHA_INICIO(t):
    r'\"fecha_inicio\":'
    return t

def t_TOK_FECHA_FIN(t):
    r'\"fecha_fin\":'
    return t

def t_TOK_VIDEO(t):
    r'\"video\":'
    return t

def t_TOK_CONCLUSION(t):
    r'\"conclusi(o|ó)n\":'
    return t

def t_VACIO(t):
    r'""'
    t.value= ""
    return t

def t_TO_DO(t):
    r'\"(T|t)(O|o)\s(D|d)(O|o)\"'
    t.value = t.value[1:-1].title()    # Elimina las comillas y pone mayúscula a la primera letra
    return t

def t_INPROGRESS(t):
    r'\"(I|i)(N|n)\s(P|p)(R|r)(O|o)(G|g)(R|r)(E|e)(S|s)(S|s)\"'
    t.value = t.value[1:-1].title() 
    return t

def t_CANCELED(t):
    r'\"(C|c)(A|a)(N|n)(C|c)(E|e)(L|l)(E|e)(D|d)\"'
    t.value = t.value[1:-1].title()    
    return t

def t_DONE(t):
    r'\"(D|d)(O|o)(N|n)(E|e)\"'
    t.value = t.value[1:-1].title()    
    return t

def t_ONHOLD(t):
    r'\"(O|o)(N|n)\s(H|h)(O|o)(L|l)(D|d)\"'
    t.value = t.value[1:-1].title() 
    return t

def t_PRODUCTANALYST(t):
    r'\"(P|p)(R|r)(O|o)(D|d)(U|u)(C|c)(T|t)\s(A|a)(N|n)(A|a)(L|l)(Y|y)(S|s)(T|t)\"'
    t.value = t.value[1:-1].title() 
    return t

def t_PROJECTMANAGER(t):
    r'\"(P|p)(R|r)(O|o)(J|j)(E|e)(C|c)(T|t)\s(M|m)(A|a)(N|n)(A|a)(G|g)(E|e)(R|r)\"'
    t.value = t.value[1:-1].title()
    return t

def t_UXDESIGNER(t):
    r'\"(U|u)(X|x)\s(D|d)(E|e)(S|s)(I|i)(G|g)(N|n)(E|e)(R|r)\"'
    t.value = t.value[1:-1].title()
    return t

def t_MARKETING(t):
    r'\"(M|m)(A|a)(R|r)(K|k)(E|e)(T|t)(I|i)(N|n)(G|g)\"'
    t.value = t.value[1:-1].title() 
    return t

def t_DEVELOPER(t):
    r'\"(D|d)(E|e)(V|v)(E|e)(L|l)(O|o)(P|p)(E|e)(R|r)\"'
    t.value = t.value[1:-1].title() 
    return t

def t_DEVOPS(t):
    r'\"(D|d)(E|e)(V|v)(O|o)(P|p)(S|s)\"'
    t.value = t.value[1:-1].title() 
    return t

def t_DBADMIN(t):
    r'\"(D|d)(B|b)\s(A|a)(D|d)(M|m)(I|i)(N|n)\"'
    t.value = t.value[1:-1].title() 
    return t

def t_DATE(t):
    r'\"(19\d{2}|20\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\"'
    t.value = t.value[1:-1] 
    return t

def t_EMAIL(t):
    r'\"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\"'
    t.value = t.value[1:-1]
    return t

def t_URL(t):
    r'\"https?://[a-zA-Z0-9\-._~:/?#\[\]@!$&\'()*+,=%]+\"'
    t.value = t.value[1:-1]
    return t

def t_STRING(t):
    r'"(\\.|[^"\\])*"'
    t.value = t.value[1:-1]
    return t


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = Decimal(t.value).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t
    

def t_TRUE(t):
    r'true'
    t.value = True
    return t

def t_FALSE(t):
    r'false'
    t.value = False
    return t

def t_NULL(t):
    r'null'
    t.value = None
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


#gramática
def p_json(p):    
    '''json : LLAVEI cuerpo LLAVED''' 
    
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = {}

def p_cuerpo(p):
    '''cuerpo : TOK_EQUIPOS CORCHETEI equipos CORCHETED COMA version COMA firma_digital
              | TOK_EQUIPOS CORCHETEI equipos CORCHETED COMA firma_digital COMA version
              | TOK_EQUIPOS CORCHETEI equipos CORCHETED
              | TOK_EQUIPOS CORCHETEI equipos CORCHETED COMA version
              | TOK_EQUIPOS CORCHETEI equipos CORCHETED COMA firma_digital
              | version COMA TOK_EQUIPOS CORCHETEI equipos CORCHETED COMA firma_digital
              | version COMA TOK_EQUIPOS CORCHETEI equipos CORCHETED
              | version COMA firma_digital COMA TOK_EQUIPOS CORCHETEI equipos CORCHETED
              | firma_digital COMA TOK_EQUIPOS CORCHETEI equipos CORCHETED COMA version
              | firma_digital COMA version COMA TOK_EQUIPOS CORCHETEI equipos CORCHETED
              | firma_digital COMA TOK_EQUIPOS CORCHETEI equipos CORCHETED
    '''
    

    if(p[1]=='"equipos":'):
        if(len(p) == 9):
            if("version" in p[6]):
                p[0] = {
                    "equipos": p[3],
                    "version": p[6]["version"],
                    "firma_digital": p[8]["firma_digital"]
                }
            else:
                p[0] ={
                    "equipos": p[3],
                    "firma_digital": p[6]["firma_digital"],
                    "version": p[8]["version"]
                }
        elif(len(p) == 5):
            p[0] = {
                "equipos": p[3]
            }
        elif("version" in p[6]):
            p[0] = {
                "equipos": p[3],
                "version": p[6]["version"]
            }
        else:
            p[0] = {
                "equipos": p[3],
                "firma_digital": p[6]["firma_digital"]
            }
    elif("version" in p[1]):
        if(len(p) == 7):
            p[0] = {
                "version": p[1]["version"],
                "equipos": p[5]
            }
        elif(p[3]=='"equipos":'):
            p[0] = {
                "version": p[1]["version"],
                "equipos": p[5],
                "firma_digital": p[8]
            }
        else:
            p[0] = {
                "version": p[1]["version"],
                "firma_digital": p[3]["firma_digital"],
                "equipos": p[7]
            }
    elif("firma_digital" in p[1]):
        if(len(p) == 7):
            p[0] = {
                "firma_digital": p[1]["firma_digital"],
                "equipos": p[5]
            }
        elif(p[3] == '"equipos":'):
            p[0] = {
                "firma_digital": p[1]["firma_digital"],
                "equipos": p[5],
                "version": p[8]["version"]
            }
        else:
            p[0] = {
                "firma_digital": p[1]["firma_digital"],
                "version": p[3]["version"],
                "equipos": p[7]                   
            }        
    

def p_version(p):
    '''version : TOK_VERSION STRING
               | TOK_VERSION NULL
               | TOK_VERSION VACIO'''
    p[0] = {"version": p[2]}

def p_firma(p):
    '''firma_digital : TOK_FIRMA_DIG STRING
                     | TOK_FIRMA_DIG NULL
                     | TOK_FIRMA_DIG VACIO
    '''
    p[0] = {"firma_digital": p[2]}

def p_equipos(p):
    '''equipos : equipo
               | equipo COMA equipos
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3] 


def p_equipo(p):
    '''equipo : LLAVEI TOK_NOMBRE_EQUIPO STRING COMA TOK_IDENTIDAD_EQ URL COMA TOK_LINK link COMA TOK_ASIGNATURA STRING COMA TOK_CARRERA STRING COMA TOK_UNIVERSIDAD STRING COMA TOK_DIRECCION direccion COMA TOK_ALIANZA STRING COMA TOK_INTEGRANTES CORCHETEI integrantes CORCHETED COMA TOK_PROYECTOS CORCHETEI proyectos CORCHETED LLAVED
              | LLAVEI TOK_NOMBRE_EQUIPO STRING COMA TOK_IDENTIDAD_EQ URL COMA TOK_ASIGNATURA STRING COMA TOK_CARRERA STRING COMA TOK_UNIVERSIDAD STRING COMA TOK_ALIANZA STRING COMA TOK_INTEGRANTES CORCHETEI integrantes CORCHETED COMA TOK_PROYECTOS CORCHETEI proyectos CORCHETED LLAVED
              | LLAVEI TOK_NOMBRE_EQUIPO STRING COMA TOK_IDENTIDAD_EQ URL COMA TOK_ASIGNATURA STRING COMA TOK_CARRERA STRING COMA TOK_UNIVERSIDAD STRING COMA TOK_DIRECCION direccion COMA TOK_ALIANZA STRING COMA TOK_INTEGRANTES CORCHETEI integrantes CORCHETED COMA TOK_PROYECTOS CORCHETEI proyectos CORCHETED LLAVED
              | LLAVEI TOK_NOMBRE_EQUIPO STRING COMA TOK_IDENTIDAD_EQ URL COMA TOK_LINK link COMA TOK_ASIGNATURA STRING COMA TOK_CARRERA STRING COMA TOK_UNIVERSIDAD STRING COMA TOK_ALIANZA STRING COMA TOK_INTEGRANTES CORCHETEI integrantes CORCHETED COMA TOK_PROYECTOS CORCHETEI proyectos CORCHETED LLAVED
    '''     
    if(len(p) == 36):
        p[0] = {
            "nombre_equipo": p[3],
            "identidad_equipo": p[6],
            "link": p[9],
            "asignatura": p[12],
            "carrera": p[15],
            "universidad_regional": p[18],
            "direccion": p[21],
            "alianza_equipo": p[24],
            "integrantes": p[28],
            "proyectos": p[33]
        }
    elif(len(p) == 30):
        p[0] = {
            "nombre_equipo": p[3],
            "identidad_equipo": p[6],            
            "asignatura": p[9],
            "carrera": p[12],
            "universidad_regional": p[15],
            "alianza_equipo": p[18],
            "integrantes": p[22],
            "proyectos": p[27]
        }
    elif(p[17]=='"direccion":'):
        p[0] = {
            "nombre_equipo": p[3],
            "identidad_equipo": p[6],
            "asignatura": p[9],
            "carrera": p[12],
            "universidad_regional": p[15],
            "direccion": p[18],
            "alianza_equipo": p[21],
            "integrantes": p[25],
            "proyectos": p[30]
        } 
    else:
        p[0] = {
            "nombre_equipo": p[3],
            "identidad_equipo": p[6],
            "link": p[9],
            "asignatura": p[12],
            "carrera": p[15],
            "universidad_regional": p[18],
            "alianza_equipo": p[21],
            "integrantes": p[25],
            "proyectos": p[30]
        }   
    

def p_link(p):
    '''link : URL 
            | NULL
            | VACIO
    '''
    p[0] = p[1]


def p_direccion(p):
    '''direccion : LLAVEI TOK_CALLE STRING COMA TOK_CIUDAD STRING COMA TOK_PAIS STRING LLAVED
                 | LLAVEI TOK_CALLE STRING COMA TOK_PAIS STRING COMA TOK_CIUDAD STRING LLAVED
                 | LLAVEI TOK_CIUDAD STRING COMA TOK_CALLE STRING COMA TOK_PAIS STRING LLAVED
                 | LLAVEI TOK_CIUDAD STRING COMA TOK_PAIS STRING COMA TOK_CALLE STRING LLAVED
                 | LLAVEI TOK_PAIS STRING COMA TOK_CALLE STRING COMA TOK_CIUDAD STRING LLAVED
                 | LLAVEI TOK_PAIS STRING COMA TOK_CIUDAD STRING COMA TOK_CALLE STRING LLAVED
                 | NULL
                 | VACIO
    '''    
    if(len(p)>2):
        if(p[2]=='"calle":'):
            if(p[5]=='"ciudad":'):                           
                p[0] = {
                    "calle": p[3],
                    "ciudad": p[6],
                    "pais": p[9]
                }         
            else:
                p[0] = {
                    "calle": p[3],
                    "pais": p[6],
                    "ciudad": p[9]                
                }
        elif(p[2]=='"ciudad":'):
            if(p[5]=='"calle":'):
                p[0] = {
                    "ciudad": p[3],
                    "calle": p[6],
                    "pais": p[9]                
                }
            else:
                p[0] = {
                    "ciudad": p[3],
                    "pais": p[6],
                    "calle": p[9]                
                }
        elif(p[2]=='"pais":' or p[2]=='"país":'):
            if(p[5]=='"calle":'):
                p[0] = {
                    "pais": p[3],
                    "calle": p[6],
                    "ciudad": p[9]                
                }
            else:
                p[0] = {
                    "pais": p[3],
                    "ciudad": p[6],
                    "calle": p[9]                
                }              

def p_integrantes(p):
    '''integrantes : integrante
                   | integrante COMA integrantes
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]    

def p_proyectos(p):
    '''proyectos : proyecto
                 | proyecto COMA proyectos
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]    


def p_integrante(p):
    '''integrante : LLAVEI TOK_NOMBRE STRING COMA TOK_EDAD edad COMA TOK_CARGO CARGO_VALOR COMA TOK_FOTO URL COMA TOK_EMAIL EMAIL COMA TOK_HABILIDADES STRING COMA TOK_SALARIO FLOAT COMA TOK_ACTIVO BOOL LLAVED
                  | LLAVEI TOK_NOMBRE STRING COMA TOK_CARGO CARGO_VALOR COMA TOK_FOTO URL COMA TOK_EMAIL EMAIL COMA TOK_HABILIDADES STRING COMA TOK_SALARIO FLOAT COMA TOK_ACTIVO BOOL LLAVED
    '''
    if(p[5]=='"edad":'):
        p[0] = {
            "nombre": p[3],
            "edad": p[6],
            "cargo": p[9],
            "foto": p[12],
            "email": p[15],
            "habilidades": p[18],
            "salario": p[21],
            "activo": p[24]
        }
    else:
        p[0] = {
            "nombre": p[3],
            "cargo": p[6],
            "foto": p[9],
            "email": p[12],
            "habilidades": p[15],
            "salario": p[18],
            "activo": p[21]
        }
        

def p_proyecto(p):
    '''proyecto : LLAVEI TOK_NOMBRE STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_RESUMEN STRING COMA TOK_TAREAS CORCHETEI tareas CORCHETED COMA TOK_FECHA_INICIO DATE COMA TOK_FECHA_FIN DATE COMA TOK_VIDEO URL COMA TOK_CONCLUSION STRING LLAVED'''
    
    p[0] = {
        "nombre": p[3],
        "estado": p[6],
        "resumen": p[9],
        "tareas": p[13],
        "fecha_inicio": p[17],
        "fecha_fin": p[20],
        "video": p[23],
        "conclusion": p[26]
    }
    

def p_edad(p):
    '''edad : NUMERO
            | NULL
            | VACIO
    '''
    p[0] = p[1]

def p_tareas(p):
    '''tareas : tarea
              | tarea COMA tareas
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]    


def p_tarea(p):
    '''tarea : LLAVEI TOK_NOMBRE STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_RESUMEN STRING COMA TOK_FECHA_INICIO fecha_inicio COMA TOK_FECHA_FIN fecha_fin LLAVED
             | LLAVEI TOK_NOMBRE STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_RESUMEN STRING LLAVED
             | LLAVEI TOK_NOMBRE STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_RESUMEN STRING COMA TOK_FECHA_INICIO fecha_inicio LLAVED
             | LLAVEI TOK_NOMBRE STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_RESUMEN STRING COMA TOK_FECHA_FIN fecha_fin LLAVED
             | LLAVEI TOK_NOMBRE STRING COMA TOK_RESUMEN STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_FECHA_INICIO fecha_inicio COMA TOK_FECHA_FIN fecha_fin LLAVED
             | LLAVEI TOK_NOMBRE STRING COMA TOK_RESUMEN STRING COMA TOK_ESTADO ESTADO_VALOR LLAVED
             | LLAVEI TOK_NOMBRE STRING COMA TOK_RESUMEN STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_FECHA_INICIO fecha_inicio LLAVED
             | LLAVEI TOK_NOMBRE STRING COMA TOK_RESUMEN STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_FECHA_FIN fecha_fin LLAVED
             | LLAVEI TOK_ESTADO ESTADO_VALOR COMA TOK_NOMBRE STRING COMA TOK_RESUMEN STRING COMA TOK_FECHA_INICIO fecha_inicio COMA TOK_FECHA_FIN fecha_fin LLAVED
             | LLAVEI TOK_ESTADO ESTADO_VALOR COMA TOK_NOMBRE STRING COMA TOK_RESUMEN STRING LLAVED
             | LLAVEI TOK_ESTADO ESTADO_VALOR COMA TOK_NOMBRE STRING COMA TOK_RESUMEN STRING COMA TOK_FECHA_INICIO fecha_inicio LLAVED
             | LLAVEI TOK_ESTADO ESTADO_VALOR COMA TOK_NOMBRE STRING COMA TOK_RESUMEN STRING COMA TOK_FECHA_FIN fecha_fin LLAVED
             | LLAVEI TOK_ESTADO ESTADO_VALOR COMA TOK_RESUMEN STRING COMA TOK_NOMBRE STRING COMA TOK_FECHA_INICIO fecha_inicio COMA TOK_FECHA_FIN fecha_fin LLAVED
             | LLAVEI TOK_ESTADO ESTADO_VALOR COMA TOK_RESUMEN STRING COMA TOK_NOMBRE STRING LLAVED
             | LLAVEI TOK_ESTADO ESTADO_VALOR COMA TOK_RESUMEN STRING COMA TOK_NOMBRE STRING COMA TOK_FECHA_INICIO fecha_inicio LLAVED
             | LLAVEI TOK_ESTADO ESTADO_VALOR COMA TOK_RESUMEN STRING COMA TOK_NOMBRE STRING COMA TOK_FECHA_FIN fecha_fin LLAVED
             | LLAVEI TOK_RESUMEN STRING COMA TOK_NOMBRE STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_FECHA_INICIO fecha_inicio COMA TOK_FECHA_FIN fecha_fin LLAVED
             | LLAVEI TOK_RESUMEN STRING COMA TOK_NOMBRE STRING COMA TOK_ESTADO ESTADO_VALOR LLAVED
             | LLAVEI TOK_RESUMEN STRING COMA TOK_NOMBRE STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_FECHA_INICIO fecha_inicio LLAVED
             | LLAVEI TOK_RESUMEN STRING COMA TOK_NOMBRE STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_FECHA_FIN fecha_fin LLAVED
             | LLAVEI TOK_RESUMEN STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_NOMBRE STRING COMA TOK_FECHA_INICIO fecha_inicio COMA TOK_FECHA_FIN fecha_fin LLAVED
             | LLAVEI TOK_RESUMEN STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_NOMBRE STRING LLAVED
             | LLAVEI TOK_RESUMEN STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_NOMBRE STRING COMA TOK_FECHA_INICIO fecha_inicio LLAVED
             | LLAVEI TOK_RESUMEN STRING COMA TOK_ESTADO ESTADO_VALOR COMA TOK_NOMBRE STRING COMA TOK_FECHA_FIN fecha_fin LLAVED
    '''
    if(p[2]=='"nombre":'):
        if(len(p) == 17):
            if(p[5] == '"estado":'):
                p[0] = {
                    "nombre": p[3],
                    "estado": p[6],
                    "resumen": p[9],
                    "fecha_inicio": p[12],
                    "fecha_fin": p[15]
                }
            else:
                p[0] = {
                    "nombre": p[3],
                    "resumen": p[6],
                    "estado": p[9],
                    "fecha_inicio": p[12],
                    "fecha_fin": p[15]
                }
        elif(len(p) == 11):
            if(p[5] == '"estado":'):
                p[0] = {
                    "nombre": p[3],
                    "estado": p[6],
                    "resumen": p[9]
                }
            else:
                p[0] = {
                    "nombre": p[3],
                    "resumen": p[6],
                    "estado": p[9]
                }
        elif(p[5] == '"estado":'):
            if(p[11] == '"fecha_inicio":'):
                p[0] = {
                    "nombre": p[3],
                    "estado": p[6],
                    "resumen": p[9],
                    "fecha_inicio": p[12]
                }
            else:
                p[0] = {
                    "nombre": p[3],
                    "estado": p[6],
                    "resumen": p[9],
                    "fecha_fin": p[12]
                }
        else:
            if(p[11] == '"fecha_inicio":'):
                p[0] = {
                    "nombre": p[3],
                    "resumen": p[6],
                    "estado": p[9],
                    "fecha_inicio": p[12]
                }
            else:
                p[0] = {
                    "nombre": p[3],
                    "resumen": p[6],
                    "estado": p[9],
                    "fecha_fin": p[12]
                }
    elif(p[2]=='"estado":'):
        if(len(p) == 17):
            if(p[5] == '"nombre":'):
                p[0] = {
                    "estado": p[3],
                    "nombre": p[6],
                    "resumen": p[9],
                    "fecha_inicio": p[12],
                    "fecha_fin": p[15]
                }
            else:
                p[0] = {
                    "estado": p[3],
                    "resumen": p[6],
                    "nombre": p[9],
                    "fecha_inicio": p[12],
                    "fecha_fin": p[15]
                }
        elif(len(p) == 11):
            if(p[5] == '"nombre":'):
                p[0] = {
                    "estado": p[3],
                    "nombre": p[6],
                    "resumen": p[9]
                }
            else:
                p[0] = {
                    "estado": p[3],
                    "resumen": p[6],
                    "nombre": p[9]
                }
        elif(p[5] == '"nombre":'):
            if(p[11] == '"fecha_inicio":'):
                p[0] = {
                    "estado": p[3],
                    "nombre": p[6],
                    "resumen": p[9],
                    "fecha_inicio": p[12]
                }
            else:
                p[0] = {
                    "estado": p[3],
                    "nombre": p[6],
                    "resumen": p[9],
                    "fecha_fin": p[12]
                }
        else:
            if(p[11] == '"fecha_inicio":'):
                p[0] = {
                    "estado": p[3],
                    "resumen": p[6],
                    "nombre": p[9],
                    "fecha_inicio": p[12]
                }
            else:
                p[0] = {
                    "estado": p[3],
                    "resumen": p[6],
                    "nombre": p[9],
                    "fecha_fin": p[12]
                }
    if(p[2]=='"resumen":'):
        if(len(p) == 17):
            if(p[5] == '"estado":'):
                p[0] = {
                    "resumen": p[3],
                    "estado": p[6],
                    "nombre": p[9],
                    "fecha_inicio": p[12],
                    "fecha_fin": p[15]
                }
            else:
                p[0] = {
                    "resumen": p[3],
                    "nombre": p[6],
                    "estado": p[9],
                    "fecha_inicio": p[12],
                    "fecha_fin": p[15]
                }
        elif(len(p) == 11):
            if(p[5] == '"estado":'):
                p[0] = {
                    "resumen": p[3],
                    "estado": p[6],
                    "nombre": p[9]
                }
            else:
                p[0] = {
                    "resumen": p[3],
                    "nombre": p[6],
                    "estado": p[9]
                }
        elif(p[5] == '"estado":'):
            if(p[11] == '"fecha_inicio":'):
                p[0] = {
                    "resumen": p[3],
                    "estado": p[6],
                    "nombre": p[9],
                    "fecha_inicio": p[12]
                }
            else:
                p[0] = {
                    "resumen": p[3],
                    "estado": p[6],
                    "nombre": p[9],
                    "fecha_fin": p[12]
                }
        else:
            if(p[11] == '"fecha_inicio":'):
                p[0] = {
                    "resumen": p[3],
                    "nombre": p[6],
                    "estado": p[9],
                    "fecha_inicio": p[12]
                }
            else:
                p[0] = {
                    "resumen": p[3],
                    "nombre": p[6],
                    "estado": p[9],
                    "fecha_fin": p[12]
                }
                                               

def p_fecha_inicio(p):
    '''fecha_inicio : DATE
                    | NULL
                    | VACIO
    '''
    p[0] = p[1]

def p_fecha_fin(p):
    '''fecha_fin : DATE
                 | NULL
                 | VACIO
    '''
    p[0] = p[1]    

def p_BOOL(p):
    '''BOOL : TRUE
            | FALSE
    '''
    p[0] = p[1]

def p_ESTADO_VALOR(p):
    '''ESTADO_VALOR : TO_DO
                    | INPROGRESS
                    | CANCELED
                    | DONE
                    | ONHOLD
    '''
    p[0] = p[1]

def p_CARGO_VALOR(p):
    '''CARGO_VALOR : PRODUCTANALYST
                   | PROJECTMANAGER
                   | UXDESIGNER
                   | MARKETING
                   | DEVELOPER
                   | DEVOPS
                   | DBADMIN
    '''
    p[0] = p[1]

errores_lexicos=[]
errores_sintacticos = []


def t_error(t):

    msg = f"Línea {t.lineno}:  Caracter ilegal: {t.value[0]}"
    if msg not in errores_lexicos:
        errores_lexicos.append(msg)
        marcar_linea_error_lexico(t.lineno)
    t.lexer.skip(1)

lexer = lex.lex()



def p_error(p): 

    if p:
        encontrado = str(p.value)
        valor = str(p.value)
        tipo_error = "Token inesperado"

        if valor.startswith("http"):
            tipo_error = "Error de URL"
        elif "@" in valor:
            tipo_error = "Error de email"
        elif valor.isdigit():
            tipo_error = "Número mal ubicado"
        elif valor.startswith('"') and valor.endswith('"'):
            tipo_error = "String mal colocado"    


    if p:

        errores_sintacticos.append(f"Línea {p.lineno}: {encontrado} es un TOKEN de tipo {p.type} y no el esperado. Error de sintaxis cerca de '{p.value}': {tipo_error}.\nSe detiene el análisis sintáctico.")
        marcar_linea_error_sintactico(p.lineno)       



#parser
parser = yacc.yacc(tabmodule='parsetab', write_tables=True, debug=False)


#funciones 
def cargar_archivo():
    try:
        archivo_json = filedialog.askopenfilename(
            title="Seleccionar archivo JSON",
            filetypes=[("Archivos JSON", "*.json"), ("Todos los archivos", "*.*")]
        )

        if archivo_json:
            # Validar extensión
            _, ext = os.path.splitext(archivo_json)
            if ext.lower() != ".json":
                messagebox.showwarning("Archivo inválido", "Solo se permiten archivos con extensión .json")
                return

            with open(archivo_json, "r", encoding="utf-8") as f:
                contenido = f.read()

            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, contenido)

            global ruta_json
            ruta_json = archivo_json
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
        

def generar_html(resultado):
    html = ['<!DOCTYPE html>']
    html.append('<html lang="es">')
    html.append('<head>')
    html.append('<meta charset="UTF-8">')
    html.append('<title>Informe del TPI</title>')
    html.append('<style>')
    html.append('body { font-family: Arial, sans-serif; margin: 20px; background: #f9f9f9; font-weight: normal;}')
    html.append('div { border: 1px solid #9d9d9d ; padding: 20px; }')
    html.append('img { max-width: 300px; }')
    html.append('.foto { max-width: 100px; }')
    html.append('</style>')
    html.append('</head>')
    html.append('<body>')

    
    for equipo in resultado.get("equipos", []):
        html.append('<div>')
        html.append(f"<h1><b>Nombre del Equipo:</b> {equipo.get('nombre_equipo')}")
        html.append("<p><b>Identidad del Equipo:</b></p>")
        html.append(f"<img src='{equipo.get("identidad_equipo")}'>")
        html.append(f"<p><b>Link:</b> <a href='{equipo.get("link")}' target='_blank' style='text-decoration:none; color: #919191;'>{equipo.get("link")}</a></p>")
        html.append(f"<p><b>Asignatura:</b> {equipo.get("asignatura")}</p>")
        html.append(f"<p><b>Carrera:</b> {equipo.get("carrera")}</p>")
        html.append(f"<p><b>Universidad Regional:</b> {equipo.get("universidad_regional")}</p>")
        direccion = equipo.get("direccion")
        if direccion:
            html.append(f"<p><b>Dirección:</b>  {direccion.get("calle")}, {direccion.get("ciudad")}, {direccion.get("pais")}</p>")
        html.append(f"<p><b>Alianza Equipo:</b> {equipo.get("alianza_equipo")}</p>")
        html.append("<p><b>Integrantes:</b></p>")
        integrantes = equipo.get("integrantes", [])
        for integrante in integrantes:
            html.append(f"<h2>Nombre: {integrante.get("nombre")}</h2>")
            html.append("<ul>")
            if (integrante.get("edad")):
                html.append(f"<li><b>Edad: </b>{integrante.get('edad')}</li>")
            html.append(f"<li><b>Cargo: </b>{integrante.get('cargo')}</li>")
            html.append(f"<img src='{integrante.get("foto")}' class='foto'>")
            html.append(f"<li><b>Email: </b>{integrante.get('email')}</li>")
            html.append(f"<li><b>Habilidades: </b>{integrante.get('habilidades')}</li>")
            html.append(f"<li><b>Salario:</b> ${integrante.get("salario")}</li>")
            if(integrante.get("activo")):
                html.append(f"<li><b>Activo:</b> Sí</li>")
            else:
                html.append(f"<li><b>Activo:</b> No</li>")
            html.append("</ul>")
        html.append('<p><b>Proyectos:</b></p>')
        proyectos = equipo.get("proyectos", [])
        for proyecto in proyectos:
            html.append(f'<h3>Nombre del Proyecto: {proyecto.get("nombre")}</h3>')
            html.append('<ul>')
            html.append(f'<li><b>Estado: </b> {proyecto.get("estado")}</li>')
            html.append(f'<li><b>Resumen: </b>{proyecto.get("resumen")}</li>')
            html.append('</ul>')
            html.append('<table border="1">')
            html.append('<thead>')
            html.append('<tr><th>Nombre</th><th>Estado</th><th>Resumen</th><th>Fecha de Inicio</th><th>Fecha de Fin</th></tr>')
            html.append('</thead>')
            html.append('<tbody>')
            tareas = proyecto.get("tareas", [])
            for tarea in tareas:
                html.append(f'<tr><td>{tarea.get("nombre")}</td>')
                html.append(f'<td>{tarea.get("estado")}</td>')
                html.append(f'<td>{tarea.get("resumen")}</td>')
                if(tarea.get("fecha_inicio")):
                    html.append(f'<td>{tarea.get("fecha_inicio")}</td>')
                else:
                    html.append('<td>-</td>')
                if(tarea.get("fecha_fin")):
                    html.append(f'<td>{tarea.get("fecha_fin")}</td>')
                else:
                    html.append('<td>-</td>')
                html.append('</tr>')
            html.append('</tbody></table>')
            html.append('<ul>')
            if(proyecto.get("fecha_inicio")):
                html.append(f'<li><b>Fecha Inicio: </b>{proyecto.get("fecha_inicio")}</li>')
            if(proyecto.get("fecha_fin")):
                html.append(f'<li><b>Fecha Fin: </b>{proyecto.get("fecha_fin")}</li>')
            html.append(f'<li><b>Video: </b><a href="{proyecto.get("video")}" target="_blank" style="text-decoration:none; color: #919191;">{proyecto.get("video")}</a></li>')
            html.append(f'<li><b>Conclusión: </b> {proyecto.get("conclusion")}</li>')
            html.append('</ul>')
        html.append('</div>')


    html.append('</body>')
    html.append('</html>')

    return '\n'.join(html)

def guardar_html(contenido_html, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(contenido_html)
    

def hacer_parser(contenido):
    lexer.lineno = 1
    try:
        resultado = parser.parse(contenido, lexer=lexer)
        
        if(not errores_sintacticos and not errores_lexicos):
            nombre_base = os.path.splitext(os.path.basename(ruta_json))[0]
            nombre_html = f"{nombre_base}.html"
            html = generar_html(resultado)
            guardar_html(html, nombre_html)
            webbrowser.open(nombre_html)

        return resultado

    except LexError as e:
        return None



def obtener_json():
    
    text_area.tag_remove("error_lexico", "1.0", tk.END)
    text_area.tag_remove("error_sintactico", "1.0", tk.END)
    contenido = text_area.get(1.0, tk.END).strip() 
    error_area.config(state='normal')
    error_area.delete(1.0, tk.END) 
    error_area.config(state='disabled') 
    lexer.lineno = 1  # Reinicia el contador de líneas
    errores_sintacticos.clear() 
    errores_lexicos.clear() # Limpia la lista de errores
    
    if contenido:
        lexer.input(contenido)

        for tok in lexer: 
            pass #lo dejamos para que muestre los errores del lexer

        # Procesar el contenido con el parser
        hacer_parser(contenido)
        todos_los_errores = errores_lexicos + errores_sintacticos
        
        if todos_los_errores:            
            mensaje = "\n".join(todos_los_errores)
            error_area.config(state='normal')
            error_area.delete(1.0, tk.END)
            error_area.insert(tk.END, mensaje + "\n")
            error_area.config(state='disabled')
            messagebox.showerror("Fin del proceso", f"Análisis finalizado con errores.")
            todos_los_errores.clear()
    else:
        error_area.config(state='normal')
        error_area.delete(1.0, tk.END)
        error_area.insert(tk.END, "No se ha ingresado ningún contenido.\n")    
 
 

def marcar_linea_error_lexico(linea):
    inicio = f"{linea}.0"
    fin = f"{linea}.end"
    text_area.tag_add("error_lexico", inicio, fin)

def marcar_linea_error_sintactico(linea):
    inicio = f"{linea}.0"
    fin = f"{linea}.end"
    text_area.tag_add("error_sintactico", inicio, fin)


#interfaz gráfica
root = tk.Tk()
root.title("Analizador Léxico y Sintáctico")
root.geometry("1000x650")
root.iconbitmap("LogoSSL.ico")

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

main_frame.columnconfigure(0, weight=1)  # Entrada JSON (izquierda)

main_frame.rowconfigure(0, weight=3) # Panel superior (entrada JSON y resultado)
main_frame.rowconfigure(1, weight=1) # Panel inferior (errores)

# Panel superior (entrada JSON)
frame_entrada = tk.Frame(main_frame)
frame_entrada.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

btn_cargar = tk.Button(frame_entrada, text="Cargar JSON", command=cargar_archivo)
btn_cargar.pack(pady=5)

text_area = scrolledtext.ScrolledText(frame_entrada, height=18, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True)

text_area.tag_config("error_lexico", background="misty rose")
text_area.tag_config("error_sintactico", background="light salmon")

btn_obtener = tk.Button(frame_entrada, text="Procesar JSON", command=obtener_json)
btn_obtener.pack(pady=5)


frame_errores = tk.Frame(main_frame, height=250)
frame_errores.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

label_errores = tk.Label(frame_errores, text="Errores", font=("Arial", 12, "bold"))
label_errores.pack(pady=5)

error_area = scrolledtext.ScrolledText(frame_errores, wrap=tk.WORD, height=10, state='disabled', fg='red')
error_area.pack(fill=tk.BOTH, expand=True)


root.mainloop()


