from faker import Faker
import pandas as pd
import numpy as np
import random
from datetime import timedelta, datetime

# Initialize Faker to generate fake data
fake = Faker()

# Detailed project types with corresponding skills and realistic budget ranges
tech_info = {
    'Front-end': {
        'HTML': {'complexity': 1, 'duration_factor': 1.0, 'budget_factor': 1.0},
        'CSS': {'complexity': 1, 'duration_factor': 1.0, 'budget_factor': 1.0},
        'JavaScript': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'React': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'Angular': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'Vue.js': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'Svelte': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'TypeScript': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'Bootstrap': {'complexity': 1, 'duration_factor': 1.0, 'budget_factor': 1.0},
        'Tailwind CSS': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'Sass': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'Less': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'Ember.js': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'Backbone.js': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1}
    },
    'Back-end': {
        'Node.js': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'Express.js': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'Python': {'complexity': 2, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'Django': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3},
        'Flask': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'Java': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3},
        'Spring': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3},
        'Ruby': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'Ruby on Rails': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'PHP': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'Laravel': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'ASP.NET': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3},
        'Go': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'Rust': {'complexity': 4, 'duration_factor': 1.4, 'budget_factor': 1.4},
        'Scala': {'complexity': 4, 'duration_factor': 1.4, 'budget_factor': 1.4},
        'Elixir': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3},
        'FastAPI': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'ASP.NET Core': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3}
    },
    'Database': {
        'MySQL': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'PostgreSQL': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'MongoDB': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'Oracle': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3},
        'SQL Server': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'Redis': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'SQLite': {'complexity': 1, 'duration_factor': 1.0, 'budget_factor': 1.0},
        'Cassandra': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'MariaDB': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'Neo4j': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'Couchbase': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1}
    },
    'DevOps': {
        'Docker': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'Kubernetes': {'complexity': 4, 'duration_factor': 1.4, 'budget_factor': 1.4},
        'Ansible': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'Terraform': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3},
        'Jenkins': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'GitHub Actions': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'GitLab CI/CD': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'CircleCI': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'AWS CloudFormation': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3},
        'Azure DevOps': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3}
    },
    'Security': {
        'OAuth': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'JWT': {'complexity': 2, 'duration_factor': 1.2, 'budget_factor': 1.1},
        'OpenSSL': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3},
        'Penetration Testing Tools': {'complexity': 3, 'duration_factor': 1.4, 'budget_factor': 1.4},
        'OWASP': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3},
        'ZAP': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'Nmap': {'complexity': 2, 'duration_factor': 1.2, 'budget_factor': 1.1}
    },

    'Mobile Development': {
        'Android': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3},
        'iOS': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3},
        'React Native': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'Flutter': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.2},
        'Xamarin': {'complexity': 3, 'duration_factor': 1.2, 'budget_factor': 1.1}
    },
    'AI and Machine Learning': {
        'TensorFlow': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'PyTorch': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'Scikit-Learn': {'complexity': 3, 'duration_factor': 1.4, 'budget_factor': 1.3},
        'Keras': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'NLTK': {'complexity': 3, 'duration_factor': 1.4, 'budget_factor': 1.3}
    },
    'Big Data': {
        'Hadoop': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.4},
        'Spark': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'Kafka': {'complexity': 4, 'duration_factor': 1.4, 'budget_factor': 1.3},
        'Data Lakes': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5}
    },
    'Cloud Computing': {
        'AWS': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'Azure': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'Google Cloud': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'IBM Cloud': {'complexity': 3, 'duration_factor': 1.4, 'budget_factor': 1.4}
    },
    'Networking': {
        'SDN (Software Defined Networking)': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.4},
        'Network Automation': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.4},
        '5G Technology': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5}
    },
    'Software Testing': {
        'Selenium': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'Cucumber': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'Appium': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'TestNG': {'complexity': 2, 'duration_factor': 1.2, 'budget_factor': 1.1}
    },
    'Blockchain': {
        'Ethereum': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'Solidity': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'Hyperledger': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'Chaincode': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5}
    },
    'IoT (Internet of Things)': {
        'MQTT': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'CoAP': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'IoT Security': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'IoT Platforms': {'complexity': 3, 'duration_factor': 1.4, 'budget_factor': 1.3}
    },
    'User Interface (UI) Design': {
        'Figma': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'Sketch': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1},
        'Adobe XD': {'complexity': 2, 'duration_factor': 1.1, 'budget_factor': 1.1}
    },
    'User Experience (UX) Design': {
        'Usability Testing': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'User Journey Mapping': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'Information Architecture': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2}
    },
    'Artificial Intelligence': {
        'Natural Language Processing (NLP)': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'Computer Vision': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'AI Ethics & Governance': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2}
    },
    'Quantum Computing': {
        'Quantum Algorithms': {'complexity': 5, 'duration_factor': 1.6, 'budget_factor': 1.6},
        'Quantum Cryptography': {'complexity': 5, 'duration_factor': 1.6, 'budget_factor': 1.6}
    },
    'Data Management and Analytics': {
        'Data Governance': {'complexity': 4, 'duration_factor': 1.4, 'budget_factor': 1.3},
        'Master Data Management': {'complexity': 4, 'duration_factor': 1.4, 'budget_factor': 1.3}
    },
    'Digital Transformation and Change Management': {
        'Digital Strategy Development': {'complexity': 4, 'duration_factor': 1.4, 'budget_factor': 1.4},
        'Change Management': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2}
    },
    'Cybersecurity (Specialized)': {
        'Intrusion Detection Systems (IDS)': {'complexity': 4, 'duration_factor': 1.4, 'budget_factor': 1.3},
        'Security Orchestration, Automation, and Response (SOAR)': {'complexity': 4, 'duration_factor': 1.4, 'budget_factor': 1.4}
    },
    'Virtual and Augmented Reality': {
        'Unity for VR/AR': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'ARKit for iOS': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'ARCore for Android': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5}
    },
    'Legal Tech': {
        'Document Automation': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'Case Management Software': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3},
        'Compliance Management': {'complexity': 3, 'duration_factor': 1.4, 'budget_factor': 1.3},
        'E-Discovery Software': {'complexity': 3, 'duration_factor': 1.4, 'budget_factor': 1.3}
    },
    'Educational Technology (EdTech)': {
        'Learning Management Systems (LMS)': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'Virtual Classrooms': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.2},
        'MOOC Platforms': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.4},
        'Adaptive Learning Platforms': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5}
    },
    'FinTech': {
        'Blockchain for Finance': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'Robo-Advisors': {'complexity': 4, 'duration_factor': 1.5, 'budget_factor': 1.5},
        'High-Frequency Trading Systems': {'complexity': 5, 'duration_factor': 1.6, 'budget_factor': 1.6},
        'Payment Gateway Integration': {'complexity': 3, 'duration_factor': 1.3, 'budget_factor': 1.3}
    },

}

