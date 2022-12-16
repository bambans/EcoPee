# EcoPee
## Componentes gerais

Para a parte elétrica e computacional do projeto, foi utilizado um microcontrolador que receberá informações do sensor de umidade e emitirá um alerta via Telegram para o usuário quando a fralda estiver úmida. Não houve nenhuma implementação específica para a integração com o Telegram, visto que o aplicativo de mensagens possui API para facilitar a comunicação. 
Dos componentes utilizados, tem-se:
- ESP32: microcontrolador ao qual o sensor de umidade direta é conectado. Nele roda o programa em quase todas as suas funcionalidades, exceto a API, a qual faz parte - do próprio Telegram;
- Sensor de umidade: sensor fabricado pelo grupo, que tem por função dar um sinal verdadeiro quando conectado ao ESP32 e quando estiver molhado, de forma simultânea;
- Adaptador de pilhas: componente ao qual se conectam pilhas, para alimentação elétrica do circuito.

## Programação
O programa para o projeto foi desenvolvido em Python 3, sob a plataforma MicroPython para ESP32.
De forma lógico-sequencial, a execução se dá por:
- Testa se existe o arquivo “config.json” para configurar o sistema;
- Se existe:
	- Lê os dados do arquivo;
	- Conecta à rede Wi-Fi especificada no arquivo com o nome da rede (SSID) e senha;
	- Conecta à API do Telegram, a qual retorna um conjunto de dados do EcoPee, filtra pelo usuário especificado no arquivo (o especificado na configuração - explicação mais abaixo), coleta o identificador de chat do usuário e guarda em uma variável;
	- A partir do identificador, envia duas mensagens ao cliente, a primeira informando que o circuito está ligado e a segunda de que será avisado quando o sensor estiver molhado;
	- Fica aguardando sinal verdadeiro no pino 34 (o qual está conectado o sensor) e, quando verdadeiro, avisa ao usuário	sobre a fralda estar molhada;
- Se não existe:
	- Cria uma rede Wifi chamada EcoPee;
	- Cria um socket de comunicação (servidor) e aguarda conexões;
	- Quando conectado, recebe e decodifica as requisições e, dados os casos, tomas as seguintes ações:
	- “GET / HTTP/1.1”: abre, lê, envia e fecha o arquivo “index.html”, o qual contém uma página com um formulário a ser preenchido pelo cliente;
	- “GET /wifi_scan HTTP/1.1”: cria um objeto que trata sobre as redes Wi-Fi, o qual escaneia as redes próximas e guarda em uma variável. Essa variável é empacotada no formato JSON e enviada ao cliente, o qual cria uma lista de redes próximas;
	- “POST /config HTTP/1.1”: recebe os dados de configuração do formulário do cliente e os escreve no arquivo de configuração “config.json”;
	- “GET /exit.html HTTP/1.1”: abre, lê, envia e fecha o arquivo “exit.html”, o qual contém uma página com o resultado do teste do arquivo de configuração;
	- “GET /test_config HTTP/1.1”: testa se o arquivo “config.json” existe e envia verdadeiro (existe) ou falso (não existe) ao cliente;
	- “GET /reset HTTP/1.1”: desliga a rede wifi própria e reinicia o produto, o qual, sempre quando ligar, realizará todos os testes na ordem e fluxo especificados.
Quanto à escolha do Telegram, deve-se ao fato de que o mensageiro é open source e sua API é aberta, de fácil uso e acesso. Não só, o aplicativo possui uma grande base de usuários, o que não é um fator limitante quanto à execução do projeto.
