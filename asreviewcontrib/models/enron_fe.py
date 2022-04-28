
from asreview.models.feature_extraction.base import BaseFeatureExtraction

class Enron(BaseFeatureExtraction):
    """Naive Bayes classifier

    The Naive Bayes classifier with the default SKLearn parameters.
    """

    name = "enron_fe"
    label = "enron_custom_feature_extraction"

    def __init__(self):

        super(Enron, self).__init__()
