""" status checkers
"""
import autoparse.pattern as app
import autoparse.find as apf
import elstruct.par


def has_normal_exit_message(output_string):
    """ does this output string have a normal exit message?
    """
    pattern = app.escape('*** Psi4 exiting successfully.')
    return apf.has_match(pattern, output_string, case=False)


def _has_scf_nonconvergence_error_message(output_string):
    """ does this output string have an SCF non-convergence message?
    """
    pattern = app.escape('PsiException: Could not converge SCF iterations')
    return apf.has_match(pattern, output_string, case=False)


def _has_opt_nonconvergence_error_message(output_string):
    """ does this output string have an optimization non-convergence message?
    """
    pattern = app.escape('PsiException: Could not converge geometry '
                         'optimization')
    return apf.has_match(pattern, output_string, case=False)


ERROR_READER_DCT = {
    elstruct.par.Error.SCF_NOCONV: _has_scf_nonconvergence_error_message,
    elstruct.par.Error.OPT_NOCONV: _has_opt_nonconvergence_error_message,
}


def error_list():
    """ list of errors that be identified from the output file
    """
    return tuple(sorted(ERROR_READER_DCT.keys()))


def has_error_message(error, output_string):
    """ does this output string have an error message?
    """
    assert error in error_list()
    # get the appropriate reader and call it
    error_reader = ERROR_READER_DCT[error]
    return error_reader(output_string)
