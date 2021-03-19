+++
type = "question"
title = "How do you capture FCoE frames?"
description = '''After capturing on a CNA CEE interface, The only FCoE packet that I see is a FIP advertisement. I don&#x27;t see any Flogis, Plogis, etc. Even if I disable and enable the CNA while the capture is running. Are there specific steps to take to properly capture FCoE traffic?'''
date = "2011-01-14T11:49:00Z"
lastmod = "2011-01-14T13:19:00Z"
weight = 1752
keywords = [ "fcoe", "cna" ]
aliases = [ "/questions/1752" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do you capture FCoE frames?](/questions/1752/how-do-you-capture-fcoe-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1752-score" class="post-score" title="current number of votes">0</div><span id="post-1752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After capturing on a CNA CEE interface, The only FCoE packet that I see is a FIP advertisement. I don't see any Flogis, Plogis, etc. Even if I disable and enable the CNA while the capture is running. Are there specific steps to take to properly capture FCoE traffic?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fcoe" rel="tag" title="see questions tagged &#39;fcoe&#39;">fcoe</span> <span class="post-tag tag-link-cna" rel="tag" title="see questions tagged &#39;cna&#39;">cna</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '11, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/2362cd2186a47e8bd20d50910f02501b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Khenson&#39;s gravatar image" /><p><span>Khenson</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Khenson has no accepted answers">0%</span></p></div></div><div id="comments-container-1752" class="comments-container"></div><div id="comment-tools-1752" class="comment-tools"></div><div class="clear"></div><div id="comment-1752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1753"></span>

<div id="answer-container-1753" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1753-score" class="post-score" title="current number of votes">0</div><span id="post-1753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would assume that you are running this capture on the host and there is some TOE or something that could be causing issues. I'm not that familiar with integrating FCoE with the host. What I'd try to do is capture it on an independent machine using a span or monitor port on the Ethernet Switch. That should allow you to avoid any issues with acceleration hardware on the NIC.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '11, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1753" class="comments-container"><span id="1754"></span><div id="comment-1754" class="comment"><div id="post-1754-score" class="comment-score"></div><div class="comment-text"><p>The CNA is an Emulex 10102FX CEE adapter. It has two devices that drive the same physical transciever. I think that is where my problem is. Since the FCoE device is using a different driver than the NIC on the same CNA, Wireshark is looking at the network interface which isn't driving the FCoE part of the card, so Wireshark doesn't see it.</p></div><div id="comment-1754-info" class="comment-info"><span class="comment-age">(14 Jan '11, 13:19)</span> <span class="comment-user userinfo">Khenson</span></div></div></div><div id="comment-tools-1753" class="comment-tools"></div><div class="clear"></div><div id="comment-1753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

