+++
type = "question"
title = "Cannot capture Local traffic"
description = '''Dear friend, when I Open Interface select dialog I saw two interfaces 1)Marvell Yukon Ethernet controller fe80::8847.... 2)Microsoft 192.168.1.2 I want to capture local traffic 127.0.0.1:5000 to 127.0.0.1 simple terminal applications But I can&#x27;t see any on above interfaces!!! I runned wireshark 1.6....'''
date = "2012-01-19T22:17:00Z"
lastmod = "2012-01-20T03:38:00Z"
weight = 8491
keywords = [ "traffic", "local" ]
aliases = [ "/questions/8491" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot capture Local traffic](/questions/8491/cannot-capture-local-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8491-score" class="post-score" title="current number of votes">0</div><span id="post-8491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear friend, when I Open Interface select dialog I saw two interfaces 1)Marvell Yukon Ethernet controller fe80::8847.... 2)Microsoft 192.168.1.2 I want to capture local traffic 127.0.0.1:5000 to 127.0.0.1 simple terminal applications But I can't see any on above interfaces!!! I runned wireshark 1.6.4 on win7 64x professional I have same problem on many computers in my work. what should I do? Thanks Tarvirdi</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '12, 22:17</strong></p><img src="https://secure.gravatar.com/avatar/fb0a958221cff71be78a0325f627bebf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tarvirdi&#39;s gravatar image" /><p><span>Tarvirdi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tarvirdi has no accepted answers">0%</span></p></div></div><div id="comments-container-8491" class="comments-container"><span id="8492"></span><div id="comment-8492" class="comment"><div id="post-8492-score" class="comment-score"></div><div class="comment-text"><p>Dear Friends, I Installed Microsoft loopback adapter and assigned 10.0.0.10 255.255.255.0 10.0.0.1 settings. But installed adapter not shown in available interfaces! what can I do? Thanks Tarvirdi</p></div><div id="comment-8492-info" class="comment-info"><span class="comment-age">(20 Jan '12, 00:08)</span> <span class="comment-user userinfo">Tarvirdi</span></div></div></div><div id="comment-tools-8491" class="comment-tools"></div><div class="clear"></div><div id="comment-8491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8494"></span>

<div id="answer-container-8494" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8494-score" class="post-score" title="current number of votes">0</div><span id="post-8494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Capturing loopback traffic on windows is awkward. Have you read and followed the various instructions on the <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">Capture Loopback</a> page on the Wiki?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '12, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-8494" class="comments-container"><span id="8497"></span><div id="comment-8497" class="comment"><div id="post-8497-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Yes I read, as I mentioned. I installed LoopBack driver and now after restart windows I saw it in drivers's List. I disabled my physical LAN card also. By selecting LoopBack driver, still I can't capture 127.0.0.1 traffic. I set IP 10.0.0.10 and mask 255.255.255.0. I done all in blue box said by mitra (note for XP, but mine is win7) Thanks for your help</p></div><div id="comment-8497-info" class="comment-info"><span class="comment-age">(20 Jan '12, 03:05)</span> <span class="comment-user userinfo">Tarvirdi</span></div></div><span id="8500"></span><div id="comment-8500" class="comment"><div id="post-8500-score" class="comment-score"></div><div class="comment-text"><p>I converted your "answer" to a comment as that is the way this site works, see the <a href="http://ask.wireshark.org/faq/">FAQ</a> for details.</p><p>I can only suggest you try more of the options discussed on the page.</p></div><div id="comment-8500-info" class="comment-info"><span class="comment-age">(20 Jan '12, 03:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-8494" class="comment-tools"></div><div class="clear"></div><div id="comment-8494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

