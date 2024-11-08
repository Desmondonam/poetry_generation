def create_prompt(theme: str, form: str = "poem") -> str:
    if form == "poem":
        return f"Write a beautiful poem about {theme}."
    elif form == "haiku":
        return f"Write a haiku about {theme}."
    else:
        return f"Write a verse about {theme}."
