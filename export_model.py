import torch
import torch.onnx
from model import SimpleCNN

def export_to_onnx(model_path='best_model.pth', output_path='model.onnx'):
    """
    Export trained PyTorch model to ONNX format.
    """
    # Load the model
    model = SimpleCNN()
    model.load_state_dict(torch.load(model_path, map_location='cpu'))
    model.eval()
    
    # Create dummy input (batch_size=1, channels=3, height=32, width=32)
    dummy_input = torch.randn(1, 3, 32, 32)
    
    # Export to ONNX
    torch.onnx.export(
        model,
        dummy_input,
        output_path,
        export_params=True,
        opset_version=11,
        do_constant_folding=True,
        input_names=['input'],
        output_names=['output'],
        dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}
    )
    
    print(f"Model exported to {output_path}")

if __name__ == "__main__":
    export_to_onnx()