import torch
import torch.nn as nn

class BaselineCNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),

            nn.Conv2d(32, 32, kernel_size=3, padding=1),
            nn.ReLU(),

            nn.Conv2d(32, 4, kernel_size=3, padding=1)
        )

    def forward(self, x):
        B,T,C,H,W = x.shape

        x = x.reshape(B, T*C, H, W)

        return self.net(x)