from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm , MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', views.CarView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.CarDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('aboutus/', views.about_us, name='aboutus'),
    path('company/',views.company, name='company'),
    path('company/<slug:data>', views.company, name='company_data'),
    
    path('companysedan/',views.companysedan, name='companysedan'),
    path('companysedan/<slug:data>', views.companysedan, name='companysedan_data'),
    
    path('companysuv/',views.companysuv, name='companysuv'),
    path('companysuv/<slug:data>', views.companysuv, name='companysuv_data'),
    
    path('companymuv/',views.companymuv, name='companymuv'),
    path('companymuv/<slug:data>', views.companymuv, name='companymuv_data'),
    
    
    # AUTHENTICATION
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm , success_url='/passwordchangedone/'), name='passwordchange'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    # AUTHENTICATION



    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)