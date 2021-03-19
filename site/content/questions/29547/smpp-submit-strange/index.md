+++
type = "question"
title = "SMPP Submit strange"
description = '''Hi ! I cannot explain myself the following case. http://cloudshark.org/captures/4de5550070f7 The SubmitSM packet was sent directly in one session (using Java application) making even socket flush after, but when I examine it in a Wireshark, I can see last 4 bytes (74203430) displayed, but not marked...'''
date = "2014-02-08T03:23:00Z"
lastmod = "2014-02-10T08:27:00Z"
weight = 29547
keywords = [ "smpp", "java", "stack" ]
aliases = [ "/questions/29547" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SMPP Submit strange](/questions/29547/smpp-submit-strange)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29547-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi !</p><p>I cannot explain myself the following case. <a href="http://cloudshark.org/captures/4de5550070f7">http://cloudshark.org/captures/4de5550070f7</a></p><p>The SubmitSM packet was sent directly in one session (using Java application) making even socket flush after, but when I examine it in a Wireshark, I can see last 4 bytes (74203430) displayed, but not marked as part of the SubmitSM. However, they are marked as the begining of the next SMPP packet (Unbind). That's why the SMPP server cannot decode properly Unbind, since the first 4 bytes are wrong. Within the application log, I can see proper byte stream to be sent on the stream (including missing last 4 bytes) Do we have a problem with Tcp stack as Java is not dealing with Windows etc, just puts stream to the system Tcp stack ?</p></div><div id="question-tags" class="tags-container tags">smpp java stack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '14, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/0b74304b7f2b17bae10c78728f8b874b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Miskulinko&#39;s gravatar image" /><p>Miskulinko<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Miskulinko has no accepted answers">0%</span></p></div></div><div id="comments-container-29547" class="comments-container"></div><div id="comment-tools-29547" class="comment-tools"></div><div class="clear"></div><div id="comment-29547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29639"></span>

<div id="answer-container-29639" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29639-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like the Length field of the SMPP is incorrect: in frame 9 if you expand the SMPP tree you can see that it is 678 bytes. If you click on the SMPP line in the protocol-tree (middle) frame you'll see in the bottom status line that Wireshark thinks the SMPP is 678 bytes long but in the hex (bottom) pane you'll see this does not include the final 4 bytes.</p><p>So: the sender has a problem. It needs to include those final 4 bytes in the smpp length field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '14, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-29639" class="comments-container"><span id="29641"></span><div id="comment-29641" class="comment"><div id="post-29641-score" class="comment-score"></div><div class="comment-text"><p>Uh, ive checked several times, but was concentrated on payload tlv length which is correct (630), not the header length :) Thx</p></div><div id="comment-29641-info" class="comment-info"><span class="comment-age">(10 Feb '14, 09:15)</span> Miskulinko</div></div></div><div id="comment-tools-29639" class="comment-tools"></div><div class="clear"></div><div id="comment-29639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

