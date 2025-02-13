# Carrega as dependências
import cv2
import time

# Cores das classes
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

# Carrega as classes
class_names = [0]
with open("coco.names.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

# Captura do vídeo
cap = cv2.VideoCapture(0)

# Carregando os pesos da rede neural
# net = cv2.dnn.readNet("weights/yolov4.weights", "cfg/yolov4.cfg")
net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg")

# Setando os parâmetros da rede neural
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255)

# Lendo os frames do vídeo
while True:
    # Captura o frame
    _, frame = cap.read()
    if frame is None:
        break  # Se o frame for None, significa que o vídeo acabou.

    # Começo da contagem dos MS
    start = time.time()

    # Detecção
    classes, scores, boxes = model.detect(frame, 0.1, 0.2)

    # Fim da contagem dos MS
    end = time.time()

    # Percorre todas as detecções
    for (classid, score, box) in zip(classes, scores, boxes):
        # Gerando uma cor para a classe
        color = COLORS[int(classid) % len(COLORS)]

        # Pegando o nome da classe pelo ID e o seu score de acurácia
        label = f"{class_names[classid]} : {score}"

        # Desenhando a box de detecção
        cv2.rectangle(frame, box, color, 2)

        # Escrevendo o nome da classe em cima da box do objeto
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Calculando o tempo que demorou para fazer a detecção
    fps_label = f"FPS: {round((1.0 / (end - start)), 2)}"

    # Escrevendo o fps da imagem
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5)
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    # Mostrando a imagem
    cv2.imshow("Detections", frame)

    # Espera da resposta (pressione 'ESC' para sair)
    if cv2.waitKey(1) == 27:  # 27 é o código para a tecla 'ESC'
        break

# Liberação da captura de vídeo e destruição das janelas
cap.release()
cv2.destroyAllWindows()
