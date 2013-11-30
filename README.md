FSMT-experiments
================

This repository aggregates fsmt experiment use-cases 

Requirements
===========

You will need a version of FSMT (Finite State Machine Based Testing)
You can get a copy, if you drop me a line: flier@techfak.uni-bielefeld.de

If you already have a copy of FSMT you should probably use the current 
trunk version in the following.

Depending on your experiment you might also need ROS and/or MORSE.
In this repository, I provide a "bootstrap script" which will
(both) install MORSE ans ROS, depending on your requirements.

Installation
===========

If you know what's going on here, you may change the paths 
according to your needs. Otherwise, execute the following: 

1. sudo mkdir -p /opt/fsmt-base/lib/python2.7/site-packages
2. sudo mkdir -p /opt/fsmt-experiments
3. sudo chown -R $USER /opt/fsmt-base && sudo chown -R /opt/fsmt-experiments
4. cd /opt/fsmt-base
5. copy/checkout your FSMT version to /opt/fsmt
6. export PYTHONPATH=/opt/fsmt-base/lib/python2.7/site-packages/:$PYTHONPATH
7. python setup.py install --prefix=/opt/fsmt-base/
8. cd /opt/fsmt-experiments
9. git clone https://github.com/warp1337/fsmt_experiments.git .
9a. Optionally, if you want to use/install MORSE and/or ROS
  sh morse-setup.sh (MORSE only, from GIT master), Press "y"
  sh morse-setup.sh --ROS (MORSE and ROS, "Groovy"), Press "y"
10. cd DESIRED_EXPERIMENT
11. export PATH=/opt/fsmt-base/bin/:$PATH
12. You may need to change the [environment] paths in the desired *.ini file depending on your installion
13. fsmtiniparser -o DESIRED_EXPERIMENT.scxml DESIRED_EXPERIMENT.ini
  Example: fsminiparser -o hri-morse-find-scenario.scxml hri-morse-find-scenario.ini   
14. Now you should have a DESIRED_EXPERIMENT.scxml in your current folder
Optional, if you use ROS
  source /opt/ros/groovy/setup.bash
15. fsmtest DESIRED_EXPERIMENT.scxml
  Example: fsmtest hri-morse-find-scenario.scxml
16. Have fun!