hourly_rate =12.5
def assess_risks(technologies):
    high_risk_threshold = 4
    medium_risk_threshold = 3
    if any(tech_info[cat][tech]['complexity'] >= high_risk_threshold for cat, tech in technologies):
        return 'High', 1.2  # Increase duration and budget by 20% for high risk
    elif any(tech_info[cat][tech]['complexity'] >= medium_risk_threshold for cat, tech in technologies):
        return 'Medium', 1.1  # Increase duration and budget by 10% for medium risk
    else:
        return 'Low', 1.0  # No change for low risk

def calculate_project_params(technologies):
    total_complexity = sum(tech_info[cat][tech]['complexity'] for cat, tech in technologies)
    total_duration = sum(tech_info[cat][tech]['duration_factor'] for cat, tech in technologies)
    total_budget = sum(tech_info[cat][tech]['budget_factor'] for cat, tech in technologies)
    return total_complexity, total_duration, total_budget

def weighted_choice(choices):
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w
    return None

def generate_projects(num_projects, max_categories=5):
    projects = []
    for _ in range(num_projects):
        selected_techs = []
        categories = list(tech_info.keys())
        weights = [1.0 for _ in categories]

        num_categories = random.randint(1, max_categories)
        for _ in range(num_categories):
            category = weighted_choice(list(zip(categories, weights)))
            if not category:
                continue
            tech = random.choice(list(tech_info[category].keys()))
            selected_techs.append((category, tech))
            weights[categories.index(category)] *= 0.5

        if not selected_techs:
            continue

        complexity, duration_factor, budget_factor = calculate_project_params(selected_techs)
        risk_level, risk_multiplier = assess_risks(selected_techs)
        base_duration = random.randint(30, 360)  # Duration in days
        base_budget = random.randint(2000, 1000000)

        # Calculate additional budget based on estimated hours
        estimated_hours = base_duration * 8  # Assuming 8 working hours per day
        additional_budget = estimated_hours * hourly_rate

        adjusted_duration = base_duration * duration_factor * risk_multiplier
        adjusted_budget = (base_budget * budget_factor * risk_multiplier) + additional_budget
        
        project = {
            'Technologies': ', '.join([f"{cat}: {tech}" for cat, tech in selected_techs]),
            'Complexity': complexity,
            'Risk Level': risk_level,
            'Duration (days)': round(adjusted_duration),
            'Budget (TND)': round(adjusted_budget)
        }
        projects.append(project)
    
    return pd.DataFrame(projects)

num_projects = 3000
project_data = generate_projects(num_projects)
print(project_data)
project_data.to_csv('generated_project_data_with_hours.csv', index=False)

max_budget = project_data['Budget (TND)'].max()
min_budget = project_data['Budget (TND)'].min()

print(f"Maximum Budget (TND): {max_budget}")
print(f"Minimum Budget (TND): {min_budget}")

