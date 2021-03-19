+++
type = "question"
title = "tcp acking every other segment?"
description = '''I am working on the tcp lab and am having trouble understading how the ack is and why it skips some segments? Can anyone shed a little light on this for me?'''
date = "2011-11-14T10:05:00Z"
lastmod = "2011-11-14T12:23:00Z"
weight = 7418
keywords = [ "ack" ]
aliases = [ "/questions/7418" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [tcp acking every other segment?](/questions/7418/tcp-acking-every-other-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7418-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working on the tcp lab and am having trouble understading how the ack is and why it skips some segments? Can anyone shed a little light on this for me?</p></div><div id="question-tags" class="tags-container tags">ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '11, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/f49572556c83f79bc390b9b12b838df6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hatcher44&#39;s gravatar image" /><p>hatcher44<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hatcher44 has no accepted answers">0%</span></p></div></div><div id="comments-container-7418" class="comments-container"></div><div id="comment-tools-7418" class="comment-tools"></div><div class="clear"></div><div id="comment-7418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="7423"></span>

<div id="answer-container-7423" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7423-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are seeing a feature known as "delayed ACK." Remember that ACKs are cumulative and the ACK number from the receiving system is the next expected sequence number from the sending system. Assuming relative sequence numbers are turned on in your Wireshark preferences, if the receiver sends an ACK with ACK number 1,000, it's saying "I've received bytes 1 through 999, and I expect 1,000 next."</p><p>Because ACKs are cumulative, it's not necessary to ACK every packet. When delayed ACK is turned on, the receiver will usually ACK every other packet.</p><p>Let's say the sender is sending 100 byte packets, and it starts with sequence number 1. If every packet is being ACKed:</p><p>The first sent packet will have sequence number 1, and will contain bytes 1 through 100. The first ACK will have ACK number 101, meaning that the receiver expects sequence number 101 next.</p><p>The second sent packet will have sequence number 101 and will contain bytes 101 through 200. The second ACK will have ACK number 201, meaning that the receiver expects sequence number 201 next.</p><p>If delayed ACK is on, no ACK will be sent in response to the first packet. When the second packet is received, an ACK will be sent with ACK number 201. This means that the receiver has received bytes 1 through 200 and is expecting 201 next.</p><p>Delayed ACK normally ACKS every other segment. The delayed ACK timer takes care of the situation where there is an odd number of segments.</p><p>See <a href="http://ask.wireshark.org/questions/4798/when-does-delayed-ack-start?page=1#4804">When Does Delayed Ack Start?</a> for a discussion of delayed ACKs or Google "Delayed ACK". There are a lot of good explanations on the web.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '11, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Nov '11, 12:24</p></div></div><div id="comments-container-7423" class="comments-container"></div><div id="comment-tools-7423" class="comment-tools"></div><div class="clear"></div><div id="comment-7423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7419"></span>

<div id="answer-container-7419" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7419-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You will want to look at the differences in the acknowledged sequence numbers of the2 consecutive ACKs if you lok at the amount of acknowledged data from each ACK, sometimes you will find that the your system is only acking every other segement sent to it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '11, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/058c809d2fc2a9728c4149dfe251b761?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="modernman&#39;s gravatar image" /><p>modernman<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="modernman has no accepted answers">0%</span></p></div></div><div id="comments-container-7419" class="comments-container"></div><div id="comment-tools-7419" class="comment-tools"></div><div class="clear"></div><div id="comment-7419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7420"></span>

<div id="answer-container-7420" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7420-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found this online which uses the etheral lab file.</p><p>The acknowledged sequence numbers of the ACKs are listed as follows. acknowledged sequence number acknowledged data ACK 1 566 566 ACK 2 2026 1460 ACK 3 3486 1460 ACK 4 4946 1460 ACK 5 6406 1460 ACK 6 7866 1460 ACK 7 9013 1147 ACK 8 10473 1460 ACK 9 11933 1460 ACK 10 13393 1460 ACK 11 14853 1460 ACK 12 16313 1460 IF you use this I would advise that you reword it so as not to be exactly the same.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '11, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/803e7f4ef2b3d28229d6dd5fa3e93376?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sheldor&#39;s gravatar image" /><p>sheldor<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sheldor has no accepted answers">0%</span></p></div></div><div id="comments-container-7420" class="comments-container"><span id="7421"></span><div id="comment-7421" class="comment"><div id="post-7421-score" class="comment-score"></div><div class="comment-text"><p>I appreciate the help sheldor but I dont want to just copy past the answer I just wanted to know how to calculate and determine it.</p></div><div id="comment-7421-info" class="comment-info"><span class="comment-age">(14 Nov '11, 10:22)</span> hatcher44</div></div></div><div id="comment-tools-7420" class="comment-tools"></div><div class="clear"></div><div id="comment-7420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

