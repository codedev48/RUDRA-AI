import webbrowser
import wikipedia


def google_search(query):
    """
    Opens Google search in browser.
    """
    webbrowser.open(f"https://www.google.com/search?q={query}")


def wikipedia_search(query):
    """
    Fetches Wikipedia summary text.
    Returns summary string.
    Does NOT speak. AI brain will handle speaking.
    """

    try:
        # Fetch longer summary for expansion
        result = wikipedia.summary(query, sentences=8)
        return result

    except wikipedia.exceptions.DisambiguationError as e:
        try:
            # Try first suggested option
            result = wikipedia.summary(e.options[0], sentences=8)
            return result
        except:
            return None

    except wikipedia.exceptions.PageError:
        return None

    except Exception:
        return None