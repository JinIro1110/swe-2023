from sentiment.app import getJson

def run_get_json(item_id):
    return getJson(item_id)

if __name__ == "__main__":
    # 이 부분은 sentiment_api.py를 직접 실행할 때 실행되는 코드
    item_id = 123  # 예시로 아이템 ID를 지정
    result = run_get_json(item_id)
    print(result)
