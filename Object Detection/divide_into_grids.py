import os
import pandas as pd
import shutil
import subprocess
import sys
import matplotlib.pyplot as plt
from PIL import Image

dataset = "../../Dataset/"
final_dataset = dataset + "/Final Dataset/"
frames = os.listdir("../../Dataset/Frames")

for frame in frames:
    print("Starting Image Labelling of Image: " + frame)
    path = dataset + "Frames/" + frame
    os.mkdir("./Temp Folder")
    shutil.copy(path, "./Temp Folder/")
    temp_folder_path = "./Temp Folder/" + frame
    subprocess.run(["split-image", temp_folder_path, "20", "20"])

    print("The original image: " + frame)
    frame_img = Image.open(path)
    frame_img.show(frame_img)
    os.remove("./Temp Folder/" + frame)
    os.remove(path)

    images_grids = os.listdir("./Temp Folder")

    for grid_im in images_grids:
        classification = ""
        grid_path = "./Temp Folder/" + grid_im
        print("Grid image: " + grid_im)
        grid_image = Image.open(grid_path)
        grid_image.show(frame_img)

        print("For classification - \n 0 - Ball \n 1 - Not ball \n 2 - Dont consider the original image \n 3 - Dont consider this grid image")
        user_inp = input("Enter the classification:  ")

        try:
            user_inp = int(user_inp)
        except Exception as e:
            print("Non int input, will skip this frame")
            user_inp = "aa"

        if user_inp == 0:
            classification = "Ball"
        elif user_inp == 1:
            classification = "Not ball"
        elif user_inp == 2:
            break
        else:
            continue

        grid_img_name = grid_im.split(".")[0]
        grid_data = {"Img": [grid_img_name], "Classification": [classification]}
        df_grid_im = pd.DataFrame(grid_data)

        df = pd.read_excel(dataset + "final_data.xlsx")

        df = pd.concat([df, df_grid_im], axis=0)

        os.remove(dataset + "final_data.xlsx")

        df.to_excel(dataset + "final_data.xlsx", index=False)
        shutil.copy(grid_path, final_dataset)
    print("Completed image")
    shutil.rmtree("./Temp Folder")