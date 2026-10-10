import matplotlib.pyplot as plt
import numpy as np



# x = np.array([100, 200, 300, 400, 500])
# y = np.array([10,78,30,40,50])
# y1 = np.array([45,67,89,55,45])
# y2 = np.array([4,6,8,5,4])

# # plt.plot(x, y, marker = "o",
# #          markersize = 20,
# #          markerfacecolor = "cyan")

# # line_style = dict(marker = "o",
# #          markersize = 20,
# #          markerfacecolor = "cyan")

# # plt.plot(x, y, color = "green", **line_style)
# # plt.plot(x, y1, color = "orange", **line_style)
# # plt.plot(x, y2, color = "red", **line_style)

# plt.title("gu gu gaga", fontsize = 20,
#                     family = "Arial",
#                     fontweight = "bold",
#                     color = "red")
# plt.xlabel("gu1", fontsize = 15,
#                     family = "Arial",
#                     fontweight = "bold",
#                     color = "purple")
# plt.ylabel("gu2", fontsize = 15,
#                     family = "Arial",
#                     fontweight = "bold",
#                     color = "purple")

# plt.tick_params(axis= "both",
#                 colors = "brown")

# plt.plot(x, y,)
# plt.plot(x, y1,)
# plt.plot(x, y2,)

# plt.xticks(x)

# plt.grid(axis= "both")
# plt.show()

# //////


# games =["subnautica", "minecraft", "free fire", "valorant"]
# hours = np.array([24,56,44,300])

# plt.bar(games, hours, 
#         color = "yellow")
# plt.title("Speding hours",
#           color = "Purple")
# plt.xlabel("Games",
#            fontsize = 20)
# plt.ylabel("Hours",
#            fontsize = 20)
# plt.show()

# /////


# games =["subnautica", "minecraft", "free fire", "valorant"]
# hours = np.array([24,56,44,300])
# colors = ["purple", "yellow", "blue", "green"]

# plt.pie(hours, labels= games,
#         autopct= "%1.1f%%",
#         colors = colors,
#         explode = [0, 0, 0, 0.1],
#         shadow = True,
#         startangle=90)

# plt.title("Game i play")

# plt.show()


# /////
# graph




# x = np.array([100, 200, 300, 400, 500])
# y = np.array([10,78,30,40,50])
# x1 = np.array([10, 20, 30, 40, 50])
# y2= np.array([20,78,50,80,66])


# plt.scatter(x, y, color ="skyblue",
#             alpha = 0.5,
#             s = 100,
#             label = "Class A")
# plt.scatter(x1, y2, color ="yellow",
#             alpha = 0.5,
#             s = 100,
#             label = "Class B")


# plt.title("gu gu gaga")
# plt.xlabel("games")
# plt.ylabel("hours i play")

# plt.show()


# ////
# histogram

# scores = np.random.normal(loc=80, scale =10, size = 100)
# scores = np.clip(scores, 0, 100)


# plt.hist(scores, bins= 10,
#          color= "purple",
#          edgecolor = "black")

# plt.title("exam score")
# plt.xlabel("Score")
# plt.ylabel("# of Student")

# plt.show()


# ////
# figure

# x = np.array([1, 2, 3, 4, 5, 6, 7])

# figure, axes = plt.subplots(2, 2)

# axes[0, 0].plot(x, x*2, color = "red")
# axes[0, 0].set_title("x*2")

# axes[0, 1].plot(x, x*3, color = "blue")
# axes[0, 1].set_title("x*3")

# axes[1, 0].plot(x, x*4, color = "yellow")
# axes[1, 0].set_title("x*4")

# axes[1, 1].plot(x, x*5, color = "purple")
# axes[1, 1].set_title("x*5")

# plt.tight_layout()

# plt.show()



# ////

