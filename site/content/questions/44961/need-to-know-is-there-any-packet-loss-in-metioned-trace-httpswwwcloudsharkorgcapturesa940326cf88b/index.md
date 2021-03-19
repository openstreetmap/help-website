+++
type = "question"
title = "Need to  know is there any packet loss in metioned trace : https://www.cloudshark.org/captures/a940326cf88b"
description = '''I want to know that is there any packet loss in my trace ... please guide  i captured the trace at client side and when i apply filter &quot;tcp.analysis.retransmission&quot; i get several message in that also some with fast retransmission Also if i can see duplicate ack with its count increasing 5 to 6 when ...'''
date = "2015-08-11T06:45:00Z"
lastmod = "2015-08-12T00:43:00Z"
weight = 44961
keywords = [ "packetloss" ]
aliases = [ "/questions/44961" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need to know is there any packet loss in metioned trace : https://www.cloudshark.org/captures/a940326cf88b](/questions/44961/need-to-know-is-there-any-packet-loss-in-metioned-trace-httpswwwcloudsharkorgcapturesa940326cf88b)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44961-score" class="post-score" title="current number of votes">0</div><span id="post-44961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to know that is there any packet loss in my trace ... please guide</p><p>i captured the trace at client side and when i apply filter "tcp.analysis.retransmission" i get several message in that also some with fast retransmission Also if i can see duplicate ack with its count increasing 5 to 6 when i apply filter tcp.analysis.duplicate_ack i cant see any message when i apply filter " tcp.analysis.ack_lost_segment " or tcp.analysis.lost_segment.</p><p>trace for reference : <a href="https://www.cloudshark.org/captures/a940326cf88b">https://www.cloudshark.org/captures/a940326cf88b</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packetloss" rel="tag" title="see questions tagged &#39;packetloss&#39;">packetloss</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '15, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/5d42867d67503ea73857da49a4b9e1a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vishnupal&#39;s gravatar image" /><p><span>vishnupal</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vishnupal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Aug '15, 22:43</strong> </span></p></div></div><div id="comments-container-44961" class="comments-container"><span id="44962"></span><div id="comment-44962" class="comment"><div id="post-44962-score" class="comment-score"></div><div class="comment-text"><p>You can upload to any place that is publicly accessible: Google Drive, Dropbox, Cloudshark ,etc. I recommend Cloudshark (www.cloudshark.org). When you upload the file, make note of the URL that Cloudshark generates, and then edit your question and paste in the URL.</p></div><div id="comment-44962-info" class="comment-info"><span class="comment-age">(11 Aug '15, 08:26)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-44961" class="comment-tools"></div><div class="clear"></div><div id="comment-44961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44987"></span>

<div id="answer-container-44987" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44987-score" class="post-score" title="current number of votes">1</div><span id="post-44987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, TCP does not retransmit segments just for fun.<br />
So the filter <code>tcp.analysis.retransmission</code> shows you which segments were lost</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '15, 00:26</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-44987" class="comments-container"><span id="44989"></span><div id="comment-44989" class="comment"><div id="post-44989-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Well, TCP does not retransmit segments just for fun.</p></blockquote><p>+1</p></div><div id="comment-44989-info" class="comment-info"><span class="comment-age">(12 Aug '15, 00:43)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-44987" class="comment-tools"></div><div class="clear"></div><div id="comment-44987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

