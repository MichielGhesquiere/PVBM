import os
import requests
from setuptools import setup, find_packages

def download_model(url, destination_file_name):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(destination_file_name, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f'Model downloaded to {destination_file_name}')

def read_readme(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()

long_description = read_readme("README.md")

# Define the URL to your model file on GitHub
model_url = 'https://github.com/aim-lab/PVBM/raw/main/PVBM/lunetv2_odc.onnx?download='
model_path = os.path.join(os.path.dirname(__file__), 'PVBM', 'lunetv2_odc.onnx')

# Download the model if it does not exist
if not os.path.exists(model_path):
    download_model(model_url, model_path)

setup(
    name='pvbm',
    version='2.9.3',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "scikit-image",
        "pillow",
        "gdown",
        "onnxruntime",
        "torchvision",
        "opencv-python"
    ],
    # Remove 'package_data' and 'include_package_data'
    author='Jonathan Fhima, Yevgeniy Men',
    author_email='jonathanfh@campus.technion.ac.il',
    description="Python Vasculature Biomarker toolbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aim-lab/PVBM',
)
