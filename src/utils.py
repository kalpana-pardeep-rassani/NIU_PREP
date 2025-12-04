import logging
import sys

# Configure basic logging to output to the console
# The level is set to INFO, which means INFO, WARNING, ERROR, and CRITICAL messages are shown.
logging.basicConfig(
    stream=sys.stdout, 
    level=logging.INFO, 
    format='[%(levelname)s] %(message)s'
)
log = logging.getLogger(__name__)

def greet(name: str) -> str:
    """
    Returns a personalized greeting message and handles invalid input types.
    """
    
    # try block
    try:
        if not isinstance(name, str):
            raise TypeError("Greeting name must be a string (text). Received type: " + str(type(name).__name__))

        # Use standard logging functions
        log.info(f"Received request to greet user: {name}")

        result = f"Hello, {name}! Welcome to the Neuroinformatics Kit."

        if not name:
            log.warning("Name was empty. Defaulting to standard greeting structure.")
        
        # Standard logging does not have 'success', so we use 'info'
        log.info("Greeting message constructed successfully.")
        
        return result
    
    # 2. Catch the specific error
    except TypeError as e:
        # Log the error using standard logging
        log.error(f"Input Error: {e}")
        # Return a simple, safe fallback message instead of crashing
        return "Hello! I received bad input and cannot greet you properly."