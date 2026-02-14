def combine_skills(data):
    return (
        data.get("technical_skills", []) +
        data.get("tools", [])
    )
