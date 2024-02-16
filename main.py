from flask import Flask, render_template, request, redirect
import cv2
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=['POST'])
def upload():
    if "image" not in request.files:
        print(request.url)
        return redirect(request.url)

    file = request.files['image']

    if file.filename == "":
        return redirect(request.url)
    a = file.filename
    destination_path = "./"

    if file:
        file.save(os.path.join(destination_path, a))
        image = cv2.imread(filename=a)
        pixel = image.reshape((-1, 3))
        unique_colors = set(map(tuple, pixel))
        print(unique_colors)
        hex_colors = ["#{:02x}{:02x}{:02x}".format(b, g, r) for (r, g, b) in unique_colors]
        print(len(hex_colors))  # 227435
        dictionary = {}
        count = 0
        for _ in range(len(hex_colors)):
            num = 0
            for i in range(len(hex_colors)):
                if hex_colors[count] == hex_colors[i]:
                    num += 1
                    dictionary.update({hex_colors[count]: num})
            count += 1

        # print(dictionary)
        v = list(dictionary.values())
        max_of_v = max(v)
        new_list = []
        for key, val in dictionary.items():
            if dictionary[key] == max_of_v:
                new_list.append(key)
        # print(new_list)
        return render_template("msg.html", list=new_list, n=1)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
