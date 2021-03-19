+++
type = "question"
title = "ICMP reply packets are exist, but cmd say “Request timed out”"
description = '''I try to ping my device. My device supports ARP answer and ICMP reply. I send ICMP request from CMD. My device receive one and fast reply to back. WireShark see my reply, but CMD doesn&#x27;t see and print &quot;No reply&quot;. How can I resolve this problem?  Here it&#x27;s the CMD output The screenshot above is just ...'''
date = "2017-07-25T05:11:00Z"
lastmod = "2017-07-25T05:19:00Z"
weight = 63086
keywords = [ "icmp", "cmd", "ping", "echo" ]
aliases = [ "/questions/63086" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [ICMP reply packets are exist, but cmd say “Request timed out”](/questions/63086/icmp-reply-packets-are-exist-but-cmd-say-request-timed-out)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63086-score" class="post-score" title="current number of votes">0</div><span id="post-63086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I try to ping my device. My device supports ARP answer and ICMP reply. I send ICMP request from CMD. My device receive one and fast reply to back. WireShark see my reply, but CMD doesn't see and print "No reply". How can I resolve this problem?</p><hr /><p>Here it's the <a href="https://yadi.sk/i/FluLu0sf3LPQgZ">CMD output</a></p><p>The screenshot above is just an illustration of "Request timed out".</p><hr /><p>Also the <a href="https://yadi.sk/d/GGEipSzL3LPJk2">WireShark capture</a> is attached.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-cmd" rel="tag" title="see questions tagged &#39;cmd&#39;">cmd</span> <span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span> <span class="post-tag tag-link-echo" rel="tag" title="see questions tagged &#39;echo&#39;">echo</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '17, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/de3c61cd1cd74757814c55554c8cd612?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CatWithoutBoots&#39;s gravatar image" /><p><span>CatWithoutBoots</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CatWithoutBoots has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jul '17, 05:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-63086" class="comments-container"></div><div id="comment-tools-63086" class="comment-tools"></div><div class="clear"></div><div id="comment-63086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63087"></span>

<div id="answer-container-63087" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63087-score" class="post-score" title="current number of votes">0</div><span id="post-63087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="CatWithoutBoots has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I was expecting the IPv4 header checksum to be correct on the ICMP reply at least.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '17, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-63087" class="comments-container"></div><div id="comment-tools-63087" class="comment-tools"></div><div class="clear"></div><div id="comment-63087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

