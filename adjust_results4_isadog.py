#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Douglas Sur
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    print("adjust_results4_isadog.py(results_dic,", dogfile, ")")
    dognames_dic = {}
    #    print('dogfile:',dogfile)
    # Read dogfile into dictionary
    with open(dogfile) as dogfile_fh:
        for line in dogfile_fh:
            dogs = line.strip().rstrip("\n").split(',')  # get indi
            for dog in dogs:
                temp_dog = dog.strip()
                dognames_dic[temp_dog] = 1
    #                print("dognames_dic[",temp_dog,"]")
    # print('dognames_dic:', dognames_dic)

    # print out dog names ie like labordor
    #    for pet in dognames_dic:
    #        print('dognames:', pet)
    #    print("dogfile type:",type(dogfile))   # 'Labordor0123.txt'
    #    for pet in dogfile:
    #        print("dogfile:", type(pet))

    # TODO: Loop through results_dic to determine if item is in dognames_dic
    # TODO: what is the values()?
    """
    No idea what this means-
                 ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
   """
    # NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
    #                            0 = pet Image 'is-NOT-a' dog. 
    for key, value in results_dic.items():
        # value.extend()
        if value[0] in dognames_dic.keys():
            value.append(1)
        else:
            value.append(0)
    #        results_dic[key] = value
    #        print("check_image.py-results_dic[",key,"]:",value)

    # NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
    #   'as-a' dog and 0 = Classifier classifies image  
    #   'as-NOT-a' dog.
    # TODO: this may not be correct. May neee to loop through each item
    #   example value string 'dalmatian, coach dog, carriage dog'
    for key, value in results_dic.items():
        # value.extend()
        result = 1  # assume breed in dognames_dic
        # get inidividual breed names
        breeds = value[1].strip().rstrip("\n").split(',')  # get individula breeds
        for breed in breeds:
            temp_breed = breed.strip()
            # dognames_dic[temp_dog] = 1
            if temp_breed not in dognames_dic.keys():  # breed not found in dogname dictionary
                #                print("temp_breed:",temp_breed)
                value.append(0)
                result = 0
                break
        #        results_dic[key] = value
        #        print("check_image.py-results_dic[",key,"]:",value)
        if result:  # breed found in dogname dictionary ie is-a-dog
            value.append(1)
    #        print("result_dic:", results_dic[key])

    print("adjust_results4_isadog.py>")
    None


def main():
    #    results_dic = {}
    dogfile = 'dognames.txt'
    adjust_results4_isadog(results_dic, dogfile)
    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
