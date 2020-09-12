# dog_breed_image_classifier
### dog_breed_image_classifier is a sample that shows developers how to classify images of dogs to particular breeds using a pre-trained image classifier. 
## Prerequisites:
- Operating system: Any OS 
- Framework infrastructure: Python 3.7+
- Knowledge: This was taken from a class project I did on Udacity.com.  There is a sample run_models_batch.sh shell script that runs some samples. You can take a look at the script to see what calls what.  It runs 3 different convolutional neural networks (CNN) and spits out the output to a text file.

## Usage:
sh run_models_batch.sh
## Sample Output:
```
root@a3b6cfc4447f:/home/workspace# sh run_models_batch.sh
Downloading: "https://download.pytorch.org/models/resnet18-5c106cde.pth" to /root/.torch/models/resnet18-5c106cde.pth
100%|██████████████████████████████████████████████████████████████| 46827520/46827520 [00:00<00:00, 107821335.61it/s]
Downloading: "https://download.pytorch.org/models/alexnet-owt-4df8aa71.pth" to /root/.torch/models/alexnet-owt-4df8aa71.pth
100%|██████████████████████████████████████████████████████████████| 244418560/244418560 [00:26<00:00, 5179190.55it/s]
Downloading: "https://download.pytorch.org/models/vgg16-397923af.pth" to /root/.torch/models/vgg16-397923af.pth
100%|████████████████████████████████████████████████████████████| 553433881/553433881 [00:04<00:00, 119085200.65it/s]
root@a3b6cfc4447f:/home/workspace# ls *_pet-images.txt
alexnet_pet-images.txt  resnet_pet-images.txt  vgg_pet-images.txt
root@a3b6cfc4447f:/home/workspace# cat resnet_pet-images.txt
...
...
...
# Total Images 40 # Matches: 33 # NOT Matches: 7
calculates_results_stat.py
calculates_results_stat.py>

 ** Statistics from calculates_results_stats() function:
N Images: 40  N Dog Images: 30  N NotDog Images: 10 
Pct Corr dog: 100.0 Pct Corr NOTdog:  90.0  Pct Corr Breed:  90.0

 ** Check Statistics - calculated from this function as a check:
N Images: 40  N Dog Images: 30  N NotDog Images: 10 
Pct Corr dog: 100.0 Pct Corr NOTdog:  90.0  Pct Corr Breed:  90.0
print_results.py
CNN Model Architecture:  resnet
Number of Images: 40
Number of "Not-a" Dog Images: 10
Number of Dog Images: 30
% Correct "Not-a" Dog: 90.0 %
% Correct Dogs: 100.0 %
% Correct Breed: 90.0 %
% Match (optional - this includes both dogs and not-a dog): 82.5 %
print_results.py>

** Total Elapsed Runtime: 0:0:6.117403984069824
root@a3b6cfc4447f:/home/workspace# 
```
