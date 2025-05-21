📝 Descrição
Este é um script Python que valida números de cartão de crédito utilizando o algoritmo de Luhn e identifica a bandeira do cartão com base em prefixos e comprimentos específicos.

O script suporta as seguintes bandeiras:

Master Card

Visa Electron

American Express

Diners Club

Discover

JCB

Maestro

enRoute

Laser

Visa (16 dígitos)

🛠️ Pré-requisitos
Python 3.x instalado

Nenhuma dependência externa necessária

🚀 Como Usar:

Clone o repositório ou baixe o arquivo script.py

Execute o script com: python script.py

Digite o número do cartão quando solicitado (sem espaços ou hífens, ou com eles - o script faz a limpeza automaticamente)

O script retornará a bandeira identificada ou uma mensagem de erro se o número for inválido

Digite 'sair' para encerrar o programa

🔍 Exemplos de Números de Teste
(Observação: estes são números de teste que passam no algoritmo de Luhn, mas não são cartões reais)

Visa: 4111111111111111

MasterCard: 5555555555554444

American Express: 378282246310005

Discover: 6011111111111117

JCB: 3530111333300000

Diners Club: 30569309025904

⚙️ Funcionalidades
Validação do número usando algoritmo de Luhn

Identificação da bandeira baseada em prefixos e comprimento

Suporte a múltiplos formatos de entrada (com ou sem espaços/hífens)

Interface simples de linha de comando

📌 Limitações
O script identifica a bandeira com base em padrões conhecidos, mas não verifica se o cartão realmente existe

Algumas bandeiras têm intervalos de prefixos que podem mudar com o tempo

O script não faz conexão com nenhum serviço externo para validação adicional

📜 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para:

Adicionar novas bandeiras

Melhorar a precisão da identificação

Adicionar funcionalidades extras
