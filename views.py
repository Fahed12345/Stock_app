from django.shortcuts import render
import yfinance as yf
import plotly.graph_objs as go

def stock_form(request):
    if request.method == 'POST':
        ticker = request.POST.get('ticker')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Fetch stock data using yfinance
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)

        # Extract dates and prices from fetched data
        dates = data.index
        open_prices = data['Open'].tolist()
        close_prices = data['Close'].tolist()

        # Plotting chart using Plotly
        trace1 = go.Scatter(x=dates, y=open_prices, mode='lines', name='Open Price')
        trace2 = go.Scatter(x=dates, y=close_prices, mode='lines', name='Close Price')

        layout = go.Layout(
            title='Stock Prices',
            xaxis=dict(title='Date'),
            yaxis=dict(title='Price')
        )

        fig = go.Figure(data=[trace1, trace2], layout=layout)
        chart = fig.to_html(full_html=False)

        # Convert dates and prices to lists of tuples for rendering in the template
        data_rows = list(zip(dates, open_prices, close_prices))

        return render(request, 'stockapp/stock_result.html', {'data_rows': data_rows, 'chart': chart})

    return render(request, 'stockapp/form.html')
