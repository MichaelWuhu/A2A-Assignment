async def handle_task(request: TaskRequest) -> str:
    text_parts = [part.text for part in request.message.parts if part.type == 'text']
    combined_text = ' '.join(text_parts)
    # ECHO skill: return the combined text
    return combined_text