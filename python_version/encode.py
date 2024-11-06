import os
import cv2
import face_recognition
import numpy as np

def preprocess_image(image_path, output_size=(128, 128)):
    """
    Prétraitement d'une image pour la reconnaissance faciale.
    - Détecte et recadre le visage.
    - Redimensionne et normalise les pixels.

    Args:
        image_path (str): Chemin de l'image à traiter.
        output_size (tuple): Taille de sortie souhaitée (largeur, hauteur).

    Returns:
        np.ndarray: L'image prétraitée.
    """
    # Charger l'image
    image = face_recognition.load_image_file(image_path)
    
    # Détection des visages
    face_locations = face_recognition.face_locations(image)
    if face_locations:
        # Prendre le premier visage détecté
        top, right, bottom, left = face_locations[0]
        face_image = image[top:bottom, left:right]
    else:
        # Si aucun visage détecté, utiliser l'image entière
        face_image = image

    # Redimensionner l'image à la taille souhaitée
    face_image = cv2.resize(face_image, output_size)

    # Normaliser les pixels (mise à l'échelle entre 0 et 1)
    face_image = face_image / 255.0

    return face_image

def preprocess_dataset(input_dir, output_dir, output_size=(128, 128)):
    """
    Prétraite toutes les images d'un dossier et les sauvegarde dans un nouveau dossier.
    
    Args:
        input_dir (str): Chemin vers le dossier des images originales.
        output_dir (str): Chemin vers le dossier de sortie pour les images traitées.
        output_size (tuple): Taille de sortie souhaitée (largeur, hauteur).
    """
    # Créer le dossier de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)

    for person_name in os.listdir(input_dir):
        person_dir = os.path.join(input_dir, person_name)
        output_person_dir = os.path.join(output_dir, person_name)
        
        # S'assurer que chaque sous-dossier pour les personnes est créé dans le dossier de sortie
        os.makedirs(output_person_dir, exist_ok=True)
        
        if not os.path.isdir(person_dir):
            continue
        
        for image_name in os.listdir(person_dir):
            image_path = os.path.join(person_dir, image_name)
            processed_image = preprocess_image(image_path, output_size=output_size)
            
            # Convertir l'image en valeurs 8 bits pour la sauvegarde
            processed_image_uint8 = (processed_image * 255).astype(np.uint8)

            # Sauvegarder l'image traitée
            output_path = os.path.join(output_person_dir, image_name)
            cv2.imwrite(output_path, cv2.cvtColor(processed_image_uint8, cv2.COLOR_RGB2BGR))
            print(f"Image traitée et sauvegardée : {output_path}")

# Exécuter le prétraitement
input_directory = './../secu'  # Chemin vers le dossier contenant les images originales
output_directory = './../secu_preprocess'  # Chemin vers le dossier pour sauvegarder les images traitées
preprocess_dataset(input_directory, output_directory)
