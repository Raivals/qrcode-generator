import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Fonction pour générer le QR code
def generate_qr():
    # Récupérer l'URL saisie
    url = url_entry.get()
    if not url:
        messagebox.showerror("Erreur", "Veuillez entrer une URL ou un texte.")
        return
    
    try:
        # Générer le QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Sauvegarder l'image
        img.save("qrcode.png")
        
        # Afficher le QR code dans l'interface
        img_tk = ImageTk.PhotoImage(img)
        qr_label.config(image=img_tk)
        qr_label.image = img_tk  # Conserver une référence pour éviter le garbage collection
        messagebox.showinfo("Succès", "QR code généré et sauvegardé sous 'qrcode.png'.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur de QR Code")
root.geometry("400x500")
root.resizable(False, False)

# Nouvelle "page" : Titre principal
title_label = tk.Label(root, text="Générateur de QR Code", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Nouvelle "section" : Saisie de l'URL
url_label = tk.Label(root, text="Entrez l'URL ou le texte :", font=("Arial", 12))
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=40, font=("Arial", 12))
url_entry.pack(pady=5)

# Nouvelle "section" : Bouton pour générer le QR code
generate_button = tk.Button(root, text="Générer le QR Code", command=generate_qr, font=("Arial", 12), bg="blue", fg="white")
generate_button.pack(pady=10)

# Nouvelle "section" : Zone pour afficher le QR code
qr_label = tk.Label(root)
qr_label.pack(pady=20)

# Démarrer l'application
root.mainloop()
