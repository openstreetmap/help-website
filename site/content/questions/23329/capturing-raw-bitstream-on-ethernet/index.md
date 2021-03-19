+++
type = "question"
title = "Capturing raw bitstream on Ethernet"
description = '''According to 802.3-2012 (Section 3.3), each octet of a MAC frame is transmitted Least Significant Bit (LSB) first, with the exception of the FCS. Therefore, a DEST MAC of 00:00:00:00:00:02 would be transmitted on the line as 02 00 00 00 00 00 – or 0010 0000 0000 0000 0000 0000 (in Binary). Is there ...'''
date = "2013-07-24T08:55:00Z"
lastmod = "2013-07-24T09:24:00Z"
weight = 23329
keywords = [ "bitstream", "raw", "ethernet" ]
aliases = [ "/questions/23329" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing raw bitstream on Ethernet](/questions/23329/capturing-raw-bitstream-on-ethernet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23329-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>According to 802.3-2012 (Section 3.3), each octet of a MAC frame is transmitted Least Significant Bit (LSB) first, with the exception of the FCS. Therefore, a DEST MAC of 00:00:00:00:00:02 would be transmitted on the line as 02 00 00 00 00 00 – or 0010 0000 0000 0000 0000 0000 (in Binary). Is there a way to capture the raw binary or hex bit stream as it exists on the wire?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">bitstream raw ethernet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '13, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/88ad52dda879b36120672877f21efc0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddimarco&#39;s gravatar image" /><p>ddimarco<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddimarco has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jul '13, 14:20</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-23329" class="comments-container"></div><div id="comment-tools-23329" class="comment-tools"></div><div class="clear"></div><div id="comment-23329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23330"></span>

<div id="answer-container-23330" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23330-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think it can be done with normal Ethernet equipment, because in my point of view the transmission is signaling technology that will not be visible on the digital side of the card and only happens "on the wire". So if you want to see how the raw bits are transferred you'll probably need to use a layer 1 analysis device that can show you what is happening on the physical wire.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '13, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-23330" class="comments-container"><span id="23331"></span><div id="comment-23331" class="comment"><div id="post-23331-score" class="comment-score"></div><div class="comment-text"><p>Makes sense, thanks for your feedback</p></div><div id="comment-23331-info" class="comment-info"><span class="comment-age">(24 Jul '13, 09:26)</span> ddimarco</div></div><span id="23332"></span><div id="comment-23332" class="comment"><div id="post-23332-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-23332-info" class="comment-info"><span class="comment-age">(24 Jul '13, 09:59)</span> grahamb ♦</div></div></div><div id="comment-tools-23330" class="comment-tools"></div><div class="clear"></div><div id="comment-23330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

