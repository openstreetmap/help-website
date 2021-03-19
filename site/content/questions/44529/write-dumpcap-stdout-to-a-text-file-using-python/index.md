+++
type = "question"
title = "Write dumpcap stdout to a text file using python"
description = '''I am currently trying to parse the filename from dumpcap&#x27;s stdout in order to set it to a variable within my python script. def startdump():  global DUMPCAP  #global dumpdirectory  global eventfile  setDumpcapOptions() # Function that sets DUMPCAP = dumpcap -b duration:2147483647 -c 100 -i 1 -n -p -...'''
date = "2015-07-27T08:29:00Z"
lastmod = "2015-07-27T08:46:00Z"
weight = 44529
keywords = [ "python", "dumpcap", "linux" ]
aliases = [ "/questions/44529" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Write dumpcap stdout to a text file using python](/questions/44529/write-dumpcap-stdout-to-a-text-file-using-python)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44529-score" class="post-score" title="current number of votes">0</div><span id="post-44529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am currently trying to parse the filename from dumpcap's stdout in order to set it to a variable within my python script.<br />
<code>def startdump():     global DUMPCAP     #global dumpdirectory     global eventfile     setDumpcapOptions() # Function that sets DUMPCAP = dumpcap -b duration:2147483647 -c 100 -i 1 -n -p -s 2 -w test3 -B 20     print("dumpcap.exe = " + DUMPCAP)     #os.chdir(dumpdirectory)     proc1 = subprocess.Popen(DUMPCAP, shell=True, stdout=subprocess.PIPE)     if dc_mode == "Dumpcap Only":         time.sleep(5)         with open("proc1stdout.txt", 'w+') as proc1stdout:             proc1stdout.write(str(proc1.stdout))             for line in proc1stdout:                 print("%s" % line)                 if "File:" in line:                     print(line)                     eventfile = line.split('File:')[1]                     print(eventfile)                     mail_man()         proc1.communicate()</code></p><p>This gives me an error <code>[Errno 2] No such file or directory: ''</code></p><p>I am coding in Python2.6.6. The Popen module does not support iterating so I cannot parse directly from the stdout in the terminal. Is there a way to write the Dumpcap stdout to a text file so that I can much more easily parse it from there?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '15, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/d2c595443d278142503a2dde970a0630?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Googlesomething&#39;s gravatar image" /><p><span>Googlesomething</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Googlesomething has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jul '15, 08:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-44529" class="comments-container"></div><div id="comment-tools-44529" class="comment-tools"></div><div class="clear"></div><div id="comment-44529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44531"></span>

<div id="answer-container-44531" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44531-score" class="post-score" title="current number of votes">1</div><span id="post-44531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Googlesomething has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>Dumpcap</code> writes the filename to <code>stderr</code>, not <code>stdout</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '15, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-44531" class="comments-container"></div><div id="comment-tools-44531" class="comment-tools"></div><div class="clear"></div><div id="comment-44531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

