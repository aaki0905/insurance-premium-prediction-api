from pydantic import BaseModel,Field,computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities

# Create a Pydantic model for the input data validation
### input data : age,weight,height,income_lpa,smoker,city,occupation, : insurance_premium_category
class InsuranceData(BaseModel):
    age: Annotated[int, Field(...,gt=0, lt=120, description="Age of the individual in years")]
    weight: Annotated[float, Field(...,gt=0, description="Weight of the individual in kilograms")]
    height: Annotated[float, Field(...,gt=0, description="Height of the individual in centimeters")]
    income_lpa: Annotated[float, Field(...,gt=0, description="Income in LPA (Lakhs per Annum)")]
    smoker: Annotated[bool, Field(..., description="Whether the individual is a smoker or not")]
    city: Annotated[str, Field(..., description="City of residence")]
    ### occupation list(['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'], dtype=object)
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the individual. Must be one of ['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job']")]

    @field_validator('city')
    @classmethod
    def normalize_city(cls, v: str) -> str:
        return v.strip().title()  # Normalize city names to title case

    @computed_field
    @property
    def bmi(self) -> float:
        """Compute BMI from weight and height."""
        return self.weight / ((self.height / 100) ** 2)

    @computed_field
    @property
    # Feature 3: Lifestyle Risk
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    ####### Feature 2: Age Group
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3