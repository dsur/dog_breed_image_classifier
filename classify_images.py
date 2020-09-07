#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Douglas Sur   
# DATE CREATED: 2020-08-25                                
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
import importlib
from classifier import classifier
from get_pet_labels import *


# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    print("classify_images.py(", images_dir, ", results_dic,", model, ")")
    # image_dir = 'pet_images/' # for testing HAD TO hard code. WHY?
    # test_image="pet_images/Collie_03797.jpg" # for testing
    # model = 'vgg' # for testing HAD TO hard code. WHY?
    # temp_dict = get_pet_labels(images_dir)
    # results_dic = {}
    temp_dict = results_dic
    results_list = []
    # print('temp_dict',temp_dict)
    for test_image_fn, answer in temp_dict.items():
        test_image = images_dir + test_image_fn  # add directory info
        # print('get_pet_labels:', test_image, answer, model)
        image_classification = classifier(test_image, model)  # classify image

        # add result to result_list wher 1 is matched
        #        if answer in image_classification.lower().strip():
        if answer[0] in image_classification.lower().strip():
            result_list = [answer[0], image_classification.lower().strip(),
                           1]  # not sure to use image_classifacation or model
        else:
            result_list = [answer[0], image_classification.lower().strip(),
                           0]  # not sure to use image_classifacation or model
        #            print("answer.lower().strip():", answer)
        #            result_list = [answer, model, 0]
        # print("Results Image/answer:", test_image, "/", answer, "using model:", model, "\n\twas classified as a:", image_classification, "\n\tresult_list:",result_list,"\n")
        # result_list = []
        results_dic[test_image_fn] = result_list  # assign key values to function return value

    # prints result from running classifier() function
    # for key, value in results_dic.items():
    #     print("results_dic[",key,"]:",value)

    print("classify_images.py>")
    None


def main():
    #    results_dic = {}
    #    model = 'vgg'
    #    classify_images('pet_images', results_dic, model)

    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
