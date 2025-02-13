import matplotlib.pyplot as plt
import pandas as pd

def plot_score_per_training_episodes():

    df = pd.read_csv("./csv/q_learning_tuning_results_9x9.csv")

    plt.figure(figsize=(10, 6))

    for alpha in df["Alpha"].unique():
        subset = df[df["Alpha"] == alpha]
        plt.plot(subset["Episodes"], subset["Avg_Score"], marker="o", label=f"Alpha {alpha}")

    plt.title("Variación de Avg_Score por cantidad de Episodios de entrenamiento", fontsize=14)
    plt.xlabel("Episodios de entrenamiento", fontsize=12)
    plt.ylabel("Avg Score", fontsize=12)

    plt.legend(title="Alpha")
    plt.savefig("avg_score_vs_episodes_9x9.png")
    plt.close()

if __name__ == "__main__":
    plot_score_per_training_episodes()