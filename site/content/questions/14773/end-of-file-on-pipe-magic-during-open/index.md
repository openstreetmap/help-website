+++
type = "question"
title = "End of file on pipe magic during open"
description = '''I&#x27;m trying to pipe my android device&#x27;s network traffic on wireshark, which is installed on my desktop.  Terminal 1 sudo ./adb shell &quot;./data/local/tcpdump-armn -s 0 -v -w - | ./data/local/netcat -l -p 12345&quot; This would allow me to route the data to port number 12345 on the android device. Terminal 2 ...'''
date = "2012-10-08T02:49:00Z"
lastmod = "2012-10-08T11:35:00Z"
weight = 14773
keywords = [ "android", "ubuntu", "wireshark" ]
aliases = [ "/questions/14773" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [End of file on pipe magic during open](/questions/14773/end-of-file-on-pipe-magic-during-open)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14773-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to pipe my android device's network traffic on wireshark, which is installed on my desktop.</p><h2 id="terminal-1">Terminal 1</h2><p>sudo ./adb shell "./data/local/tcpdump-armn -s 0 -v -w - | ./data/local/netcat -l -p 12345"</p><p>This would allow me to route the data to port number 12345 on the android device.</p><h2 id="terminal-2">Terminal 2</h2><p>sudo ./adb forward tcp:12345 tcp:54321 &amp;&amp; netcat 127.0.0.1 54321 | wireshark -k -S -i -</p><p>This should allow me to send the data from port 12345 on the device to port 54321 on the desktop and then pipe it to wireshark.</p><p>But, on execution I get <strong><code>End of file on pipe magic during open</code></strong> in wireshark. How do I solve this issue?</p></div><div id="question-tags" class="tags-container tags">android ubuntu wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '12, 02:49</strong></p><img src="https://secure.gravatar.com/avatar/7e3d6d4994b243ae7f34116a5dcbd565?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harshal%20Kshatriya&#39;s gravatar image" /><p>Harshal Ksha...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harshal Kshatriya has no accepted answers">0%</span></p></div></div><div id="comments-container-14773" class="comments-container"></div><div id="comment-tools-14773" class="comment-tools"></div><div class="clear"></div><div id="comment-14773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14780"></span>

<div id="answer-container-14780" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14780-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><code>sudo ./adb shell "./data/local/tcpdump-armn -s 0 -v -w - | ./data/local/netcat -l -p 12345"</code><br />
</p></blockquote><p>You <strong>cannot</strong> use netcat option -l and -p together. You should see an error message when running the above command.</p><p>The following command works on my system, HOWEVER beware that netcat (the OS) might not buffer enough data if it's a busy network and it takes to long to start the command in terminal 2!</p><blockquote><p><code>sudo ./adb shell "./data/local/tcpdump-armn -s 0 -v -w - | ./data/local/netcat -l 12345"</code><br />
</p></blockquote><p>You better do this:</p><p>Open a netcat server in terminal 2 (first!) and then send the output of tcpdump with netcat to that server.</p><p><strong>Terminal 2 (first!)</strong></p><blockquote><p><code>sudo -l 12345 | wireshark -k -S -i -</code><br />
</p></blockquote><p><strong>Terminal 1 (second!)</strong></p><blockquote><p><code>sudo ./adb shell "./data/local/tcpdump-armn -s 0 -v -w - | ./data/local/netcat x.x.x.x 12345</code><br />
</p></blockquote><p>Replace x.x.x.x with the IP address of your Wireshark system.</p><p>Regards<br />
Kurt<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '12, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14780" class="comments-container"></div><div id="comment-tools-14780" class="comment-tools"></div><div class="clear"></div><div id="comment-14780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

