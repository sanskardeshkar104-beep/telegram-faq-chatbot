"""FAQ knowledge for Cafe Aroma, a demo business."""

FAQS = {
    "hours": "We are open Monday to Friday 8am to 9pm, and Saturday to Sunday 9am to 11pm.",
    "location": "You'll find us at 42 Rose Street, next to the old bookshop.",
    "menu": "Our menu covers espresso drinks, filter coffee, pastries and a small all-day brunch list.",
    "wifi": "Yes, free WiFi with no password needed, just accept the terms page.",
    "booking": "Call us on 555-0142 or walk in, we hold tables for 15 minutes.",
    "price": "Coffee starts at 120 rupees, brunch plates from 250 rupees.",
}

KEYWORDS = {
    "hours": ["hour", "open", "close", "timing"],
    "location": ["where", "location", "address", "reach"],
    "menu": ["menu", "food", "serve", "eat", "snack"],
    "wifi": ["wifi", "internet", "password"],
    "booking": ["book", "reserve", "table", "reservation"],
    "price": ["price", "cost", "how much", "expensive"],
}

DEFAULT_REPLY = ("I'm not sure about that one. Try asking about hours, location, menu, "
                 "wifi, bookings or prices. For anything else our team replies on 555-0142.")
