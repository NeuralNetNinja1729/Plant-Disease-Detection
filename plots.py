import json
import matplotlib.pyplot as plt
with open('training_hist.json') as json_file:
    data = json.load(json_file)
    loss = data['loss']
    accuracy = data['accuracy']
    val_loss = data['val_loss']
    val_accuracy = data['val_accuracy']
    
    epochs = range(1, 11)
    plt.plot(epochs, accuracy, color = 'red', label = 'Training Accuracy')
    plt.plot(epochs, val_accuracy, color = 'blue', label = 'Validation Accuracy')
    plt.show()
    



