from typing import List


class Metrics:
    @staticmethod
    def get_metrics(test_data: list, predicted_data: list):
        small_number = 0.000000000000000001
        true_positive = small_number
        false_positive = small_number
        true_negative = small_number
        false_negative = small_number

        for i in range(len(predicted_data)):
            if (test_data[i] == 0) and (predicted_data[i] == 0):
                true_negative += 1
            if (test_data[i] == 0) and (predicted_data[i] == 1):
                false_positive += 1
            if (test_data[i] == 1) and (predicted_data[i] == 1):
                true_positive += 1
            if (test_data[i] == 1) and (predicted_data[i] == 0):
                false_negative += 1
        return (true_positive, false_positive, true_negative, false_negative)

    @staticmethod
    def f_score(test_data, predicted_data):
        metrics = Metrics.get_metrics(test_data, predicted_data)

        true_positive = metrics[0]
        false_positive = metrics[1]
        #true_negative = metrics[2]
        false_negative = metrics[3]

        precision = true_positive / (true_positive + false_positive)
        recall = true_positive / (true_positive + false_negative)
        fscore = 2*(precision*recall) / (precision+recall)

        return (fscore)

    @staticmethod
    def plot_confusion_matrix(test_data, predicted_data):
        import numpy as np
        metrics = Metrics.get_metrics(test_data, predicted_data)
        aplot_confusion_matrix(cm=np.array([[metrics[0], metrics[1]],
                                            [metrics[3], metrics[2]]]), normalize=True, target_names=["ham", "spam"], title="Confusion Matrix, Normalized")


def aplot_confusion_matrix(cm, target_names, title='Confusion matrix', cmap=None, normalize=True):

    import matplotlib.pyplot as plt
    import numpy as np
    import itertools

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(
        accuracy, misclass))
    plt.show()
