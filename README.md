# Gerador de Lote PDF

**Autor:** Você

## Descrição

Este projeto é um pequeno utilitário em Python para agrupar arquivos PDF sequencialmente em lotes. Ele percorre uma pasta contendo arquivos `.pdf`, ordena-os e cria novos arquivos de saída `LOTE1.pdf`, `LOTE2.pdf`, etc., de modo que cada lote não ultrapasse 9 MB.

O objetivo é facilitar a divisão de uma coleção de PDFs em pacotes menores, preservando a sequência dos arquivos originais.

## O que o projeto faz

- Solicita ao usuário o caminho da pasta que contém os PDFs.
- Detecta e ordena automaticamente todos os arquivos `.pdf` dentro dessa pasta.
- Calcula lotes com base no tamanho total, usando um limite de 9 MB por lote.
- Solicita ao usuário um caminho de destino para salvar os lotes gerados.
- Cria uma pasta de saída com o mesmo nome da pasta de origem dentro do diretório de destino informado.
- Gera arquivos `LOTE1.pdf`, `LOTE2.pdf`, etc., contendo os PDFs agrupados.
- Mostra uma barra de progresso durante a geração dos lotes.

## Requisitos

- Python 3.14 (ou uma versão compatível com `pypdf` e `tqdm`)
- Dependências Python:
  - `pypdf`
  - `tqdm`

## Instalação

1. Clone ou copie o projeto para sua máquina.
2. Instale as dependências necessárias.

```bash
cd /caminho/para/geradorLotePDF
python -m pip install -r requirements.txt
```

> Observação: o arquivo `requirements.txt` contém todas as dependências do ambiente, mas o script usa basicamente `pypdf` e `tqdm`.

## Uso

Execute o script principal:

```bash
python main.py
```

Durante a execução, o programa irá:

1. Pedir o caminho da pasta com os arquivos PDF.
2. Pedir o caminho de destino para gerar os lotes.
3. Confirmar se deseja prosseguir.
4. Gerar os arquivos `LOTE1.pdf`, `LOTE2.pdf`, etc.

### Exemplo de fluxo

- Informe o caminho da pasta com os PDFs: `/home/usuario/documentos/pdfs`
- Informe o caminho de destino sem espaços: `/home/usuario/saida`
- Confirme a operação digitando `S`

Após a conclusão, os arquivos serão gerados em:

```text
/home/usuario/saida/nome-da-pasta-de-origem
```

## Observações

- Se um único PDF for maior que 9 MB, ele será colocado em um lote exclusivo.
- O caminho de destino não pode conter espaços.
- O script só processa arquivos com extensão `.pdf`.

## Estrutura do projeto

- `main.py` - script principal que contém a lógica de agrupamento e geração dos lotes.
- `requirements.txt` - lista de pacotes Python instaláveis para o ambiente.

## Contato

Este README foi criado para documentar o projeto e explicar como usar o utilitário.
