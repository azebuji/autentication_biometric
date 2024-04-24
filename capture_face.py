import cv2
import face_recognition

# Inicializar a webcam
webcam = cv2.VideoCapture(0)

# Capturar imagens de treinamento
print("Pressione 'c' para capturar uma imagem. Pressione 'q' para sair.")
while True:
    # Capturar um frame da webcam
    ret, frame = webcam.read()

    # Exibir o frame
    cv2.imshow('Video', frame)

    # Se a tecla 'c' for pressionada, capturar a imagem e salvar no arquivo
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # Salvar a imagem capturada em um arquivo (por exemplo, 'captured_image.jpg')
        cv2.imwrite('captured_image.jpg', frame)
        print("Imagem capturada e salva.")
        break

# Liberar a webcam e fechar todas as janelas abertas
webcam.release()
cv2.destroyAllWindows()

# Carregar a imagem capturada e codificar as características faciais
captured_image = face_recognition.load_image_file('captured_image.jpg')
captured_face_encoding = face_recognition.face_encodings(captured_image)[0]


# Carregar as informações de pessoas cadastradas do arquivo de texto
known_face_encodings = []
known_face_names = []

with open('cadastro.txt', 'r') as file:
    for line in file:
        name, encoding = line.strip().split(':')
        known_face_names.append(name)
        encoding_array = np.fromstring(encoding, dtype=float, sep=',')
        known_face_encodings.append(encoding_array)

# Adicionar a nova face ao arquivo de texto
with open('cadastro.txt', 'a') as file:
    file.write('Nova Pessoa:')
    for enc in captured_face_encoding:
        file.write(f'{enc},')
    file.write('\n')

# Agora, known_face_encodings e known_face_names contêm as informações de todas as pessoas cadastradas

# Salvar a codificação facial no banco de dados
# Por exemplo, você pode usar um banco de dados SQLite
#import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
#conn = sqlite3.connect('cadastro.db')
#cursor = conn.cursor()

# Criar a tabela se não existir
#cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas
#                  (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, face_encoding TEXT)''')

# Inserir os dados na tabela
#cursor.execute('INSERT INTO pessoas (nome, face_encoding) VALUES (?, ?)', ('Nome da Pessoa', captured_face_encoding.tobytes()))

# Commit para salvar as alterações
#conn.commit()

# Fechar a conexão com o banco de dados
#conn.close()