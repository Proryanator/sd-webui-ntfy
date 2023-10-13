from modules import scripts_postprocessing, shared

from scripts.ntfy import send_ntfy


# this enables notifications to be sent when doing stuff in the 'Extras' tab
class ScriptPostprocessingNTFY(scripts_postprocessing.ScriptPostprocessing):
    name = "NTFY"
    order = 5000

    def ui(self):
        return {}

    def process(self, pp: scripts_postprocessing.PostprocessedImage):
        if not shared.opts.ntfy_enable:
            return

        send_ntfy()
