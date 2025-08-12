import lime.lime_text
from lime.lime_text import LimeTextExplainer

# Initialize LIME Explainer
explainer = LimeTextExplainer(class_names=["Relevant", "Irrelevant"])

def lime_explanation(query, response, retriever):
    """
    Use LIME to generate explanation for AI response.
    """
    def prediction_function(texts):
        # Retrieve the related contexts
        retrievals = [retriever.get_relevant_documents(text) for text in texts]
        # Dummy prediction probabilities (adjust based on your model)
        return [[0.8, 0.2] if "medical" in doc[0].metadata['source'] else [0.4, 0.6] for doc in retrievals]

    exp = explainer.explain_instance(response, prediction_function, num_features=5)
    return exp.as_list()

# Example Usage:
query = "What are the symptoms of diabetes?"
retriever = get_vectorstore().as_retriever()
response = "Diabetes symptoms include excessive thirst, frequent urination, fatigue, and blurred vision."

# Get LIME explanation
oo
lime_explanations = lime_explanation(query, response, retriever)
print("LIME Explanation:", lime_explanations)