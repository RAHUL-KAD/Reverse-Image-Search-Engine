![IMG_20190818_174223_8__1_-removebg-preview (1)](https://user-images.githubusercontent.com/63397654/162138000-2856940c-34da-407e-9563-62aa9bc1259c.png)


# Reverse Image Search :eyeglasses: Engine 
**A picture :framed_picture: is worth a thousand words**

## Introduction :pushpin:
Reverse Image Search also known as Content based Image retrevial, This is the application of computer vision techniques to the image retrieval problem, that is, the problem of searching for images in large databases.
 
## Table of Content :chart:
1. [Motivation](#motivation)
2. [Dataset](#dataset)
3. [Model Weights](#model-weights)
4. [How to use it](#how-to-use-it)


## :thinking: Motivation[](#motivation)
Ever wondered how the [Google reverse image search](https://en.wikipedia.org/wiki/Google_Images#Search_by_Image_feature) works, which take in an image and returns you the most similar images in a fraction of a second? 

Having a large database of images with no available metadata is not an ideal starting point, searching through those images can be exhausting to solve that we can use Image search engine, which will iterate through all the images and find all the similar images.

## Dataset[](#dataset) :chart_with_upwards_trend: :chart_with_downwards_trend: :bar_chart:
To build search engine we need massive amount of data to seach on. For this image search engine I used [Caltech101](https://data.caltech.edu/records/20086) dataset.

This dataset contains 101 classes and there are about 40 to 800 images per category.
    

## :weight_lifting_man: Model Weights[](#model-weights) :weight_lifting_woman:


| Model Name                                          | Weight size   | Weight Link
| -------------                                       | ------------- | --------
| Resnet Model Finetuned on **Caltech101 dataset**        | 96 MB         | [Link](https://drive.google.com/file/d/1BQrPqh-CYey4vU0x3H4Ok5EX5WE-JV_K/view?usp=sharing)
| Feature list resnet finutuned on **Caltech101 dataset** | 3 MB          | [Link](https://drive.google.com/file/d/1BR2x6kPLSRgrh1NMrd1wd7mJOccbqKmh/view?usp=sharing)


## :test_tube: How to use it[](#how-to-use-it) :microscope:
