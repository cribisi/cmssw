# getDatasets.py

import FWCore.ParameterSet.Config as cms


# dump of the Stream A Datasets defined in the HLT table as Stream A Datasets

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetBTag_selector
streamA_datasetBTag_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetBTag_selector.l1tResults = cms.InputTag('')
streamA_datasetBTag_selector.throw      = cms.bool(False)
streamA_datasetBTag_selector.triggerConditions = cms.vstring('HLT_BTagMu_DiJet110_Mu5_v3', 
    'HLT_BTagMu_DiJet20_Mu5_v3', 
    'HLT_BTagMu_DiJet40_Mu5_v3', 
    'HLT_BTagMu_DiJet70_Mu5_v3', 
    'HLT_BTagMu_Jet300_Mu5_v3')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetCommissioning_selector
streamA_datasetCommissioning_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetCommissioning_selector.l1tResults = cms.InputTag('')
streamA_datasetCommissioning_selector.throw      = cms.bool(False)
streamA_datasetCommissioning_selector.triggerConditions = cms.vstring('HLT_Activity_Ecal_SC7_v11', 
    'HLT_BeamGas_HF_Beam1_v4', 
    'HLT_BeamGas_HF_Beam2_v4', 
    'HLT_IsoTrackHB_v13', 
    'HLT_IsoTrackHE_v14', 
    'HLT_L1ETM100_v1', 
    'HLT_L1ETM30_v1', 
    'HLT_L1ETM40_v1', 
    'HLT_L1ETM70_v1', 
    'HLT_L1SingleEG12_v5', 
    'HLT_L1SingleEG5_v5', 
    'HLT_L1SingleJet16_v6', 
    'HLT_L1SingleJet36_v6', 
    'HLT_L1SingleMuOpen_v6', 
    'HLT_L1Tech_DT_GlobalOR_v3')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetCosmics_selector
streamA_datasetCosmics_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetCosmics_selector.l1tResults = cms.InputTag('')
streamA_datasetCosmics_selector.throw      = cms.bool(False)
streamA_datasetCosmics_selector.triggerConditions = cms.vstring('HLT_BeamHalo_v12', 
    'HLT_L1SingleMuOpen_AntiBPTX_v5', 
    'HLT_L1TrackerCosmics_v6')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetDoubleElectron_selector
streamA_datasetDoubleElectron_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetDoubleElectron_selector.l1tResults = cms.InputTag('')
streamA_datasetDoubleElectron_selector.throw      = cms.bool(False)
streamA_datasetDoubleElectron_selector.triggerConditions = cms.vstring('HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_CaloIdT_TrkIdVL_v10', 
    'HLT_Ele15_Ele8_Ele5_CaloIdL_TrkIdVL_v4', 
    'HLT_Ele17_CaloIdL_CaloIsoVL_v15', 
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v16', 
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v4', 
    'HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v4', 
    'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_Ele8_Mass50_v4', 
    'HLT_Ele20_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC4_Mass50_v4', 
    'HLT_Ele23_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT30_v5', 
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele15_CaloIdT_CaloIsoVL_trackless_v5', 
    'HLT_Ele27_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_HFT15_v5', 
    'HLT_Ele32_CaloIdT_CaloIsoT_TrkIdT_TrkIsoT_SC17_Mass50_v4', 
    'HLT_Ele5_SC5_Jpsi_Mass2to15_v2', 
    'HLT_Ele8_CaloIdL_CaloIsoVL_v15', 
    'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Jet30_v4', 
    'HLT_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v13', 
    'HLT_Ele8_CaloIdT_TrkIdVL_v3', 
    'HLT_Photon22_R9Id90_HE10_Iso40_EBOnly_v3', 
    'HLT_Photon36_R9Id90_HE10_Iso40_EBOnly_v3', 
    'HLT_Photon50_R9Id90_HE10_Iso40_EBOnly_v3', 
    'HLT_Photon75_R9Id90_HE10_Iso40_EBOnly_v3', 
    'HLT_Photon90_R9Id90_HE10_Iso40_EBOnly_v3', 
    'HLT_TripleEle10_CaloIdL_TrkIdVL_v16')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetDoubleMu_selector
