+++
type = "question"
title = "tcp.length 1460 for downloads"
description = '''If the TCP length is always set to 1460 for a file tranfer download, but it&#x27;s up to 10 times that amount for the same file uploaded, what could be a contributing factor?'''
date = "2012-04-09T12:35:00Z"
lastmod = "2012-04-10T06:58:00Z"
weight = 10034
keywords = [ "length", "1460", "tcp" ]
aliases = [ "/questions/10034" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tcp.length 1460 for downloads](/questions/10034/tcplength-1460-for-downloads)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10034-score" class="post-score" title="current number of votes">0</div><span id="post-10034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If the TCP length is always set to 1460 for a file tranfer download, but it's up to 10 times that amount for the same file uploaded, what could be a contributing factor?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-1460" rel="tag" title="see questions tagged &#39;1460&#39;">1460</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '12, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/42c25e25fa835c0a2bbed16e02eba0d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dij&#39;s gravatar image" /><p><span>dij</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dij has no accepted answers">0%</span></p></div></div><div id="comments-container-10034" class="comments-container"></div><div id="comment-tools-10034" class="comment-tools"></div><div class="clear"></div><div id="comment-10034-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10035"></span>

<div id="answer-container-10035" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10035-score" class="post-score" title="current number of votes">3</div><span id="post-10035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dij has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's probably because you're capturing on the uploading PC, and that PC uses LSO (Large Send Offloading) to have the network interface card handle the segmentation into 1460 byte segments. Wireshark captures the packet before it is sliced into the real segments - this is one of the side effects you need to cope with if you're not using a 3rd PC to capture the traffic between two nodes.</p><p>Incoming packets (your "download") are already segmented by the other node, so they're correct.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '12, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10035" class="comments-container"><span id="10037"></span><div id="comment-10037" class="comment"><div id="post-10037-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Incoming packets (your "download") are already segmented by the other node, so they're correct.</p></blockquote><p>(Unless they're getting <em>reassembled</em> by the network adapter and handed to the host as a larger-than-segment-size chunk. This might not be happening with the adapter dij's using, but it might happen with other adapters.)</p></div><div id="comment-10037-info" class="comment-info"><span class="comment-age">(09 Apr '12, 23:35)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="10039"></span><div id="comment-10039" class="comment"><div id="post-10039-score" class="comment-score"></div><div class="comment-text"><p>I know; I just decided to not further confuse dij for the moment by adding more complexity to the explanation :-)</p></div><div id="comment-10039-info" class="comment-info"><span class="comment-age">(10 Apr '12, 00:43)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="10043"></span><div id="comment-10043" class="comment"><div id="post-10043-score" class="comment-score"></div><div class="comment-text"><p>thank you very much!</p></div><div id="comment-10043-info" class="comment-info"><span class="comment-age">(10 Apr '12, 06:58)</span> <span class="comment-user userinfo">dij</span></div></div></div><div id="comment-tools-10035" class="comment-tools"></div><div class="clear"></div><div id="comment-10035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

