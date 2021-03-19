+++
type = "question"
title = "why is random website slow to download?"
description = '''Hi all,  Im currently experiencing random latency on my network when connecting to random websites. The three way handshake is ok but during the conversation I get an ACK and then an RST,ACK about a minute later. Then the Three way handshake starts again and during the conversation I get another ACK...'''
date = "2014-06-30T19:04:00Z"
lastmod = "2014-07-02T08:46:00Z"
weight = 34303
keywords = [ "latency", "tcp", "rst+ack" ]
aliases = [ "/questions/34303" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why is random website slow to download?](/questions/34303/why-is-random-website-slow-to-download)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34303-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>Im currently experiencing random latency on my network when connecting to random websites. The three way handshake is ok but during the conversation I get an ACK and then an RST,ACK about a minute later. Then the Three way handshake starts again and during the conversation I get another ACK then RST,ACK. This does not happen on other network that I've looked at. can any one explain why this might be happening?? Please use the link to see the capture. Thanks Phil</p></div><div id="question-tags" class="tags-container tags">latency tcp rst+ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '14, 19:04</strong></p><img src="https://secure.gravatar.com/avatar/cf5e213cd3cc17b7d2dccfaad3fa7973?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dalyphilip&#39;s gravatar image" /><p>dalyphilip<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dalyphilip has no accepted answers">0%</span></p></div></div><div id="comments-container-34303" class="comments-container"><span id="34304"></span><div id="comment-34304" class="comment"><div id="post-34304-score" class="comment-score"></div><div class="comment-text"><p>Capture file is available here</p><p><a href="https://osqa-ask.wireshark.org/upfiles/Capture_9.JPG">https://osqa-ask.wireshark.org/upfiles/Capture_9.JPG</a></p></div><div id="comment-34304-info" class="comment-info"><span class="comment-age">(30 Jun '14, 19:05)</span> dalyphilip</div></div><span id="34317"></span><div id="comment-34317" class="comment"><div id="post-34317-score" class="comment-score"></div><div class="comment-text"><p>can you upload a capture file,difficult to understand on basis of screenshot.</p></div><div id="comment-34317-info" class="comment-info"><span class="comment-age">(01 Jul '14, 04:53)</span> kishan pandey</div></div><span id="34334"></span><div id="comment-34334" class="comment"><div id="post-34334-score" class="comment-score"></div><div class="comment-text"><p>Hi Kishan, you can get the capture file from the below address <a href="https://www.dropbox.com/s/igmsj2s2hhgtlej/capture%20file.pcapng">https://www.dropbox.com/s/igmsj2s2hhgtlej/capture%20file.pcapng</a></p><p>The filter i used was (((ip.src == 10.50.2.7) &amp;&amp; (ip.dst == 157.56.58.13)) || ((ip.src == 157.56.58.13) &amp;&amp; (ip.dst == 10.50.2.7)))</p><p>Hope that helps. Thanks</p></div><div id="comment-34334-info" class="comment-info"><span class="comment-age">(01 Jul '14, 16:03)</span> dalyphilip</div></div></div><div id="comment-tools-34303" class="comment-tools"></div><div class="clear"></div><div id="comment-34303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34351"></span>

<div id="answer-container-34351" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34351-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem lies in the client not completing the TLS negotiation in time. the https server sends a RST after not haveng received the Client Key Exchange in a reasonable amount of time.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_049.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '14, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jul '14, 08:47</p></div></div><div id="comments-container-34351" class="comments-container"><span id="34455"></span><div id="comment-34455" class="comment"><div id="post-34455-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the diagnostics on the Packet capture. I found the problem to be the anti-virus in the Sophos client.</p><p>The followiing is from <a href="http://www.sophos.com/en-us/support/knowledgebase/27213.aspx">http://www.sophos.com/en-us/support/knowledgebase/27213.aspx</a> Web protection | Download scanning</p><p>Sophos Control Center: Configure scanning | Web scanning is</p><p>Set Download scanning set to off. Download scanning can cause minor delays whilst a portion of the data from the site is scanned before delivery to the end user's internet browser, some websites may be adversely affected by this.</p></div><div id="comment-34455-info" class="comment-info"><span class="comment-age">(07 Jul '14, 18:33)</span> dalyphilip</div></div></div><div id="comment-tools-34351" class="comment-tools"></div><div class="clear"></div><div id="comment-34351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

