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
```bash
pip install mido pyperclip
```

## Uso
Abrir un archivo MIDI:

Haz clic en el botón "Seleccionar archivo MIDI" para abrir un archivo MIDI. El contenido del archivo se mostrará en el área de texto.
Convertir a MIDI:

Modifica el contenido en el área de texto según sea necesario.
Selecciona el instrumento deseado en el combo box.
Haz clic en "Convertir a MIDI" para guardar el archivo modificado.
Información del formato:

Haz clic en el botón "?" para abrir una ventana con instrucciones detalladas sobre el formato de entrada.
Interfaz de Usuario
Botón "Seleccionar archivo MIDI": Abre un cuadro de diálogo para seleccionar un archivo MIDI.
Botón "Convertir a MIDI": Guarda el contenido del área de texto como un archivo MIDI con el instrumento seleccionado.
Combo Box de instrumentos: Permite seleccionar el instrumento que se aplicará a la pista MIDI.
Botón "?": Muestra una ventana con información sobre el formato de entrada esperado para la conversión.

##  Ejemplo de Formato de Entrada
Track 0:
program_change <instrument_number> 0 0
note_on <note> <velocity> <start_time> 0
note_off <note> <velocity> <end_time> 0

Track 1:
program_change <instrument_number> 0 1
note_on <note> <velocity> <start_time> 1
note_off <note> <velocity> <end_time> 1

<instrument_number>: El número del instrumento (por ejemplo, 0 para Piano).
<note>: El número de la nota (por ejemplo, 60 para C4).
<velocity>: La velocidad de la nota (por ejemplo, 100).
<start_time>: El tiempo de inicio de la nota en ticks.
<end_time>: El tiempo de finalización de la nota en ticks.


