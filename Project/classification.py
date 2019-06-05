import loadData as ld
import preprocessing as pp
import metrics as met

from sklearn.decomposition import PCA
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

import numpy as np
from sklearn.metrics import f1_score

useNaiveBayes = True
useSupportVectorMachine = True
useRandomForest = True
useADABoost = True
useGradBoost = True

numberOfLoops1 = 1
numberOfLoops2 = 1

for multiplyer1 in range(1, numberOfLoops1+1):
    #print(multiplyer1)
    for multiplyer2 in range(1, numberOfLoops2 + 1):
        #print(multiplyer2)

        numFolds = 10
        dataPerClass = 400

        pcaModel = PCA(0.95)  # Keeps 95% of variation

        trainingIndexes, testingIndexes, labels, combinedReducedTags = pp.prepareData(dataPerClass, numFolds)

        nbAccuracy, svmAccuracy, rfAccuracy, adaAccuracy, gradBoostAccuracy = 0, 0, 0, 0, 0
        nbF1Score, svmF1Score, rfF1Score, adaF1Score, gradBoostF1Score = 0, 0, 0, 0, 0

        for i in range(0, numFolds):
            rawTrainData, rawTestData = [], []
            trainLabels, testLabels = [], []
            for j in range(0, len(trainingIndexes[i])):
                rawTrainData.append(combinedReducedTags[trainingIndexes[i][j]])
                trainLabels.append(labels[trainingIndexes[i][j]])
            for m in range(0, len(testingIndexes[i])):
                rawTestData.append(combinedReducedTags[testingIndexes[i][m]])
                testLabels.append(labels[testingIndexes[i][m]])

            normalisedTrainData = pp.getNormalisedData(rawTrainData)
            normalisedTestData = pp.getNormalisedData(rawTestData)

            pcaModel.fit(normalisedTrainData)

            pcaTrainData = pcaModel.transform(normalisedTrainData)
            pcaTestData = pcaModel.transform(normalisedTestData)

            trainLabels = pp.convertLabels(trainLabels)
            testLabels = pp.convertLabels(testLabels)

            if(useNaiveBayes):
                NB = MultinomialNB()
                nbModel = NB.fit(np.array(normalisedTrainData), np.array(trainLabels))
                predictionsMade = nbModel.predict(np.array(normalisedTestData)).tolist()

                tempAcc = met.accuracy(predictionsMade, testLabels)
                #tempF1 = met.precision_score(predictionsMade, testLabels)
                tempF1 = f1_score(testLabels, predictionsMade, average = None)
                nbAccuracy += tempAcc
                nbF1Score += tempF1


            if(useSupportVectorMachine):
                svmModel = svm.SVC(gamma = "scale")
                svmModel.fit(np.array(pcaTrainData), np.array(trainLabels))
                predictionsMade = svmModel.predict(np.array(pcaTestData)).tolist()

                tempAcc = met.accuracy(predictionsMade, testLabels)
                #tempF1 = met.precision_score(predictionsMade, testLabels)
                tempF1 = f1_score(testLabels, predictionsMade, average = None)
                svmAccuracy += tempAcc
                svmF1Score += tempF1

            if(useRandomForest):
                rfModel = RandomForestClassifier(n_estimators = 300, max_depth = 12, random_state = 0)
                rfModel.fit(np.array(pcaTrainData), np.array(trainLabels))
                predictionsMade = rfModel.predict(np.array(pcaTestData)).tolist()

                tempAcc = met.accuracy(predictionsMade, testLabels)
                #tempF1 = met.precision_score(predictionsMade, testLabels)
                tempF1 = f1_score(testLabels, predictionsMade, average = None)
                rfAccuracy += tempAcc
                rfF1Score += tempF1

            if(useADABoost):
                adaModel = AdaBoostClassifier(n_estimators = 300)
                adaModel.fit(np.array(pcaTrainData), np.array(trainLabels))
                predictionsMade = adaModel.predict(np.array(pcaTestData)).tolist()

                tempAcc = met.accuracy(predictionsMade, testLabels)
                #tempF1 = met.precision_score(predictionsMade, testLabels)
                tempF1 = f1_score(testLabels, predictionsMade, average = None)
                adaAccuracy += tempAcc
                adaF1Score += tempF1

            if(useGradBoost):
                gradBoostModel = GradientBoostingClassifier(n_estimators = 240, learning_rate = 0.5, max_depth = 21)
                gradBoostModel.fit(np.array(pcaTrainData), np.array(trainLabels))
                predictionsMade = gradBoostModel.predict(np.array(pcaTestData)).tolist()

                tempAcc = met.accuracy(predictionsMade, testLabels)
                #tempF1 = met.precision_score(predictionsMade, testLabels)
                tempF1 = f1_score(testLabels, predictionsMade, average = None)
                gradBoostAccuracy += tempAcc
                gradBoostF1Score += tempF1

        print("----------------------")
        print("NB Accuracy: ", nbAccuracy/numFolds)
        print("NB F1-Score: ", nbF1Score / numFolds)
        print("----------------------")
        print("SVM Accuracy: ", svmAccuracy/numFolds)
        print("SVM F1-Score: ", svmF1Score / numFolds)
        print("----------------------")
        print("RF Accuracy: ", rfAccuracy/numFolds)
        print("RF F1-Score: ", rfF1Score / numFolds)
        print("----------------------")
        print("Ada Accuracy: ", adaAccuracy/numFolds)
        print("Ada F1-Score: ", adaF1Score / numFolds)
        print("----------------------")
        print("GradBoost Accuracy: ", gradBoostAccuracy/numFolds)
        print("GradBoost F1-Score: ", gradBoostF1Score / numFolds)
        print("----------------------")
