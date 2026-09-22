import matplotlib.pyplot as plt

class CHART:

    def __init__(self):
        pass

    def BAR_CHART(self,keys, values):
        plt.figure(figsize=(18,6))
        plt.bar(keys,values)
        plt.title("Bar chart of the feature continent")
        plt.xlabel("Continent")
        plt.ylabel("Count")
        plt.show()

if __name__ == "__main__":
    CHART.BAR_CHART(keys, values)