+++
type = "question"
title = "Filter out duplicate IP addresses"
description = '''Hi Wireshark Community, I was wondering how I could filter out duplicate instances of IP addresses when in a live capture so that only one instance of each different IP is listed. Is this possible and if so how do I go about achieving this? Thanks sNiPel2'''
date = "2015-07-10T19:00:00Z"
lastmod = "2015-07-12T01:02:00Z"
weight = 44068
keywords = [ "capture-filter" ]
aliases = [ "/questions/44068" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter out duplicate IP addresses](/questions/44068/filter-out-duplicate-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44068-score" class="post-score" title="current number of votes">0</div><span id="post-44068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Wireshark Community, I was wondering how I could filter out duplicate instances of IP addresses when in a live capture so that only one instance of each different IP is listed. Is this possible and if so how do I go about achieving this?</p><p>Thanks sNiPel2</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '15, 19:00</strong></p><img src="https://secure.gravatar.com/avatar/d8a6d32acc04714e7a4a2f7bf122e1bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sNiPel2&#39;s gravatar image" /><p><span>sNiPel2</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sNiPel2 has no accepted answers">0%</span></p></div></div><div id="comments-container-44068" class="comments-container"></div><div id="comment-tools-44068" class="comment-tools"></div><div class="clear"></div><div id="comment-44068-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44075"></span>

<div id="answer-container-44075" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44075-score" class="post-score" title="current number of votes">0</div><span id="post-44075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you are looking for a list of the active IP addresses. Use;</p><ul><li>Statistics &gt; Endpoints &gt; IPv4</li></ul><p>This will show all the active endpoints (IP addresses), along with some basic statistics.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '15, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/e4a81395f6649e064887d7f57ee653eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chillypenguin&#39;s gravatar image" /><p><span>chillypenguin</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chillypenguin has one accepted answer">25%</span></p></div></div><div id="comments-container-44075" class="comments-container"><span id="44076"></span><div id="comment-44076" class="comment"><div id="post-44076-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your help this answered my question. Do you know of a way to filter endpoint results?</p></div><div id="comment-44076-info" class="comment-info"><span class="comment-age">(11 Jul '15, 19:02)</span> <span class="comment-user userinfo">sNiPel2</span></div></div><span id="44077"></span><div id="comment-44077" class="comment"><div id="post-44077-score" class="comment-score"></div><div class="comment-text"><p>Just use the "Limit to display filter" option in the bottom left of the Endpoints screen.</p></div><div id="comment-44077-info" class="comment-info"><span class="comment-age">(12 Jul '15, 01:02)</span> <span class="comment-user userinfo">chillypenguin</span></div></div></div><div id="comment-tools-44075" class="comment-tools"></div><div class="clear"></div><div id="comment-44075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

