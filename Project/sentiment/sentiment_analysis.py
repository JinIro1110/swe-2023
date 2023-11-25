import torch
from torch import nn
from kobert_tokenizer import KoBERTTokenizer
from transformers import BertModel

class BERTClassifier(nn.Module):
    def __init__(self,
                 bert,
                 hidden_size = 768,
                 num_classes=3,
                 dr_rate=None,
                 params=None):
        super(BERTClassifier, self).__init__()
        self.bert = bert
        self.dr_rate = dr_rate

        self.classifier = nn.Linear(hidden_size , num_classes)
        if dr_rate:
            self.dropout = nn.Dropout(p=dr_rate)

    def gen_attention_mask(self, token_ids, valid_length):
        attention_mask = torch.zeros_like(token_ids)
        for i, v in enumerate(valid_length):
            attention_mask[i][:v] = 1
        return attention_mask.float()

    def forward(self, token_ids, valid_length, segment_ids):
        attention_mask = self.gen_attention_mask(token_ids, valid_length)

        _, pooler = self.bert(input_ids = token_ids, token_type_ids = segment_ids.long(), attention_mask = attention_mask.float().to(token_ids.device))
        if self.dr_rate:
            out = self.dropout(pooler)
        return self.classifier(out)
    
class BERTSentimentAnalyzer(nn.Module):
    def __init__(self, model_path='C:/Users/user/Desktop/model.pt', device='cuda:0' if torch.cuda.is_available() else 'cpu'):
        super(BERTSentimentAnalyzer, self).__init__()

        # Load tokenizer and BERT model
        self.tokenizer = KoBERTTokenizer.from_pretrained('skt/kobert-base-v1')
        self.bertmodel = BertModel.from_pretrained('skt/kobert-base-v1', return_dict=False)

        # Load the pre-trained sentiment analysis model
        self.loaded_model = self.load_model(model_path, device)

    def load_model(self, model_path, device):
        # Create BERTClassifier model
        model = BERTClassifier(self.bertmodel, dr_rate=0.5).to(device)

        # Load the trained model state
        model.load_state_dict(torch.load(model_path, map_location=device))

        # Set the model to evaluation mode
        model.eval()

        return model

    def perform_sentiment_analysis(self, text, device='cuda:0' if torch.cuda.is_available() else 'cpu'):
        # Tokenize input text
        tokenized_input = self.tokenizer.tokenize(text)
        indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokenized_input)

        # Convert to model input format (batch size 1 assumed)
        token_ids = torch.tensor([indexed_tokens]).to(device)
        valid_length = torch.tensor([len(indexed_tokens)]).to(device)
        segment_ids = torch.tensor([[0] * len(indexed_tokens)]).to(device)

        # Make predictions
        with torch.no_grad():
            output = self.loaded_model(token_ids, valid_length, segment_ids)

        # Process predictions
        probabilities = torch.softmax(output, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()

        # Display results
        class_names = ['부정', '중립', '긍정']
        #print(f"Predicted Class: {class_names[predicted_class]}")

        for i, class_name in enumerate(class_names):
            class_prob = probabilities[0][i].item()
            #print(f"{class_name} Probability: {class_prob:.4f}")

        return class_names[predicted_class]
    
    