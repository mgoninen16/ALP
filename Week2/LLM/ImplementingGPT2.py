topP = input("Please input the \"Top-P\" / \"Top-K\" value for the Top-P and Top-K Searches (must be inbetween 0 and 1): ")
penAlp = input("Please input the \"penalty_alpha\" value for the Contrastive Search (must be > 0): ")
topK = int(input("Please input the \"Top-K\" value for the Contrastive Search (must be > 1): "))

from huggingface_hub.inference_api import InferenceApi

topPparameters = {"max_length": 150, "top_p": topP, "do_sample": True}
topKparameters = {"max_length": 150, "top_p": topP, "do_sample": True}
conSearch = {"max_length": 150, "penalty_alpha": penAlp, "top_k": topK, "do_sample": True}

inference = InferenceApi(repo_id="gpt2", token ="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")

input_string = input("Please input a phrase for the GPT2-Large model to finish: ")

resultP = inference(input_string, topPparameters)
resultK = inference(input_string, topKparameters)
resultCon = inference(input_string, conSearch)


print("Top-P Result: ")
print(resultP)
print()
print("Top-K Result: ")
print(resultK)
print()
print("Contrastive Search with Top-K Result: ")
print(resultCon)