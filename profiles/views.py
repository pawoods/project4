from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, WishList
from .forms import UserProfileForm
from products.models import Product


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    wish_list = profile.wishlist.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'wish_list': wish_list,
        'on_profile': True,
    }

    return render(request, template, context)


@login_required
def wish_list(request, product_id):
    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    try:
        wish_list = WishList.objects.get(product=product, profile=profile)
    except WishList.DoesNotExist:
        wish_list = None    

    if wish_list:
        wish_list.delete()
        messages.info(request, 'Removed from your Wish List')
    else:
        wish_list_instance = WishList.objects.create(
            profile=profile,
            product=product,
        )
        messages.info(request, 'Added to your Wish List')
    return redirect(reverse('products'))
        