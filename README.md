## DIMScern 
- - -
## Directory structure of the DIMScern 
```
.
├── Inputs
│   └── SOP_UID.txt
├── Logs                (If you didn't run the main script, it doesn't exist.)
│   └── DIMScern_log.txt
├── Outputs             (If you didn't run the main script, it doesn't exist.)
│   └── [Target]_sop_uid_accept.txt
├── README.md
├── discerning.py
├── main.py
├── packet_generation.py
└── sop_target.cfg

3 directory, 8 files
```
```
Usage : python3 main.py -c sop_target.cfg
```
- If you want to run DIMScern on another target, just define the target's name, ip, port, and Called_AE_Title in "sop_target.cfg".
- The SOP Class UIDs in our input "SOP_UID.txt" are a list obtained from the DICOM standards [PS 3.4](https://dicom.nema.org/medical/dicom/2024c/output/pdf/part04.pdf), [PS 3.6](https://dicom.nema.org/medical/dicom/2024c/output/pdf/part06.pdf).
- - -
## \<Targets download URL\>

+ DCMTK : <https://dicom.offis.de/en/dcmtk/dcmtk-tools/>

+ DCMTK Source Code  : <https://github.com/DCMTK/dcmtk>

+ dcm4che  : <https://web.dcm4che.org/>

+ dcm4che Source Code  : <https://github.com/dcm4che/dcm4che>

+ merative  : <https://www.merative.com/merge-imaging/dicom-toolkit>

+ leadtools  : <https://www.leadtools.com/sdk/medical/dicom>

+ pynetdicom  : <https://pydicom.github.io/pynetdicom/stable/>

- - -

+ Orthanc  : <https://www.orthanc-server.com/>

+ SonicDicom  : <https://sonicdicom.com/>

+ Sante Pacs  : <https://santesoft.com/win/sante-pacs-server/sante-pacs-server.html>

+ Dicoogle  : <https://dicoogle.com/>

+ ConQuest  : <https://www.natura-ingenium.nl/dicom.html>

- - - 

## Citing our [paper](https://www.mdpi.com/1424-8220/24/23/7470)
```bibtex
@article{kim2024dimscern,
title={DIMScern: A Framework for Discerning DIMSE Services on Remote Medical Devices},
author={Kim, Gunhee and Kim, Dohyun and Seo, Jeonghun and Lee, Seyoung and Song, Wonjun},
journal={Sensors (Basel, Switzerland)},
volume={24},
number={23},
pages={7470},
year={2024}
}
```

