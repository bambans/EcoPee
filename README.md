# UNIVERSIDADE DE SÃO PAULO
## ESCOLA DE ARTES, CIÊNCIAS E HUMANIDADES
### BACHARELADO EM TÊXTIL E MODA E BACHARELADO EM SISTEMAS DE INFORMAÇÃO
---
<br>

# Relatório de pesquisa em wearables:
> ## Fralda ecologicamente inteligente (EcoPee)
> Integrantes:
> - Letícia Mender Ribeiro – 11779476
> - Thamires de Freitas Sant'Ana - 10282449
> - Perciliana Pereira - 11020772
> - Otávio Rodrigues Bambans - 12701582
> ### São Paulo - 2022
---
<br>

# Sumário
1. [Introdução](#introdução)
2. [Materiais e métodos](#materiais-e-métodos)
3. [Resultados](#resultados)
4. [Conclusão](#conclusão)
5. [Referências bibliográficas](#referências-bibliográficas)

<!-- ![EcoPee Logo](ecoPee.svg) -->

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="500" preserveAspectRatio="xMidYMid meet" version="1.0" viewBox="0.0 -2.5 99.4 104.6" zoomAndPan="magnify">
    <g data-name="Layer 2">
        <g data-name="Layer 1" fill="#288b18" id="change1_1">
            <path d="M32.36,78.1c0-15.82,8.66-37.59,28.69-45-23.49,7.41-31.4,29.91-31.4,45C29.65,78.1,30.56,79.12,32.36,78.1Z"/>
            <path d="M31.47,61C21.94,47.17,36.85,18,81.55,28.4,65.69,32.1,61.46,63,36.34,62.4A45.1,45.1,0,0,1,65.69,32.1C45.35,33.34,32.71,53.16,31.47,61Z"/>
            <path d="M66.26,96.58A49.34,49.34,0,0,1,0,50.25,50.46,50.46,0,0,1,33.14,3,49.35,49.35,0,0,1,99.41,49.32,50.47,50.47,0,0,1,66.26,96.58Zm-33.12-91A46.72,46.72,0,0,0,2.54,49.32a47.63,47.63,0,0,0,47.6,47.54A46.57,46.57,0,0,0,96.87,50.24,47.62,47.62,0,0,0,49.27,2.7,46.9,46.9,0,0,0,33.14,5.53Z"/>
        </g>
    </g>
</svg>


# RESUMO

O presente relatório tem como objetivo demonstrar a pesquisa realizada sobre a construção de uma fralda wearable e sustentável, que avisasse ao tutor quando houvesse a necessidade da troca por meio de um sensor de umidade. Para a elaboração desse projeto foi necessário uma pesquisa sobre materiais para a confecção de uma fralda que fosse confortável, de valor acessível e fácil higienização, além de buscar meios para que os componentes da parte eletrônica fossem o menos perceptível e incômodo para o usuário final, que poderia ser uma criança, um animal de estimação ou um adulto com necessidades especiais.

Através desse levantamento, foram criadas hipóteses e protótipos para analisar modelagem, conforto e adequação dos componentes eletrônicos que serão expostas ao longo deste relatório.

<br>

# INTRODUÇÃO

As fraldas descartáveis são hoje parte integrante do dia a dia de muitas famílias, assim que um recém nascido vem ao mundo é muito comum que mães e familiares façam um estoque dessas fraldas para o cuidado com o bebê. Em paralelo, adultos e animais acamados também acabam se tornando um público alvo para a venda de fraldas.

De acordo com a ABIHPEC, Associação Brasileira da Indústria de Higiene Pessoal, Perfumaria e Cosméticos, o Brasil já era em 2014 o terceiro maior consumidor de fraldas descartáveis do mundo com 7,9 bilhões de fraldas descartáveis vendidas no país. O impacto ambiental causado pelo consumo dessas fraldas é irrecuperável, já que como explica Monteiro (2018, apud ROKUGAWA, 2019), a previsão para a decomposição das fraldas descartáveis é de aproximadamente 450 anos, além de aumentar o fluxo de lixo em aterros sanitários, já que crianças e adultos podem necessitar de até 8 fraldas por dia, até os 4 anos de idade, ou nos casos de adultos e animais de estimação, por prazo indeterminado.

Esse tipo de fralda pode causar danos não só no meio ambiente,  como também para seus usuários. Em estudo feito pela Anses, Agência Francesa para Segurança Alimentar, Ambiental e do Trabalho, foram identificadas dezenas de substâncias prejudiciais nas fraldas descartáveis. Entre elas, o herbicida glifosato, apontado como causador de doenças neurodegenerativas, distúrbios reprodutivos e infertilidade (STACHIW, 2019; TELEKEN, 2018 apud PROBST e FIORIN, 2021), entre outros.

## FRALDAS ECOLÓGICAS

Para Lampreia (2013), a sustentabilidade tornou-se parte integrante das discussões contemporâneas, logo, pensar em alternativas sustentáveis para substituir itens de consumo diário é uma preocupação constante de empresas e consumidores conscientes. 

As fraldas ecológicas aparecem no mercado como uma alternativa para a redução de resíduos causados pelas fraldas descartáveis comuns. Por se tratar de itens reutilizáveis, já que são feitas com tecidos de fácil higienização, as fraldas ecológicas resultam em uma forma coerente e fácil de substituir as fraldas comuns. Além de ser economicamente mais atraentes, as fraldas reutilizáveis são mais confortáveis para o usuário, não possuem substâncias nocivas e evitam alergias e possíveis problemas com assaduras por serem confeccionadas com tecidos leves e que proporcionam que a pele respire.
	
## FRALDAS WEARABLES

Para Rocha e Selores (2004), “a fralda ideal deveria ter uma boa capacidade de conter água, permitir um bom arejamento (menos oclusiva) e mudar de cor imediatamente após a criança urinar”, essa medida seria uma forma de avisar os pais ou tutores dos usuários de fraldas que há urina ou fezes e é necessário a troca. As autoras alegam ainda que a alergia conhecida como “dermatite das fraldas” é causada pelo contato demorado com as secreções produzidas, dessa forma, um dispositivo que avisa os tutores quando há a necessidade de trocar a fralda seria imprescindível para o conforto e saúde do usuário final. 
Em 2019, a marca de produtos para bebês Pampers, anunciou o lançamento de um sistema chamado Lumi; um sistema que monitora a atividade dos bebês por meio de um sensor inserido nas fraldas e avisa os pais assim que precisa ser trocada, prevista para entrar no mercado americano ainda em 2019, não há previsão para a chegada da tecnologia no Brasil (BACA, 2019).

Figura 01. Fralda Lumi Pampers 

![Fralda Lumi Pampers](https://assets.b9.com.br/wp-content/uploads/2019/07/pampers-fralda-inteligente-1280x677.jpg)

Fonte: B9

Em outros lugares do mundo, também foram criadas iniciativas para a construção de um sensor que monitora-se as crianças e avisa-se aos pais e tutores da necessidade da troca, empresas como Alphabet, Huggies e até mesmo o Massachusetts Institute of Technology - MIT tentaram criar uma solução para um possível sensor, ainda sem representações no mercado.

Aliando a busca pelo conforto no uso de fraldas, sustentabilidade, economia e a necessidade de uma troca rápida, para que a pele possa respirar  evitando assim alergias e assaduras, foi pensado em uma fralda ecológica que unisse tecnologia e sustentabilidade, e que pudesse contemplar crianças e animais de estimação, produzida com tecidos tecnológicos que promovam a alta absorção dos fluidos, respirabilidade e conforto, além de incluir um sistema eletrônico que através de um sensor de umidade, criado com tecido condutivo; localizado no absorvente removível da fralda, que ao entrar em contato com a urina, se comunica com um servidor e por meio do aplicativo de mensagens instantâneas Telegram, avisa o tutor da necessidade da troca da fralda.


# MATERIAIS E MÉTODOS
	
## Fralda ecológica
	
Para a confecção da fralda, foram feitos levantamentos sobre os tecidos e modelagem comumente utilizados por meio da consulta de marcas de fraldas ecológicas já consolidadas no mercado, como por exemplo as marcas Dipano e Fraldadinhos. De acordo com o encontrado nos sites institucionais das empresas, percebemos que os tecidos escolhidos deveriam possuir características funcionais e fundamentais para cada parte da modelagem da fralda, sendo elas:

- Fralda - Para garantir a usabilidade, necessita ser confeccionada com um tecido resistente, maleável, impermeável, que impeçam possíveis vazamentos, e de fácil higienização;
- Forro - Para garantir melhor desempenho, necessita ser confeccionado com um tecido confortável, absorvente, de fácil secagem e que facilite a transpiração da pele;
- Absorvente removível - Para garantir que não haja vazamentos, necessita ser confeccionado com um tecido de tecnologia absorvente, maleável e resistente a lavagens;
- Sensor de umidade: Necessita ser construído com tecido de tecnologia condutiva;

Após o levantamento das características necessárias para a construção da parte têxtil do projeto, foram escolhidos os seguintes materiais:

- Fralda - Tecido impermeável PUL (Poliuretano Laminado) - Composição: 78%  poliéster, 22% Poliuretano (PU);
- Forro - Tecido DryFit - Composição: 100% poliéster;
- Absorvente removível - Tecido Melton - Composição: 80% Algodão, 20% Poliéster;

## Modelagem e funcionamento

Para a modelagem da fralda infantil, foram pesquisados moldes prontos encontrados na internet, para serem utilizados como referência nas medidas e posteriormente adaptados para acomodar os componentes eletrônicos. Já para a modelagem pet, foi utilizado uma fralda pet descartável para referência e também adaptada para acomodar os componentes eletrônicos.

## Fralda

As fraldas foram confeccionadas em tecido impermeável PUL na parte externa e Dryfit no forro, com uma modelagem pensada na usabilidade, e conforto, de modo que não prejudicasse a movimentação do usuário. Para garantir a vestibilidade, foram inseridos elásticos ao redor das pernas e botões de pressão nas laterais para garantir um melhor ajuste no fechamento. Já para acomodar os componentes eletrônicos, foram criados um bolso em tecido Dryfit para inserir o absorvente sensor, um recorte no interior da fralda para conectar o absorvente aos componentes eletrônicos utilizados e um bolso frontal fechado com zíper invisível para armazenar os componentes eletrônicos como o microcontrolador ESP32 e o adaptador de pilhas.

<!-- (inserir fotos da fralda) -->

## Absorvente sensor

O absorvente sensor removível, foi criado com quatro camadas de Melton, tecido responsável por absorver líquidos. Na segunda camada, foram costuradas duas tiras de tecido condutivo em formato de “E” para formar um circuito sensor de umidade. O sensor construído, ao entrar em contato com a urina, que também é condutiva, fecha o circuito emitindo sinal para os componentes eletrônicos. Esse sinal é enviado para o microcontrolador ESP32 através de 2 botões de pressão em metal, fixados na extremidade de cada tira de tecido condutivo, que fazem a função de positivo e negativo. 
Para testar a funcionalidade do sensor, foram pesquisadas fórmulas de como simular a urina humana, entre elas, a mais completa encontrada, foi criada por Louzada (2019), e necessita dos seguintes reagentes:

> ### Tabela de reagentes
> Reagente | Massa (g)
> --- | ---
> Fosfato de amônio | 1,7
> Creatina | 0,7
> Glicose | 0,35
> Glicina | 0,7
> Ácido oxálico | 0,7
> Alanina | 0,7
> Uréia | 14
> Cloreto de sódio | 0,25
> Albumina | 0,35

Fonte: Louzada

Infelizmente, não foi possível ter acesso a todos os reagentes mencionados na tabela, inviabilizando assim, a realização da solução. Como era necessário saber se o sensor responderia com uma substância diferente da água, optamos por incluir à água 2,4g de cloreto de sódio, por se tratar de um composto de base, no meio da escala de ácido-alcalino.
Com a solução, foi possível testar o sensor e comprovar sua eficácia.

<!-- Figura x. Sensor de umidade

Fonte: Autoria própria -->

## Protótipos

Para viabilizar o projeto, foram criados dois protótipos em algodão cru, um para analisarmos a modelagem da fralda infantil, e outro para analisarmos a modelagem da fralda pet.

<!-- Figura x. Protótipo fralda infantil

Fonte: Autoria própria -->

Por meio da construção do protótipo infantil, pudemos perceber a necessidade de alterar o tamanho da fralda, principalmente para um melhor acondicionamento do sensor absorvente.

<!-- Figura x. Protótipo fralda PET

Fonte: Autoria própria -->

Já com o protótipo da fralda pet, conseguimos observar a necessidade de alterar a cava da perna, de forma que ficasse mais confortável para o usuário, além de perceber que a modelagem deveria ser alterada para que a fralda tivesse um cós mais alto para melhor acomodar os componentes eletrônicos.

## Computação Física e Aplicações

### Descrição

A parte elétrica e computacional do projeto foi feita utilizando um microcontrolador que recebe informações de um sensor de umidade e emite um alerta via Telegram para o usuário quando a fralda estiver úmida. Não houve nenhuma implementação específica para a integração com o Telegram, visto que o aplicativo de mensagens possui API para facilitar a comunicação. 

Dos componentes utilizados, de forma geral, tem-se:

- ESP32: microcontrolador ao qual o sensor de umidade direta é conectado. Nele roda o programa em quase todas as suas funcionalidades, exceto a API, a qual faz parte do próprio Telegram;
- Sensor de umidade: sensor fabricado pelo grupo, que tem por função dar um sinal verdadeiro quando conectado ao ESP32 e quando estiver molhado, concomitantemente;
- Adaptador de pilhas: componente ao qual se conectam pilhas, para alimentação elétrica do circuito.

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

### Lista de materiais
Quantidade | Nome | Referência
---- | ---- | ----
1 | ESP32 | [Espressif - ESP32](https://www.espressif.com/en/products/socs/esp32)
1 | Suporte para pilhas USB | [Imagem do suporte](https://drive.google.com/file/d/17pR94_S-K_3fohaxDNsq9pAetnVxjmXu/view?usp=sharing)
1 | Sensor de umidade direta/urina | [Imagem do sensor: feito à mão](https://drive.google.com/file/d/18gWiOcuHPGUFPEBeWU-moolkF33-8-92/view?usp=sharing)
2 | Botão de pressão metálicos | [Imagem dos biotões](https://drive.google.com/file/d/17B5EzAg6SMNSU35E2-hMkUhNJSNeOvjI/view?usp=sharing)
2 | Fio de cobre | [Imagem de exemplo; Fios de cobre](https://www.solucoesindustriais.com.br/images/produtos/imagens_10127/p_fio-de-cobre-encapado-10.jpg)
1 | Cabo USB A para micro B | [Imagem de exemplo; Cabo USB](https://d3ugyf2ht6aenh.cloudfront.net/stores/001/930/347/products/cabo_usb_microb_m_2-7249b69acfc54fe23516389599662276-1024-1024.jpg)
2 | Pilha AA | [Imagem de exemplo; Pilhas AA](https://www.baudaeletronica.com.br/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/p/i/pilha-aa.jpg)
 
### Conexões

O sensor de umidade possui dois fios, a se ententer como um polo positivo e um, negativo; entretanto, não há necessidade de distinção, nem ordem.

Destes, um fio é conectado a um dos GNDs do ESP32 e o outro, ao pino 34 - o pino 34 recebe uma atenuação de sinal de 11DB o que, nas configurações estabelecidas, significa que pretende-se ler os valores do pino em toda a sua extensão.

Assim, é feita uma leitura contínua do pino 34 e sempre que haver um valor acima de 1000 (dentro do intervalo `[0, 4095]` - 12bit)

### Montagem do dispositivo

O ESP32, sem os pinos

### Arquitetura e Organização
### Usabilidade
### Construção do programa
### Referências

# RESULTADOS

As fraldas ecológicas confeccionadas para o projeto, tanto a fralda pet, quanto a fralda infantil, se adaptam perfeitamente aos possíveis usuários, trazendo conforto e mantendo a mobilidade do usuário.

<!-- Figura x. Fralda infantil em uso
(inserir imagem)
Fonte: -->

A fralda infantil respondeu perfeitamente aos testes, mostrou-se adaptável ao movimento e confortável, já os componentes acabaram se tornando um distração devido a luz constante presente no microcontrolador que ultrapassa a fralda. Outro ponto que necessitará uma reavaliação, é a fonte de energia escolhida, no caso, o adaptador de pilhas USB. Além de pesar um pouco a fralda, o adaptador esquenta quando em uso, o que pode incomodar e prejudicar a saúde do usuário.

<!-- Figura x. Fralda pet em uso
(inserir imagem)
Fonte: -->

A fralda pet, assim como a infantil, mostrou-se confortável e bem adaptável aos movimentos do usuário, apenas as cavas se mostraram maiores do que o necessário, mesmo com a aplicação de elásticos.  Devendo ser repensadas em uma próxima modelagem, assim como o bolso frontal. O ideal seria que o elástico ficasse mais tensionado, para um melhor ajuste. Com a fralda em uso, percebemos que manter o componente na parte frontal, acaba incomodando o usuário, já que é comum animais deitarem de barriga para baixo. Por isso, torna-se necessário repensar a modelagem para que o componente fique nas costas do animal, evitando desconforto e um possível acesso. Assim como na fralda infantil, há a necessidade de repensar a fonte de energia devido ao calor gerado.

## EXPERIÊNCIA DO USUÁRIO	

Para que a experiência de usuário fosse completa, foi criado um design de marca com logo e slogan, manual de instruções de como conectar os componentes e configurar a fralda.

<!-- Logo e slogan

Figura x. Logo

Fonte: -->

Para a logo da marca EcoPee, pensamos em um design simples e objetivo, com o nome da marca centralizada em fonte Agrandir, ao lado de uma folha em verde, representando a sustentabilidade promovida pela marca. Abaixo está inserida a frase “Fraldas ecologicamente inteligentes” na mesma fonte, dentro de uma forma com bordas arredondadas. As cores escolhidas como identidade da marca foram:

- Creme - código hex: #fff5ed;
- Verde claro - código hex: #d6dfcc;
- Verde escuro - código hex: #288b18;
- Preto - código hex: #000000;

Como slogan, escolhemos a frase “Ecopee, ajudando tutores a zelar com carinho daqueles que mais precisam”  como uma forma de representar os valores da marca.

### Manual de instruções

O manual de instruções foi criado para que facilitasse o entendimento do usuário ao utilizar a fralda inteligente; uma forma de comunicação rápida entre a marca e o cliente.

<!-- Figura x. Capa do manual

Fonte: Autoria própria -->


<!-- Figura x. Manual (conteúdo)


Fonte: Autoria própria -->

### Embalagem

(Inserir imagem da embalagem)

A embalagem escolhida para o recebimento do kit Ecopee, constitui-se de uma caixa de papelão reciclado em tom pardo com etiqueta com o logo da marca e folha de papel de seda para acomodar os componentes do kit.


# CONCLUSÃO

Através do levantamento bibliográfico, pudemos observar que o nosso projeto é além de viável, uma promessa no mercado brasileiro que ainda não possui representantes diretos. Acompanhar crianças e animais de estimação, usuários de fralda, é uma constante diária na vida dos tutores. Ter uma fralda inteligente, e aliada a sustentabilidade, poderia preencher de forma concisa essa lacuna observada.

O projeto em si, trouxe vários desafios que foram aos poucos resolvidos, como a escolha dos tecidos, por exemplo. Ainda assim, para que o projeto se torne viável para comercialização, é necessário que algumas melhorias sejam feitas, como ajustes de modelagem e, principalmente, a busca por componentes que sejam menores, mais leves e que não causem qualquer desconforto ou dano aos usuários, seja por meio de luzes ou por aquecimento. Há também a necessidade da realização de testes de durabilidade em relação aos desgastes de tempo, contato com a urina e lavagem a máquina para definir a resistência do produto. 

# REFERÊNCIAS BIBLIOGRÁFICAS

- Anfíbia Tecidos. Disponível em: <https://www.anfibiatecidos.com.br/pagina/tecido-impermeavel-em-poliuretano-laminado-pul.html>. Acesso em: 4 nov. 2022.

- BACA, M. C. A internet do cocô vem aí: Pampers cria fralda inteligente para bebês. Disponível em: <https://www.terra.com.br/byte/a-internet-do-coco-vem-ai-pampers-cria-fralda-inteligente-para-bebes,874c7bb5265d4c471fd538582a25e1c6ihulqu3a.html>. Acesso em: 16 dez. 2022.

- DIGITAL, O.; REDAÇÃO. Empresa sul-coreana apresenta uma fralda inteligente na CES 2019. Veja como ela funciona. Disponível em: <https://olhardigital.com.br/2019/01/09/consumer-eletronics-show-2019/empresa-sul-coreana-apresenta-uma-fralda-inteligente-na-ces-2019-veja-como-ela-funciona/>. Acesso em: 4 nov. 2022.‌

- DIPANO. Por que Fraldas Dipano. Disponível em: https://www.fraldasdipano.com.br/institucional/produto-e-tecnologia. Acesso em: 03 nov. 2022.

- FRALDA Ecológica - Tecido Interno e Externo das fraldas nacionais. [S.I]: Youtube, 2021. (08 min.), son., color. Disponível em: https://www.youtube.com/watch?v=rtQoAkXTvY4. Acesso em: 03 nov. 2022.

- FRALDADINHOS. Sobre os absorventes. Disponível em: https://www.fraldadinhos.com.br/pagina/sobre-os-absorventes.html. Acesso em: 03 nov. 2022.

- HARTMAN, Kate. Make: Wearable Electronics: Design, prototype, and wear your own interactive garments. Ed. Maker Media, 2014.

- LAMPREIA, L. F. (2013). Sustentabilidade e relações internacionais: a importância das negociações internacionais. Sumários Revista Da ESPM, 17(1), 88–89.

- Louzada, Natasha Veiga. Validação Da Metodologia De Quantificação De Esteróides Anabólicos Androgênicos Endógenos Em Urina Humana. Universidade Federal do Rio de Janeiro, 2019.

- MEU BABY. Tudo Sobre Fraldas Ecológicas. Disponível em: https://meubabyshop.com.br/tudo-sobre-fraldas-ecologicas/. Acesso em: 03 nov. 2022.

- PROBST, Rafaela Quintana; FIORIN, Pauline Brendler Goettems. IMPACTOS DO HERBICIDA À BASE DE GLIFOSATO NO SISTEMA REPRODUTOR E ENDÓCRINO: UMA REVISÃO SISTEMÁTICA. In: Congresso Internacional em Saúde. 2021.

- ROCHA, Natividade; SELORES, Manuela. Dermatite das fraldas. Revista Nascer e Crescer, n. 13 (3), p. 206-214, 2004.

- ROKUGAWA, Marceli Yuli Cunha. Processo de desenvolvimento de uma fralda de alta absorção para incontinência urinária. 2019. Trabalho de Conclusão de Curso. Universidade Tecnológica Federal do Paraná.
