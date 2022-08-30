class Locators:
    """Login Page Locators"""
    textbox_username_name = "username"
    textbox_password_name = "password"
    button_login_css = "button[class$='orangehrm-login-button']"
    link_forgot_password_css = "p[class$='orangehrm-login-forgot-header']"
    error_invalid_login_css = "p[class$='oxd-alert-content-text']"
    copyright_info_css = ".orangehrm-copyright-wrapper p:nth-child(2)"
    form_header = "h5"

    """Side Hamburger Menu Locators"""
    side_menu_items_inactive = "a[class='oxd-main-menu-item'] span"
    side_menu_item_active = "a[class='oxd-main-menu-item active'] span"
    side_menu_toggle_button = "button[class='oxd-icon-button oxd-main-menu-button']"
    side_menu_item_search = "input[placeholder='Search']"
    side_menu_brand_logo = "img[alt$='banner']"


