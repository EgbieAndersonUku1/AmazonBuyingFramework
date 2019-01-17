# Errors that will be displayed whenever a test is not executed correctly

# Sign error is displayed if the user's application is in correctly
SIGN_IN_ERROR = "Not logged in. Expected to find order link from home page."

# Displayed if the first item in the cart is not the expected item
FIRST_ITEM_ERROR = "Expected the first item in the cart to be the item <{}>, found <{}>}"

# Displayed if no item is found in saved in 'save for later' section
SAVE_FOR_LATER_ERROR = "Expected to find heading <{}> with one saved item, found instead <{}>"

# Displayed when the expected current cart item expectation is not met
QUANTITY_ERROR = "Expected the current cart item_quantity to be <{}> items, found <{}> items instead"

# Displayed whenever an item in cart is not deleted
DELETION_QUANTITY_ERROR = "Expected the number of items in the cart to be <{}> after deletion, found <{}> instead"

# Displayed when the expected items in the cart is not incremented
ITEM_INCREMENT_ERROR = "Expected the number of items to be <{}> after incremention, found <{}> instead"

# Displayed if the cart is not empty
EMPTY_CART_ERROR = "Expected to find that the string that cart is empty. Found something else instead"