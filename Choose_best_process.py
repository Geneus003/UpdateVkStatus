# This function will choose best process xD


def find_best(data):
    print(data[0][1])

    useful_processes = []

    for i in range(len(data)):
        if data[i][1].find("PyCharm") != -1 and "Кодит в PyCharm'e" not in useful_processes:
            useful_processes.append("Кодит в PyCharm'e")

        elif data[i][1].find("Spotify") != -1 and "Слушает Spotify" not in useful_processes:
            useful_processes.append("Слушает Spotify")

        elif data[i][1].find("csgo") != -1 and "Играет Counter-strike" not in useful_processes:
            useful_processes.append("Играет Counter-strike")

        elif data[i][1].find("Google") != -1 and "Сидит в Google" not in useful_processes:
            useful_processes.append("Сидит в Google")

        elif data[i][1].find("vk") != -1 and "Ждет вас в Vk" not in useful_processes:
            useful_processes.append("Ждет вас в Vk")

        elif data[i][1].find("telegram") != -1 and "Ждет вас в Telegram" not in useful_processes:
            useful_processes.append("Ждет вас в Telegram")

        elif data[i][1].find("minecraft") != -1 and "Фанится с друзьями в Minecraft(ну почему-бы и нет)" not in useful_processes:
            useful_processes.append("Фанится с друзьями в Minecraft(ну почему-бы и нет)")

    return useful_processes
