# Job Notifications to Any Platform with ntfy

No need to wait by your computer or mobile device until a job finishes for stable diffusion.

Introducing a custom extension that enables notifications once image generation jobs are done for the project <a href='https://github.com/AUTOMATIC1111/stable-diffusion-webui'>AUTOMATIC1111/stable-diffusion-webui</a>. 

If you are unfamiliar with <a href='https://docs.ntfy.sh/'>ntfy</a>, the big takeaway is how easy it is to send notifications anywhere from a computer; to your mobile devices, other computers, etc. This extension brings that ease of use and flexibility to the stable-diffusion-webui project.

## Installation

---

1. In sd-webui, open up `Settings -> Extensions -> Install from URL`
2. Copy `https://github.com/Proryanator/sd-webui-ntfy.git` and paste it into the "URL for extension's git repository" and click `Install`
4. Once installed, go back to the `Installed Tab` and click `Apply and restart UI`


## Quick Setup Guide

---

After installing, this extension is enabled by default for ease of use. You will need to make 1 change though in settings.

1. Go to `Settings -> NTFY` and enter some unique name in the `Topic Name` field. This will be appended to the ntfy server url in the first field as such: 
`https://ntfy.sh/topic-name`

2. Click `Apply settings` and you're good to go
3. On your device of choice (most likely will be mobile), subscribe to the topic you just made. Please follow instructions <a href='https://docs.ntfy.sh/'>here</a> on how to set this up
4. That's it! You should get notified when image generations finish (this includes batch jobs and anything in the `Extras` tab like upscaling)

For message customization or other details, see the next section.

## More Configuration

---

You have more config options if you so choose to change them. Here's all the settings available to you:

![settings.png](docs%2Fsettings.png)

If you have your own private server of `ntfy` running, simply update the url in the settings. You are also more than welcome to change the default message being sent.

## Future improvements:

---

- [ ] add notification for server startup
- [ ] add notification for when training on a dataset has completed
- [ ] add notifications when an error occurs during your batch run

## References

- <a href='https://github.com/AUTOMATIC1111/stable-diffusion-webui'>AUTOMATIC1111/stable-diffusion-webui</a>
- <a href='https://github.com/udon-universe/stable-diffusion-webui-extension-templates'>stable-diffusion-webui-extension-templates</a>
- <a href='https://docs.ntfy.sh/'>ntfy docs</a>