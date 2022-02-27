import aircv as ac


def matchImg(imgsrc, imgobj, confidence):  # imgsrc=原始图像，imgobj=待查找的图片
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)

    match_result = ac.find_template(imsrc, imobj, confidence)
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽

    return match_result


if __name__ == "__main__":
    r = matchImg('./res/screen.png', './res/icon.png', 0.8)
    print(str(r))
