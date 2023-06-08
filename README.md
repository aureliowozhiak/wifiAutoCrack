# README - PoC para Teste de Senhas Fracas em Wi-Fi
Este é um código de prova de conceito (PoC) para testar senhas fracas em redes Wi-Fi. É importante observar que a execução de testes de senhas fracas em redes Wi-Fi sem a permissão explícita do proprietário da rede é uma atividade ilegal e antiética. Este código deve ser utilizado apenas para fins educacionais e de conscientização, e nunca para acessar redes Wi-Fi sem a devida autorização.

## Requisitos
Python 3.x
nmcli (NetworkManager command-line tool)
Certifique-se de ter o Python 3.x instalado em seu sistema, bem como o utilitário nmcli. Você pode instalá-lo usando os comandos apropriados para o seu sistema operacional.

## Uso
Certifique-se de ter um arquivo de senhas (senhas.txt) contendo as senhas que você deseja testar. Cada senha deve ser listada em uma linha separada.
Abra o arquivo Python (crack.py) em seu editor de texto ou ambiente de desenvolvimento preferido.
No código-fonte, substitua 'HUAWEI-2.4G-ttHH' pela SSID da rede Wi-Fi que você deseja testar.
Execute o código e observe os resultados no console.
Observação: Este código tentará se conectar à rede Wi-Fi usando as senhas fornecidas no arquivo de senhas. Se uma conexão for bem-sucedida (retorno 0 do comando nmcli), a senha correspondente será exibida no console e o programa será encerrado.

## Aviso Legal
O uso deste código é de total responsabilidade do usuário. Certifique-se de ter a autorização adequada antes de executar qualquer teste em redes Wi-Fi que não sejam de sua propriedade. O autor deste código não se responsabiliza por quaisquer consequências legais ou danos causados pelo uso indevido deste código.

## Nota Final
Este código é fornecido apenas para fins educacionais e de conscientização. Use-o de forma ética e responsável, respeitando sempre as leis e regulamentações locais.
