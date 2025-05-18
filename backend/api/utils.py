from Bio.Seq import Seq


def reverso_complementario(secuencia_str):
    secuencia = Seq(secuencia_str)
    return str(secuencia.reverse_complement())


def traducir_secuencia_adn(secuencia_str):
    secuencia = Seq(secuencia_str)
    return str(secuencia.translate())
