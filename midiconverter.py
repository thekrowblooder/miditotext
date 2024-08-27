import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage
import pyperclip

def open_midi_file():
    midi_file_path = filedialog.askopenfilename(filetypes=[("MIDI files", "*.mid")])
    if not midi_file_path:
        return

    text_area.delete(1.0, tk.END)
    
    midi_file = MidiFile(midi_file_path)
    text = ""
    for i, track in enumerate(midi_file.tracks):
        text += f"Track {i}: {track.name}\n"
        for msg in track:
            if msg.type in ['note_on', 'note_off']:
                text += f"{msg.type} {msg.note} {msg.velocity} {msg.time} {i}\n"
            elif msg.type == 'meta':
                text += f"meta {msg.type} {msg.time} {i}\n"
    text_area.insert(tk.END, text)

def save_midi_file():
    text = text_area.get(1.0, tk.END).strip()
    if not text:
        messagebox.showerror("Error", "El texto no se convirtió.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".mid", filetypes=[("MIDI files", "*.mid")])
    if not file_path:
        return

    midi_file = MidiFile()
    tracks_dict = {}

    lines = text.split('\n')
    for line in lines:
        parts = line.split()
        if len(parts) >= 5:
            msg_type = parts[0]
            try:
                note = int(parts[1])
                velocity = int(parts[2])
                time = int(parts[3])
                track_index = int(parts[4])

                if track_index not in tracks_dict:
                    tracks_dict[track_index] = MidiTrack()
                    midi_file.tracks.append(tracks_dict[track_index])

                if msg_type == 'note_on':
                    tracks_dict[track_index].append(Message('note_on', note=note, velocity=velocity, time=time))
                elif msg_type == 'note_off':
                    tracks_dict[track_index].append(Message('note_off', note=note, velocity=velocity, time=time))
                elif msg_type == 'meta':
                    tracks_dict[track_index].append(MetaMessage(parts[1], time=time))

            except ValueError:
                continue

    selected_instrument = instrument_combobox.get()
    instrument_map = {
        'Piano': 0,
        'Guitar': 24,
        'Violin': 40,
        'Flute': 73,
        'Organ': 19,
        'Trumpet': 56,
        'Synth Lead': 81,
        'Strings': 50,
        'Drums': 118,
        'Bass': 33
    }
    instrument_number = instrument_map.get(selected_instrument, 0)

    for i, track in enumerate(midi_file.tracks):
        track = [msg for msg in track if msg.type != 'program_change']
        track.insert(0, Message('program_change', program=instrument_number))
        midi_file.tracks[i] = track

    midi_file.save(file_path)
    messagebox.showinfo("Info", "El MIDI fue guardado con el instrumento seleccionado.")

def show_format_info():
    message = (
        "Este es el formato que maneja para la creación de MIDI:\n\n"
        "Track 0:\n"
        "program_change <instrument_number> 0 0\n"
        "note_on <note> <velocity> <start_time> 0\n"
        "note_off <note> <velocity> <end_time> 0\n\n"
        "Track 1:\n"
        "program_change <instrument_number> 0 1\n"
        "note_on <note> <velocity> <start_time> 1\n"
        "note_off <note> <velocity> <end_time> 1\n\n"
        "Track 2:\n"
        "program_change <instrument_number> 0 2\n"
        "note_on <note> <velocity> <start_time> 2\n"
        "note_off <note> <velocity> <end_time> 2\n\n"
        "<instrument_number>: El número del instrumento (por ejemplo, 0 para Piano).\n"
        "<note>: El número de la nota (por ejemplo, 60 para C4).\n"
        "<velocity>: La velocidad de la nota (por ejemplo, 100).\n"
        "<start_time>: El tiempo de inicio de la nota en ticks.\n"
        "<end_time>: El tiempo de finalización de la nota en ticks."
    )

    def copy_to_clipboard():
        pyperclip.copy(message)
        messagebox.showinfo("Copiado", "Instrucciones copiadas al portapapeles.")

    msg_box = tk.Toplevel(app)
    msg_box.title("Formato MIDI")
    msg_box.geometry("600x400")

    label = tk.Label(msg_box, text=message, justify=tk.LEFT, padx=10, pady=10, wraplength=580)
    label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    copy_button = ttk.Button(msg_box, text="Copiar instrucciones", command=copy_to_clipboard)
    copy_button.pack(side=tk.BOTTOM, padx=10, pady=10)

app = tk.Tk()
app.title("MIDI Converter - By TheKrowBlooder")
app.geometry("700x500")
app.configure(bg='#f0f0f0')

control_frame = tk.Frame(app, bg='#f0f0f0')
control_frame.pack(pady=20, padx=10, fill='x')

select_button = ttk.Button(control_frame, text="Seleccionar archivo MIDI", command=open_midi_file)
select_button.grid(row=0, column=0, padx=5, pady=5, sticky='w')

convert_button = ttk.Button(control_frame, text="Convertir a MIDI", command=save_midi_file)
convert_button.grid(row=0, column=1, padx=5, pady=5, sticky='w')

instrument_label = ttk.Label(control_frame, text="Seleccionar instrumento:", background='#f0f0f0')
instrument_label.grid(row=0, column=2, padx=5, pady=5, sticky='w')

instrument_combobox = ttk.Combobox(control_frame, values=[
    'Piano', 'Guitar', 'Violin', 'Flute', 'Organ', 'Trumpet', 'Synth Lead', 'Strings', 'Drums', 'Bass'
], state='readonly')
instrument_combobox.grid(row=0, column=3, padx=5, pady=5, sticky='w')
instrument_combobox.set('Piano')

faq_button = ttk.Button(control_frame, text="?", command=show_format_info)
faq_button.grid(row=0, column=4, padx=5, pady=5, sticky='w')

text_frame = tk.Frame(app, bg='#ffffff', bd=1, relief='solid')
text_frame.pack(fill='both', expand=True, padx=10, pady=10)

scrollbar_y = ttk.Scrollbar(text_frame, orient=tk.VERTICAL)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

text_area = tk.Text(text_frame, height=15, wrap='word', font=('Helvetica', 12), yscrollcommand=scrollbar_y.set)
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

scrollbar_y.config(command=text_area.yview)

app.mainloop()
