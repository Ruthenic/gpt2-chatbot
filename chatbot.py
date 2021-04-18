import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
checkpoint_name = "Face1"
gpt2.load_gpt2(sess, run_name=checkpoint_name)
username = input("What would you like your username to be? ")
prevtext = ""
message = ""
while True:
    message = input("{}: ".format(username))
    if message.startswith("/direct"):
        prevtext += message.replace("/direct ", "") + "\n"
    else:
        prevtext += username + ":" + message + '\n'
    result = username
    while username in result:
        result = gpt2.generate(sess, run_name=checkpoint_name, length = 30, prefix = prevtext, truncate = "\n", include_prefix = False, return_as_list = True)[0]
    print(result)
    prevtext += result + "\n"
