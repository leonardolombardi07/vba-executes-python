# Planilha

Ver código VBA, tá tudo explicadinho lá.

## Código

Pra transformar o arquivo main.py em um executável:
Ver: https://pyinstaller.org/

1. `pip install pyinstaller`
2. Na mesma pasta do arquivo main.py:
   `pyinstaller main.py`

Isso vai gerar um arquivo e duas pastas:
main.spec -> arquivo com informações sobre o comando que você deu (pyinstaller main.py)
build -> gera alguns arquivos temporários que o pyinstaller precisa pra gerar o executável propriamente dito
dist -> contém o executável, que pode ser "distribuído"

O óbvio precisa ser dito: importante lembrar que qualquer alteração no código (nesse caso, main.py), tem que rodar
pyinstaller main.py pra atualizar o executável
