import os
import platform
from pathlib import Path
from pypdf import PdfWriter
from tqdm import tqdm

def main():
    print("--- Agrupador Sequencial de PDFs ---")
    
    # Pergunta a pasta e limpa possíveis aspas/espaços em branco residuais no início/fim
    input_path = input("Digite o caminho da pasta com os PDFs: ").strip(" '\"")
    folder_path = Path(input_path).resolve()
    
    if not folder_path.is_dir():
        print(f"Erro: O diretório '{folder_path}' não foi encontrado.")
        return

    # Buscar e ordenar arquivos PDFs para garantir a sequência (001, 002, etc.)
    pdf_files = sorted(folder_path.glob("*.pdf"))
    
    if not pdf_files:
        print("Nenhum arquivo '.pdf' encontrado na pasta informada.")
        return

    print(f"\nAnalisando {len(pdf_files)} PDFs. Calculando estimativa de lotes...")

    # Calcular lotes baseados no tamanho (Máximo 9MB por lote)
    MAX_SIZE_BYTES = 9 * 1024 * 1024 
    lots = []
    current_lot = []
    current_size = 0

    for pdf in pdf_files:
        file_size = pdf.stat().st_size
        
        if file_size > MAX_SIZE_BYTES:
            print(f"Aviso: O arquivo '{pdf.name}' excede 9MB sozinho ({file_size / (1024*1024):.2f} MB). Ele ocupará um lote exclusivo.")
            
        if current_size + file_size > MAX_SIZE_BYTES and current_lot:
            lots.append(current_lot)
            current_lot = [pdf]
            current_size = file_size
        else:
            current_lot.append(pdf)
            current_size += file_size
            
    if current_lot:
        lots.append(current_lot)

    # NOVO: Solicitar caminho exato e bloquear espaços
    print("\nDefinição do local de saída:")
    while True:
        dest_input = input("Digite o caminho exato onde deseja salvar os lotes (NÃO pode conter espaços): ").strip(" '\"")
        
        if not dest_input:
            print("Erro: O caminho não pode estar vazio. Tente novamente.")
            continue
            
        if " " in dest_input:
            print("Erro: O caminho de destino contém espaços. Por favor, insira um caminho válido e sem espaços.")
            continue
            
        output_base = Path(dest_input).resolve()
        break

    # Monta a estrutura de saída usando o nome da pasta original
    folder_name = folder_path.name
    output_dir = output_base / folder_name

    # Resumo para o usuário antes da confirmação
    print(f"\nResumo da Operação:")
    print(f"- Total de arquivos: {len(pdf_files)}")
    print(f"- Quantidade estimada de lotes: {len(lots)}")
    print(f"- Diretório de destino final: {output_dir}")
    
    confirm = input("\nDeseja prosseguir com a juntada? (S/N): ").strip().upper()
    if confirm != 'S':
        print("Operação cancelada pelo usuário.")
        return

    # Criar a estrutura de pastas necessária (cria o caminho todo se não existir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Juntar PDFs e mostrar progresso
    print("\nIniciando a geração dos lotes...")
    
    for i, lot in enumerate(tqdm(lots, desc="Progresso da Juntada", unit="lote"), start=1):
        writer = PdfWriter()
        
        for pdf_path in lot:
            writer.append(pdf_path)
            
        output_file = output_dir / f"LOTE{i}.pdf"
        
        with open(output_file, "wb") as f_out:
            writer.write(f_out)
            
    print(f"\nProcesso concluído com sucesso! Os {len(lots)} lotes estão salvos em:\n{output_dir}")

if __name__ == "__main__":
    main()