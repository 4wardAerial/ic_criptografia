# Sistema Criptográfico
Esse repositório contém um projeto complementar à Iniciação Científica do PICME sobre Estruturas Algébricas e Criptografia, e consiste em um programa para criptografar e decriptografar mensagens ou arquivos de texto por sistemas de criptografia de chave pública estudados na IC; mais precisamente: *RSA*, *ElGamal* e *Curvas Elípticas*. No momento, apenas RSA foi implementada.

O programa foi feito totalmente em Python e roda no terminal. Instruções para utilização podem ser encontradas abaixo. Os algoritmos para calcular a encriptação, bem como as funções necessárias para isso, foram baseados no livro usado na IC, *Algebra for Applications, A. Slinko*.

## Rodando o programa
Sua máquina precisa ter ```Python 3``` instalado para rodar o programa.

Dentro da pasta instalada, basta executar o arquivo ```sistema.exe```

## Uso do programa
Para selecionar uma opções nos menus, basta digitar o número daquela opção e pressionar *Enter*. Caso digite uma opção inválida, o sistema vai apenas recusá-la e pedir outra entrada.

Para as entradas e arquivos de mensagem a serem criptografadas, essas podem conter apenas os caracteres: ```a, b, ..., y, z```, ```A, B, ..., Y, Z```, ```0, 1, ..., 8, 9```, ```, . : ! ? ( )``` e ```espaço```.

### RSA
- **Criptografar mensagem:** Criptografa a mensagem digitada para a pessoa selecionada, usando as chaves públicas dela. A mensagem corresponde a toda sequência de números digitada, incluindo os espaços.

- **Criptografar arquivo:** Criptografa todo o conteúdo do arquivo de texto ```msg.txt```, localizado na pasta ```~sistema\content\src\arquivos\mensagens```, para a pessoa selecionada e salva o resultado em outro arquivo de texto, ```cyph.txt``` no mesmo diretório. 

- **Decriptografar mensagem:** Decriptografa a mensagem digitada para o usuário, usando a sua própria chave privada. 

- **Decriptografar arquivo:** Decriptografa todo o conteúdo do arquivo de texto ```cyph.txt```, localizado na pasta ```~sistema\content\src\arquivos\mensagens```, para o usuário e salva o resultado em outro arquivo de texto, ```msg.txt``` no mesmo diretório.

- **Gerenciar chaves públicas:** Permite que o usuário adicione, remova ou mude pessoas (e suas chaves públicas) do sistema, além de suas próprias chaves. Para adicionar uma nova pessoa, basta digitar seu nome e suas chaves. Caso ela já esteja no sistema, suas chaves públicas são atualizadas para as recém-inseridas. Para remover uma pessoa, basta digitar seu nome e inserir *0* como qualquer uma das chaves. 

    O sistema começa com os seguintes dados carregados:

    | Nome    | Chave pública 'n'             | Chave pública 'e'       |
    |---------|----------------------------------------------|----------|
    | Lucas   | 262925991035088606941229933230703962484209   | 65537    |
    | Alyssa  | 33055727833500460002449499088102170314572649 | 65537    |
    | Anabela | 4711013007790938878139374864507774937997     | 65537    |
    | Leticia | 111777757087311284697527464893754543574057   | 65537    |  
    | João    | 4274790255060999669466438070099888371        | 65537    |

    > *OBS.*: As chaves privadas das pessoas acima não estão armazenadas no sistema, mas foram guardadas abaixo caso seja necessário:

    | Nome    | Chave privada 'd'                            |
    |---------|----------------------------------------------|
    | Lucas   | 62837935785626328843393636080334283176269    |
    | Alyssa  | 27712802082546489378068296278991851489475073 |
    | Anabela | 1205985401097221135340396725521695843869     |
    | Leticia | 19525333218419207273412107861800528952033    |
    | João    | 3927455801115902648102102854245339617        |

- **Criar chaves:** Escolhe dois primos aleatórios (dentre os pré-listados num arquivo) e gera o par de chaves públicas (*n*, *e*) e a chave privada (*d*) para o usuário. As chaves públicas são salvas em um arquivo no sistema e passam a ser as novas chaves do usuário. A chave privada não é salva e o usuário deve salvá-la por conta própria.

    > *OBS.*: Embora o sistema já tenha chaves públicas salvas para o usuário, é necessário que novas sejam geradas para que o novo usuário (você) possa guardar a chave privada correspondente.

#### **# Exemplo**
João usa seu sistema para criar chaves novas:

(n, e, d) = (4274790255060999669466438070099888371, 65537, 3927455801115902648102102854245339617)

Maria faz o mesmo com seu sistema e gera:

(n, e, d) = (270704023373008444681673490480975121, 65537, 200645721338590789097496227963862785)

Eles então compartilham as chaves públicas (n, e), e João adiciona Maria em seu sistema. Daí, criptografa a mensagem ```Oi Maria! Aqui eh o Joao :)```, que resulta em:

```267270009290200582326079739699382790 119690501687953434965511702811910125```

e manda para Maria. Se Maria, no sistema dela, escolher decriptografar a mensagem acima com a sua própria chave privada, vai obter exatamente a mensagem original! Caso queira confirmar, o sistema já começa com os dados de Maria, então resta apenas copiar a mensagem e sua chave privada.

Para mandar mensagens em arquivos, a ideia é a mesma, a diferença é que João escreveria a mensagem no arquivo ```msg.txt``` e passaria para Maria o arquivo ```cyph.txt```.

## Arquivos do progama
Esses arquivos encontram-se em ```~sistema/src/arquivos/dados``` e são essenciais para que o programa funcione.

- ```dados_usuario.txt```: Armazena as chaves públicas do usuário em duas linhas separadas. A primeira contém o valor de *n*, a segunda, de *e*.

- ```dados_publicos.txt```: Armazena os nomes e as chaves públicas de outras pessoas separados por vírgula e sem espaços entre eles.
 
- ```primos.txt```: Armazena uma lista de vários primos grandes, um em cada linha.

Não é recomendado que se altere esse arquivos manualmente, visto que sua formatação incorreta vai interromper o funcionamento do sistema. Todas as alterações importantes podem ser feitas pelo próprio sistema.

A pasta ```~\src``` (fora da pasta ```~\sistema```) contém os arquivos de código e os arquivos de texto originais, que foram convertidos em um executável para facilitar o uso do sistema com uso da ferramenta [*auto-py-to-exe*](https://github.com/brentvollebregt/auto-py-to-exe). Note que alterar os arquivos de texto dessa pasta não influencia o sistema, pois esse usa os que estão no diretório ```~sistema/src/arquivos```.