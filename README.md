introduction 
------------

We've opted to focus on α-amylase (AA) sourced from Alteromonas haloplanktis, a Gram-negative bacterium found solely in the frigid waters of the Antarctic, thriving at -20°C. Although the protein's structure has been previously elucidated through X-ray crystallography (PDB code: 1AQM), we'll utilize it specifically for this tutorial.
This pipeline is built generations of homology-models of protein from a template to a model 
The modeling method is based on the Basic Modeling tutorial of Modeller, and the template selection rule is just to select the structure with the highest sequence identity to the target sequence.
Installation
------------
'''
python : 3.12
Modeller : 10.5
pymol : 3
'''
first i set up my file with the 6 template i choosen from an BLAST and choose 6 of the must identical pourcentage with my trguet sequence and placed in the bin file of modeller directory  
Your workspace should look like this:
'''
.
├── template1.pdb
├── template2.pdb
├── template3.pdb
├── template4.pdb
├── template5.pdb
├── template6.pdb
├── align2d.py
├── compare.py
├── evaluate_model.py
├── model_single.py
└── P29957.ali
'''
start automated modelling with the 'compare.py' to generat the 'compare.log' file with the comparaison 
'''
Weighted pair-group average clustering based on a distance matrix:


                                                               .--- 1hx0A @1.4     0.0000
                                                               |
                                                               .--- 1ua3A @2.0     0.5000
                                                               |
                                                              .---- 1vahA @2.4     1.0000
                                                              |
                                                             .----- 3l2lA @2.1     1.8750
                                                             |
        .---------------------------------------------------------- 1pifA @2.3    44.5625
        |
      .------------------------------------------------------------ 8orpA @2.0

      +----+----+----+----+----+----+----+----+----+----+----+----+
    46.3450   38.3237   30.3025   22.2812   14.2600    6.2387   -1.7825
         42.3344   34.3131   26.2919   18.2706   10.2494    2.2281

'''
i did the alignement with the 'align2d.py' file 
After establishing a target-template alignment, MODELLER automatically generates a 3D model of the target using its AutoModel class, streamlining the process without manual intervention.
following script will generate five similar models based on the template and the alignment in file it will generate5 models
execute the the 'evaluate_model.py'
'''shell
29/03/2024  00:56           408 505 P29957.B99990002.pdb
29/03/2024  00:57           408 505 P29957.B99990003.pdb
29/03/2024  00:58           408 505 P29957.B99990004.pdb
29/03/2024  00:59           408 505 P29957.B99990005.pdb
'''
 The most important output file is "model-single.log", it's help to choose one of the models based on the best DOPE score
'''
>> Summary of successfully produced models:
Filename                          molpdf     DOPE score    GA341 score
----------------------------------------------------------------------
P29957.B99990001.pdb          5467.51807   -57145.13281        1.00000
P29957.B99990002.pdb          5804.31494   -56630.82422        0.98957
P29957.B99990003.pdb          5459.31641   -56651.69531        0.88546
P29957.B99990004.pdb          5588.89746   -57296.24219        1.00000
P29957.B99990005.pdb          5761.77441   -57081.95703        0.99589
'''
Model evaluation
----------------
now i evalute my model with the 'evaluate_model.py' and creat a plot with GNUPLOT using the 'template.profile' file 
Launch a new PyMol session and load the model, crystal, and template structures, then execute the following commands.
'''shell
select reference, 1AQM and name CA
select mob_model, model and name CA
align mob_model, reference

'''
the output is the calculation of  RMSD
'''
RMSD =    0.578 (322 to 322 atoms)
''' 
