from modules import script_callbacks, shared
import re
from modules.shared import state
import requests

batch_count = 0
count = 1

def ntfy_on_img_save(img):
    global batch_count, count

    if not shared.opts.ntfy_enable:
        return

    if batch_count == 0:
        batch_count = get_batch_count(str(state.job))

    if batch_count == count:
        send_ntfy()
        batch_count = 0
        count = 1
        return

    # increment count if we're not yet done
    count += 1

def send_ntfy():
    assert shared.opts.ntfy_topic != "", "ntfy topic was empty; please set it in the Settings -> NTFY tab"
    requests.put(shared.opts.ntfy_server_url + "/" + shared.opts.ntfy_topic, shared.opts.ntfy_message)

# determines the total number of images to generate based on the output
def get_batch_count(input):
    # state.job has either 'task(####)' or 'Batch X out of X'
    if "task" in input:
        return 1

    last_number = re.search(r'\d+', input[::-1]).group()[::-1]
    return int(last_number)


# using count logic, this only gets called when all image processing is done
script_callbacks.on_image_saved(ntfy_on_img_save)
