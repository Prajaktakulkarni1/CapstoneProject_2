def summarize_by_category(expenses):
    summary = {}

    for expense in expenses:
        if expense.category not in summary:
            summary[expense.category] = 0
        summary[expense.category] += expense.amount

    return summary