streamA_datasetDoubleMu_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetDoubleMu_selector.l1tResults = cms.InputTag('')
streamA_datasetDoubleMu_selector.throw      = cms.bool(False)
streamA_datasetDoubleMu_selector.triggerConditions = cms.vstring('HLT_DoubleMu11_Acoplanarity03_v3', 
    'HLT_DoubleMu4_Acoplanarity03_v3', 
    'HLT_DoubleMu5_IsoMu5_v17', 
    'HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v2', 
    'HLT_L2DoubleMu23_NoVertex_v10', 
    'HLT_L2DoubleMu38_NoVertex_2Cha_Angle2p5_v2', 
    'HLT_Mu17_Mu8_v16', 
    'HLT_Mu17_TkMu8_v9', 
    'HLT_Mu17_v3', 
    'HLT_Mu22_TkMu22_v4', 
    'HLT_Mu22_TkMu8_v4', 
    'HLT_Mu8_v16', 
    'HLT_TripleMu5_v17')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetDoubleMuParked_selector
streamA_datasetDoubleMuParked_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetDoubleMuParked_selector.l1tResults = cms.InputTag('')
streamA_datasetDoubleMuParked_selector.throw      = cms.bool(False)
streamA_datasetDoubleMuParked_selector.triggerConditions = cms.vstring('HLT_Dimuon10_Jpsi_v3', 
    'HLT_Dimuon5_PsiPrime_v3', 
    'HLT_Dimuon8_Jpsi_v3', 
    'HLT_Dimuon9_PsiPrime_v9', 
    'HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v3', 
    'HLT_DoubleMu3p5_LowMass_Displaced_v3', 
    'HLT_Mu13_Mu8_v16')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetElectronHad_selector
streamA_datasetElectronHad_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetElectronHad_selector.l1tResults = cms.InputTag('')
streamA_datasetElectronHad_selector.throw      = cms.bool(False)
streamA_datasetElectronHad_selector.triggerConditions = cms.vstring('HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET40_v4', 
    'HLT_DoubleEle14_CaloIdT_TrkIdVL_Mass8_PFMET50_v4', 
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFHT175_v4', 
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_Mass8_PFHT225_v4', 
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_v10', 
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_DoubleCentralJet65_v4', 
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR30_Rsq0p04_MR200_v4', 
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR40_Rsq0p04_MR200_v4', 
    'HLT_Ele12_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_RsqMR45_Rsq0p04_MR200_v3', 
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFJet30_BTagIPIter_v5', 
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFJet30_v9', 
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v4', 
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_v4', 
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_DiCentralPFJet30_v9', 
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_DiCentralPFNoPUJet30_v4', 
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TriCentralPFJet30_v9', 
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TriCentralPFJet50_40_30_v4', 
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TriCentralPFNoPUJet30_v4', 
    'HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TriCentralPFNoPUJet50_40_30_v4', 
    'HLT_Ele25_CaloIdVT_TrkIdT_TriCentralPFJet30_v9', 
    'HLT_Ele25_CaloIdVT_TrkIdT_TriCentralPFJet50_40_30_v4', 
    'HLT_Ele25_CaloIdVT_TrkIdT_TriCentralPFNoPUJet30_v4', 
    'HLT_Ele25_CaloIdVT_TrkIdT_TriCentralPFNoPUJet50_40_30_v4', 
    'HLT_Ele27_WP80_CentralPFJet30_CentralPFJet25_PFMET20_v3', 
    'HLT_Ele27_WP80_CentralPFJet30_CentralPFJet25_v5', 
    'HLT_Ele27_WP80_CentralPFJet80_v5', 
    'HLT_Ele27_WP80_PFJet30_PFJet25_Deta3_v5', 
    'HLT_Ele27_WP80_WCandPt80_v4', 
    'HLT_Ele30_CaloIdVT_TrkIdT_PFJet100_PFJet25_v4', 
    'HLT_Ele30_CaloIdVT_TrkIdT_PFJet150_PFJet25_v4', 
    'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v3', 
    'HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v3', 
    'HLT_Ele8_CaloIdT_TrkIdT_DiJet30_v14', 
    'HLT_Ele8_CaloIdT_TrkIdT_QuadJet30_v14', 
    'HLT_Ele8_CaloIdT_TrkIdT_TriJet30_v14', 
    'HLT_Ele8_CaloIdT_TrkIdVL_Jet30_v3', 
    'HLT_HT650_Track50_dEdx3p6_v5', 
    'HLT_HT650_Track60_dEdx3p7_v5', 
    'HLT_MET80_Track50_dEdx3p6_v4', 
    'HLT_MET80_Track60_dEdx3p7_v4', 
    'HLT_MET80_v3')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetFEDMonitor_selector
