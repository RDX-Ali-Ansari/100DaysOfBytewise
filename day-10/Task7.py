print("Coefficients:")
for i, coef in enumerate(model.coef_):
    print(f"Feature {i+1}: {coef:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

print("\nInterpretation:")
for i, coef in enumerate(model.coef_):
    print(f"A unit increase in Feature {i+1} is associated with a {coef:.2f} unit change in the target variable, holding all other features constant.")
