+++
type = "question"
title = "lot of TCP DUP &amp; Retransmission"
description = '''I see a lot of DUP ACKS and re transmission &amp;amp; fast re-transmissions. Can this be a reason of slow transfer rate over the wan links ?'''
date = "2014-07-14T08:54:00Z"
lastmod = "2014-07-15T00:39:00Z"
weight = 34631
keywords = [ "retransmissions" ]
aliases = [ "/questions/34631" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [lot of TCP DUP & Retransmission](/questions/34631/lot-of-tcp-dup-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34631-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I see a lot of DUP ACKS and re transmission &amp; fast re-transmissions. Can this be a reason of slow transfer rate over the wan links ?<img src="https://osqa-ask.wireshark.org/upfiles/1_2.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '14, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/4316c1946f08f682c8b02ca026a5a95e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rikki&#39;s gravatar image" /><p>Rikki<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rikki has no accepted answers">0%</span></p></img></div></div><div id="comments-container-34631" class="comments-container"><span id="34632"></span><div id="comment-34632" class="comment"><div id="post-34632-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.cloudshark.org/captures/ef3bb6cb4701">https://www.cloudshark.org/captures/ef3bb6cb4701</a></p><p>here is the upload of the capture</p></div><div id="comment-34632-info" class="comment-info"><span class="comment-age">(14 Jul '14, 09:38)</span> Rikki</div></div><span id="34657"></span><div id="comment-34657" class="comment"><div id="post-34657-score" class="comment-score"></div><div class="comment-text"><p>That capture file does <strong>not</strong> match the screenshot. Any reason for that?</p></div><div id="comment-34657-info" class="comment-info"><span class="comment-age">(15 Jul '14, 03:58)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-34631" class="comment-tools"></div><div class="clear"></div><div id="comment-34631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34642"></span>

<div id="answer-container-34642" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34642-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like classic packet loss with a latency that leads to multiple DUP ACKs to be sent for each of the missing packets. So without looking too deeply into the packets I'd say you have packet loss, leading to retransmissions (which take a while) and this results in slow transfer rates.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '14, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-34642" class="comments-container"><span id="34653"></span><div id="comment-34653" class="comment"><div id="post-34653-score" class="comment-score"></div><div class="comment-text"><p>thanks, The link has no packet loss as this is a very critical link and no latency or packet loss is affordable to us. I am taking this capture at receiver end &amp; RTT from source to destination is 130ms, probably that is the reason why we see so many DUP ACKs being sent before fast re transmitted packet arrives. Can there be any other reason.</p></div><div id="comment-34653-info" class="comment-info"><span class="comment-age">(15 Jul '14, 03:39)</span> Rikki</div></div><span id="34655"></span><div id="comment-34655" class="comment"><div id="post-34655-score" class="comment-score"></div><div class="comment-text"><p>Still, looks like the packet #119 in your trace is a true retranmission (not an out-of-order), which means it is quite certain that there has been packet loss.</p><p>I can't tell where or why this happened, as that would require to have two simultaneous traces taken at both ends of the conversation.</p><p>By the way, it is next to impossible to simply declare a line "not having packet loss", because with standard Ethernet packet loss is <strong>always</strong> possible.</p></div><div id="comment-34655-info" class="comment-info"><span class="comment-age">(15 Jul '14, 03:47)</span> Jasper ♦♦</div></div><span id="34656"></span><div id="comment-34656" class="comment"><div id="post-34656-score" class="comment-score"></div><div class="comment-text"><blockquote><p>and <strong>no latency</strong> or packet loss <strong>is affordable</strong> to us.</p></blockquote><p>hm.. that link seems to have quite <strong>some</strong> latency ;-))</p></div><div id="comment-34656-info" class="comment-info"><span class="comment-age">(15 Jul '14, 03:54)</span> Kurt Knochner ♦</div></div><span id="34658"></span><div id="comment-34658" class="comment"><div id="post-34658-score" class="comment-score"></div><div class="comment-text"><p>I am taking a capture on the source side as well to see if we get same<br />
re transmissions or multiple DUP ACKs</p></div><div id="comment-34658-info" class="comment-info"><span class="comment-age">(15 Jul '14, 04:18)</span> Rikki</div></div><span id="34704"></span><div id="comment-34704" class="comment"><div id="post-34704-score" class="comment-score"></div><div class="comment-text"><p>You were right, there are about 1-5% packet drops in the link but they are for very short interval &amp; highly intermittent &amp; our monitoring tools did not detect that. Thanks...</p></div><div id="comment-34704-info" class="comment-info"><span class="comment-age">(16 Jul '14, 04:25)</span> Rikki</div></div></div><div id="comment-tools-34642" class="comment-tools"></div><div class="clear"></div><div id="comment-34642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

