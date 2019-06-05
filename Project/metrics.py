from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

def accuracy(predicted, actual):
    correctCount = 0
    for i in range(0, len(actual)):
        if(actual[i] == predicted[i]):
            correctCount +=1
    return correctCount/len(actual)

def precision(predicted, actual):
    return precision_score(actual, predicted, average = "micro")

def recall(predicted, actual):
    return recall_score(actual, predicted, average = "micro")

def f1Score(predicted, actual):
    return f1_score(actual, predicted, average = "micro")