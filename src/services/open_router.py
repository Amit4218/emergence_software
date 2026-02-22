import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def send_chat_request(resume_data, question):

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
                "Content-Type": "application/json",
            },
            data=json.dumps(
                {
                    "model": "liquid/lfm-2.5-1.2b-thinking:free",
                    "messages": [
                        {
                            "role": "system",
                            "content": f"""
                            
                                You are an experienced technical recruiter assistant.

                                Your task is to analyze Amit's resume and respond to recruiter questions with:
                                - Insightful summaries
                                - Value-focused explanations
                                - Clear strengths
                                - Impact-oriented language

                                DO NOT:
                                - Copy or restate resume bullet points.
                                - List technologies without context.
                                - Provide generic responses.
                                - Synthesize information.

                                DO:
                                - Highlight measurable impact.
                                - Emphasize strengths and differentiators.
                                - Infer soft skills when reasonable.
                                - Keep responses concise (3-6 sentences unless otherwise asked).
                                - Maintain a professional tone.

                                Resume:
                                {resume_data}""",
                        },
                        {
                            "role": "user",
                            "content": f"{question}",
                        },
                    ],
                }
            ),
        )

        data = response.json()
        return data["choices"][0]["message"]["content"]

    except Exception:
        return "Error requesting ai model"
