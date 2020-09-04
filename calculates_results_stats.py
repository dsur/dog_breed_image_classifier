#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Douglas Sur
# DATE CREATED: 8/28/2020                                 
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
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
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
                     
  The results statistics dictionary will have the following format:
    key = statistic's name (e.g. n_correct_dogs, pct_correct_dogs, n_correct_breed, pct_correct_breed)
    value = statistic's value (e.g. 30, 100%, 24, 80%)
    example_dictionary = {'n_correct_dogs': 30, 'pct_correct_dogs': 100.0, 'n_correct_breed': 24, 'pct_correct_breed': 80.0}

  """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    # Total Images 40 # Matches: 35 # NOT Matches: 5
    """
    Counts:
        Number of Images
        Number of Dog Images
        Number of "Not-a" Dog Images
    Percentages:
        % Correctly Classified Dog Images
        % Correctly Classified "Not-a" Dog Imagesu
        % Correctly Classified Breeds of Dog Images
    """
    print("calculates_results_stat.py")
    results_stats_dic = {}
    num_of_images = 0
    num_of_dog_images = 0
    num_of_not_dog_images = 0
    classified_dog_images = 0 # correctly classified dog images
    classified_breeds = 0 # correctly classified breeds
    for key, value in results_dic.items():
        num_of_images += 1
        if value[3]:  # calculate is a dog
            num_of_dog_images += 1
        else:
            num_of_not_dog_images += 1

        if value[2] and value[3]: # correctly classified as a dog
            classified_dog_images += 1

        if value[4]: # correctly classified breed as a dog
            classified_breeds += 1
            
        #print('calculates_results:',key,value)
        
#    print("images=",num_of_images," dogs=",num_of_dog_images," not-dogs=",num_of_not_dog_images)
#    print("% Correctly Classified Dog Images",num_of_dog_images/num_of_images, num_of_dog_images, num_of_not_dog_images)
#    print('% Correctly Classified "Not-a" Dog Imagesu',1-(num_of_dog_images/num_of_images))
#    print("% Correctly Classified Breeds of Dog Images",classified_breeds/num_of_images, classified_breeds)

    # n_correct_dogs, pct_correct_dogs, n_correct_breed, pct_correct_breed
    results_stats_dic['n_images'] = num_of_images
    results_stats_dic['n_dogs_img'] = num_of_dog_images
    results_stats_dic['n_notdogs_img'] = num_of_images - num_of_dog_images
    results_stats_dic['pct_correct_dogs'] = (num_of_dog_images/num_of_images) * 100.0
    results_stats_dic['pct_correct_notdogs'] = (1 - (num_of_dog_images/num_of_images)) * 100.0
    results_stats_dic['n_correct_breed'] = classified_breeds
    results_stats_dic['pct_correct_breed'] = (classified_breeds/num_of_images) * 100.0
    print("calculates_results_stat.py>")
    return results_stats_dic


