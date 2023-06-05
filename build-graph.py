import matplotlib.pyplot as plt


def generate_bar_graphs(file_path):
    page_names = []
    sizes = []
    first_load_js = []

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            currLine = line.strip().split()
            page_names.append(currLine[2])
            if currLine[4] == "B":
                sizes.append(float(currLine[3]) / 1024)
            else:
                sizes.append(float(currLine[3]))
            first_load_js.append(float(currLine[5]))

    plt.figure(figsize=(12, 6))
    plt.bar(page_names, sizes, color="#08453A")
    plt.xlabel("Page")
    plt.ylabel("Size (kB)")
    plt.title("Page Size")
    plt.tight_layout()
    plt.xticks(rotation=45, ha="right")
    plt.subplots_adjust(bottom=0.2)
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.bar(page_names, first_load_js, color="#08453A")
    plt.xlabel("Page")
    plt.ylabel("First Load JS (kB)")
    plt.title("First Load JS")
    plt.xticks(rotation=45, ha="right")
    plt.subplots_adjust(bottom=0.2)
    plt.tight_layout()
    plt.show()


file_path = "./build-stats.txt"
generate_bar_graphs(file_path)
