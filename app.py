import os
import gradio as gr
import requests

# Simple config describing the roles
ROUTES = {
    "Gemini / Claude / Grok": {
        "Gemini (big & messy)": "Long-context analysis, multimodal-heavy workflows.",
        "Claude (careful & precise)": "Polished writing, structured reasoning, and coding.",
        "Grok (live & social)": "Current events, social context, X-native content.",
    },
    "Nova / Gemma / Kimi": {
        "Nova 2 Lite (ingest & reason)": "Multimodal docs, long-context synthesis, agent workflows.",
        "Gemma 4 31B (self-hosted control)": "Open-weight, self/remote hosted; good for RAG and coding.",
        "Kimi K2.5 (agentic & visual)": "High-context, agentic behavior with visual/code understanding.",
    },
}

def route_request(route_family, model_role, user_input):
    if not user_input.strip():
        return "Please enter a task or prompt."
    role_description = ROUTES[route_family].get(model_role, "")
    plan = []
    plan.append(f"**Selected route family:** {route_family}")
    plan.append(f"**Selected model role:** {model_role}")
    plan.append(f"**Role description:** {role_description}")
    if route_family == "Gemini / Claude / Grok":
        plan.append("\n### Suggested handoff chain")
        plan.append("- Gemini: summarize sources, extract structure, identify gaps.")
        plan.append("- Claude: turn structure into a clean draft, code, or plan.")
        plan.append("- Grok: sanity-check against current chatter, trends, or social context.")
    else:
        plan.append("\n### Suggested handoff chain")
        plan.append("- Nova 2 Lite: ingest mixed content and extract structure.")
        plan.append("- Gemma 4 31B: refine, rewrite, or run locally / self-hosted.")
        plan.append("- Kimi K2.5: explore alternative reasoning paths or agent-style follow-ups.")
    plan.append("\n### Example routing for your input")
    plan.append(f"User task: `{user_input}`")
    if "code" in user_input.lower() or "implement" in user_input.lower():
        plan.append("- Primary worker: Claude or Gemma 4 31B for coding-quality output.")
    elif "research" in user_input.lower() or "compare" in user_input.lower():
        plan.append("- Primary worker: Gemini or Nova 2 Lite for long-context synthesis.")
    elif "twitter" in user_input.lower() or "x.com" in user_input.lower() or "social" in user_input.lower():
        plan.append("- Primary worker: Grok or Kimi K2.5 for social / agentic context.")
    else:
        plan.append("- Primary worker: use the selected role as the main model, with the other two as support.")
    plan.append("\n*(Demo mode: no external LLM call performed. Swap in your providers when ready.)*")
    return "\n".join(plan)

with gr.Blocks() as demo:
    gr.Markdown("# Hermes-style Agentic Model Picker Demo")
    gr.Markdown(
        "Select a route family and model role, enter a task, and see how the routing plan would look.\n"
        "You can later wire this to real providers (e.g., OpenRouter, Bedrock, or Vertex AI)."
    )
    with gr.Row():
        route_family = gr.Dropdown(
            choices=list(ROUTES.keys()),
            value="Gemini / Claude / Grok",
            label="Route family",
        )
        model_role = gr.Dropdown(
            choices=list(ROUTES["Gemini / Claude / Grok"].keys()),
            value="Gemini (big & messy)",
            label="Model role",
        )
    def update_roles(family):
        return gr.Dropdown(
            choices=list(ROUTES[family].keys()),
            value=list(ROUTES[family].keys())[0],
        )
    route_family.change(
        update_roles,
        inputs=route_family,
        outputs=model_role,
    )
    user_input = gr.Textbox(
        lines=4,
        label="Task / prompt",
        placeholder="e.g. 'Compare recent LLM papers and draft a summary for my team.'",
    )
    output = gr.Markdown(label="Routing plan")
    submit = gr.Button("Generate routing plan")
    submit.click(
        route_request,
        inputs=[route_family, model_role, user_input],
        outputs=output,
    )

if __name__ == "__main__":
    demo.launch()