class ResBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv1 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(channels)
        self.conv2 = nn.Conv2d(channels, channels, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(channels)

    def forward(self, x):
        x_input = torch.clone(x)
        out = self.conv1(x)
        out = self.bn1(out)
        out = F.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        out = x + x_input
        out = F.relu(out)
        return out

class ChessNet(nn.Module):
    def __init__(self, num_res_blocks=4):
        super().__init__()
        self.input_conv = nn.Conv2d(6, 4, 3, padding=1)

        self.res_blocks = nn.Sequential(
            *(ResBlock(4) for _ in range(num_res_blocks))
             )

        self.output_conv = nn.Conv2d(4, 2, 3, padding=1)

    def forward(self, x):
        out = self.input_conv(x.float())
        out = self.res_blocks(out)
        out = self.output_conv(out)
        return out
    

    model_0 = ChessNet( num_res_blocks=4)

    metric_from = nn.CrossEntropyLoss()
    metric_to = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(params=model_0.parameters(), lr=0.1)
    