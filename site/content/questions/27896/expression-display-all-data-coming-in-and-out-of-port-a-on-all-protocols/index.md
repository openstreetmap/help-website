+++
type = "question"
title = "Expression: Display all data coming in AND out of port A on ALL protocols"
description = '''I&#x27;m having a devil of a time discovering an expression for displaying only packets which have come to from one particular port using any protocol. Any help?'''
date = "2013-12-07T11:12:00Z"
lastmod = "2013-12-08T10:13:00Z"
weight = 27896
keywords = [ "any", "expressions", "data", "port", "all" ]
aliases = [ "/questions/27896" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Expression: Display all data coming in AND out of port A on ALL protocols](/questions/27896/expression-display-all-data-coming-in-and-out-of-port-a-on-all-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27896-score" class="post-score" title="current number of votes">0</div><span id="post-27896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm having a devil of a time discovering an expression for displaying only packets which have come to from one particular port using any protocol. Any help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-any" rel="tag" title="see questions tagged &#39;any&#39;">any</span> <span class="post-tag tag-link-expressions" rel="tag" title="see questions tagged &#39;expressions&#39;">expressions</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-all" rel="tag" title="see questions tagged &#39;all&#39;">all</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '13, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/22c0ce7dfcca02abe029772610d051a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JourneyJay&#39;s gravatar image" /><p><span>JourneyJay</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JourneyJay has no accepted answers">0%</span></p></div></div><div id="comments-container-27896" class="comments-container"></div><div id="comment-tools-27896" class="comment-tools"></div><div class="clear"></div><div id="comment-27896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27897"></span>

<div id="answer-container-27897" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27897-score" class="post-score" title="current number of votes">0</div><span id="post-27897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A port is generally associated with tcp or udp so <code>tcp.port == xxx || udp.port == xxx</code></p><p><strong>Correction:</strong></p><p>As the user seems to really mean <strong>all</strong> protocols that have a notion of a "port", then the answer is not really. The Wireshark display filters refer to fields within a container (such as a protocol) so you would have to enumerate all possible containers that have a field corresponding to the notion of a port (and in same it may not be named as such). There is no "global" field named port such that all dissectors would match their internal notion of a port to the global one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '13, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Dec '13, 05:07</strong> </span></p></div></div><div id="comments-container-27897" class="comments-container"><span id="27902"></span><div id="comment-27902" class="comment"><div id="post-27902-score" class="comment-score"></div><div class="comment-text"><p>These aren't the only options.</p></div><div id="comment-27902-info" class="comment-info"><span class="comment-age">(07 Dec '13, 17:17)</span> <span class="comment-user userinfo">JourneyJay</span></div></div><span id="27903"></span><div id="comment-27903" class="comment"><div id="post-27903-score" class="comment-score"></div><div class="comment-text"><p>Yes, there's also the SCTP port.</p><p>There are, however, many many many protocols that don't have "ports" in the sense of a TCP or UDP or SCTP port. If that's the sense in which you meant port, there obviously does not exist, and obviously cannot ever exist, "packets which have come to from one particular port using any protocol", as "any protocol" includes protocols that have no notion of a "port".</p></div><div id="comment-27903-info" class="comment-info"><span class="comment-age">(07 Dec '13, 18:09)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="27921"></span><div id="comment-27921" class="comment"><div id="post-27921-score" class="comment-score"></div><div class="comment-text"><p>@JouneyJay: Could you please add more information? What are you trying to find with such a filter?</p></div><div id="comment-27921-info" class="comment-info"><span class="comment-age">(08 Dec '13, 10:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-27897" class="comment-tools"></div><div class="clear"></div><div id="comment-27897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

