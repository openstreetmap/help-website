+++
type = "question"
title = "can&#x27;t see outbound traffic"
description = '''Hi, I&#x27;m trying to troubleshoot network traffic on my Windows machine but WireShark doesn&#x27;t show any outbound traffic. Just the replies. I would really need to see if/when there is traffic sent from the server. Even if there is no reply (all traffic).  Does anyone know how to do this? Not using any f...'''
date = "2016-01-11T04:17:00Z"
lastmod = "2016-01-11T05:06:00Z"
weight = 49075
keywords = [ "to", "outgoing", "outbound" ]
aliases = [ "/questions/49075" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can't see outbound traffic](/questions/49075/cant-see-outbound-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49075-score" class="post-score" title="current number of votes">0</div><span id="post-49075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to troubleshoot network traffic on my Windows machine but WireShark doesn't show any outbound traffic. Just the replies. I would really need to see if/when there is traffic sent from the server. Even if there is no reply (all traffic).</p><p>Does anyone know how to do this?</p><p>Not using any filters etc.</p><p>Details:</p><ul><li>WireShark version: Portable 2.0.1</li><li>WinPcap: 4.1.3</li><li>OS: WIndows Server 2008 R2</li><li>Platform: VMware Virtual Machine</li><li>VMware Tools: 9.0.5</li></ul><p>Thanks</p><p>lakend</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-to" rel="tag" title="see questions tagged &#39;to&#39;">to</span> <span class="post-tag tag-link-outgoing" rel="tag" title="see questions tagged &#39;outgoing&#39;">outgoing</span> <span class="post-tag tag-link-outbound" rel="tag" title="see questions tagged &#39;outbound&#39;">outbound</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '16, 04:17</strong></p><img src="https://secure.gravatar.com/avatar/f92bb93ebc60f3aea4198c28a2a70b9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lakend&#39;s gravatar image" /><p><span>lakend</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lakend has no accepted answers">0%</span></p></div></div><div id="comments-container-49075" class="comments-container"><span id="49078"></span><div id="comment-49078" class="comment"><div id="post-49078-score" class="comment-score"></div><div class="comment-text"><p>Are you capturing at all available interfaces? This typically happens when you capture on a single interface and another one is used for outbound traffic.</p><p>Plus, how do you know that what you can capture are "replies" and not just "inbound traffic"?</p></div><div id="comment-49078-info" class="comment-info"><span class="comment-age">(11 Jan '16, 04:29)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-49075" class="comment-tools"></div><div class="clear"></div><div id="comment-49075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49081"></span>

<div id="answer-container-49081" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49081-score" class="post-score" title="current number of votes">1</div><span id="post-49081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Standard response to this question, did you search first? Search for questions with tags of <a href="https://ask.wireshark.org/tags/outbound/">outbound</a> or <a href="https://ask.wireshark.org/tags/outgoing/">outgoing</a></p><p>Do you have any non-MS AV or VPN software installed?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '16, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49081" class="comments-container"></div><div id="comment-tools-49081" class="comment-tools"></div><div class="clear"></div><div id="comment-49081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

