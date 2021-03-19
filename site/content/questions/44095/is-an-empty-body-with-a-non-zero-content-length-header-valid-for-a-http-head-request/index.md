+++
type = "question"
title = "Is an empty body with a non-zero Content-Length header valid for a HTTP HEAD request?"
description = '''I encountered a pcap file involving HTTP HEAD request. The response (packet 6) has a HTTP header Content-Length being 163 but there is no body. Packet 7 is another request. Wonder if this is a valid HTTP transaction. File: https://www.cloudshark.org/captures/f5349e67266c Thanks. '''
date = "2015-07-13T07:24:00Z"
lastmod = "2015-07-20T10:50:00Z"
weight = 44095
keywords = [ "http" ]
aliases = [ "/questions/44095" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is an empty body with a non-zero Content-Length header valid for a HTTP HEAD request?](/questions/44095/is-an-empty-body-with-a-non-zero-content-length-header-valid-for-a-http-head-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44095-score" class="post-score" title="current number of votes">0</div><span id="post-44095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I encountered a <a href="https://www.cloudshark.org/captures/f5349e67266c">pcap</a> file involving HTTP HEAD request. The response (packet 6) has a HTTP header Content-Length being 163 but there is no body. Packet 7 is another request. Wonder if this is a valid HTTP transaction.</p><p>File: <a href="https://www.cloudshark.org/captures/f5349e67266c">https://www.cloudshark.org/captures/f5349e67266c</a></p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '15, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jul '15, 05:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span></p></div></div><div id="comments-container-44095" class="comments-container"></div><div id="comment-tools-44095" class="comment-tools"></div><div class="clear"></div><div id="comment-44095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44119"></span>

<div id="answer-container-44119" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44119-score" class="post-score" title="current number of votes">1</div><span id="post-44119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it is. This HTTP feature is intended for just that, getting URL meta information (like its size) from the source without actually getting the object. It would defeat its purpose if the Content-Length would be 0 then.</p><p>See also <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '15, 22:10</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-44119" class="comments-container"><span id="44311"></span><div id="comment-44311" class="comment"><div id="post-44311-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@jaap</span>! It makes sense.</p></div><div id="comment-44311-info" class="comment-info"><span class="comment-age">(20 Jul '15, 10:50)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-44119" class="comment-tools"></div><div class="clear"></div><div id="comment-44119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

