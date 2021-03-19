+++
type = "question"
title = "Cannot access google"
description = '''Hello, I am trying to access Google from my mobile phone but it does not work. I have put the phone on portable hotspot, connected with a laptop under it ran Wireshark and tried to access Google.com. It takes me to google.de which is resolved with the 173.194.70.94 IP. From the trace I understand th...'''
date = "2014-07-22T03:21:00Z"
lastmod = "2014-07-23T13:41:00Z"
weight = 34818
keywords = [ "access", "google.de", "cannot", "google" ]
aliases = [ "/questions/34818" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot access google](/questions/34818/cannot-access-google)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34818-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to access Google from my mobile phone but it does not work. I have put the phone on portable hotspot, connected with a laptop under it ran Wireshark and tried to access Google.com. It takes me to google.de which is resolved with the 173.194.70.94 IP. From the trace I understand that there is an issue with the TCP handshake but I do not have the knowledge to interpret it. Could you please help ?</p><p>You can find the trace here:</p><p><a href="https://drive.google.com/file/d/0B3IpHDQOfcURbmdzWkZpc3VEemc/edit?usp=sharing">https://drive.google.com/file/d/0B3IpHDQOfcURbmdzWkZpc3VEemc/edit?usp=sharing</a></p><p>Best regards,</p></div><div id="question-tags" class="tags-container tags">access google.de cannot google</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '14, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/e4aff7b8c432a9302b8c6e35c106e9a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vladimirb&#39;s gravatar image" /><p>vladimirb<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vladimirb has no accepted answers">0%</span></p></div></div><div id="comments-container-34818" class="comments-container"><span id="34819"></span><div id="comment-34819" class="comment"><div id="post-34819-score" class="comment-score"></div><div class="comment-text"><p>also cloudshark link:</p><p><a href="https://www.cloudshark.org/captures/b18fbd0a42d0">https://www.cloudshark.org/captures/b18fbd0a42d0</a></p></div><div id="comment-34819-info" class="comment-info"><span class="comment-age">(22 Jul '14, 03:29)</span> vladimirb</div></div><span id="34845"></span><div id="comment-34845" class="comment"><div id="post-34845-score" class="comment-score"></div><div class="comment-text"><p>Hy guys, could you please help me with this ? Please tell me if you need any additional information. What I am seeing in the trace seems like an errorr in the TCP handshake (goole ip is resolved to 173.194.70.94) Error is TCP Previous segment not captured (packet no 182).</p></div><div id="comment-34845-info" class="comment-info"><span class="comment-age">(23 Jul '14, 04:33)</span> vladimirb</div></div></div><div id="comment-tools-34818" class="comment-tools"></div><div class="clear"></div><div id="comment-34818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34855"></span>

<div id="answer-container-34855" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34855-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You seem to have a MTU problem because the IP packets coming from Google server with a TCP size of 1430 bytes (corresponding to the MSS negotiated during the TCP handshake) are not received on your laptop. Try to lower the MTU setting of the interface used for tethering on your laptop (you can search on Internet how to do it depending on your OS).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '14, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-34855" class="comments-container"></div><div id="comment-tools-34855" class="comment-tools"></div><div class="clear"></div><div id="comment-34855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

