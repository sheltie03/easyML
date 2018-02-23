# -*- coding: utf-8 -*-
import os
import numpy as np
from PIL import Image
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

STANDARD_SIZE = (640, 480)


def img_to_matrix(filename, verbose=False):
    img = Image.open(filename)
    if verbose:
        print 'change size'
    img = img.resize(STANDARD_SIZE)
    imgArray = np.asarray(img)
    return imgArray


def flatten_img(img):
    s = img.shape[0] * img.shape[1] * img.shape[2]
    img_wide = img.reshape(1, s)
    return img_wide[0]


if __name__ == '__main__':

    print '🤖 ... Hello, I am a learning bot!!'

    img_dir = './training_data/'
    images = [img_dir + f for f in sorted(os.listdir(img_dir))]

    X = []
    for image in images:
        img = img_to_matrix(image)
        img = flatten_img(img)
        X.append(img)

    y = []
    for i in range(36):
        y.append('GREEN')
    for i in range(36):
        y.append('RED')

    X_train = X
    y_train = y

    X_test = []
    img_dir = './test_data/'
    tag = [f for f in sorted(os.listdir(img_dir))]
    images = [img_dir + f for f in tag]
    for image in images:
        img = img_to_matrix(image)
        img = flatten_img(img)
        X_test.append(img)

    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)

    label = ['GREEN', 'RED']
    ind = 0
    for test_case in X_test:
        ans = []
        X_list = X_train + [test_case]
        for y_test_case in label:
            y_list = y_train + [y_test_case]
            sc = StandardScaler()
            sc.fit(X_list)
            X_list_std = sc.transform(X_list)
            model = SVC(kernel='linear', random_state=None)
            model.fit(X_list_std, y_list)
            pred_train = model.predict(X_list_std)
            accuracy_train = accuracy_score(y_list, pred_train)
            ans.append(accuracy_train)
        if ans[0] > ans[1]:
            judge = 'may be green.'
        elif ans[0] < ans[1]:
            judge = 'may be red.'
        else:
            judge = 'have never seen the color.'
        print '   ...', tag[ind], judge
        ind += 1
