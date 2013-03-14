from FastSimulation.PileUpProducer.PileUpSimulator8TeV_cfi import *

#### mix at GEN level:

from FastSimulation.Configuration.MixingFull_cff import *

mixGenPU.input.nbPileupEvents.averageNumber = cms.double(10.0) 
mixGenPU.input.type = cms.string('poisson')

# mix at SIM level:

from FastSimulation.Configuration.MixingHitsAndTracks_cff import *

mixSimCaloHits.input.nbPileupEvents.averageNumber = cms.double(10.0) 
mixSimCaloHits.input.type = cms.string('poisson')

mixRecoTracks.input.nbPileupEvents.averageNumber = cms.double(10.0) 
mixRecoTracks.input.type = cms.string('poisson')
