# OraCAN
AI-powered hardware device that can detect 3 different types of oral-cancer using NVIDIA Jetson Nano and Endoscope Camera

**Software Used:** 
- [Edge Impulse Studio](https://studio.edgeimpulse.com)
- [NVIDIA TAO](https://developer.nvidia.com/tao-toolkit)
- Python3 (for Desktop App)

**Hardware Used:** 

- [NVIDIA Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano) (2GB RAM variant used here, 4GB would work as well)
- [Endoscope Camera](https://amzn.in/d/04WuWB4u) / [Intraoral Camera](https://www.dentalkart.com/waldent-intraoral-camera.html?gad_source=1&gbraid=0AAAAADeTeHzzWyVyDrab62eRbYRPes4Bx)
- 15 inch desktop monitor
- Basic Keyboard and Mouse

## ML Model

Machine Learning model has been made using Edge Impulse Studio. 
Here is the [public project](https://studio.edgeimpulse.com/public/179102/latest).

Here is a tutorial on how to train and develop ML models using Edge Impulse Studio: 

[![NVIDIA TAO X EI Tutorial](http://img.youtube.com/vi/bErEJ2lwCWg/0.jpg)](https://www.youtube.com/watch?v=bErEJ2lwCWg "Getting Started with Nvidia TAO and Jetson Devices for Edge AI")

## Hardware Deployment

Follow the setup as shown in this [video demo](https://drive.google.com/file/d/1zvXUHxisUpUC6fo0dSPK5SHCFXGCkf0n/view?usp=share_link) and execute the following in terminal:

```
git clone https://github.com/arijitdas123student/oral-cancer
cd oral-cancer
pip3 install -r requirements.txt
sudo chmod u+x modelfile-nano.eim
python3 main.py
```
