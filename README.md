# Sorteador de Números Mega Sena

## Descrição

Este programa simula a geração de números aleatórios para o sorteio da **Mega Sena**. O usuário pode inserir o número do jogo vencedor, e o script irá gerar diversos bilhetes aleatórios. O programa irá comparar cada bilhete gerado com o número vencedor e mostrar quantos acertos (3, 4 ou 5) ocorreram, além de contar o número de vezes que você ganhou (com todos os 6 números). Também serão exibidos os números de **Quinas** (5 acertos), **Quadras** (4 acertos) e **Triplas** (3 acertos).

## Funcionalidades

- **Geração de Números Aleatórios**: Gera números aleatórios (6 números entre 1 e 60) para cada bilhete.
- **Entrada de Números Vencedores**: O usuário pode inserir os números vencedores.
- **Contagem de Acertos**: O programa compara cada bilhete gerado com os números vencedores, contando quantos números coincidem.
- **Exibição de Resultados**: Exibe o número de vitórias (todos os 6 números), Quinas (5 acertos), Quadras (4 acertos) e Triplas (3 acertos).

## Como Usar

1. **Inicie o Programa**: Execute o script.
2. **Informe a Quantidade de Jogos**: O programa pedirá quantos jogos você deseja sortear.
3. **Digite os Números Vencedores**: O programa pedirá para você inserir os números vencedores (6 números entre 1 e 60), separados por espaço.
4. **Resultados**: O programa irá gerar os jogos e mostrar os acertos em cada um, além de contar as vitórias e os acertos.

## Exemplo de Execução

```text
Quantos jogos deseja sortear
R: 5

Digite o numero do jogo vencedor com espaços
Exp: "10 20 30 40 50 60"
R: 10 20 30 40 50 60

00001)  05  10  15  20  30  40 | Acertos: 4
00002)  01  08  13  14  22  60 | Acertos: 3
00003)  10  20  30  40  50  60 | Acertos: 6 (Ganhou!)
...
Numero de jogos ganhos: 1
Numero de quinas: 0
Numero de quadras: 0
Numero de triplas: 1
```

## Requisitos

- Python 3.x

## Como Rodar o Script

1. **Instalar o Python**: Certifique-se de que o Python 3.x está instalado em seu computador.
2. **Executar o Script**: Abra o terminal e execute o arquivo Python:
   ```bash
   python sorteio_mega_sena.py
   ```
