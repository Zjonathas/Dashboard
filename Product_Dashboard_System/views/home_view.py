from django.shortcuts import render
from Product_Dashboard_System.models import Product, Order, ItemOrder


def calculate_qunatity_in_percentage(quantity, total_itens):
    value = f'{((quantity / total_itens) * 100):.2f}'
    return float(value)


def home(request):
    products = Product.objects.all().order_by("-price")
    orders = Order.objects.all()
    item_orders = ItemOrder.objects.all()

    total_price = 0
    total_itens = 0
    percentage_itens = []

    for item_order in item_orders:
        total_price = item_order.product.price * item_order.quantity
        total_itens += item_order.quantity

    for item_order in item_orders:
        percentage_itens.append(
                (calculate_qunatity_in_percentage
                    (
                        item_order.quantity,
                        total_itens

                    ),
                    item_order.quantity,
                    item_order.product.name))
    context = {
                   "products": products,
                   "orders": orders,
                   "item_orders": item_orders,
                   "total_price": total_price,
                   "total_itens": total_itens,
                   "percentage_itens": percentage_itens
                }
    print(percentage_itens)
    return render(request,
                  "Product_Dashboard_System/pages/home.html",
                  context=context
                  )
