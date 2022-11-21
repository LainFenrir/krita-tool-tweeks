# krita-tool-tweeks
krita plugin to make tweeks to krita tool options

## Features
V1.0
Reference Layer moved up in the tools:
- Fill tool
- Enclose and fill tool
- Contiguous selection tool
- Similar color selection tool

How does it work: when you open a document or creates one, It triggers all the tools that have a reference layer to change the order then goes back to the brush tool. that will only happen once as it stores the positions have been changed so it doesnt do the whole process again.


## Installation
Download the zip from github (press the code button> download zip, or click the tags in release and download the zip from there), open krita then go to:  
Tools>scripts>import plugin from file  
Click ok and close and open krita.  

Or follow the manual installation:  

1- Copy the contents of the plugin folder into the pykrita folder in the krita resource folder (accessible through settings>manage resources>open resource folder).  
The folder label-box need to be completely moved (moving just the files inside will not work).  
2- Open krita, go to settings>configure krita> python plugin manager. Locate the Label Box and check it.  
3- Restart krita. It should appear in the layer docker.  



## How to use
Just install it and it will work.


