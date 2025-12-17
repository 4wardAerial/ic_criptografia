# Sistema Criptográfico
Esse repositório contém um projeto complementar à Iniciação Científica do PICME sobre Estruturas Algébricas e Criptografia, e consiste em um programa para criptografar e decriptografar mensagens ou arquivos de texto por sistemas de criptografia de chave pública estudados na IC; mais precisamente: *RSA*, *ElGamal* e *Curvas Elípticas*.

O programa foi feito totalmente em Python e roda no terminal. Instruções para utilização podem ser encontradas abaixo. Os algoritmos para calcular a encriptação, bem como as funções necessárias para isso, foram baseados no livro usado na IC, *Algebra for Applications, A. Slinko*.

## Como usar:
### Rodando o programa
Sua máquina precisa ter ```Python 3``` instalado para rodar o programa.

Dentro da pasta instalada, basta executar o arquivo ```sistema.exe```

### Uso do programa
Para selecionar uma opções nos menus, basta digitar o número daquela opção e pressionar *Enter*. Caso digite uma opção inválida, o sistema vai apenas recusá-la e pedir outra entrada.

Para as entradas e arquivos de mensagem a serem criptografadas, essas podem conter apenas os caracteres: ```a, b, ..., y, z```, ```A, B, ..., Y, Z```, ```0, 1, ..., 8, 9```, ```, . ! ?``` e ```espaço```.

#### RSA
- **Criptografar mensagem:** Criptografa a mensagem digitada para a pessoa selecionada, usando as chaves públicas dela. A mensagem corresponde a toda sequência de números digitada, incluindo os espaços.

- **Criptografar arquivo:** Criptografa todo o conteúdo do arquivo de texto ```msg.txt```, localizado na pasta ```~\arquivos\mensagens```, para a pessoa selecionada e salva o resultado em outro arquivo de texto, ```cyph.txt``` no mesmo diretório. 

- **Decriptografar mensagem:** Decriptografa a mensagem digitada para o usuário, usando a sua própria chave privada. 

- **Decriptografar arquivo:** Decriptografa todo o conteúdo do arquivo de texto ```cyph.txt```, localizado na pasta ```~\arquivos\mensagens```, para o usuário e salva o resultado em outro arquivo de texto, ```msg.txt``` no mesmo diretório.

- **Criar chaves:** Escolhe dois primos aleatórios (dentre os pré-listados num arquivo) e gera o par de chaves públicas (*n*, *e*) e a chave privada (*d*) para o usuário. As chaves públicas são salvas em um arquivo no sistema e passam a ser as novas chaves do usuário. A chave privada não é salva e o usuário deve salvá-la por conta própria. 

- **Gerenciar chaves públicas:** Permite que o usuário adicione, remova ou mude pessoas (e suas chaves públicas) do sistema. Para adicionar uma nova, basta digitar seu nome e suas chaves. Caso essa pessoa já esteja no sistema, suas chaves públicas são atualizadas para as recém-inseridas. Para remover uma pessoa, basta digitar seu nome e inserir *0* como qualquer uma das chaves.

#### ElGamal

### Arquivos do progama
- ```dados_publicos.txt```: 

Não é recomendado alterar os arquivos localizado em ```~/arquivos/dados``` manualmente, visto que formatações indevidas vão causar erros no sistema. 