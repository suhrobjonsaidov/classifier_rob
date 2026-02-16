import re # regex - helps to get clean lists
from collections import Counter

class PromptClassifier:

    def __init__(self, categories):
        self.categories = categories


    def classify(self, prompt):
        

        """
        1 put the words into a list 
        2then count how many words from the prompt are in each category
        3 return the category that has the most words in
        """

        #1 
        words = re.findall(r'\w+', prompt)

        #2 
        count = {}
        for category, keywords in self.categories.items():
            current_category_counter = 0

            for word in words:
                if word.lower() in keywords:
                    current_category_counter+=1
            
            count[category] =current_category_counter

        
        #3
        is_empty = all(value == 0 for value in count.values())
        
        if is_empty:
            return "OTHER"
        else:
            return max(count, key=count.get)


    

    
categories = {
    'MATH': ['solve', 'equation', 'calculate', 'sum', 'derivative', 'integral'],
    'CODING': ['function', 'code', 'python', 'loop', 'variable', 'debug'],
    'SCIENCE': ['atom', 'molecule', 'gravity', 'experiment', 'hypothesis']
}

classifier = PromptClassifier(categories)
print(classifier.classify("solve code gravity sum"))
print(classifier.classify("write a python function for fibonacci"))
print(classifier.classify("what is the derivative of x squared"))
print(classifier.classify("how does gravity affect molecules"))
print(classifier.classify("what is the meaning of life"))








    