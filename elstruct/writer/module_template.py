""" empty functions defining the function signatures for each program module
"""


def energy(geom, charge, mult, method, basis,
           # molecule options
           mol_options=(),
           # machine options
           memory=1, comment='', machine_options=(),
           # theory options
           orb_restricted=None,
           scf_options=(), casscf_options=(), corr_options=(),
           # generic options
           gen_lines=()):
    """ _ """

    raise NotImplementedError(
        geom, charge, mult, method, basis,
        mol_options,
        memory, comment, machine_options,
        scf_options, casscf_options, corr_options,
        gen_lines
    )


def gradient(geom, charge, mult, method, basis,
             # molecule options
             mol_options=(),
             # machine options
             memory=1, comment='', machine_options=(),
             # theory options
             orb_restricted=None,
             scf_options=(), casscf_options=(), corr_options=(),
             # generic options
             gen_lines=(),
             # job options
             job_options=()):
    """ _ """

    raise NotImplementedError(
        geom, charge, mult, method, basis,
        mol_options,
        memory, comment, machine_options,
        scf_options, casscf_options, corr_options,
        gen_lines,
        job_options,
    )


def hessian(geom, charge, mult, method, basis,
            # molecule options
            mol_options=(),
            # machine options
            memory=1, comment='', machine_options=(),
            # theory options
            orb_restricted=None,
            scf_options=(), casscf_options=(), corr_options=(),
            # generic options
            gen_lines=(),
            # job options
            job_options=()):
    """ _ """

    raise NotImplementedError(
        geom, charge, mult, method, basis,
        mol_options,
        memory, comment, machine_options,
        scf_options, casscf_options, corr_options,
        gen_lines,
        job_options,
    )


def vpt2(geom, charge, mult, method, basis,
         # molecule options
         mol_options=(),
         # machine options
         memory=1, comment='', machine_options=(),
         # theory options
         orb_restricted=None,
         scf_options=(), casscf_options=(), corr_options=(),
         # generic options
         gen_lines=(),
         # job options
         job_options=()):
    """ _ """

    raise NotImplementedError(
        geom, charge, mult, method, basis,
        mol_options,
        memory, comment, machine_options,
        scf_options, casscf_options, corr_options,
        gen_lines,
        job_options,
    )


def irc(geom, charge, mult, method, basis,
        # molecule options
        mol_options=(),
        # machine options
        memory=1, comment='', machine_options=(),
        # theory options
        orb_restricted=None,
        scf_options=(), casscf_options=(), corr_options=(),
        # generic options
        gen_lines=(),
        # job options
        job_options=(), frozen_coordinates=(), irc_direction=None):
    """ _ """

    raise NotImplementedError(
        geom, charge, mult, method, basis,
        mol_options,
        memory, comment, machine_options,
        scf_options, casscf_options, corr_options,
        gen_lines,
        job_options, frozen_coordinates, irc_direction
    )


def optimization(geom, charge, mult, method, basis,
                 # molecule options
                 mol_options=(),
                 # machine options
                 memory=1, comment='', machine_options=(),
                 # theory options
                 orb_restricted=None,
                 scf_options=(), casscf_options=(), corr_options=(),
                 # generic options
                 gen_lines=(),
                 # job options
                 job_options=(), frozen_coordinates=(), saddle=False):
    """ _ """

    raise NotImplementedError(
        geom, charge, mult, method, basis,
        mol_options,
        memory, comment, machine_options,
        scf_options, casscf_options, corr_options,
        gen_lines,
        job_options, frozen_coordinates, saddle
    )
