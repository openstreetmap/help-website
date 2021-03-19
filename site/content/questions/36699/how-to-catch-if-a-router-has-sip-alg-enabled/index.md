+++
type = "question"
title = "How to catch if a router has SIP ALG enabled"
description = '''Hi guys, i cannot touch the customer&#x27;s firewall. I have all the required ports open but my SIP calls are randomly failing. I suspect a hidden (wouldnt be the first time) SIP ALG inspection rule/helper is messing up the calls. Anybody can please advise how to check that? Thanks a million!'''
date = "2014-09-29T09:16:00Z"
lastmod = "2014-09-29T15:25:00Z"
weight = 36699
keywords = [ "alg", "sip" ]
aliases = [ "/questions/36699" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to catch if a router has SIP ALG enabled](/questions/36699/how-to-catch-if-a-router-has-sip-alg-enabled)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36699-score" class="post-score" title="current number of votes">0</div><span id="post-36699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>i cannot touch the customer's firewall. I have all the required ports open but my SIP calls are randomly failing. I suspect a hidden (wouldnt be the first time) SIP ALG inspection rule/helper is messing up the calls. Anybody can please advise how to check that?</p><p>Thanks a million!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-alg" rel="tag" title="see questions tagged &#39;alg&#39;">alg</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '14, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/691f0ea4b3726d9cd3e45e7f6339a2ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dorian%20Marsovina&#39;s gravatar image" /><p><span>Dorian Marso...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dorian Marsovina has no accepted answers">0%</span></p></div></div><div id="comments-container-36699" class="comments-container"></div><div id="comment-tools-36699" class="comment-tools"></div><div class="clear"></div><div id="comment-36699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36713"></span>

<div id="answer-container-36713" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36713-score" class="post-score" title="current number of votes">0</div><span id="post-36713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you able to trace the RTP/RTCP traffic along with SIP for these failed calls, and on both sides of the firewall? If you see SIP in both directions, where the RTP media reaches the firewall on one leg but not on the other, that would be a smoking gun more-or-less that the firewall is dropping the frames.</p><p>Another thing you (or in this case the customer) could do is configure a catch-all UDP port rule at the bottom of their security policy and log it, to see if any UDP traffic between your VoIP systems in the media network are not catching any of the higher permit rules for RTP/RTCP.</p><p>What is the firewall vendor?</p><p>What is the configured firewall logic for this from the customer's perspective, and when you say you're certain you have all the required ports permitted is this a pure IP-level permit policy for the media or are they specifying exact RTP/RTCP port numbers? Have you confirmed in SIP/SDP info and in the RTP media that the failing calls are using the expected ports, and are you absolutely certain you're not forgetting about the corresponding RTCP ports (note: SIP implementations can vary and the original RFCs left a lot of "should"s in there so unless I saw the port number on the wire I wouldn't necessarily assume it to be what I'd want or expect)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '14, 15:25</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-36713" class="comments-container"></div><div id="comment-tools-36713" class="comment-tools"></div><div class="clear"></div><div id="comment-36713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

