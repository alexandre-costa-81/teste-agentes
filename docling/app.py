import os
import curses
from docling.document_converter import DocumentConverter

DOCUMENTS_DIR = "documentos"
CONVERTED_DIR = "convertidos"


def list_files(directory):
    """Lista todos os arquivos em um diretório."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def file_selector(stdscr, files):
    """Interface de seleção de arquivos usando setas do teclado."""
    curses.curs_set(0)  # Oculta o cursor
    selected = 0

    while True:
        stdscr.clear()
        stdscr.addstr("Selecione um arquivo e pressione Enter:\n", curses.A_BOLD)

        for i, file in enumerate(files):
            mode = curses.A_REVERSE if i == selected else curses.A_NORMAL
            stdscr.addstr(f"{file}\n", mode)

        key = stdscr.getch()

        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(files) - 1:
            selected += 1
        elif key == 10:  # Tecla Enter
            return files[selected]


def main(stdscr):
    """Função principal do programa."""
    files = list_files(DOCUMENTS_DIR)
    if not files:
        stdscr.addstr("Nenhum arquivo encontrado no diretório documentos.\n")
        stdscr.getch()
        return

    selected_file = file_selector(stdscr, files)

    source_path = os.path.join(DOCUMENTS_DIR, selected_file)
    output_filename = os.path.splitext(selected_file)[0] + ".md"
    output_path = os.path.join(CONVERTED_DIR, output_filename)

    os.makedirs(CONVERTED_DIR, exist_ok=True)

    converter = DocumentConverter()
    result = converter.convert(source_path)

    markdown_content = result.document.export_to_markdown()

    with open(output_path, "w") as file:
        file.write(markdown_content)

    stdscr.clear()
    stdscr.addstr(f"Arquivo convertido e salvo em '{output_path}'\n", curses.A_BOLD)
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
