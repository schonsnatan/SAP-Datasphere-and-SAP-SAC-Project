def transform(data):

    # Handle missing values
    data['Quantity'] = data['Quantity'].fillna(0)
    data['UnitPrice'] = data['UnitPrice'].fillna(0.0)
    data['Discount'] = data['Discount'].fillna(0.0)
    data['ShippingCost'] = data['ShippingCost'].fillna(0.0)
    data['OrderPriority'] = data['OrderPriority'].fillna('Medium')  # Default priority

    # Calculate Total Revenue without considering the discount
    data['TotalRevenue'] = data['Quantity'] * data['UnitPrice']

    # Calculate Profit, considering discounts and shipping costs
    data['Profit'] = data['TotalRevenue'] * (1 - data['Discount']) - data['ShippingCost']

    # The actual discount value applied
    data['DiscountAmount'] = data['TotalRevenue'] * data['Discount']

    # Calculate Shipping Cost per Unit
    # To avoid division errors, ensure Quantity > 0
    data['ShippingCostPerUnit'] = data['ShippingCost'] / data['Quantity']
    data['ShippingCostPerUnit'] = data['ShippingCostPerUnit'].replace([float('inf'), -float('inf')], 0)  # Handle division by 0

    return data