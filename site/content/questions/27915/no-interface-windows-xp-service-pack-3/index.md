+++
type = "question"
title = "No interface - Windows XP Service Pack 3"
description = '''I installed WireShark 3.10.3, which has WinPcap 4.1.3 installed. The only interface displayed is &quot;&#92;Device&#92;NPF_GenericDialupAdapter&quot;. I a NIC card using the &quot;Realtek RTL8168C(P)/8111C(P) PCI-E Gigabit Ethernet NIC&quot;. The driver is located in &quot;C:&#92;WINDOWS&#92;system32&#92;DRIVERS&#92;Rtenicxp.sys&quot;. And the file ver...'''
date = "2013-12-08T06:40:00Z"
lastmod = "2013-12-08T10:01:00Z"
weight = 27915
keywords = [ "interface" ]
aliases = [ "/questions/27915" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No interface - Windows XP Service Pack 3](/questions/27915/no-interface-windows-xp-service-pack-3)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27915-score" class="post-score" title="current number of votes">0</div><span id="post-27915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I installed WireShark 3.10.3, which has WinPcap 4.1.3 installed. The only interface displayed is "\Device\NPF_GenericDialupAdapter". I a NIC card using the "Realtek RTL8168C(P)/8111C(P) PCI-E Gigabit Ethernet NIC". The driver is located in "C:\WINDOWS\system32\DRIVERS\Rtenicxp.sys". And the file version is 5.690.0307.2008 built by: WinDDk. How do I get my NIC interface listed, so that I can capture packets?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '13, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/7e7b82e2371d8916e07088665cb64925?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lalawdba&#39;s gravatar image" /><p><span>lalawdba</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lalawdba has no accepted answers">0%</span></p></div></div><div id="comments-container-27915" class="comments-container"><span id="27916"></span><div id="comment-27916" class="comment"><div id="post-27916-score" class="comment-score"></div><div class="comment-text"><p>I am awaiting an answer.</p></div><div id="comment-27916-info" class="comment-info"><span class="comment-age">(08 Dec '13, 06:41)</span> <span class="comment-user userinfo">lalawdba</span></div></div><span id="27920"></span><div id="comment-27920" class="comment"><div id="post-27920-score" class="comment-score"></div><div class="comment-text"><p>Yes my master! See below... ;-)</p></div><div id="comment-27920-info" class="comment-info"><span class="comment-age">(08 Dec '13, 10:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-27915" class="comment-tools"></div><div class="clear"></div><div id="comment-27915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27919"></span>

<div id="answer-container-27919" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27919-score" class="post-score" title="current number of votes">0</div><span id="post-27919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try to restart the WinPcap service as Administrator.</p><p>From an elevated DOS box</p><blockquote><p>sc stop npf<br />
sc start npf<br />
</p></blockquote><p>Then restart Wireshark as <strong>regular</strong> user.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '13, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Dec '13, 10:45</strong> </span></p></div></div><div id="comments-container-27919" class="comments-container"></div><div id="comment-tools-27919" class="comment-tools"></div><div class="clear"></div><div id="comment-27919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

