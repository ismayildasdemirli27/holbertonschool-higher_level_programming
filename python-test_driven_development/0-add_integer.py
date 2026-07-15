#!/usr/bin/python3
"""
Bu modul iki tam ədədi (integer) toplamaq üçün funksiya təqdim edir.
"""

def add_integer(a, b=98):
    """
    İki ədədi toplayır. Əgər ədədlər float (kəsr) tiplidirsə, onları
    integer-ə (tam ədədə) çevirir. 
    
    Əgər parametr int və ya float deyilsə, TypeError verir.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
