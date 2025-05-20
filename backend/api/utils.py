from Bio.Seq import Seq
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def reverso_complementario(secuencia_str):
    secuencia = Seq(secuencia_str)
    return str(secuencia.reverse_complement())


def traducir_secuencia_adn(secuencia_str):
    secuencia = Seq(secuencia_str)
    return str(secuencia.translate())

def alinear_secuencias(seq1, seq2):
    """
    Realiza un alineamiento global entre dos secuencias y devuelve el mejor alineamiento.
    """
    # Realizar alineamiento global con puntajes por defecto
    alignments = pairwise2.align.globalxx(seq1, seq2)
    
    # Tomar el mejor alineamiento (el primero)
    mejor_alineamiento = alignments[0]
    
    # Formatear el alineamiento para mostrarlo bonito
    resultado = format_alignment(*mejor_alineamiento)
    return resultado