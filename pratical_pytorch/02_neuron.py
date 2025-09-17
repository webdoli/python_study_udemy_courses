import torch
from torch import nn

# Input
X = torch.tensor([
    [10],
    [37.78]
], dtype = torch.float32 )
# X입력 묶음

Y = torch.tensor([
    [50],
    [100.0]
], dtype = torch.float32 )
# Y 출력 묶음

model = nn.Linear(1, 1)
loss_fn = torch.nn.MSELoss() #손실 함수 설정
optimizer = torch.optim.SGD( model.parameters(), lr=0.0001 ) #최적화, 
#lr=학습속도(학습률), 학습속도가 너무 빠르면 계산이 제대로 안 되고 훈련이 제대로 안 될 수 있음


for i in range( 0, 1000 ):
    # 훈련
    optimizer.zero_grad() # 프로그램에게 처음부터 다시하라고 명령
    outputs = model( X )
    loss = loss_fn( outputs, Y ) #첫번째 파라미터: 모델의 예측, 
    loss.backward() # 손실함수의 기울기 가파름 정도를 계산, b or w 중에 1개 변경해야 함
    optimizer.step()

    if i % 10 == 0: # 루프가 10000번 실행되는데, 100번 마다 한번씩 가중치와 bias를 체크하기 위해
        print( '2] w:', model.weight )
        print( '2] bias:', model.bias )


print("------")

measurements = torch.tensor([
    [ 37.5 ]
], dtype = torch.float32 )

model.eval() #실전용으로 변경
with torch.no_grad(): # 위에서 1000번 모델 훈련이 끝났으므로 기울기를 계산하지 말것을 주문
    prediction = model( measurements )
    print( prediction )
