import os, numpy as np

MODEL = os.environ.get("MODEL", "models/model.tflite")
ON_K10 = os.environ.get("SIMULATE","0") != "1"

def classify_stub(_):
    labels = ["gato", "cachorro", "teclado", "tela", "copo"]
    return {"label": str(np.random.choice(labels)), "score": float(np.random.rand())}

def load_tflite(model_path):
    try:
        import tflite_runtime.interpreter as tflite
        interpreter = tflite.Interpreter(model_path=model_path)
    except Exception:
        # fallback tenta TensorFlow lite (PC)
        import tensorflow as tf
        interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

def run_classifier(interpreter, img):
    import numpy as np
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    inp = np.zeros(input_details[0]["shape"], dtype=input_details[0]["dtype"])
    interpreter.set_tensor(input_details[0]["index"], inp)
    interpreter.invoke()
    out = interpreter.get_tensor(output_details[0]["index"])
    idx = int(np.argmax(out))
    score = float(np.max(out))
    return {"label": f"classe_{idx}", "score": score}

def main():
    if not os.path.exists(MODEL):
        print("Modelo não encontrado, rodando simulado:", classify_stub(None)); return
    try:
        interpreter = load_tflite(MODEL)
        print("TFLite carregado:", MODEL)
        # TODO: capturar imagem da câmera da K10 e pré-processar conforme o seu modelo
        result = run_classifier(interpreter, None)
        print(result)
    except Exception as e:
        print("Falha TFLite:", e)
        print("Fallback simulado:", classify_stub(None))

if __name__ == "__main__":
    main()
