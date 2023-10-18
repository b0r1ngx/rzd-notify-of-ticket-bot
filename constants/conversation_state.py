from telegram.ext import ConversationHandler

# State definitions for top level conversation
SELECTING_ACTION, ADDING_MEMBER, ADDING_SELF, DESCRIBING_SELF = map(chr, range(4))

# State definitions for second level conversation
SELECTING_LEVEL, SELECTING_GENDER = map(chr, range(4, 6))

# State definitions for descriptions conversation
SELECTING_FEATURE, TYPING = map(chr, range(6, 8))

# Meta states
STOPPING, SHOWING = map(chr, range(8, 10))

# Shortcut for ConversationHandler.END
END = ConversationHandler.END