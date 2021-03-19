+++
type = "question"
title = "filtering inner header"
description = '''I have captured thousand of ERSPAN packets which are in the form of IP IP tunnels. I would like to filter the packets which have ttl == 1 on inner IP header. But wireshark filters on the outer header as well. Is there any way to create filter for for the inside header ONLY. THanks Umair'''
date = "2012-11-22T01:57:00Z"
lastmod = "2012-11-22T05:44:00Z"
weight = 16196
keywords = [ "filter", "ipip", "erspan" ]
aliases = [ "/questions/16196" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [filtering inner header](/questions/16196/filtering-inner-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16196-score" class="post-score" title="current number of votes">0</div><span id="post-16196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have captured thousand of ERSPAN packets which are in the form of IP IP tunnels. I would like to filter the packets which have ttl == 1 on inner IP header. But wireshark filters on the outer header as well. Is there any way to create filter for for the inside header ONLY.</p><p>THanks</p><p>Umair</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ipip" rel="tag" title="see questions tagged &#39;ipip&#39;">ipip</span> <span class="post-tag tag-link-erspan" rel="tag" title="see questions tagged &#39;erspan&#39;">erspan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '12, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/0289a2a275051a8de121e030140cf799?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umairali&#39;s gravatar image" /><p><span>umairali</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umairali has no accepted answers">0%</span></p></div></div><div id="comments-container-16196" class="comments-container"></div><div id="comment-tools-16196" class="comment-tools"></div><div class="clear"></div><div id="comment-16196-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16203"></span>

<div id="answer-container-16203" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16203-score" class="post-score" title="current number of votes">1</div><span id="post-16203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think there is a normal IP TTL filter that can be applied selectively on only just one of the IP layers.</p><p>But maybe you can work with an offset filter, for example "frame[46] == 1" (if offset 46 is the byte where the TTL of the inner IP layer is found - the offset needs to be written as a decimal value). This approach requires all frames to have the same header length before the IP layer you want to filter on, because otherwise the offset are not always the same.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '12, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '12, 04:33</strong> </span></p></div></div><div id="comments-container-16203" class="comments-container"><span id="16211"></span><div id="comment-16211" class="comment"><div id="post-16211-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper ... I get the point. Probably, I have to add IP to avoid arp, and other non IP packets etc</p><p>frame[72] == 1 &amp;&amp; ip</p></div><div id="comment-16211-info" class="comment-info"><span class="comment-age">(22 Nov '12, 05:38)</span> <span class="comment-user userinfo">umairali</span></div></div><span id="16212"></span><div id="comment-16212" class="comment"><div id="post-16212-score" class="comment-score"></div><div class="comment-text"><p>[i converted your answer to a comment to make it easier to tell question and answers apart]</p><p>yes, adding "ip" is probably a good idea. BTW, if you like my answer you can accept it with the checkmark button on the left :-)</p></div><div id="comment-16212-info" class="comment-info"><span class="comment-age">(22 Nov '12, 05:44)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-16203" class="comment-tools"></div><div class="clear"></div><div id="comment-16203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

