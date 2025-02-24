## 0. machine options block
%%mem=${memory}GB
${machine_options}
## 1. theoretical method block
% if reference:
#P ${reference} ${method}/${basis}
% else:
#P ${method}/${basis}
% endif
% if reference != 'rohf' and method != 'rohf':
# SCF=(xqc)
% endif
% if scf_options != '':
# SCF=(${scf_options})
% endif
% if scf_guess_options != '':
# Guess=(${scf_guess_options})
% endif
## 2. job options block (when we get to it)
% if job_key == 'optimization':
# POpt=(${job_options})
% elif job_key == 'gradient':
# Force=(${job_options})
## ^ ensure the the hessian is always printed
% elif job_key == 'hessian':
# Freq=(${job_options})
# IOp(7/33=1)
% elif job_key == 'vpt2':
# Freq=(ANHARM,VIBROT${job_options})
% elif job_key == 'irc':
# IRC=(${job_options})
# IOp(7/33=1)
% endif
% if gen_lines != '':
${gen_lines}
% endif
## 3. molecule block
% if mol_options != '':
# ${mol_options}
% endif

comment: ${comment}

${charge} ${mult}
${geom}
  Variables:
% if zmat_var_vals != '':
${zmat_var_vals}
% endif
% if zmat_const_vals != '':
  Constants:
${zmat_const_vals}
% endif

