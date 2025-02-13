# Detector de Objetos com YOLOv4-Tiny 🚀

Este projeto usa o YOLOv4-Tiny para detectar objetos em tempo real através da câmera do seu dispositivo! Com ele, você pode identificar o que está acontecendo ao seu redor com uma precisão surpreendente.

## Como Funciona 💡

1. O código carrega os pesos da rede neural YOLOv4-Tiny, que é super eficiente para detecção de objetos em tempo real.
2. Ele processa cada frame da câmera, detectando objetos como pessoas, animais e muito mais!
3. As caixas de detecção aparecem ao redor dos objetos, e você pode ver as informações de acurácia e o FPS (frames por segundo) na tela.
4. Quando você pressiona "ESC", o código para a execução.

## Como Rodar o Projeto 🏃‍♂️

1. Instale as dependências:
    ```bash
    pip install opencv-python
    ```

2. Certifique-se de que você tem o arquivo `coco.names.txt`, que contém os nomes das classes de objetos que o modelo pode detectar.

3. Baixe os pesos do modelo `yolov4-tiny.weights` e o arquivo de configuração `yolov4-tiny.cfg`. Você pode encontrar esses arquivos na página oficial do YOLO ou outros repositórios confiáveis.

4. Execute o código:
    ```bash
    python seu_codigo.py
    ```

5. Aproveite a magia! ✨

## Detalhes Técnicos 📊

- **Modelo Usado:** YOLOv4-Tiny (uma versão mais leve e rápida do YOLO)
- **Entrada:** Câmera do dispositivo (geralmente a webcam)
- **Saída:** Vídeo com caixas de detecção de objetos e FPS em tempo real.

## Como Funciona o Código? 🤔

- O código começa carregando o modelo pré-treinado e os nomes das classes de objetos.
- Ele abre a câmera, captura o vídeo em tempo real e começa a fazer a detecção com o modelo YOLO.
- A cada detecção, ele desenha caixas ao redor dos objetos e exibe o nome da classe e a acurácia dessa detecção.
- No final, ele mostra a taxa de FPS (quantos frames por segundo o código está processando).

## Teclas de Atalho 🖱️

- **ESC:** Para sair do programa.

## Dicas e Sugestões 💬

- Se quiser tentar outro modelo, basta trocar os arquivos de configuração e pesos para outro modelo YOLO.
- Teste diferentes resoluções de entrada para ver como o FPS muda.
