from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for expenses
expenses = []

@app.route('/')
def index():
    total_expense = sum(exp['amount'] for exp in expenses)
    return render_template('index.html', expenses=expenses, total=total_expense)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amount = float(request.form.get('amount'))
        category = request.form.get('category')
        description = request.form.get('description')
        date = request.form.get('date')

        expense = {
            'id': len(expenses) + 1,
            'amount': amount,
            'category': category,
            'description': description,
            'date': date
        }
        expenses.append(expense)
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/delete/<int:expense_id>')
def delete_expense(expense_id):
    global expenses
    expenses = [exp for exp in expenses if exp['id'] != expense_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
