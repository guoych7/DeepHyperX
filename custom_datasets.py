from utils import open_file
import numpy as np
import cv2 as cv
import os

CUSTOM_DATASETS_CONFIG = {
    # "Puer0921_train": {
    #     "img": "train_data.mat",
    #     "gt": "train_gt.mat",
    #     "download": False,
    #     "loader": lambda folder: puer0921_train_loader(folder),
    # },
    # "Puer0921_test": {
    #     "img": "test_data.mat",
    #     "gt": "test_gt.mat",
    #     "download": False,
    #     "loader": lambda folder: puer0921_test_loader(folder),
    # },
    "Puer0921": {
        "img": "train_data.mat",
        "gt": "train_gt.mat",
        "download": False,
        "loader": lambda folder: puer0921_loader(folder),
    },
}

def puer0921_loader(folder):
    img = open_file(folder + "train_data.mat")["train_data"]
    gt = open_file(folder + "train_gt.mat")["train_gt"]
    gt = gt.astype("uint8")

    rgb_bands = (2, 1, 0)

    label_values = [
        "Background",
        "tea",
        "impurities",
    ]
    ignored_labels = [0]
    palette = None
    return img, gt, rgb_bands, ignored_labels, label_values, palette


def puer0921_train_loader(folder):
    img = open_file(folder + "train_data.mat")["train_data"]
    gt = open_file(folder + "train_gt.mat")["train_gt"]
    gt = gt.astype("uint8")

    rgb_bands = (2, 1, 0)

    label_values = [
        "Background",
        "tea",
        "impurities",
    ]
    ignored_labels = [0]
    palette = None
    return img, gt, rgb_bands, ignored_labels, label_values, palette


def puer0921_test_loader(folder):
    img = open_file(folder + "test_data.mat")["train_data"]
    gt = open_file(folder + "test_gt.mat")["train_gt"]
    gt = gt.astype("uint8")

    rgb_bands = (2, 1, 0)

    label_values = [
        "Background",
        "tea",
        "impurities",
    ]
    ignored_labels = [0]
    palette = None
    return img, gt, rgb_bands, ignored_labels, label_values, palette
