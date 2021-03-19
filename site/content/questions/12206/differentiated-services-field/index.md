+++
type = "question"
title = "Differentiated Services Field?"
description = '''Does anyone know what this is using port 1433 for? Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport)) Total Length: 732 Identification: 0x0599 (1433)'''
date = "2012-06-26T13:06:00Z"
lastmod = "2012-06-27T03:44:00Z"
weight = 12206
keywords = [ "services", "field", "differentiated", "identification" ]
aliases = [ "/questions/12206" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Differentiated Services Field?](/questions/12206/differentiated-services-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12206-score" class="post-score" title="current number of votes">0</div><span id="post-12206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anyone know what this is using port 1433 for?</p><p>Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport)) Total Length: 732 Identification: 0x0599 (1433)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-services" rel="tag" title="see questions tagged &#39;services&#39;">services</span> <span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-differentiated" rel="tag" title="see questions tagged &#39;differentiated&#39;">differentiated</span> <span class="post-tag tag-link-identification" rel="tag" title="see questions tagged &#39;identification&#39;">identification</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '12, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/991ca2397da5a59c06ac8972abe3cb0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wshark6&#39;s gravatar image" /><p><span>Wshark6</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wshark6 has no accepted answers">0%</span></p></div></div><div id="comments-container-12206" class="comments-container"></div><div id="comment-tools-12206" class="comment-tools"></div><div class="clear"></div><div id="comment-12206-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12230"></span>

<div id="answer-container-12230" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12230-score" class="post-score" title="current number of votes">2</div><span id="post-12230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Identification field is simply a unique ID applied to each packet a host sends on a particular connection. It is generally only useful if a packet needs to fragmented (say by a router) - each fragment will retain the original Identification. It allows the receiving host to know how to reassemble the fragments.</p><p>It doesn't have anything to do with DiffServ (it appears after it), and doesn't tell you anything about the port or protocol that the packet is associated with.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '12, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-12230" class="comments-container"></div><div id="comment-tools-12230" class="comment-tools"></div><div class="clear"></div><div id="comment-12230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

