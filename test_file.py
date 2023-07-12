from adjust_results4_isadog import adjust_results4_isadog
from get_pet_labels import get_pet_labels #works
from classify_images import classify_images #list extended correctly, but false classification (labels match in fact but yields 0)
from classifier import classifier

results_dic = get_pet_labels('/home/workspace/pet_images')
classify_images('/home/workspace/pet_images', results_dic, 'vgg')
dognames_dic = adjust_results4_isadog(results_dic, '/home/workspace/dognames.txt')

print(dognames_dic)
