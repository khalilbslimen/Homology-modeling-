from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='1hx0', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1hx0', atom_files='1hx0.pdb')
aln.append(file='P29957.ali', align_codes='P29957')
aln.align2d(max_gap_length=50)
aln.write(file='P29957-1hx0.ali', alignment_format='PIR')
aln.write(file='P29957-1hx0.pap', alignment_format='PAP')