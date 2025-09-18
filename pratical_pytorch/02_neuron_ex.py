import torch
from torch import nn

# 1] 훈련 데이터 설정 (라벨 포함:tensor 데이터셋)
X = torch.tensor([
    [10],
    [37.78]
], dtype=torch.float32 )

y = torch.tensor([
    [50],
    [100.0]
], dtype = torch.float32 )

# 2] 모델 시작점 초기화
model = nn.Linear( 1, 1 ) # 입력값 1개(화씨 온도), 출력값 1개(예상값)

# 3] 손실함수 생성 및 지정: MSE(최소제곱오차)
loss_fn = torch.nn.MSELoss()

# 4] 최적화: 옵티마이저(ex.경사하강법, 기타, 등..)
optimizer = torch.optim.SGD( model.parameters(), lr = 0.001 ) #lr: 학습속도

# 5] 모델 훈련하기
for i in range( 0, 15000 ):
    optimizer.zero_grad()
    outputs = model(X)
    loss = loss_fn( outputs, y )
    loss.backward()
    optimizer.step()
    
    if i % 100 == 0:
        print( model.bias )
        print( model.weight )

# 6] 훈련된 모델 실전 투입