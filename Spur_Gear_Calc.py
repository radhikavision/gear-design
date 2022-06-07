#!/usr/bin/env python
# coding: utf-8

# ## Gear Design Equations and Formula

# ## Spur Gear
# A spur gear is one of the simplest and most common types of cylindrical gears. Spur gears have straight teeth that run parallel to the shaft.
# These gears are easy to manufacture and can be used in a variety of applications. These applications include speed increase or reduction, torque multiplication, 
# and enhancing accuracy for positioning systems.
# 
# In this blog, we are going to define spur gear terminology and provide formulas for determining the values of these terms.

# ## Spur Gears – Terms, Definitions, and Calculations

# ## # The following terms are related to spur gears:

# In[ ]:




# Pitch diameter: Diameter of the pitch circle.

# Diametral pitch: The number of teeth per inch of pitch diameter.

# Addendum: The height of the tooth above the pitch circle.

# dedendum: Depth of the tooth between the pitch circle and the minor diameter.

# Clearance (Backlash) : The clearance between two mating teeth of separate gears.


#Circular pitch: Measurement of the pitch circle arc length from one point on a tooth to the same point on the adjacent tooth.

#Circular thickness: The thickness of the tooth at the pitch circle.

#Clearance: The space between one gears minor diameter and the mating gears major diameter.

#Module: Teeth per millimeter of pitch diameter.

#Outside diameter: The major diameter of the gear.

#Pitch circle: The circle, the radius of which is equal to the distance from the center of the gear to the pitch point. This is where the gear’s speed is measured.


# #### A 22-tooth gear has AGMA standard full-depth involute teeth with diametral pitch of 4. 
# Calculate the pitch diameter, circular pitch, addendum, dedendum, tooth thickness, and clearance.
# 
# Given : 
# tooth  = 22
# Diametral pitch  dp = 4 

# In[203]:


import math

# Pitch diameter d = N//pd

# Circular pitch pc = pi//pd

# Addendum  a = 1000//pd

# Dedendum b = 1.2500//pd

# Clearance c = 0.2500//pd


# In[204]:


def pitch_diameter(Tooth_number, Diametral_pitch):
    
    """
    To calculate the pitch diameter
    Enter the diametral pitch
    """
    return Tooth_number//Diametral_pitch


# In[205]:


pitch_diameter(22, 4)


# In[206]:


# Circular pitch

def Circular_pitch(Diametral_pitch):
    """
    To calculate the Circular pitch
    Enter the diametral pitch
    """
    return math.pi//Diametral_pitch


# In[207]:


Circular_pitch(4)


# In[208]:


# Addendum

def Addendum(pitch_diameter):
    """
    To calculate the pitch diameter
    Enter the diametral pitch
    """
    
    return 1000//pitch_diameter


# In[209]:


Addendum(4)


# In[210]:


# dedendum

def dedendum(pitch_diameter):
    """
    To calculate dedendum
    Enter the pitch diameter
    """
    return 250//pitch_diameter


# In[211]:


dedendum(4)


# In[212]:


# Tooth thickness

def Tooth_thickness(Circular_pitch):
    """
    To calculate Tooth thickness
    Enter the Circular pitch
    """
    return 0.5*Circular_pitch


# In[213]:


Tooth_thickness(0.78539)


# In[214]:


# Clearance

def Clearance(pitch_diameter):
    """
    To calculate Clearance
    Enter the pitch diameter
    """

    return 0.2500//pitch_diameter


# In[215]:


Clearance(4)


# In[ ]:




