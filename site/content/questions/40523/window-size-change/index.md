+++
type = "question"
title = "Window Size change"
description = '''hi guys, i captured a trace while accessing a web page and there&#x27;s one thing that i don&#x27;t understand.  in the first SYN sent from my station to the web server i see a 8192 bytes Window Size and 140 MSS. in the SYN,ACK from the web server WS=65535 and MSS=1452.  The ACK from my station advertises it&#x27;...'''
date = "2015-03-12T15:37:00Z"
lastmod = "2015-03-12T20:57:00Z"
weight = 40523
keywords = [ "window", "size" ]
aliases = [ "/questions/40523" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Window Size change](/questions/40523/window-size-change)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40523-score" class="post-score" title="current number of votes">0</div><span id="post-40523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi guys,</p><p>i captured a trace while accessing a web page and there's one thing that i don't understand.</p><p>in the first SYN sent from my station to the web server i see a 8192 bytes Window Size and 140 MSS. in the SYN,ACK from the web server WS=65535 and MSS=1452.</p><p>The ACK from my station advertises it's WS now to = 4356 and right after the ACK i receive an TCP Window Update from the web server with a WS of 2064 ????</p><p>why such a big decrease if no actual data has been transferred yet?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '15, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p><span>adasko</span><br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div></div><div id="comments-container-40523" class="comments-container"></div><div id="comment-tools-40523" class="comment-tools"></div><div class="clear"></div><div id="comment-40523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40531"></span>

<div id="answer-container-40531" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40531-score" class="post-score" title="current number of votes">0</div><span id="post-40531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Lower window sizes conserve memory, so an operating systems may decide to use small sizes. And as long as it doesn't prevent the sender from continuing to send more data, it's not a problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '15, 20:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40531" class="comments-container"></div><div id="comment-tools-40531" class="comment-tools"></div><div class="clear"></div><div id="comment-40531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

