import re

def validar_luhn(numero):
    """Implementação do algoritmo de Luhn para validar números de cartão"""
    soma = 0
    alterna = False
    for digito in reversed(numero):
        if not digito.isdigit():
            return False
        n = int(digito)
        if alterna:
            n *= 2
            if n > 9:
                n = (n % 10) + 1
        soma += n
        alterna = not alterna
    return soma % 10 == 0

def identificar_bandeira(numero):
    """Identifica a bandeira do cartão com base nos prefixos e comprimento"""
    numero = numero.replace(" ", "").replace("-", "")
    
    if not numero.isdigit() or not validar_luhn(numero):
        return "Número de cartão inválido"
    
    comprimento = len(numero)
    
    # Visa (16 dígitos)
    if re.match(r'^4\d{15}$', numero):
        return "Visa 16 dígitos"
    
    # Visa Electron
    if (comprimento == 16 and 
        (re.match(r'^4(026|175|407|508|844|913|917|918)\d{10}$', numero) or 
         re.match(r'^4026\d{12}$', numero) or 
         re.match(r'^417500\d{10}$', numero) or 
         re.match(r'^4508\d{12}$', numero) or 
         re.match(r'^4844\d{12}$', numero) or 
         re.match(r'^4913\d{12}$', numero) or 
         re.match(r'^4917\d{12}$', numero))):
        return "Visa Electron"
    
    # MasterCard
    if (comprimento == 16 and 
        (re.match(r'^5[1-5]\d{14}$', numero) or 
         re.match(r'^222[1-9]\d{12}$', numero) or 
         re.match(r'^22[3-9]\d{13}$', numero) or 
         re.match(r'^2[3-6]\d{14}$', numero) or 
         re.match(r'^27[0-1]\d{13}$', numero) or 
         re.match(r'^2720\d{12}$', numero))):
        return "MasterCard"
    
    # American Express
    if comprimento == 15 and re.match(r'^3[47]\d{13}$', numero):
        return "American Express"
    
    # Diners Club
    if (comprimento == 14 and 
        (re.match(r'^3(0[0-5]|[68]\d)\d{11}$', numero) or 
         re.match(r'^30[0-5]\d{11}$', numero) or 
         re.match(r'^3095\d{10}$', numero) or 
         re.match(r'^36\d{12}$', numero) or 
         re.match(r'^38\d{12}$', numero) or 
         re.match(r'^39\d{12}$', numero))):
        return "Diners Club"
    
    # Discover
    if (comprimento in [16, 19] and 
        (re.match(r'^6011\d{12}$', numero) or 
         re.match(r'^64[4-9]\d{13}$', numero) or 
         re.match(r'^65\d{14}$', numero) or 
         re.match(r'^622(12[6-9]|1[3-9]\d|[2-8]\d{2}|9[01]\d|92[0-5])\d{10}$', numero))):
        return "Discover"
    
    # JCB
    if (comprimento in [16, 17, 18, 19] and 
        re.match(r'^(2131|1800|35\d{3})\d{11}$', numero)):
        return "JCB"
    
    # Maestro
    if (comprimento in [12, 13, 14, 15, 16, 17, 18, 19] and 
        (re.match(r'^(5018|5020|5038|5893|6304|6759|6761|6762|6763)\d+$', numero))):
        return "Maestro"
    
    # enRoute
    if comprimento == 15 and re.match(r'^(2014|2149)\d{11}$', numero):
        return "enRoute"
    
    # Laser
    if (comprimento in [16, 17, 18, 19] and 
        re.match(r'^(6304|6706|6771|6709)\d+$', numero)):
        return "Laser"
    
    return "Bandeira não identificada"

# Exemplo de uso
if __name__ == "__main__":
    while True:
        numero_cartao = input("\nDigite o número do cartão (ou 'sair' para encerrar): ").strip()
        
        if numero_cartao.lower() == 'sair':
            break
            
        if not numero_cartao:
            continue
            
        resultado = identificar_bandeira(numero_cartao)
        print(f"Resultado: {resultado}")