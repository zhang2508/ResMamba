from ResMamba import ResMamba
import torch

if __name__ == '__main__':
    model = ResMamba()
    model.load_state_dict(torch.load(r"ResMamba.pkl"))