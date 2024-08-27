# MIDI Converter

MIDI Converter es una aplicación de escritorio diseñada para convertir archivos de texto en archivos MIDI y viceversa. Utiliza la biblioteca `tkinter` para la interfaz gráfica y `mido` para la manipulación de archivos MIDI.

## Características

- **Abrir archivos MIDI:** Permite seleccionar un archivo MIDI y visualizar su contenido en un área de texto.
- **Guardar archivos MIDI:** Convierte el contenido del área de texto a un archivo MIDI, aplicando el instrumento seleccionado.
- **Seleccionar instrumento:** Ofrece una lista desplegable para seleccionar el instrumento que se aplicará a la pista MIDI.
- **Formato de archivo:** Proporciona información detallada sobre el formato de entrada esperado para la conversión.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `tkinter` (generalmente incluida en las instalaciones estándar de Python)
  - `mido`
  - `pyperclip`

Puedes instalar las bibliotecas necesarias usando pip:

```sh
pip install mido pyperclip
