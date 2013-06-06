Whonix (build) scripts currently "trap INT TERM ERR". ERR is used stop the script (in most cases) and to inform where the error occurred. For cleanup, it would be better if EXIT where used other than trapping individual signals. There is no real limitation because of this, would just be more correct to have separate ERR and EXIT traps.

Some extra old notes:

HUP (Hang up detected on controlling terminal or death of controlling process) should be definitively added.

INT (Issued if the user sends an interrupt signal (Ctrl + C).) is in, because users of my build scripts are free to press Ctrl + C to interrupt them for whatever reason. What it does is informing about the last $BASH_COMMAND, cleaning up, dismounting an image (because not doing so and re-running the build script while the image is still mounted could lead to strange errors).

TERM (Software termination signal (sent by kill by default).) If one thinks "build script takes to long, I forgot to add some files" and uses kill to stop it, it's best to do the same cleanup as for INT.

ERR (Non-expected non-zero return code in rare cases (bugs).) Same information and cleanup as if INT or TERM.

SIGQUIT (Issued if the user sends a quit signal (Ctrl + D).) Well, I think Ctrl + C is more common than Ctrl + D. If one really wants this and stops my scripts this way, so be it. I think having one way to stop it while cleaning and and one just exiting is good.