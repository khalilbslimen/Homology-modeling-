from modeller import *

env = Environ()
aln = Alignment(env)
for (pdb, chain) in (('template1', 'A'), ('template2', 'A'), ('template3', 'A'),
                     ('template4', 'A'), ('template5', 'A'), ('template6', 'A')):
    m = Model(env, file=pdb, model_segment=('FIRST:'+chain, 'LAST:'+chain))
    aln.append_model(m, atom_files=pdb, align_codes=pdb+chain)
aln.malign()
aln.malign3d()
aln.compare_structures()
aln.id_table(matrix_file='family.mat')
env.dendrogram(matrix_file='family.mat', cluster_cut=-1.0)
