## @ingroup methods-aerodynamics-Supersonic_Zero-Drag
# wave_drag_lift.py
# 
# Created:  Jun 2014, T. Macdonald
# Modified: Jul 2014, T. Macdonald
#           Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import numpy as np
from SUAVE.Analyses import Results

# ----------------------------------------------------------------------
#   Wave Drag Lift
# ----------------------------------------------------------------------

## @ingroup methods-aerodynamics-Supersonic_Zero-Drag
def wave_drag_lift(conditions,configuration,wing):
<<<<<<< HEAD
    """Computes wave drag due to lift

    Assumptions:
    Simplified equations

    Source:
    http://adg.stanford.edu/aa241/drag/ssdragcalc.html

    Inputs:
    conditions.freestream.mach_number        [Unitless]
    conditions.aerodynamics.lift_coefficient [Unitless]
    wing.total_length                        [m]
    wing.areas.reference                     [m^2]

    Outputs:
    wave_drag_lift                           [Unitless]

    Properties Used:
    N/A
    """  
=======
    """ SUAVE.Methods.wave_drag_lift(conditions,configuration,wing)
        computes the wave drag due to lift 
        Based on http://adg.stanford.edu/aa241/drag/ssdragcalc.html
        
        Inputs:
        - SUave wing
        - Sref - wing reference area
        - Mc - mach number
        - CL - coefficient of lift
        - total_length - length of the wing root
        Outputs:
        - CD due to wave drag from the wing
        Assumptions:
        - Supersonic mach numbers
        - Reference area of passed wing is desired for CD
        
    """
>>>>>>> develop

    # Unpack
    freestream = conditions.freestream
    total_length = wing.total_length
    Sref = wing.areas.reference
    
    # Conditions
    Mc  = freestream.mach_number * 1.0

    # Length-wise aspect ratio
    ARL = total_length**2/Sref
    
    # Lift coefficient
    if wing.vertical:
        CL = np.zeros_like(conditions.aerodynamics.lift_coefficient)
    else:
        # get wing specific CL
        CL = conditions.aerodynamics.lift_breakdown.inviscid_wings_lift[wing.tag]
    
    # Computations
    x = np.pi*ARL/4
    beta = np.array([[0.0]] * len(Mc))
    beta[Mc >= 1.05] = np.sqrt(Mc[Mc >= 1.05]**2-1)
    wave_drag_lift = np.array([[0.0]] * len(Mc))
    wave_drag_lift[Mc >= 1.05] = CL[Mc >= 1.05]**2*x/4*(np.sqrt(1+(beta[Mc >= 1.05]/x)**2)-1)
    wave_drag_lift[0:len(Mc[Mc >= 1.05]),0] = wave_drag_lift[Mc >= 1.05]
    
    # Dump data to conditions
    wave_lift_result = Results(
        reference_area             = Sref   , 
        wave_drag_lift_coefficient = wave_drag_lift ,
        length_AR                  = ARL,
    )

    return wave_drag_lift
