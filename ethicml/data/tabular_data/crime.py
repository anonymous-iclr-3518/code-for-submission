"""Class to describe features of the Communities and Crime dataset."""
from typing_extensions import Literal

from ..dataset import Dataset

__all__ = ["crime"]


def crime(split: Literal["Race-Binary"] = "Race-Binary", discrete_only: bool = False) -> Dataset:
    """UCI Communities and Crime dataset."""
    if True:  # pylint: disable=using-constant-test
        features = [
            "communityname",
            "fold",
            "population",
            "householdsize",
            "racepctblack",
            "racePctWhite",
            "racePctAsian",
            "racePctHisp",
            "agePct12t21",
            "agePct12t29",
            "agePct16t24",
            "agePct65up",
            "numbUrban",
            "pctUrban",
            "medIncome",
            "pctWWage",
            "pctWFarmSelf",
            "pctWInvInc",
            "pctWSocSec",
            "pctWPubAsst",
            "pctWRetire",
            "medFamInc",
            "perCapInc",
            "whitePerCap",
            "blackPerCap",
            "indianPerCap",
            "AsianPerCap",
            "HispPerCap",
            "NumUnderPov",
            "PctPopUnderPov",
            "PctLess9thGrade",
            "PctNotHSGrad",
            "PctBSorMore",
            "PctUnemployed",
            "PctEmploy",
            "PctEmplManu",
            "PctEmplProfServ",
            "PctOccupManu",
            "PctOccupMgmtProf",
            "MalePctDivorce",
            "MalePctNevMarr",
            "FemalePctDiv",
            "TotalPctDiv",
            "PersPerFam",
            "PctFam2Par",
            "PctKids2Par",
            "PctYoungKids2Par",
            "PctTeen2Par",
            "PctWorkMomYoungKids",
            "PctWorkMom",
            "NumIlleg",
            "PctIlleg",
            "NumImmig",
            "PctImmigRecent",
            "PctImmigRec5",
            "PctImmigRec8",
            "PctImmigRec10",
            "PctRecentImmig",
            "PctRecImmig5",
            "PctRecImmig8",
            "PctRecImmig10",
            "PctSpeakEnglOnly",
            "PctNotSpeakEnglWell",
            "PctLargHouseFam",
            "PctLargHouseOccup",
            "PersPerOccupHous",
            "PersPerOwnOccHous",
            "PersPerRentOccHous",
            "PctPersOwnOccup",
            "PctPersDenseHous",
            "PctHousLess3BR",
            "MedNumBR",
            "HousVacant",
            "PctHousOccup",
            "PctHousOwnOcc",
            "PctVacantBoarded",
            "PctVacMore6Mos",
            "MedYrHousBuilt",
            "PctHousNoPhone",
            "PctWOFullPlumb",
            "OwnOccLowQuart",
            "OwnOccMedVal",
            "OwnOccHiQuart",
            "RentLowQ",
            "RentMedian",
            "RentHighQ",
            "MedRent",
            "MedRentPctHousInc",
            "MedOwnCostPctInc",
            "MedOwnCostPctIncNoMtg",
            "NumInShelters",
            "NumStreet",
            "PctForeignBorn",
            "PctBornSameState",
            "PctSameHouse85",
            "PctSameCity85",
            "PctSameState85",
            "LandArea",
            "PopDens",
            "PctUsePubTrans",
            "LemasPctOfficDrugUn",
            "ViolentCrimesPerPop",
            "state_1",
            "state_2",
            "state_4",
            "state_5",
            "state_6",
            "state_8",
            "state_9",
            "state_10",
            "state_11",
            "state_12",
            "state_13",
            "state_16",
            "state_18",
            "state_19",
            "state_20",
            "state_21",
            "state_22",
            "state_23",
            "state_24",
            "state_25",
            "state_27",
            "state_28",
            "state_29",
            "state_32",
            "state_33",
            "state_34",
            "state_35",
            "state_36",
            "state_37",
            "state_38",
            "state_39",
            "state_40",
            "state_41",
            "state_42",
            "state_44",
            "state_45",
            "state_46",
            "state_47",
            "state_48",
            "state_49",
            "state_50",
            "state_51",
            "state_53",
            "state_54",
            "state_55",
            "state_56",
            ">0.06black",
            "high_crime",
        ]

        continuous_features = [
            "population",
            "householdsize",
            "racepctblack",
            "racePctWhite",
            "racePctAsian",
            "racePctHisp",
            "agePct12t21",
            "agePct12t29",
            "agePct16t24",
            "agePct65up",
            "numbUrban",
            "pctUrban",
            "medIncome",
            "pctWWage",
            "pctWFarmSelf",
            "pctWInvInc",
            "pctWSocSec",
            "pctWPubAsst",
            "pctWRetire",
            "medFamInc",
            "perCapInc",
            "whitePerCap",
            "blackPerCap",
            "indianPerCap",
            "AsianPerCap",
            "HispPerCap",
            "NumUnderPov",
            "PctPopUnderPov",
            "PctLess9thGrade",
            "PctNotHSGrad",
            "PctBSorMore",
            "PctUnemployed",
            "PctEmploy",
            "PctEmplManu",
            "PctEmplProfServ",
            "PctOccupManu",
            "PctOccupMgmtProf",
            "MalePctDivorce",
            "MalePctNevMarr",
            "FemalePctDiv",
            "TotalPctDiv",
            "PersPerFam",
            "PctFam2Par",
            "PctKids2Par",
            "PctYoungKids2Par",
            "PctTeen2Par",
            "PctWorkMomYoungKids",
            "PctWorkMom",
            "NumIlleg",
            "PctIlleg",
            "NumImmig",
            "PctImmigRecent",
            "PctImmigRec5",
            "PctImmigRec8",
            "PctImmigRec10",
            "PctRecentImmig",
            "PctRecImmig5",
            "PctRecImmig8",
            "PctRecImmig10",
            "PctSpeakEnglOnly",
            "PctNotSpeakEnglWell",
            "PctLargHouseFam",
            "PctLargHouseOccup",
            "PersPerOccupHous",
            "PersPerOwnOccHous",
            "PersPerRentOccHous",
            "PctPersOwnOccup",
            "PctPersDenseHous",
            "PctHousLess3BR",
            "MedNumBR",
            "HousVacant",
            "PctHousOccup",
            "PctHousOwnOcc",
            "PctVacantBoarded",
            "PctVacMore6Mos",
            "MedYrHousBuilt",
            "PctHousNoPhone",
            "PctWOFullPlumb",
            "OwnOccLowQuart",
            "OwnOccMedVal",
            "OwnOccHiQuart",
            "RentLowQ",
            "RentMedian",
            "RentHighQ",
            "MedRent",
            "MedRentPctHousInc",
            "MedOwnCostPctInc",
            "MedOwnCostPctIncNoMtg",
            "NumInShelters",
            "NumStreet",
            "PctForeignBorn",
            "PctBornSameState",
            "PctSameHouse85",
            "PctSameCity85",
            "PctSameState85",
            "LandArea",
            "PopDens",
            "PctUsePubTrans",
            "LemasPctOfficDrugUn",
            "ViolentCrimesPerPop",
        ]

        features_to_remove = ["communityname", "fold"]
        features = [feature for feature in features if feature not in features_to_remove]
        if split == "Race-Binary":
            sens_attr_spec = ">0.06black"
            s_prefix = [">0.06", "race", "white", "black", "indian", "Asian", "Hisp", "Other"]
            class_label_spec = "high_crime"
            class_label_prefix = ["high_crime", "Violent"]
        else:
            raise NotImplementedError
    return Dataset(
        name=f"Crime {split}",
        num_samples=1994,
        filename_or_path="crime.csv",
        features=features,
        cont_features=continuous_features,
        s_prefix=s_prefix,
        sens_attr_spec=sens_attr_spec,
        class_label_prefix=class_label_prefix,
        class_label_spec=class_label_spec,
        discrete_only=discrete_only,
    )
