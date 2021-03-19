+++
type = "question"
title = "TCP - debugging 3 way handshake"
description = '''I am relatively new to TCP. I am writing a small stack for our embedded system to eventually send an email. I have actually gotten it to connect to our email server and login. However, I&#x27;m getting retransmissions, and I don&#x27;t know why. I&#x27;m hoping some of you experts can enlighten me as to why. https...'''
date = "2017-02-28T11:03:00Z"
lastmod = "2017-02-28T11:37:00Z"
weight = 59741
keywords = [ "3-way-handshake", "tcp" ]
aliases = [ "/questions/59741" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP - debugging 3 way handshake](/questions/59741/tcp-debugging-3-way-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59741-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am relatively new to TCP. I am writing a small stack for our embedded system to eventually send an email. I have actually gotten it to connect to our email server and login. However, I'm getting retransmissions, and I don't know why. I'm hoping some of you experts can enlighten me as to why.</p><p><a href="https://www.cloudshark.org/captures/1e8542d7b55c">https://www.cloudshark.org/captures/1e8542d7b55c</a></p><p>Looking at this mostly 3 way handshake capture, the server sends a PSH ACK 220 packet (708), in which I ACK (709). Then, the retransmissions start. It looks like my sequence numbers are correct, so I'm not sure why the server didn't accept it.</p><p>General Questions on the capture:</p><ol><li><p>I thought, thru my reading, that after my 3 way handshake ACK (packet 688), communication stops (but the connection stays open) until I send data to the server. But the server always responds to my ACK with the 220 packet, so maybe not. I haven't logged in, so maybe that's just a general connection message. Is the ACK always followed by the 220 packet?</p></li><li><p>Why the retransmissions?</p></li><li><p>The retransmissions seem to drop a byte as the 220 becomes 20 on all 4 retransmission packets. Why? This seems to always happen on the retransmissions.</p></li></ol><p>Thanks in advance.</p><p>Sutton</p></div><div id="question-tags" class="tags-container tags">3-way-handshake tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '17, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/9f303f38b9221d23f72e6d2e5a651184?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dodge55&#39;s gravatar image" /><p>dodge55<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dodge55 has no accepted answers">0%</span></p></div></div><div id="comments-container-59741" class="comments-container"></div><div id="comment-tools-59741" class="comment-tools"></div><div class="clear"></div><div id="comment-59741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59742"></span>

<div id="answer-container-59742" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59742-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>1st) You've uploaded a filtered capture, so your packet numbers are useless.</p><p>2nd) Your ACK has a (relative) number of 2, which means only the first byte of the received 181 bytes are acknowledged, hence the retransmissions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '17, 11:37</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59742" class="comments-container"><span id="59750"></span><div id="comment-59750" class="comment"><div id="post-59750-score" class="comment-score"></div><div class="comment-text"><p>When the client is taking over 800ms to ACK the SYN/ACK from the Server, I wouldn't expect too much "good" to follow.</p></div><div id="comment-59750-info" class="comment-info"><span class="comment-age">(28 Feb '17, 21:51)</span> Rooster_50</div></div><span id="59758"></span><div id="comment-59758" class="comment"><div id="post-59758-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the tip. I found my problem in the sequence numbers. So, for now, things are working much better.<br />
</p><p>Sorry for the packet numbers. I didn't realize that exporting selective packets made the numbering scheme different.</p><p>I still haven't found out why my ACK to the SYN/ACK is taking so long. It seems to be fast some times and very slow others.</p></div><div id="comment-59758-info" class="comment-info"><span class="comment-age">(01 Mar '17, 04:43)</span> dodge55</div></div><span id="59760"></span><div id="comment-59760" class="comment"><div id="post-59760-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-59760-info" class="comment-info"><span class="comment-age">(01 Mar '17, 05:40)</span> Jaap ♦</div></div></div><div id="comment-tools-59742" class="comment-tools"></div><div class="clear"></div><div id="comment-59742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

