# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

# Example of expected output line (do not remove):


def calculate_revenue(A, B):
    revenue = []
    for i in range(len(A)):

        r = A[i]*B[i]
        revenue.append(r)
    return revenue

revenue = calculate_revenue(prices, quantities_sold)

revenue_per_product = list(zip(products, revenue))

def formatted_output(A):
    A = sorted(A)
    return A

revenue_per_product = formatted_output(revenue_per_product)

for i in range(len(revenue_per_product)):
    print(f"{revenue_per_product[i][0]} has total revenue of ${revenue_per_product[i][1]}")
    

#print(f"{revenue[0]} has total revenue of ${revenue[1]}")

