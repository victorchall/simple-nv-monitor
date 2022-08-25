# Simple NV monitor

This is a simple console app to monitor Nvidia GPUs.  It is built with the purpose of helping ML engineers that wish to help tune VRAM footprint as their app runs without having to string a series of print statements into their app or create logging and loops to call nvsmi on their own.

Run this in a separate console window while you run your app.  It will run continuosly until interrupted.

This uses the [nvsmi](https://github.com/pmav99/nvsmi) package which handles the integration work with the Nvidia SMI CLI.

![](preview.png)

# Install
pip install nvsmi

* or 

conda create env -f environment.yaml

conda activate nvsmi

# Run

python run.py
