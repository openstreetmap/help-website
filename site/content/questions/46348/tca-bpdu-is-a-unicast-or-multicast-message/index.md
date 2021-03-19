+++
type = "question"
title = "TCA BPDU is a unicast or multicast message??"
description = '''As shown below TCA BPDU is a multicast message, if it&#x27;s true, why the other switches in the scenario do not receive this message?? Scenario:  WireShark packet capture on ESW1 (root switch) shows TCA BPDU has been sent as multicast message:  WireShark packet capture on another switch (ESW2) at the sa...'''
date = "2015-10-03T08:39:00Z"
lastmod = "2015-10-03T11:21:00Z"
weight = 46348
keywords = [ "bpdu", "stp", "tca" ]
aliases = [ "/questions/46348" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCA BPDU is a unicast or multicast message??](/questions/46348/tca-bpdu-is-a-unicast-or-multicast-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46348-score" class="post-score" title="current number of votes">0</div><span id="post-46348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As shown below TCA BPDU is a multicast message, if it's true, why the other switches in the scenario do not receive this message??</p><p>Scenario:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/sc_9d2Dnqc.png" alt="alt text" /></p><p>WireShark packet capture on <strong>ESW1</strong> (root switch) shows TCA BPDU has been sent as <strong>multicast</strong> message:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/TCA_Aa9prAa.png" alt="alt text" /></p><p>WireShark packet capture on another switch (ESW2) at the same time :</p><p><img src="https://osqa-ask.wireshark.org/upfiles/TCA2_VsVF8G6.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bpdu" rel="tag" title="see questions tagged &#39;bpdu&#39;">bpdu</span> <span class="post-tag tag-link-stp" rel="tag" title="see questions tagged &#39;stp&#39;">stp</span> <span class="post-tag tag-link-tca" rel="tag" title="see questions tagged &#39;tca&#39;">tca</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '15, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/8752544ec453a6d8e08fdde4d465eca7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MehranBazgir&#39;s gravatar image" /><p><span>MehranBazgir</span><br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MehranBazgir has no accepted answers">0%</span></p></img></div></div><div id="comments-container-46348" class="comments-container"></div><div id="comment-tools-46348" class="comment-tools"></div><div class="clear"></div><div id="comment-46348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46349"></span>

<div id="answer-container-46349" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46349-score" class="post-score" title="current number of votes">1</div><span id="post-46349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Because the TCN is sent to the Root Bridge and the Root Bridge acknowledges the TCN with an TCA only on that link. The ESW4 receives the TCA but do not need to forward it, because he is the receiver.</p><p>More Details can be found here: <a href="http://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/12013-17.html">http://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/12013-17.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '15, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Oct '15, 11:39</strong> </span></p></div></div><div id="comments-container-46349" class="comments-container"></div><div id="comment-tools-46349" class="comment-tools"></div><div class="clear"></div><div id="comment-46349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

