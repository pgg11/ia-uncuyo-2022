import pandas as pd
import matplotlib.pyplot as plt

def plot_score_progression(file_path):
    # Cargar los datos del CSV
    df = pd.read_csv(file_path)

    # Graficar episodios vs score
    plt.figure(figsize=(10, 5))
    plt.plot(df["Episode"], df["Score"], marker="o", linestyle="-", color="b", label="Score")

    plt.xlabel("Episodio")
    plt.ylabel("Score")
    plt.title("Progreso del Score en el Entrenamiento")
    plt.legend()
    plt.grid(True)

    plt.savefig("training_progress_9x9.png")  # Guarda la imagen
    plt.close()


if __name__ == "__main__":
    plot_score_progression("./q-learning-score-progression-2.csv")