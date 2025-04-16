import torch
import torch.nn as nn
import torch.nn.functional as F

class ModelArgs:
    para = 1

class Block(nn.Module):


class Transformer(nn.Module):
    def __init__(self, args: ModelArgs):

        self.blocks = nn.ModuleList()
        for _ in range(args.layers_num):
            self.blocks.append(Block())

    @torch.inference_mode()
    def forward(self, tokens, start_pos):
        # 取分布区域

        # 循环block
        for layer in self.blocks:
            h = layer(h)


        # 合并分布计算的结果

        return y;


if __name__ == "__main__":
    x = torch.rand([2, 5])
    y = F.linear(x, torch.rand([10, 5]))
    print(y.shape)
