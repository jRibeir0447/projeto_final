from django.urls import path, include
from projeto_final import urls
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    path('profile/chats', views.chat_list_view, name='chatsList'),
    path('profile/propertiesManagement/listingEditing/<int:property_id>/<int:main_listing_id>/removeImage/<int:image_id>', views.remove_image_view, name='removeImage'),
    path('profile/propertiesManagement/listingEditing/deleteListing/<int:property_id>/<int:main_listing_id>', views.delete_listing_view, name='deleteListing'),
    path('profile/propertiesManagement/listingEditing/createListing/<int:property_id>', views.create_listing_view, name='createListing'),
    path('profile/propertiesManagement/listingEditing/<int:property_id>/<int:main_listing_id>', views.listing_editing_view, name='listingEditing'),
    path('profile/propertiesManagement/listingEditing/<int:property_id>', views.listings_management_view, name='listingsManagement'),
    path('profile/propertiesManagement/propertyEditing/<int:property_id>', views.property_editing_view, name='propertyEditing'),
    path('profile/propertiesManagement/bedroomsEditing/<int:property_id>', views.bedrooms_editing_view, name='bedroomsEditing'),  
    path('profile/propertiesManagement/bathroomsEditing/<int:property_id>', views.bathrooms_editing_view, name='bathroomsEditing'),
    path('profile/propertiesManagement/kitchensEditing/<int:property_id>', views.kitchens_editing_view, name='kitchensEditing'),
    path('profile/propertiesManagement/livingroomsEditing/<int:property_id>', views.livingrooms_editing_view, name='livingroomsEditing'),
    path('profile/propertiesManagement', views.properties_management_view, name='propertiesManagement'),
    path('addProperty', views.introduce_property_view, name='addProperty'),
    path('addProperty/bedroom/', views.introduce_property_view, name='addBedroom'),
    path('addProperty/bathroom/', views.introduce_property_view, name='addBathroom'),
    path('addProperty/kitchen/', views.introduce_property_view, name='addKitchen'),
    path('addProperty/livingroom/', views.introduce_property_view, name='addLivingroom'),
    path('addProperty/listing/', views.introduce_property_view, name='addListing'),
    #path('login', views.login_view, name='login_view'),
    #path('logout', views.logout_view, name='logout_view'),
    #path('register', views.register_view, name='register_view'),
    path('profile', views.profile, name = 'profile'),
    path('emailBody', views.emailBody, name = 'emailBody'),
    path('search', views.search, name='search'),
    path('', views.index, name='index'),
    path('notificationsTenant', views.notificationsTenant, name='notificationsTenant'),
    path('notificationsLandlord', views.notificationsLandlord, name='notificationsLandlord'),
    path('listing/application', views.create_request, name='create_request'),
    path('listing/<int:listing_id>', views.listing, name='listing'),
    path('notificationsLandlord/requestAccepted/<int:request_id>', views.accept_request, name='accept_request'),
    path('notificationsLandlord/requestDenied/<int:request_id>', views.deny_request, name='deny_request'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('login/confirmed', views.deletePopUp, name='deletePopUp'),
    path('profile/renewAgreement', views.renewAgreement, name='renewAgreement'),
    path('landLord', views.landlord, name='landlord'),
    path('tenant', views.tenant, name='tenant'),
    path('profile/manageAgreements', views.manage_agreements_view, name='manage_agreements_view'),
    path('profile/manageAgreementsTenant', views.manageAgreementsTenant, name='manageAgreementsTenant'),
    path('invoice', views.get_invoice_pdf, name='get_invoice_pdf'),
    path('sendInvoice', views.send_invoice, name='send_invoice'),
    path('sendPaymentWarning', views.send_payment_warning, name='send_payment_warning'),
    path('invoicesLandlord', views.invoicesLandlord, name='invoicesLandlord'),
    path('invoicesTenant', views.invoicesTenant, name='invoicesTenant'),
    path('profile/agreementDeleted', views.deleteAgreement, name='deleteAgreement'),
    path('profile/accountDeleted', views.delete_account, name='delete_account'),
    path('listing/requestPop', views.requestPop, name='requestPop'),
    path('notificationsLandlord/read/<int:id_req>', views.checkReadLandlord, name='checkReadLandlord'),
    path('notificationsTenant/read/<int:id_req>', views.checkReadTenant, name='checkReadTenant'),
    path('notificationsLandlord/readRef/<int:id_ref>', views.checkReadLandlordRef, name='checkReadLandlordRef'),
    path('notificationsLandlord/readInv/<int:id_inv>', views.checkReadTenantInvoice, name='checkReadTenantInvoice'),
    path('notificationsLandlord/readWarn/<int:id_warn>', views.checkReadTenantWarning, name='checkReadTenantWarning'),
    path('profile/delPopUpDuePayment', views.deletePopUpDuePayment, name='deletePopUpDuePayment'),
    path('receipts', views.receipts, name='receipts'),
    path('reasons/<int:agreement_id>', views.reasons, name='reasons'),
    path('receipt', views.get_receipt_pdf, name='get_receipt_pdf'),
    path('acceptDenyRequest/<int:request_id>', views.accept_deny_request, name='accept_deny_request'),
    path('review', views.review, name='review'),
    path('callReview', views.callReview, name='callReview'),
    path('profileTenant/<int:ten_id>', views.profileTenant, name='profileTenant'),
    path('profileLandlord/<int:lan_id>', views.profileLandlord, name='profileLandlord'),
    path('propertyListingNotif/<int:id_req>', views.propertyListingNotif, name='propertyListingNotif'),
    path('propertyListingRef/<int:id_ref>', views.propertyListingRef, name='propertyListingRef'),
    path('propertyListingInv/<int:id_list>', views.propertyListingInv, name='propertyListingInv'),
    path('user_manual', views.user_manual_view, name='user_manual'),
    path('1st_tenant', views.tenant_firstpage, name='1st_tenant'),
    path('num_of_unread_notifications', views.num_of_unread_notifications, name='num_of_unread_notifications'),
    path('numOfunreadMessages/', views.num_of_unread_messages, name="numOfUnreadMessages"),
    path('user_1', views.user_1, name='user_1'),
    path('user_2', views.user_2, name='user_2'),
    path('user_3', views.user_3, name='user_3'),
    path('user_4', views.user_4, name='user_4'),
    path('ut1', views.ut1, name='ut1'),
    path('ut2', views.ut2, name='ut2'),
    path('ut3', views.ut3, name='ut3'),
    path('ut4', views.ut4, name='ut4'),
    path('ut5', views.ut5, name='ut5'),
    path('ut6', views.ut6, name='ut6'),
    path('ut7', views.ut7, name='ut7'),
    path('ut8', views.ut8, name='ut8'),
    path('ut9', views.ut9, name='ut9'),
    path('ut10', views.ut10, name='ut10'),
    path('ut11', views.ut11, name='ut11'),
    path('ut12', views.ut11, name='ut12'),
]

