from openai import OpenAI

class LLMResponseAgent:
    def __init__(self,openai_key):
        self.client=OpenAI(api_key=openai_key)

    def answer(self,context,trace_id):
        prompt=f"Context:\n{chr(10).join(context['retrieved_context'])}\n\nQuery: {context['query']}\nAnswer:"

        response=self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role":"user","content": prompt}])

        return response.choices[0].message.content
