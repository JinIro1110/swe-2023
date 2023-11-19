import torch
from torch import nn
from torch.utils.data import DataLoader
import torch.nn.functional as F
import numpy as np
from tqdm import tqdm

from kobert_tokenizer import KoBERTTokenizer
from transformers import BertModel

# GPU 사용 시
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# BERT 모델 및 토크나이저 불러오기
tokenizer = KoBERTTokenizer.from_pretrained('skt/kobert-base-v1')
bertmodel = BertModel.from_pretrained('skt/kobert-base-v1', return_dict=False)

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
    
# 불러올 모델의 경로
model_path = 'C:/Users/user/Desktop/model.pt'

# 모델 생성
loaded_model = BERTClassifier(bertmodel, dr_rate=0.5).to(device)

# 저장한 모델의 상태를 불러오기
if not torch.cuda.is_available():
    checkpoint = torch.load(model_path, map_location=torch.device('cpu'))
else:
    checkpoint = torch.load(model_path)

loaded_model.load_state_dict(torch.load(model_path, map_location=device))

# 평가 모드로 설정
loaded_model.eval()

# 새로운 입력 데이터에 대한 감정 분석 수행
def perform_sentiment_analysis(text):
    # 입력 데이터 전처리 및 토큰화
    tokenized_input = tokenizer.tokenize(text)
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_input)

    # 모델 입력 형식으로 변환 (배치 크기 1로 가정)
    token_ids = torch.tensor([indexed_tokens]).to(device)
    valid_length = torch.tensor([len(indexed_tokens)]).to(device)
    segment_ids = torch.tensor([[0] * len(indexed_tokens)]).to(device)

    # 모델 예측
    with torch.no_grad():
        output = loaded_model(token_ids, valid_length, segment_ids)

    # 예측 결과 확인
    probabilities = torch.softmax(output, dim=1)
    predicted_class = torch.argmax(probabilities, dim=1).item()

    # 예측 클래스와 확률 출력
    class_names = ['부정', '중립', '긍정']  # 새로운 라벨링에 맞게 수정
    print(f"Predicted Class: {class_names[predicted_class]}")

    # 클래스별 확률 출력
    for i, class_name in enumerate(class_names):
        class_prob = probabilities[0][i].item()
        print(f"{class_name} Probability: {class_prob:.4f}")

# 예시 문장에 대한 감정 분석 수행
example_sentence = "아이 피부가 민감한데 이건 잘 맞아요."
perform_sentiment_analysis(example_sentence)
example_sentence = "일반 떡뻥만 막다가 시금치 함유 되어 있다고 해서 구매했는데"
perform_sentiment_analysis(example_sentence)
example_sentence = "아이가 유독 이 과자를 달라고 해요."
perform_sentiment_analysis(example_sentence)


