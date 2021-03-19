+++
type = "question"
title = "Decode As (DHCP)"
description = '''I tried to decode UDP packets on port 4011 as DHCP. But the Decode As dialog box shows DHCPv6 twice without DHCP option. I&#x27;m wondering if this is a bug?'''
date = "2013-11-03T06:50:00Z"
lastmod = "2013-11-04T05:32:00Z"
weight = 26639
keywords = [ "dhcp" ]
aliases = [ "/questions/26639" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Decode As (DHCP)](/questions/26639/decode-as-dhcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26639-score" class="post-score" title="current number of votes">0</div><span id="post-26639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to decode UDP packets on port 4011 as DHCP. But the Decode As dialog box shows DHCPv6 twice without DHCP option. I'm wondering if this is a bug?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '13, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/320ac4c4e2341d050e184d52cc5206cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="orion&#39;s gravatar image" /><p><span>orion</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="orion has no accepted answers">0%</span></p></div></div><div id="comments-container-26639" class="comments-container"></div><div id="comment-tools-26639" class="comment-tools"></div><div class="clear"></div><div id="comment-26639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26648"></span>

<div id="answer-container-26648" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26648-score" class="post-score" title="current number of votes">3</div><span id="post-26648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="orion has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's not a bug. DHCPv4 decoding is done by the BootP disector, so the filter and decoder name is "bootp". If you look for it in the "Decode as" section for UDP ports you'll see "BOOTP/DHCP".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '13, 20:37</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Nov '13, 20:39</strong> </span></p></div></div><div id="comments-container-26648" class="comments-container"><span id="26649"></span><div id="comment-26649" class="comment"><div id="post-26649-score" class="comment-score"></div><div class="comment-text"><p>You're right, I see them. Thanks a lot.</p></div><div id="comment-26649-info" class="comment-info"><span class="comment-age">(03 Nov '13, 23:33)</span> <span class="comment-user userinfo">orion</span></div></div><span id="26661"></span><div id="comment-26661" class="comment"><div id="post-26661-score" class="comment-score"></div><div class="comment-text"><p><span>@orion</span>: if a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-26661-info" class="comment-info"><span class="comment-age">(04 Nov '13, 05:32)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26648" class="comment-tools"></div><div class="clear"></div><div id="comment-26648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

