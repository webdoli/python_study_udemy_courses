import torch
from torch import nn

X = torch.tensor([
    [10.0],
    [38.0],
    [100.0],
    [150.0]]
)

a = torch.Size([4, 1])

# print( X[:, 0] )

model = nn.Linear(1, 1)
print( model )
y_pred = model(X)

print( y_pred)

