import gradio as gr
from modules import script_callbacks
from modules import shared


def on_ui_settings():
    section = ('ntfy', "NTFY")
    shared.opts.add_option(
        "ntfy_enable",
        shared.OptionInfo(
            True,
            "Enables this extension",
            gr.Checkbox,
            {"interactive": True},
            section=section)
    )

    shared.opts.add_option("ntfy_server_url",
                           shared.OptionInfo("https://ntfy.sh",
                                             "The ntfy server to send notifications to; defaults to the public ntfy server https://ntfy.sh",
                                             gr.Textbox, {},
                                             section=section))

    shared.opts.add_option("ntfy_topic",
                           shared.OptionInfo("",
                                             "Topic Name: the topic to send this message to. Must be set for this extension to work (and choose something unique).",
                                             gr.Textbox, {},
                                             section=section))

    shared.opts.add_option("ntfy_message",
                           shared.OptionInfo("SD Batch Complete",
                                             "The message to send to the ntfy server after images have been generated.",
                                             gr.Textbox, {},
                                             section=section))


script_callbacks.on_ui_settings(on_ui_settings)
