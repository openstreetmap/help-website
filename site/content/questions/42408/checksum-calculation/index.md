+++
type = "question"
title = "Checksum calculation"
description = '''lets say I have client &amp;gt; firewall &amp;gt; server . firewall is doing nat , my concern is how the checksum at network layer will be calculated . when client will generate a packet and put the checksum info into the header , since the firewall is doing NAT it will change IP header info so when the ser...'''
date = "2015-05-14T23:57:00Z"
lastmod = "2015-05-15T08:57:00Z"
weight = 42408
keywords = [ "checksum" ]
aliases = [ "/questions/42408" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Checksum calculation](/questions/42408/checksum-calculation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42408-score" class="post-score" title="current number of votes">0</div><span id="post-42408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>lets say I have client &gt; firewall &gt; server .</p><p>firewall is doing nat , my concern is how the checksum at network layer will be calculated . when client will generate a packet and put the checksum info into the header , since the firewall is doing NAT it will change IP header info so when the server receives will it discard the packet because of checksum ??</p><p>or is it job of the firewall or any other network device to update the checksum as well if its doing NAT ? if this is the case then in real world scenario , checksum will be calculated and updated ( if required ) at each network device .</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '15, 23:57</strong></p><img src="https://secure.gravatar.com/avatar/962349492f305ec7bae240fb8c9996ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tech%20round&#39;s gravatar image" /><p><span>tech round</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tech round has no accepted answers">0%</span></p></div></div><div id="comments-container-42408" class="comments-container"></div><div id="comment-tools-42408" class="comment-tools"></div><div class="clear"></div><div id="comment-42408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42409"></span>

<div id="answer-container-42409" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42409-score" class="post-score" title="current number of votes">2</div><span id="post-42409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>or is it job of the firewall or any other network device to update the checksum as well if its doing NAT ?</p></blockquote><p>Yes.</p><blockquote><p>checksum will be calculated and updated ( if required ) at each network device .</p></blockquote><p>every network device that changes parts of the frame, that require recalculation of the checksum, will HAVE TO generate a new checksum, otherwise it will cause massive problems on the network.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '15, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 May '15, 01:20</strong> </span></p></div></div><div id="comments-container-42409" class="comments-container"><span id="42416"></span><div id="comment-42416" class="comment"><div id="post-42416-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt :)</p></div><div id="comment-42416-info" class="comment-info"><span class="comment-age">(15 May '15, 07:25)</span> <span class="comment-user userinfo">tech round</span></div></div><span id="42423"></span><div id="comment-42423" class="comment"><div id="post-42423-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-42423-info" class="comment-info"><span class="comment-age">(15 May '15, 08:57)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-42409" class="comment-tools"></div><div class="clear"></div><div id="comment-42409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

