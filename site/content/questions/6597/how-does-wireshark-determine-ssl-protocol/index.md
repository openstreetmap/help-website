+++
type = "question"
title = "How does wireshark determine SSL protocol?"
description = '''I&#x27;m looking at a capture taken from production, and following through a particular tcp.stream. Excluding the ack packets, most are listed as SSL, but a few are listed as TLSv1. What is wireshark looking at when it makes this distinction. Additional information: to keep the file from getting out of h...'''
date = "2011-09-27T08:09:00Z"
lastmod = "2011-09-27T13:57:00Z"
weight = 6597
keywords = [ "ssl" ]
aliases = [ "/questions/6597" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How does wireshark determine SSL protocol?](/questions/6597/how-does-wireshark-determine-ssl-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6597-score" class="post-score" title="current number of votes">0</div><span id="post-6597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking at a capture taken from production, and following through a particular tcp.stream. Excluding the ack packets, most are listed as SSL, but a few are listed as TLSv1. What is wireshark looking at when it makes this distinction.</p><p>Additional information: to keep the file from getting out of hand, I'm recording the packets with a snaplen == 68.</p><p>The actual traffic in this case is coming from IE9 to our web server. The web server logs report all of the requests as TLSv1.</p><p>One particularly interesting example corresponds to a file upload - the http request body has a lot of bytes. In wireshark, I see</p><pre><code>SSL    715
SSL   1434
TLSv1 1434
TLSv1 1434
TLSv1 ...
TLSv1 1434
TLSv1 1247
SSL   1115</code></pre><p>The reply by the server is marked SSL.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '11, 08:09</strong></p><img src="https://secure.gravatar.com/avatar/8911a98abd797fd928ab9f115becd08c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanilSuits&#39;s gravatar image" /><p><span>DanilSuits</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanilSuits has no accepted answers">0%</span></p></div></div><div id="comments-container-6597" class="comments-container"></div><div id="comment-tools-6597" class="comment-tools"></div><div class="clear"></div><div id="comment-6597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6600"></span>

<div id="answer-container-6600" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6600-score" class="post-score" title="current number of votes">1</div><span id="post-6600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This comment in the dissector code may shine some light on the subject:</p><pre><code>    / Initialize the protocol column; we&#39;ll set it later when we
     * figure out what flavor of SSL it is (assuming we don&#39;t
     * throw an exception before we get the chance to do so). /</code></pre><p>So once it has a look at the record layer version it decides what to put in, i.s.o. "SSL"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '11, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6600" class="comments-container"></div><div id="comment-tools-6600" class="comment-tools"></div><div class="clear"></div><div id="comment-6600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

