# Steps to enable you MacOS environment

1. Download and Install Conda

2. Install Jupyter

3. Run Environment Setup Script

   ```
   conda env create -v -f tensorflow-env.yml
   ```

4. Install Kernel for Jupyter (I didn't require this step)

   ```
   python -m ipykernel install --user --name with_tensorflow --display-name "Python 3.7 (with_tensorflow)"
   ```
5. Switching among created environments (for macos only)

   ```
   source activate tensorflow
   ```
