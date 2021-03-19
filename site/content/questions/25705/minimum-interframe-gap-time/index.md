+++
type = "question"
title = "Minimum Interframe gap time"
description = '''Is it possible for Wireshark to indicate that the interframe gap on a network does meet the minimum time of 96 bit times?'''
date = "2013-10-07T06:54:00Z"
lastmod = "2013-10-07T07:42:00Z"
weight = 25705
keywords = [ "interframegap" ]
aliases = [ "/questions/25705" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Minimum Interframe gap time](/questions/25705/minimum-interframe-gap-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25705-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible for Wireshark to indicate that the interframe gap on a network does meet the minimum time of 96 bit times?</p></div><div id="question-tags" class="tags-container tags">interframegap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '13, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/4e4e41ac4508d0215f27fa2a1124fd2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CGooden&#39;s gravatar image" /><p>CGooden<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CGooden has no accepted answers">0%</span></p></div></div><div id="comments-container-25705" class="comments-container"></div><div id="comment-tools-25705" class="comment-tools"></div><div class="clear"></div><div id="comment-25705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25707"></span>

<div id="answer-container-25707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25707-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, you can obviously look at the time stamps and check if the delta is smaller that the interframe gap (0.096 µs for 1Gig/s). <strong>However</strong> if the accuracy of your time source is not good enough, or the timestamping was done in the kernel (by libpcap and/or winpcap - which may be much later than the packet arrived and it may also vary due to scheduling in the kernel) and <strong>not</strong> on the NIC, you cannot trust the time stamp.</p><p>So, to answer your question: No, there is <strong>no reliable</strong> way in Wireshark to check if the sending system did use a correct interframe gap. The reason is: Most of the time you don't have time stamps that are good enough for that decision.</p><p><strong>++ UPDATE ++</strong></p><p>There are more problems: The NIC might even drop a frame that comes in to fast (IFG lower than it should be), so the sniffer will not see the frame at all.</p><p>There might be hardware analyzers that are able to deal with IFG problems, however I don't know any.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Oct '13, 16:28</p></div></div><div id="comments-container-25707" class="comments-container"><span id="25719"></span><div id="comment-25719" class="comment"><div id="post-25719-score" class="comment-score"></div><div class="comment-text"><p>That's exactly what I did not want to hear, but is the answer I expected.</p><p>(Converted to a comment to match the way this site works. Please see the FaQ).</p></div><div id="comment-25719-info" class="comment-info"><span class="comment-age">(07 Oct '13, 10:15)</span> CGooden</div></div><span id="25721"></span><div id="comment-25721" class="comment"><div id="post-25721-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry to have told you ;-))</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-25721-info" class="comment-info"><span class="comment-age">(07 Oct '13, 10:48)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25707" class="comment-tools"></div><div class="clear"></div><div id="comment-25707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

