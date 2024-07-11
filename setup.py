import os
import requests
from setuptools import setup, find_packages
from setuptools.command.install import install

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        self.download_model()

    def download_model(self):
        model_url = 'https://github.com/aim-lab/PVBM/raw/main/PVBM/lunetv2_odc.onnx'
        model_path = os.path.join(os.path.dirname(__file__), 'PVBM', 'lunetv2_odc.onnx')
        if not os.path.exists(model_path):
            response = requests.get(model_url, stream=True)
            response.raise_for_status()
            with open(model_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f'Model downloaded to {model_path}')

def read_readme(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()

long_description = read_readme("README.md")

setup(
    name='pvbm',
    version='2.9.3',
    packages=find_packages(exclude=['PVBM/lunetv2_odc.onnx']),
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
    author='Jonathan Fhima, Yevgeniy Men',
    author_email='jonathanfh@campus.technion.ac.il',
    description="Python Vasculature Biomarker toolbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aim-lab/PVBM',
    cmdclass={
        'install': PostInstallCommand,
    },
)
