# Plotting scripts for MG5 tutorials

This code is pure python and does not rely on CMSSW, etc. The setup instructions below are made for lxplus,
but you should be able to get it running also on your laptop or other random environment.

```bash 
source /cvmfs/sft.cern.ch/lcg/views/LCG_99/x86_64-centos7-gcc8-opt/setup.sh

# Setup virtual environnment
# Remember to re-activate if you open a new shell
ENVNAME="mg5tut"
python3 -m venv ${ENVNAME}
source ${ENVNAME}/bin/activate
export PYTHONPATH="${ENVNAME}/lib/python3.8/site-packages/:${PYTHONPATH}"

python -m pip install -U lhereader matplotlib mplhep 

```


New instructions for CMS Connect:
```bash
source /cvmfs/sft.cern.ch/lcg/views/LCG_104/x86_64-el9-gcc12-opt/setup.sh
# Setup virtual environnment
# Remember to re-activate if you open a new shell
ENVNAME="mg5tut"
python3 -m venv ${ENVNAME}
source ${ENVNAME}/bin/activate
python -m pip install -U lhereader matplotlib mplhep 
python -m pip install pylhe
```

to make the jupyter notebook work in CMS connect, besides those installation, I had to:

```
python -m ensurepip --upgrade
python -m pip install --upgrade pip setuptools wheel
python -m pip install --upgrade ipykernel
### register the kernel for jupyter
python -m ipykernel install --user --name mg5tut --display-name "Python (mg5tut)"
### then restart VSC again, and maybe install a few other things like numpy, etc
```