streamA_datasetFEDMonitor_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetFEDMonitor_selector.l1tResults = cms.InputTag('')
streamA_datasetFEDMonitor_selector.throw      = cms.bool(False)
streamA_datasetFEDMonitor_selector.triggerConditions = cms.vstring('HLT_DTErrors_v3')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetForwardTriggers_selector
streamA_datasetForwardTriggers_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetForwardTriggers_selector.l1tResults = cms.InputTag('')
streamA_datasetForwardTriggers_selector.throw      = cms.bool(False)
streamA_datasetForwardTriggers_selector.triggerConditions = cms.vstring('HLT_L1Tech_CASTOR_HaloMuon_v3')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetHT_selector
streamA_datasetHT_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetHT_selector.l1tResults = cms.InputTag('')
streamA_datasetHT_selector.throw      = cms.bool(False)
streamA_datasetHT_selector.triggerConditions = cms.vstring('HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v4', 
    'HLT_CleanPFHT300_Ele15_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v4', 
    'HLT_CleanPFHT300_Ele40_CaloIdVT_TrkIdT_v4', 
    'HLT_CleanPFHT300_Ele60_CaloIdVT_TrkIdT_v4', 
    'HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET45_v4', 
    'HLT_CleanPFHT350_Ele5_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_PFMET50_v4', 
    'HLT_FatDiPFJetMass750_DR1p1_Deta1p5_v3', 
    'HLT_HT200_AlphaT0p57_v3', 
    'HLT_HT200_v2', 
    'HLT_HT250_AlphaT0p55_v2', 
    'HLT_HT250_AlphaT0p57_v2', 
    'HLT_HT250_DoubleDisplacedPFJet60_ChgFraction10_v3', 
    'HLT_HT250_DoubleDisplacedPFJet60_v3', 
    'HLT_HT250_SingleDisplacedPFJet60_ChgFraction10_v3', 
    'HLT_HT250_SingleDisplacedPFJet60_v3', 
    'HLT_HT250_v2', 
    'HLT_HT300_AlphaT0p53_v2', 
    'HLT_HT300_AlphaT0p54_v8', 
    'HLT_HT300_DoubleDisplacedPFJet60_ChgFraction10_v3', 
    'HLT_HT300_DoubleDisplacedPFJet60_v3', 
    'HLT_HT300_SingleDisplacedPFJet60_ChgFraction10_v3', 
    'HLT_HT300_SingleDisplacedPFJet60_v3', 
    'HLT_HT300_v2', 
    'HLT_HT350_AlphaT0p52_v2', 
    'HLT_HT350_AlphaT0p53_v13', 
    'HLT_HT350_v2', 
    'HLT_HT400_AlphaT0p51_v13', 
    'HLT_HT400_AlphaT0p52_v8', 
    'HLT_HT400_v2', 
    'HLT_HT450_AlphaT0p51_v8', 
    'HLT_HT450_v2', 
    'HLT_HT500_v2', 
    'HLT_HT550_v2', 
    'HLT_HT650_v2', 
    'HLT_HT750_v2', 
    'HLT_PFHT350_PFMET100_v4', 
    'HLT_PFHT350_v4', 
    'HLT_PFHT400_PFMET100_v4', 
    'HLT_PFHT650_DiCentralPFJet80_CenPFJet40_v4', 
    'HLT_PFHT650_v6', 
    'HLT_PFHT700_v4', 
    'HLT_PFHT750_v4', 
    'HLT_RsqMR40_Rsq0p04_v3', 
    'HLT_RsqMR45_Rsq0p09_v2', 
    'HLT_RsqMR55_Rsq0p09_MR150_v3', 
    'HLT_RsqMR60_Rsq0p09_MR150_v3', 
    'HLT_RsqMR65_Rsq0p09_MR150_v2')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetHcalHPDNoise_selector
streamA_datasetHcalHPDNoise_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetHcalHPDNoise_selector.l1tResults = cms.InputTag('')
streamA_datasetHcalHPDNoise_selector.throw      = cms.bool(False)
streamA_datasetHcalHPDNoise_selector.triggerConditions = cms.vstring('HLT_GlobalRunHPDNoise_v7', 
    'HLT_L1Tech_HBHEHO_totalOR_v5', 
    'HLT_L1Tech_HCAL_HF_single_channel_v3')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetHcalNZS_selector
streamA_datasetHcalNZS_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetHcalNZS_selector.l1tResults = cms.InputTag('')
streamA_datasetHcalNZS_selector.throw      = cms.bool(False)
streamA_datasetHcalNZS_selector.triggerConditions = cms.vstring('HLT_HcalNZS_v9', 
    'HLT_HcalPhiSym_v10')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetJet_selector
