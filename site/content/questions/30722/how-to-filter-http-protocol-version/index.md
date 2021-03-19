+++
type = "question"
title = "How to filter http protocol version?"
description = '''Hi! I suspect some snowiness between two of my servers being due to one of them sending some requests in HTTP 1.0 while the other always replies in HTPP 1.1. To confirm it I listened the traffic between both, but now I would like to filter HTTP 1.0 packets to confirm they are one sided and slow. How...'''
date = "2014-03-12T04:23:00Z"
lastmod = "2014-03-12T06:12:00Z"
weight = 30722
keywords = [ "display-filter", "http", "wireshark" ]
aliases = [ "/questions/30722" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter http protocol version?](/questions/30722/how-to-filter-http-protocol-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30722-score" class="post-score" title="current number of votes">0</div><span id="post-30722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I suspect some snowiness between two of my servers being due to one of them sending some requests in HTTP 1.0 while the other always replies in HTPP 1.1. To confirm it I listened the traffic between both, but now I would like to filter HTTP 1.0 packets to confirm they are one sided and slow.</p><p>How do I do that? I tried "http.request.version 1.0" but wireshark don't want it</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '14, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/b8154fa49a228472e647f361b1580fb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petitpoisson&#39;s gravatar image" /><p><span>petitpoisson</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petitpoisson has no accepted answers">0%</span></p></div></div><div id="comments-container-30722" class="comments-container"></div><div id="comment-tools-30722" class="comment-tools"></div><div class="clear"></div><div id="comment-30722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30724"></span>

<div id="answer-container-30724" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30724-score" class="post-score" title="current number of votes">0</div><span id="post-30724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="petitpoisson has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try something like</p><pre><code>http.request.version == &quot;HTTP/1.0&quot;</code></pre><p>You need to tell Wireshark what you're looking for. You were pretty close though :-)</p><p>Tip: if you want to filter on something that you can see in a packet, right click on that field and select the popup menu option "Apply as Filter -&gt; Selected". It helps a lot.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '14, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Mar '14, 04:38</strong> </span></p></div></div><div id="comments-container-30724" class="comments-container"></div><div id="comment-tools-30724" class="comment-tools"></div><div class="clear"></div><div id="comment-30724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30725"></span>

<div id="answer-container-30725" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30725-score" class="post-score" title="current number of votes">0</div><span id="post-30725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try <code>http.request.version == "HTTP/1.0"</code>.</p><p>You can always work out what the filter should be by right clicking on the field in the Packet Details pane and selecting "Apply as Filter ..." then "Selected".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '14, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-30725" class="comments-container"><span id="30726"></span><div id="comment-30726" class="comment"><div id="post-30726-score" class="comment-score"></div><div class="comment-text"><p>Dup, <span>@Jasper</span>'s too quick today.</p></div><div id="comment-30726-info" class="comment-info"><span class="comment-age">(12 Mar '14, 04:40)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="30728"></span><div id="comment-30728" class="comment"><div id="post-30728-score" class="comment-score"></div><div class="comment-text"><p>Sorry... but almost identical answers, great minds think alike I guess :-)))</p></div><div id="comment-30728-info" class="comment-info"><span class="comment-age">(12 Mar '14, 06:12)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-30725" class="comment-tools"></div><div class="clear"></div><div id="comment-30725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

