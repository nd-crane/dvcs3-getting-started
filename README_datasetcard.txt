---
language:
- en
pretty_name: titanic data
size_categories:
- 1K<n<10K
---
# Dataset Card for Titanic Data

Training and testing data for Titanic passengers' survival.

## Dataset Details

### Dataset Description

Train: 
- Dimensions --> 891x12
- Column names --> "PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", and "Embarked"

Test:
- Dimensions --> 418x11
- Column names --> "PassengerId", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", and "Embarked"

### Dataset Sources

Kaggle Titanic dataset
https://www.kaggle.com/competitions/titanic

## Uses

Raw datasets being used in introduction to DVC and Amazon's S3 buckets.

## Dataset Structure

# Column definitions:
- "PassengerId" --> key for each passenger (int64)
- "Survived" --> binary variable indicating survival (int64)
- "Pclass" --> first, second, or third class (int64)
- "Name" --> passenger name; maiden name in parentheses for married women (object)
- "Sex" --> male or female (object)
- "Age" --> passenger age (float64)
- "SibSp" --> unknown meaning (int64)
- "Parch" --> unknown meaning (int64)
- "Ticket" --> ticket identifier (object)
- "Fare" --> float variable (float64)
- "Cabin" --> cabin identifier (object)
- "Embarked" --> C, Q, or S (object)

Categorical columns: "Name", "Sex", "Ticket", "Cabin", "Embarked"

Continuous columns: "PassengerId", "Pclass", "SibSp", "Parch", "Age", "Fare"

# Quick Facts:
Train:
- PassengerID, Survived, Pclass, Name, Sex, SibSp, Parch, Ticket, and Fare have no NA values
- Age not documented for 177 passengers (19.8653% NA)
- Cabin not documented for 687 passengers (77.1044% NA)
- Embarked not documented for 2 passengers (0.2245% NA)

Test:
- PassengerID, Pclass, Name, Sex, SibSp, Parch, Ticket, and Embarked have no NA values
- Age not documented for 86 passengers (20.5742% NA)
- Fare not documented for 1 passenger (0.2392% NA)
- Cabin not documented for 387 passengers (78.2297% NA)

# Summary Statistics:
Train:
![image/png](https://cdn-uploads.huggingface.co/production/uploads/65119c3f02dbe541c92539d4/AJLNDr1mDXEiTLn_JAH0h.png)

Test:
![image/png](https://cdn-uploads.huggingface.co/production/uploads/65119c3f02dbe541c92539d4/PEnS25wxm6ymjgsI3QKtv.png)

## Dataset Card Author

Maria Murphy