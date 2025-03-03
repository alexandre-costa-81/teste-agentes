from docling.document_converter import DocumentConverter

source = "Regimento_COEPEA.pdf"
converter = DocumentConverter()
result = converter.convert(source)

# Obtém o markdown gerado
markdown_content = result.document.export_to_markdown()

# Salva o conteúdo em um arquivo .md
with open("nome.md", "w") as file:
    file.write(markdown_content)

print("Arquivo 'nome.md' foi salvo com sucesso!")
