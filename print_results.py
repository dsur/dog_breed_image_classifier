#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Douglas Sur
# DATE CREATED:
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """

    """
    Printing Results
The first thing to be printed is a general statement that indicates which of the three CNN model architectures you are using. You can pass the information in the model as an input parameter to be able to print it.

Next you will be printing the overall count which will be the same for all three CNN model architectures. This can be done by calling for those counts using the appropriate key within a print statement.

Number of Images
Number of Dog Images
Number of "Not-a" Dog Images
Finally, you will be iterating through the results_stats dictionary printing out the statistic's name and value for all of the percentages (e.g. key that starts with the letter "p"). Recall that we had recommended that you give the same prefix (e.g. pct_) to all of the percentage statistics, so that they could all be printed out as a group.

Percentage Calculations:

% Correct Dogs
% Correct Breed
% Correct "Not-a" Dog
% Match (optional - this includes both dogs and not-a dog)
Printing Misclassifications
This function allows one to optionally print cases of dog and breed misclassifications.

This optional feature is provided to allow improved debugging of the code. Additionally, this feature provides the ability to determine if there are certain breeds of dogs that the algorithms have difficulty identifying.

    """
    print("print_results.py")
    print("CNN Model Architecture: ", model)
    print("Number of Images:", results_stats_dic['n_images'])
    print('Number of "Not-a" Dog Images:', results_stats_dic['n_notdogs_img'])
    print("Number of Dog Images:", results_stats_dic['n_dogs_img'])
    print('% Correct "Not-a" Dog:', results_stats_dic['pct_correct_notdogs'], "%")
    print("% Correct Dogs:", results_stats_dic['pct_correct_dogs'], "%")
    print("% Correct Breed:", results_stats_dic['pct_correct_breed'], "%")
    n_match = 0
    for key, value in results_dic.items():
        if value[2]:
            n_match += 1

    print('% Match (optional - this includes both dogs and not-a dog):', n_match / results_stats_dic['n_images'] * 100,
          "%")

    # IF print_incorrect_dogs == True AND there were images incorrectly
    # classified as dogs or vice versa - print out these cases
    if (print_incorrect_dogs and
            ((results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
             != results_stats_dic['n_images'])):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        # process through results dict, printing incorrectly classified dogs
        for key in results_dic:
            # TODO: 6c. REPLACE pass with CODE that prints out the pet label 
            #           and the classifier label from results_dic dictionary    
            #           ONLY when the classifier function (classifier label) 
            #           misclassified dogs specifically: 
            #             pet label is-a-dog and classifier label is-NOT-a-dog 
            #               -OR- 
            #             pet label is-NOT-a-dog and classifier label is-a-dog 
            #          You will need to write a conditional statement that 
            #          determines if the classifier function misclassified dogs
            #          See 'Adjusting Results Dictionary' section in 
            #         'Classifying Labels as Dogs' for details on the 
            #          format of the results_dic dictionary. Remember the value
            #          is accessed by results_dic[key] and the value is a list
            #          so results_dic[key][idx] - where idx represents the 
            #          index value of the list and can have values 0-4.
            #
            # Pet Image Label is NOT-a-Dog - Classified as a-DOG
            # Pet Image Label is a Dog - Classified as NOT-A-DOG -OR- 
            if (not results_dic[key][3] and results_dic[key][4]) or (results_dic[key][3] and not results_dic[key][4]):
                print("Incorrect Dog:", results_dic[key][0])

    if (print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])):
        print("\nINCORRECT Dog Breed Assignment:")
        # process through results dict, printing incorrectly classified breeds
        for key in results_dic:
            # Pet Image Label is-a-Dog, classified as-a-dog but is WRONG breed
            if (sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0):
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0], results_dic[key][1]))
                # print("Incorrect Breed(",value[0],"):",value[1])

    print("print_results.py>")
    None


def main():
    return None


if __name__ == '__main__':
    main()
