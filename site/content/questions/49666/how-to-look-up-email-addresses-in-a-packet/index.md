+++
type = "question"
title = "How to look up email addresses in a packet?"
description = '''Hello everyone, I am very new to wireshark and have close to no idea of what I&#x27;m doing. On a practice Wireshark round (don&#x27;t worry, it&#x27;s over now), they wanted me to &quot;find the email address of a machine.&quot; The only problem is, there&#x27;s like 10000 packets. How am I supposed to find the answers? Thanks!...'''
date = "2016-01-31T16:06:00Z"
lastmod = "2016-02-01T13:35:00Z"
weight = 49666
keywords = [ "email" ]
aliases = [ "/questions/49666" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to look up email addresses in a packet?](/questions/49666/how-to-look-up-email-addresses-in-a-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49666-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone, I am very new to wireshark and have close to no idea of what I'm doing. On a practice Wireshark round (don't worry, it's over now), they wanted me to "find the email address of a machine." The only problem is, there's like 10000 packets. How am I supposed to find the answers? Thanks!</p><p>URL for capture file: <a href="https://drive.google.com/drive/folders/0B9mXYmkPhvROYV9TNjJHWmg3bFU">https://drive.google.com/drive/folders/0B9mXYmkPhvROYV9TNjJHWmg3bFU</a></p><p>Wireshark Scenario:</p><p>Several complaints are coming into the IT Department that the company, All-Time Favorites Arcade's, network is running slower than normal. Due to the amount of complaints, you as the network administrator run Wireshark to capture and analyze the companies network traffic see where the bottleneck may be occurring within the company network. During your analysis of the PCAP file you notice a specific IP address is beaconing out to the Internet every two (2) hours. While beconing IP address has nothing to do with the bottleneck you originally were working to resolve the beaconing activity is suspicious. Once your analysis of the PCAP file is complete you present the information to your Security Manager concerning the beaconing IP address. The Security Manager has determined to error on the side of caution as the machine may possibly be infected with a malicious software that is calling back every two (2) hours.<br />
The Security Manager then orderes the computer to be removed from the network immediately, so the computer is shut down and physically removed from the network for the forensic analysis team to determine if there is possible malware. Please answer the following questions concerning the PCAP file:</p><ol><li><p>What is the email address the machine within the captured PCAP Analysis (do not put the @xxx.xxx) only the first part of the inbox name?</p></li><li><p>What part of the HTTP protocol did you find the email address?<br />
</p></li><li><p>What is the destination port located in the steam you found the email address?</p></li><li><p>What is the destination IP Address?</p></li><li><p>What is the source IP Address?</p></li><li><p>What was the frame number you were able to find all the information to the above questions in?</p></li></ol></div><div id="question-tags" class="tags-container tags">email</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '16, 16:06</strong></p><img src="https://secure.gravatar.com/avatar/d9a151081bbdcf69cccfb940f82816ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanielChen&#39;s gravatar image" /><p>DanielChen<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanielChen has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-49666" class="comments-container"></div><div id="comment-tools-49666" class="comment-tools"></div><div class="clear"></div><div id="comment-49666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49698"></span>

<div id="answer-container-49698" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49698-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This takes a bit of understanding how the HTTP protocol (and thus, HTML) works, and how you can find it in Wireshark.</p><p>In Wireshark, you are able to search for strings with "Edit-&gt;Find Packet...". I would search from strings such as "email", "mail", etc. Chances are, someone has to submit an email via a form. So in the "input" tag of the HTML form, you should see references to values that would accept an email address coming from the server to the client. Once you find that, at some point in the trace thereafter, the user will have provided the email address going to the server.</p><p>So look for an email address being sent from the client source to the server destination in Wireshark.</p><p>Hope that helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '16, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/0eafb94fc68881ab754f30924ce504ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeantunis&#39;s gravatar image" /><p>jeantunis<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeantunis has no accepted answers">0%</span></p></div></div><div id="comments-container-49698" class="comments-container"></div><div id="comment-tools-49698" class="comment-tools"></div><div class="clear"></div><div id="comment-49698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

