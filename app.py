import os
import gradio as gr

print("=" * 50)
print("Python started successfully")
print("PORT =", os.environ.get("PORT"))
print("=" * 50)

with gr.Blocks() as demo:
    gr.Markdown("# 🚀 Render Test")
    gr.Markdown("If you can see this page, Render is working correctly!")

if __name__ == "__main__":
    print("Launching Gradio...")

    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860)),
        show_error=True,
        debug=True,
        quiet=False,
    )
