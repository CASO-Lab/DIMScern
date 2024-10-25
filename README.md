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
└── packet_generation.py

3 directory, 7 files
```
```
Usage : python3 main.py -c sop_target.cfg
```
- If you want to run DIMScern on another target, just define the target's name, ip, port, and Called_AE_Title in "sop_target.cfg".
- The SOP Class UIDs in our input "SOP_UID.txt" are a list obtained from the DICOM standards PS3.4, PS3.6.
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
