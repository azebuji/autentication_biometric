import face_recognition
import cv2

# Carregar imagens de treinamento e associá-las a nomes
known_face_encodings = [...]  # Lista de codificações faciais de pessoas cadastradas
known_face_names = [...]  # Lista de nomes correspondentes

# Inicializar a webcam
webcam = cv2.VideoCapture(0)

while True:
    # Capturar um frame da webcam
    ret, frame = webcam.read()
    
    # Converter o frame de BGR (OpenCV) para RGB (face_recognition)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detectar rostos no frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Para cada rosto detectado no frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Comparar com as faces conhecidas
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Desconhecido"

        # Verificar se há alguma correspondência
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Desenhar um retângulo e o nome do rosto na imagem
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    # Exibir o frame resultante
    cv2.imshow('Video', frame)

    # Se a tecla 'q' for pressionada, sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a webcam e fechar todas as janelas abertas
webcam.release()
cv2.destroyAllWindows()