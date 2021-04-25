import os

import numpy as np
from hist import Hist
from lhereader import LHEReader
from matplotlib import pyplot as plt


def setup_histograms():

    # Bin edges for each observable
    bins ={
        'dilep_minv' : np.linspace(500,1500,50),
        'lep_eta'    : np.linspace(-5,5,50),
        'lep_pt'     : np.linspace(0,1000,50),
        'dilep_pt'   : np.linspace(0,1000,50),
    } 

    histograms = { 
                    observable : (
                                    Hist.new
                                    .Var(binning, name=observable, label=observable)
                                    .Int64()
                                )
                    for observable, binning in bins.items()
    }

    return histograms

def analyze(lhe_file):
    reader = LHEReader(lhe_file)
    histograms = setup_histograms()
    for event in reader:
        # Find charged leptons
        leptons = filter(
                        lambda x: abs(x.pdgid) in (11,13,15),
                        event.particles
                        )

        # Sum over all lepton four-momenta in the event
        combined_p4 = None
        for p4 in map(lambda x: x.p4(), leptons):
            if combined_p4:
                combined_p4 += p4
            else:
                combined_p4 = p4

            histograms['lep_eta'].fill(p4.eta, weight=event.weights[0])
            histograms['lep_pt'].fill(p4.pt, weight=event.weights[0])

        histograms['dilep_minv'].fill(combined_p4.mass, weight=event.weights[0])
        histograms['dilep_pt'].fill(combined_p4.pt, weight=event.weights[0])
    return histograms

def plot(histograms):
    outdir = './plots/'
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    for observable, histogram in histograms.items():
        plt.gcf().clf()
        histogram.plot()
        plt.gcf().savefig(f"{outdir}/{observable}.pdf")

histograms = analyze('cmsgrid_final.lhe')
plot(histograms)
