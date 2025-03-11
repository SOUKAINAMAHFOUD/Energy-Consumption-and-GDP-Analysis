def specify_regression_model():
    """
    This function specifies the empirical model for energy consumption based on GDP.
    It defines the regression equation and provides a description of each variable.

    Returns:
    str: The regression equation.
    str: The description of the variables involved in the model.
    """
    # Defining the variables
    beta_0 = "β₀"  # Intercept term
    beta_1 = "β₁"  # Slope coefficient
    GDP_i = "GDP_i"  # GDP per capita for country i
    epsilon_i = "ε_i"  # Error term

    # Regression equation
    energy_equation = f"energy_i = {beta_0} + {beta_1} * {GDP_i} + {epsilon_i}"

    # Variable descriptions
    descriptions = """ 
    Where: 
    - energy_i: Energy consumption per capita in country i, 
    - GDP_i: GDP per capita in country i,
    - β₀ (beta_0): Intercept term representing the baseline energy consumption when GDP is zero,
    - β₁ (beta_1): Slope coefficient capturing the marginal effect of GDP on energy consumption,
    - ε_i (epsilon_i): Error term accounting for unobserved factors affecting energy consumption.
    """
    
    return energy_equation, descriptions
