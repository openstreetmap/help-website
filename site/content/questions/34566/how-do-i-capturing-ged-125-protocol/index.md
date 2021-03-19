+++
type = "question"
title = "How do i capturing GED 125 Protocol ?"
description = '''I am capturing GED 125 protocol and I can see the packets as TCP but not as GED 125 protocol packets. As I saw the wireshark support ged 125 protocol in my version (1.10.8) but still can’t see. How I can see them ?'''
date = "2014-07-10T09:59:00Z"
lastmod = "2014-07-10T11:10:00Z"
weight = 34566
keywords = [ "eranmos" ]
aliases = [ "/questions/34566" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do i capturing GED 125 Protocol ?](/questions/34566/how-do-i-capturing-ged-125-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34566-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am capturing GED 125 protocol and I can see the packets as TCP but not as GED 125 protocol packets. As I saw the wireshark support ged 125 protocol in my version (1.10.8) but still can’t see. How I can see them ?</p></div><div id="question-tags" class="tags-container tags">eranmos</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '14, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/2084b0ed6d02297a44fdcaa676a52e82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eranmos&#39;s gravatar image" /><p>eranmos<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eranmos has no accepted answers">0%</span></p></div></div><div id="comments-container-34566" class="comments-container"></div><div id="comment-tools-34566" class="comment-tools"></div><div class="clear"></div><div id="comment-34566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34568"></span>

<div id="answer-container-34568" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34568-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you try to specify the port number used (Edit -&gt; Preferences -&gt; Protocols -&gt; GED125 -&gt; GED125 TCP port)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '14, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-34568" class="comments-container"><span id="34590"></span><div id="comment-34590" class="comment"><div id="post-34590-score" class="comment-score"></div><div class="comment-text"><p>Yes, but its did't help i still cant see GED packets</p></div><div id="comment-34590-info" class="comment-info"><span class="comment-age">(10 Jul '14, 21:35)</span> eranmos</div></div><span id="34594"></span><div id="comment-34594" class="comment"><div id="post-34594-score" class="comment-score"></div><div class="comment-text"><p>The dissector checks that the packet length is at least 12 bytes long and that the message type is a known value before doing the dissection. Maybe your messages are not supported by the current dissector. Could you share a capture?</p></div><div id="comment-34594-info" class="comment-info"><span class="comment-age">(11 Jul '14, 02:15)</span> Pascal Quantin</div></div></div><div id="comment-tools-34568" class="comment-tools"></div><div class="clear"></div><div id="comment-34568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