streamA_datasetJet_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetJet_selector.l1tResults = cms.InputTag('')
streamA_datasetJet_selector.throw      = cms.bool(False)
streamA_datasetJet_selector.triggerConditions = cms.vstring('HLT_DiPFJetAve140_v4', 
    'HLT_DiPFJetAve200_v4', 
    'HLT_DiPFJetAve260_v4', 
    'HLT_DiPFJetAve320_v4', 
    'HLT_DiPFJetAve400_v4', 
    'HLT_DiPFJetAve40_v4', 
    'HLT_DiPFJetAve80_v4', 
    'HLT_Jet20_NoL1FastJet_v2', 
    'HLT_Jet370_NoJetID_v13', 
    'HLT_Jet50_NoL1FastJet_v2', 
    'HLT_PFJet140_v4', 
    'HLT_PFJet200_v4', 
    'HLT_PFJet260_v4', 
    'HLT_PFJet320_v4', 
    'HLT_PFJet400_v4', 
    'HLT_PFJet40_v4', 
    'HLT_PFJet80_v4', 
    'HLT_SingleForJet15_v2', 
    'HLT_SingleForJet25_v2', 
    'HLT_SingleJetC5_v2')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetLogMonitor_selector
streamA_datasetLogMonitor_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetLogMonitor_selector.l1tResults = cms.InputTag('')
streamA_datasetLogMonitor_selector.throw      = cms.bool(False)
streamA_datasetLogMonitor_selector.triggerConditions = cms.vstring('HLT_LogMonitor_v2')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetMET_selector
streamA_datasetMET_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetMET_selector.l1tResults = cms.InputTag('')
streamA_datasetMET_selector.throw      = cms.bool(False)
streamA_datasetMET_selector.triggerConditions = cms.vstring('HLT_CentralPFJet80_CaloMET50_dPhi1_PFMHT80_HBHENoiseFiltered_v4', 
    'HLT_DiCentralJet20_BTagIP_MET65_HBHENoiseFiltered_dPhi1_v4', 
    'HLT_DiCentralJet20_CaloMET65_BTagCSV07_PFMHT80_v3', 
    'HLT_DiCentralPFJet30_CaloMET50_dPhi1_PFMHT80_HBHENoiseFiltered_v4', 
    'HLT_DiCentralPFJet30_PFMHT80_v6', 
    'HLT_DiCentralPFJet50_PFMET80_v4', 
    'HLT_DiPFJet40_PFMETnoMu65_MJJ600VBF_LeadingJets_v3', 
    'HLT_DiPFJet40_PFMETnoMu65_MJJ800VBF_AllJets_v3', 
    'HLT_MET120_HBHENoiseCleaned_v3', 
    'HLT_MET120_v10', 
    'HLT_MET200_HBHENoiseCleaned_v3', 
    'HLT_MET200_v10', 
    'HLT_MET300_HBHENoiseCleaned_v3', 
    'HLT_MET300_v2', 
    'HLT_MET400_HBHENoiseCleaned_v3', 
    'HLT_MET400_v5', 
    'HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v3', 
    'HLT_PFMET150_v3', 
    'HLT_PFMET180_v3')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetMinimumBias_selector
streamA_datasetMinimumBias_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetMinimumBias_selector.l1tResults = cms.InputTag('')
streamA_datasetMinimumBias_selector.throw      = cms.bool(False)
streamA_datasetMinimumBias_selector.triggerConditions = cms.vstring('HLT_JetE30_NoBPTX3BX_NoHalo_v12', 
    'HLT_JetE30_NoBPTX_v11', 
    'HLT_JetE50_NoBPTX3BX_NoHalo_v8', 
    'HLT_JetE70_NoBPTX3BX_NoHalo_v1', 
    'HLT_Physics_v4', 
    'HLT_PixelTracks_Multiplicity70_v2', 
    'HLT_PixelTracks_Multiplicity80_v11', 
    'HLT_PixelTracks_Multiplicity90_v2', 
    'HLT_Random_v2', 
    'HLT_ZeroBiasPixel_DoubleTrack_v1', 
    'HLT_ZeroBias_v6')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetMuEG_selector
