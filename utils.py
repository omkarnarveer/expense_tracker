import pandas as pd
from models import Expense, Budget

def generate_insights(user_id):
    data = Expense.query.filter_by(user_id=user_id).all()
    df = pd.DataFrame([{
        'amount': e.amount,
        'category': e.category,
        'date': e.date
    } for e in data])
    return df.groupby('category')['amount'].sum().to_dict()

def check_budget_alerts(user_id):
    alerts = []
    budgets = Budget.query.filter_by(user_id=user_id).all()
    for b in budgets:
        total = sum(e.amount for e in Expense.query.filter_by(user_id=user_id, category=b.category).all())
        if total > b.limit:
            alerts.append(f"⚠️ You exceeded your budget for {b.category}!")
    return alerts