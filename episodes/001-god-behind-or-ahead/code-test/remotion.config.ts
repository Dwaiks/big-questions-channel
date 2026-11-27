import { Config } from "@remotion/cli/config";
// The cloud session can't download Remotion's own browser; use the headless Chromium installed on the machine.
Config.setBrowserExecutable("/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell");
