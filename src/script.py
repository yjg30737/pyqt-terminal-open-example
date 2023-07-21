import os

from diffusers import StableDiffusionPipeline
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'

if __name__ == '__main__':
    pipe = StableDiffusionPipeline.from_single_file("https://huggingface.co/Linaqruf/anything-v3.0/blob/main/anything-v3-fp32-pruned.safetensors",
                                                    cache_dir='models', torch_dtype=torch.float32, load_safety_checker=False).to(device)

    prompt = "masterpiece, best quality, high resolution, 8K, HDR, beautiful girl,\ndetailed hair, beautiful face, ultra detailed eyes, (hyperdetailed:1.15)"
    negative_prompt = "(low quality, worst quality:1.4), (bad anatomy), (inaccurate limb:1.2), bad composition, inaccurate eyes, extra digit, fewer digits, (extra arms:1.2)"
    guidance_scale = 1
    eta = 0.0

    result = pipe(
        prompt, num_inference_steps=30, num_images_per_prompt=1,
        guidance_scale=7.5, negative_prompt=negative_prompt)
    for idx, image in enumerate(result.images):
        image.save(f"character4.png")

    os.system('exit')