streamA_datasetMuEG_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetMuEG_selector.l1tResults = cms.InputTag('')
streamA_datasetMuEG_selector.throw      = cms.bool(False)
streamA_datasetMuEG_selector.triggerConditions = cms.vstring('HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v13', 
    'HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v2', 
    'HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v5', 
    'HLT_Mu22_Photon22_CaloIdL_v4', 
    'HLT_Mu30_Ele30_CaloIdL_v4', 
    'HLT_Mu7_Ele7_CaloIdT_CaloIsoVL_v4', 
    'HLT_Mu8_DoubleEle8_CaloIdT_TrkIdVL_v4', 
    'HLT_Mu8_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v5', 
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Ele8_CaloIdL_TrkIdVL_v4')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetMuHad_selector
streamA_datasetMuHad_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetMuHad_selector.l1tResults = cms.InputTag('')
streamA_datasetMuHad_selector.throw      = cms.bool(False)
streamA_datasetMuHad_selector.triggerConditions = cms.vstring('HLT_DoubleDisplacedMu4_DiPFJet40Neutral_v3', 
    'HLT_DoubleMu14_Mass8_PFMET40_v4', 
    'HLT_DoubleMu14_Mass8_PFMET50_v4', 
    'HLT_DoubleMu8_Mass8_PFHT175_v4', 
    'HLT_DoubleMu8_Mass8_PFHT225_v4', 
    'HLT_DoubleRelIso1p0Mu5_Mass8_PFHT175_v3', 
    'HLT_DoubleRelIso1p0Mu5_Mass8_PFHT225_v3', 
    'HLT_IsoMu17_eta2p1_DiCentralPFJet30_PFHT350_PFMHT40_v4', 
    'HLT_IsoMu17_eta2p1_TriCentralPFJet30_v3', 
    'HLT_IsoMu20_eta2p1_CentralPFJet30_BTagIPIter_v3', 
    'HLT_IsoMu20_eta2p1_CentralPFJet30_v3', 
    'HLT_IsoMu20_eta2p1_CentralPFJet80_v4', 
    'HLT_IsoMu20_eta2p1_CentralPFNoPUJet30_BTagIPIter_v3', 
    'HLT_IsoMu20_eta2p1_CentralPFNoPUJet30_v3', 
    'HLT_IsoMu20_eta2p1_DiCentralPFJet30_v3', 
    'HLT_IsoMu20_eta2p1_DiCentralPFNoPUJet30_v3', 
    'HLT_IsoMu20_eta2p1_TriCentralPFJet30_v3', 
    'HLT_IsoMu20_eta2p1_TriCentralPFJet50_40_30_v3', 
    'HLT_IsoMu20_eta2p1_TriCentralPFNoPUJet30_v3', 
    'HLT_IsoMu20_eta2p1_TriCentralPFNoPUJet50_40_30_v3', 
    'HLT_IsoMu20_eta2p1_WCandPt80_v4', 
    'HLT_IsoMu24_eta2p1_CentralPFJet30_CentralPFJet25_PFMET20_v3', 
    'HLT_IsoMu24_eta2p1_CentralPFJet30_CentralPFJet25_v4', 
    'HLT_IsoMu24_eta2p1_PFJet30_PFJet25_Deta3_v4', 
    'HLT_L2TripleMu10_0_0_NoVertex_PFJet40Neutral_v3', 
    'HLT_Mu12_DoubleCentralJet65_v4', 
    'HLT_Mu12_RsqMR30_Rsq0p04_MR200_v4', 
    'HLT_Mu12_RsqMR40_Rsq0p04_MR200_v4', 
    'HLT_Mu12_RsqMR45_Rsq0p04_MR200_v3', 
    'HLT_Mu12_eta2p1_DiCentral_20_v3', 
    'HLT_Mu12_eta2p1_DiCentral_40_20_BTagIP3D1stTrack_v3', 
    'HLT_Mu12_eta2p1_DiCentral_40_20_DiBTagIP3D1stTrack_v3', 
    'HLT_Mu12_eta2p1_DiCentral_40_20_v3', 
    'HLT_Mu12_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v3', 
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET40_v4', 
    'HLT_Mu14_Ele14_CaloIdT_TrkIdVL_Mass8_PFMET50_v4', 
    'HLT_Mu15_eta2p1_TriCentral_40_20_20_BTagIP3D1stTrack_v3', 
    'HLT_Mu15_eta2p1_TriCentral_40_20_20_DiBTagIP3D1stTrack_v3', 
    'HLT_Mu15_eta2p1_TriCentral_40_20_20_v3', 
    'HLT_Mu20_eta2p1_CentralPFJet30_BTagIPIter_v4', 
    'HLT_Mu20_eta2p1_CentralPFNoPUJet30_BTagIPIter_v3', 
    'HLT_Mu20_eta2p1_TriCentralPFJet30_v4', 
    'HLT_Mu20_eta2p1_TriCentralPFJet50_40_30_v3', 
    'HLT_Mu20_eta2p1_TriCentralPFNoPUJet30_v3', 
    'HLT_Mu20_eta2p1_TriCentralPFNoPUJet50_40_30_v3', 
    'HLT_Mu24_eta2p1_CentralPFJet30_CentralPFJet25_v4', 
    'HLT_Mu24_eta2p1_PFJet30_PFJet25_Deta3_v4', 
    'HLT_Mu40_FJHT200_v4', 
    'HLT_Mu40_PFHT350_v4', 
    'HLT_Mu60_PFHT350_v4', 
    'HLT_Mu8_DiJet30_v4', 
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT175_v4', 
    'HLT_Mu8_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT225_v4', 
    'HLT_Mu8_QuadJet30_v4', 
    'HLT_Mu8_TriJet30_v4', 
    'HLT_PFHT350_Mu15_PFMET45_v4', 
    'HLT_PFHT350_Mu15_PFMET50_v4', 
    'HLT_PFHT400_Mu5_PFMET45_v4', 
    'HLT_PFHT400_Mu5_PFMET50_v4', 
    'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT175_v3', 
    'HLT_RelIso1p0Mu5_Ele8_CaloIdT_TrkIdVL_Mass8_PFHT225_v3')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetMuOnia_selector
streamA_datasetMuOnia_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetMuOnia_selector.l1tResults = cms.InputTag('')
streamA_datasetMuOnia_selector.throw      = cms.bool(False)
streamA_datasetMuOnia_selector.triggerConditions = cms.vstring('HLT_Dimuon0_Jpsi_Muon_v15', 
    'HLT_Dimuon0_Jpsi_NoVertexing_v11', 
    'HLT_Dimuon0_Jpsi_v14', 
    'HLT_Dimuon0_PsiPrime_v3', 
    'HLT_Dimuon0_Upsilon_Muon_v15', 
    'HLT_Dimuon0_Upsilon_v14', 
    'HLT_Dimuon11_Upsilon_v3', 
    'HLT_Dimuon3p5_SameSign_v3', 
    'HLT_Dimuon5_Upsilon_v3', 
    'HLT_Dimuon7_Upsilon_v3', 
    'HLT_Dimuon8_Upsilon_v3', 
    'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v2', 
    'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v2', 
    'HLT_DoubleMu4_Dimuon7_Bs_Forward_v2', 
    'HLT_DoubleMu4_JpsiTk_Displaced_v3', 
    'HLT_DoubleMu4_Jpsi_Displaced_v9', 
    'HLT_Mu5_L2Mu3_Jpsi_v3', 
    'HLT_Mu5_Track2_Jpsi_v17', 
    'HLT_Mu5_Track3p5_Jpsi_v3', 
    'HLT_Mu7_Track7_Jpsi_v18', 
    'HLT_Tau2Mu_ItTrack_v2')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetMultiJet_selector
streamA_datasetMultiJet_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetMultiJet_selector.l1tResults = cms.InputTag('')
streamA_datasetMultiJet_selector.throw      = cms.bool(False)
streamA_datasetMultiJet_selector.triggerConditions = cms.vstring('HLT_DiJet40Eta2p6_BTagIP3DFastPV_v3', 
    'HLT_DiJet40Eta2p6_BTagIP3D_v3', 
    'HLT_DiJet80Eta2p6_BTagIP3DFastPVLoose_v3', 
    'HLT_DiJet80Eta2p6_BTagIP3DLoose_v3', 
    'HLT_DiJet80_DiJet60_DiJet20_v2', 
    'HLT_DoubleJet20_ForwardBackward_v2', 
    'HLT_EightJet35_v2', 
    'HLT_EightJet40_v2', 
    'HLT_ExclDiJet35_HFAND_v2', 
    'HLT_ExclDiJet35_HFOR_v2', 
    'HLT_ExclDiJet80_HFAND_v2', 
    'HLT_Jet160Eta2p4_Jet120Eta2p4_DiBTagIP3DFastPVLoose_v3', 
    'HLT_Jet160Eta2p4_Jet120Eta2p4_DiBTagIP3DLoose_v3', 
    'HLT_Jet60Eta1p7_Jet53Eta1p7_DiBTagIP3DFastPV_v3', 
    'HLT_Jet60Eta1p7_Jet53Eta1p7_DiBTagIP3D_v3', 
    'HLT_Jet80Eta1p7_Jet70Eta1p7_DiBTagIP3DFastPV_v3', 
    'HLT_Jet80Eta1p7_Jet70Eta1p7_DiBTagIP3D_v3', 
    'HLT_L1DoubleJet36Central_v6', 
    'HLT_QuadJet50_v2', 
    'HLT_QuadJet60_DiJet20_v2', 
    'HLT_QuadJet70_v2', 
    'HLT_QuadJet75_55_35_20_BTagIP_VBF_v3', 
    'HLT_QuadJet75_55_38_20_BTagIP_VBF_v3', 
    'HLT_QuadJet80_v2', 
    'HLT_QuadJet90_v2', 
    'HLT_QuadPFJet75_55_35_20_BTagCSV_VBF_v3', 
    'HLT_QuadPFJet75_55_38_20_BTagCSV_VBF_v3', 
    'HLT_SixJet35_v2', 
    'HLT_SixJet45_v2', 
    'HLT_SixJet50_v2')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetPhoton_selector
streamA_datasetPhoton_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetPhoton_selector.l1tResults = cms.InputTag('')
streamA_datasetPhoton_selector.throw      = cms.bool(False)
streamA_datasetPhoton_selector.triggerConditions = cms.vstring('HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v4', 
    'HLT_DoubleEle33_CaloIdL_v12', 
    'HLT_DoubleEle33_CaloIdT_v8', 
    'HLT_DoublePhoton40_CaloIdL_Rsq0p035_v2', 
    'HLT_DoublePhoton40_CaloIdL_Rsq0p06_v2', 
    'HLT_DoublePhoton43_HEVT_v6', 
    'HLT_DoublePhoton48_HEVT_v6', 
    'HLT_DoublePhoton5_IsoVL_CEP_v14', 
    'HLT_DoublePhoton70_v4', 
    'HLT_DoublePhoton80_v5', 
    'HLT_Photon135_v5', 
    'HLT_Photon150_v2', 
    'HLT_Photon160_v2', 
    'HLT_Photon20_CaloIdVL_IsoL_v14', 
    'HLT_Photon20_CaloIdVL_v2', 
    'HLT_Photon250_NoHE_v2', 
    'HLT_Photon26_CaloId10_Iso50_Photon18_CaloId10_Iso50_Mass60_v4', 
    'HLT_Photon26_CaloId10_Iso50_Photon18_R9Id85_Mass60_v4', 
    'HLT_Photon26_Photon18_v10', 
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_R9Id85_OR_CaloId10_Iso50_Mass60_v4', 
    'HLT_Photon26_R9Id85_OR_CaloId10_Iso50_Photon18_v3', 
    'HLT_Photon26_R9Id85_Photon18_CaloId10_Iso50_Mass60_v4', 
    'HLT_Photon26_R9Id85_Photon18_R9Id85_Mass60_v2', 
    'HLT_Photon300_NoHE_v2', 
    'HLT_Photon30_CaloIdVL_IsoL_v17', 
    'HLT_Photon30_CaloIdVL_v12', 
    'HLT_Photon36_CaloId10_Iso50_Photon22_CaloId10_Iso50_v4', 
    'HLT_Photon36_CaloId10_Iso50_Photon22_R9Id85_v4', 
    'HLT_Photon36_Photon22_v4', 
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v4', 
    'HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v3', 
    'HLT_Photon36_R9Id85_Photon22_CaloId10_Iso50_v4', 
    'HLT_Photon36_R9Id85_Photon22_R9Id85_v2', 
    'HLT_Photon50_CaloIdVL_IsoL_v15', 
    'HLT_Photon50_CaloIdVL_v8', 
    'HLT_Photon75_CaloIdVL_IsoL_v16', 
    'HLT_Photon75_CaloIdVL_v11', 
    'HLT_Photon90_CaloIdVL_IsoL_v13', 
    'HLT_Photon90_CaloIdVL_v8')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetPhotonHad_selector
streamA_datasetPhotonHad_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetPhotonHad_selector.l1tResults = cms.InputTag('')
streamA_datasetPhotonHad_selector.throw      = cms.bool(False)
streamA_datasetPhotonHad_selector.triggerConditions = cms.vstring('HLT_Photon40_CaloIdL_RsqMR35_Rsq0p09_MR150_v2', 
    'HLT_Photon40_CaloIdL_RsqMR40_Rsq0p09_MR150_v2', 
    'HLT_Photon40_CaloIdL_RsqMR45_Rsq0p09_MR150_v2', 
    'HLT_Photon40_CaloIdL_RsqMR50_Rsq0p09_MR150_v2', 
    'HLT_Photon60_CaloIdL_FJHT300_v2', 
    'HLT_Photon60_CaloIdL_MHT70_v6', 
    'HLT_Photon70_CaloIdXL_PFHT400_v3', 
    'HLT_Photon70_CaloIdXL_PFHT500_v3', 
    'HLT_Photon70_CaloIdXL_PFMET100_v3', 
    'HLT_Photon90EBOnly_CaloIdVL_IsoL_TriPFJet25_v11', 
    'HLT_Photon90EBOnly_CaloIdVL_IsoL_TriPFJet30_v11')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetSingleElectron_selector
streamA_datasetSingleElectron_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetSingleElectron_selector.l1tResults = cms.InputTag('')
streamA_datasetSingleElectron_selector.throw      = cms.bool(False)
streamA_datasetSingleElectron_selector.triggerConditions = cms.vstring('HLT_Ele100_CaloIdVT_TrkIdT_v9', 
    'HLT_Ele22_CaloIdL_CaloIsoVL_v4', 
    'HLT_Ele27_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
    'HLT_Ele27_WP80_PFMET_MT50_v3', 
    'HLT_Ele27_WP80_v9', 
    'HLT_Ele30_CaloIdVT_TrkIdT_v4', 
    'HLT_Ele32_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_v9', 
    'HLT_Ele65_CaloIdVT_TrkIdT_v12', 
    'HLT_Ele80_CaloIdVT_TrkIdT_v9')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetSingleMu_selector
streamA_datasetSingleMu_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetSingleMu_selector.l1tResults = cms.InputTag('')
streamA_datasetSingleMu_selector.throw      = cms.bool(False)
streamA_datasetSingleMu_selector.triggerConditions = cms.vstring('HLT_IsoMu20_eta2p1_v4', 
    'HLT_IsoMu24_eta2p1_v12', 
    'HLT_IsoMu30_eta2p1_v12', 
    'HLT_IsoMu34_eta2p1_v10', 
    'HLT_IsoMu40_eta2p1_v7', 
    'HLT_L1SingleMu12_v1', 
    'HLT_L2Mu10_NoVertex_NoBPTX3BX_NoHalo_v1', 
    'HLT_L2Mu20_NoVertex_NoBPTX3BX_NoHalo_v1', 
    'HLT_L2Mu20_eta2p1_NoVertex_v1', 
    'HLT_L2Mu30_NoVertex_NoBPTX3BX_NoHalo_v1', 
    'HLT_L2Mu70_eta2p1_PFMET65_v3', 
    'HLT_L2Mu80_eta2p1_PFMET70_v3', 
    'HLT_Mu12_v16', 
    'HLT_Mu15_eta2p1_v3', 
    'HLT_Mu24_eta2p1_v3', 
    'HLT_Mu30_eta2p1_v3', 
    'HLT_Mu40_eta2p1_Track50_dEdx3p6_v3', 
    'HLT_Mu40_eta2p1_Track60_dEdx3p7_v3', 
    'HLT_Mu40_eta2p1_v9', 
    'HLT_Mu50_eta2p1_v6', 
    'HLT_Mu5_v18', 
    'HLT_RelIso1p0Mu17_v3', 
    'HLT_RelIso1p0Mu5_v3')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetTau_selector
streamA_datasetTau_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetTau_selector.l1tResults = cms.InputTag('')
streamA_datasetTau_selector.throw      = cms.bool(False)
streamA_datasetTau_selector.triggerConditions = cms.vstring('HLT_DoubleMediumIsoPFTau25_Trk5_eta2p1_Jet30_v3', 
    'HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v3', 
    'HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v3', 
    'HLT_LooseIsoPFTau35_Trk20_Prong1_MET70_v3', 
    'HLT_LooseIsoPFTau35_Trk20_Prong1_MET75_v3', 
    'HLT_LooseIsoPFTau35_Trk20_Prong1_v3')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetTauPlusX_selector
streamA_datasetTauPlusX_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetTauPlusX_selector.l1tResults = cms.InputTag('')
streamA_datasetTauPlusX_selector.throw      = cms.bool(False)
streamA_datasetTauPlusX_selector.triggerConditions = cms.vstring('HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20L1Jet_v5', 
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v5', 
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau22L1Jet_v4', 
    'HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_v4', 
    'HLT_Ele20_CaloIdVT_TrkIdT_LooseIsoPFTau20_v5', 
    'HLT_Ele22_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v4', 
    'HLT_IsoMu15_eta2p1_L1ETM20_v4', 
    'HLT_IsoMu15_eta2p1_LooseIsoPFTau35_Trk20_Prong1_L1ETM20_v3', 
    'HLT_IsoMu18_eta2p1_LooseIsoPFTau20_v5', 
    'HLT_IsoMu18_eta2p1_MediumIsoPFTau25_Trk5_eta2p1_v4', 
    'HLT_IsoMu20_eta2p1_LooseIsoPFTau20_v4', 
    'HLT_Mu15_eta2p1_L1ETM20_v3', 
    'HLT_Mu18_eta2p1_LooseIsoPFTau20_v5')

