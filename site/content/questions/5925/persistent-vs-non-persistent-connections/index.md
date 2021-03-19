+++
type = "question"
title = "Persistent vs non persistent connections"
description = '''I am trying to verify which type of connection is being made - persistent or non persistent. I see the following and if someone could explain what each of these mean Keep-Alive: 300  Connections:keep-alive  Keep-Alive: timeout=max=100 '''
date = "2011-08-29T12:44:00Z"
lastmod = "2011-08-29T16:14:00Z"
weight = 5925
keywords = [ "persistent" ]
aliases = [ "/questions/5925" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Persistent vs non persistent connections](/questions/5925/persistent-vs-non-persistent-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5925-score" class="post-score" title="current number of votes">0</div><span id="post-5925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to verify which type of connection is being made - persistent or non persistent. I see the following and if someone could explain what each of these mean</p><pre><code>Keep-Alive: 300 
Connections:keep-alive

Keep-Alive: timeout=max=100</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-persistent" rel="tag" title="see questions tagged &#39;persistent&#39;">persistent</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '11, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/3e299bad7429c818cdba48831a8d89e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maxx&#39;s gravatar image" /><p><span>Maxx</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maxx has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Aug '11, 16:09</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-5925" class="comments-container"></div><div id="comment-tools-5925" class="comment-tools"></div><div class="clear"></div><div id="comment-5925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5933"></span>

<div id="answer-container-5933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5933-score" class="post-score" title="current number of votes">1</div><span id="post-5933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If this is exactly what was in the trace file, the connection will not be persistent as the headers are not correct. The correct header would be:</p><pre><code>Connection: keep-alive</code></pre><p>Please note that:</p><ul><li><p>In HTTP/1.0 the connection is <em>non-persistent</em> by default <strong>unless</strong> you add the "Connection: keep-alive" header in the http request. After that, it is up to the server to choose whether to use a persistent connection or not</p></li><li><p>In HTTP/1.1 the connection is <em>persistent</em> by default <strong>unless</strong> you add the "Connection: close" header to the http request. In which case the server has to close the connection the requested object has been sent.</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '11, 16:14</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5933" class="comments-container"></div><div id="comment-tools-5933" class="comment-tools"></div><div class="clear"></div><div id="comment-5933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

