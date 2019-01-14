import webbrowser

proxyAddress = "10.0.0.3"
proxyPort = 12000
proxyURL = proxyAddress + ":" + str(proxyPort)

webbrowser.open_new_tab(proxyURL + "/libgen.io")
webbrowser.open_new_tab(proxyURL + "/rpm.org")
