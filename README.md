# LED Matrix Mouth

This project illuminates a MD_MAX72XX LED dot matrix in response to audio signals in order to mimic robotic speech. The system processes `.wav` files, analyzes frequency bands, and communicates with an Arduino Uno to control LED patterns. 

*This project was made as part of Oregon State University's ROB 421 Intro to Robotics course and created for the [SHARE Lab's SAMI Robot](https://github.com/shareresearchteam/SAMI-Robot).*

## Key Highlights
- Implemented real‑time audio processing using FFT to detect volume in the 40–600 Hz range.
- Applied a moving average filter to smooth noise and improve threshold detection.
- Integrated Python with Arduino via serial communication for hardware control.
- Developed a responsive LED matrix system that activates at sound thresholds to simulate speech.
- Applied principles of signal processing, embedded systems, and robotics integration.

## Usage
1. Upload the Arduino sketch (`ROB421_Matrix_Mouth.ino`) to your board.
2. Connect the LED matrix according to this easy [Tutorial page](https://lastminuteengineers.com/max7219-dot-matrix-arduino-tutorial/).
3. Run the Python script (`SAMIHardwareProject.py`) and provide a `.wav` file path.
4. The LED matrix will illuminate when audio exceeds the defined threshold.
