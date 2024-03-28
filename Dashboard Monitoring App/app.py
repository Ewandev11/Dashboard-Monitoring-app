from flask import Flask, render_template
import plotly.express as px
import pandas as pd
import random

app = Flask(__name__)

# Generate sample data
random.seed(42)
data = pd.DataFrame({
    'Time': pd.date_range(start='2024-01-01', end='2024-03-28', freq='D'),
    'Value': [random.randint(0, 100) for _ in range(0, 87)]
})


# Route for dashboard page
@app.route('/')
def dashboard():
    # Create plot
    fig = px.line(data, x='Time', y='Value', title='Dashboard Monitoring Application')

    # Convert plot to HTML
    plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    # Render the dashboard template with the plot HTML
    return render_template('dashboard.html', plot_html=plot_html)


if __name__ == '__main__':
    app.run(debug=True)
