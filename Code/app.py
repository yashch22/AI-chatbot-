import gradio as gr
from chatbot import Chatbot


chatbot_qa = Chatbot(model_name="gpt-3.5-turbo")

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(value=[[None,"Hi, My Name is Groot from FlexCart. How can I help you?"]])
    msg = gr.Textbox(label="Input")
    clear = gr.ClearButton([msg, chatbot])
    with gr.Accordion("See Details"):
        source_output = gr.Textbox( label = "Source")
    # source_accordion = gr.Accordion()
    
    def respond(message, chat_history):
        bot_message, source = chatbot_qa.chat(message)
        chat_history.append((message, bot_message))
        source_output.value = source
        # source_button.click = lambda: source_output.set_visible(True) if source else None
        print()
        return "", chat_history, source

    msg.submit(respond, [msg, chatbot], [msg, chatbot,source_output])

    # msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch(share = True)
