+++
type = "question"
title = "Filtering out All LTE Transmissions"
description = '''I would like to filter an existing pcap to produce anything that happens in an LTE connection with a phone. What filter should I use to do this? I know there are sub-layers/display filters such as MAC-LTE, PDCP-LTE, etc. but I want all layers/filter types that occur during an LTE transmission. Is th...'''
date = "2016-03-02T10:23:00Z"
lastmod = "2016-03-03T00:52:00Z"
weight = 50684
keywords = [ "transmission", "lte", "display-filter" ]
aliases = [ "/questions/50684" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering out All LTE Transmissions](/questions/50684/filtering-out-all-lte-transmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50684-score" class="post-score" title="current number of votes">0</div><span id="post-50684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to filter an existing pcap to produce anything that happens in an LTE connection with a phone. What filter should I use to do this?</p><p>I know there are sub-layers/display filters such as MAC-LTE, PDCP-LTE, etc. but I want all layers/filter types that occur during an LTE transmission. Is there any way to do this?</p><p>I already know how to filter the data using tshark, I just need the right filter is all.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-transmission" rel="tag" title="see questions tagged &#39;transmission&#39;">transmission</span> <span class="post-tag tag-link-lte" rel="tag" title="see questions tagged &#39;lte&#39;">lte</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '16, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/3a4bc2ba5c09d24f214dc472eb5b7993?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Midimistro&#39;s gravatar image" /><p><span>Midimistro</span><br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Midimistro has one accepted answer">50%</span></p></div></div><div id="comments-container-50684" class="comments-container"></div><div id="comment-tools-50684" class="comment-tools"></div><div class="clear"></div><div id="comment-50684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50700"></span>

<div id="answer-container-50700" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50700-score" class="post-score" title="current number of votes">0</div><span id="post-50700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you looking for protocols used on the air interface between an eNB and a UE? If yes, the involved protocols are the following display filters: mac-lte, rlc-lte, pdcp-lte, lte_rrc, nas-eps.</p><p>If you are capturing in network, you could also be interested by the following display filters: s1ap, x2ap, gtp, gtpv2,...</p><p>If you use a proprietary solution to capture packets, you might have other dissectors (and thus display filters) on top of the ones I listed above (that are part of the standard Wireshark source code).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '16, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-50700" class="comments-container"></div><div id="comment-tools-50700" class="comment-tools"></div><div class="clear"></div><div id="comment-50700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

