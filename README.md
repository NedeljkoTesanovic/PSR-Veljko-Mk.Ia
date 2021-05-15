# Photo Surveillance System with PSR-Veljko-Mk.Ia
Collaboration project with friends.
Parking Service Robot "Veljko" Mk.Ia. Automated parking ticket sistem with a camera-carrying robot that displays information about parked cars after optically recognizing the characters on the licence plates.


The system consists of the main station's software with a visualization of a 6 slot parking area, that communicates with databases containing the data about the licences (and information about the drivers), as well robot agent (Veljko) that traverses along the lines drawn on the ground and takes photos with his camera.
The main station receives the image snapped by Veljko, then uses heuteristic methods to preprocess the image before utilizing a trained OCR neural network to read the characters.
The main station was realized in National Insturment's LABview, whilst Veljko's software and behaviour was realized by my dear colleagues in Python. The robot itself was built from a LEGO Mindstorm on a simple two-track chassis, with a fixed GOPro camera.
