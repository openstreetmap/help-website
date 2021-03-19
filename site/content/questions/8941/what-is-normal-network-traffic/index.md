+++
type = "question"
title = "What is normal network traffic?"
description = '''What is the normal network traffic to open a webpage?'''
date = "2012-02-09T19:25:00Z"
lastmod = "2012-02-10T13:38:00Z"
weight = 8941
keywords = [ "webpage", "http", "traffic", "analysis" ]
aliases = [ "/questions/8941" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [What is normal network traffic?](/questions/8941/what-is-normal-network-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8941-score" class="post-score" title="current number of votes">0</div><span id="post-8941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the normal network traffic to open a webpage?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-webpage" rel="tag" title="see questions tagged &#39;webpage&#39;">webpage</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '12, 19:25</strong></p><img src="https://secure.gravatar.com/avatar/61eb24ce851fd326d509fef810d804d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="susan&#39;s gravatar image" /><p><span>susan</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="susan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Feb '12, 13:39</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8941" class="comments-container"></div><div id="comment-tools-8941" class="comment-tools"></div><div class="clear"></div><div id="comment-8941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="8958"></span>

<div id="answer-container-8958" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8958-score" class="post-score" title="current number of votes">1</div><span id="post-8958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As the other answers have noted, there is no one simple definition of "normal" when it comes to web traffic. There are a few things that will be common to each attempt, but the number of things that not only can, but very likely will, be different make it difficult to describe exactly what will constitute normal web traffic. That said, there are a few things that <em>should</em> (but will not necessarily) happen in a usual transaction:</p><ul><li>There will be a DNS lookup, possibly preceded by some ARP requests <sup>[<a href="http://tools.ietf.org/html/rfc826">RFC 726</a>]</sup>, for the given domain name (unless it is already cached) <sup>[<a href="http://www.ietf.org/rfc/rfc1035.txt">RFC 1035</a>]</sup></li><li>There will be a TCP connection established (as @dixglata notes, this will be the <code>[SYN]</code>, <code>[SYN/ACK]</code>, <code>[ACK]</code> sequence in most cases), usually over port 80 or 443 (as @jaz0nj4ckal noted) <sup>[<a href="http://www.ietf.org/rfc/rfc793.txt">RFC 793</a>]</sup></li><li>There will be <em>at least</em> one <code>HTTP GET</code> request <sup>[<a href="http://www.ietf.org/rfc/rfc2616.txt">RFC 2616</a>]</sup></li><li>The server will transfer the content of the page</li></ul><p>The overall amount of traffic you see will depend on many things (e.g. does the <code>GET</code> result in a redirect? does the page contain a flash animation, Java applet, or other content that may transfer data between the browser server or even other servers? etc.). What kind of traffic you capture may also look different (e.g. does the connection leverage TLS <sup>[<a href="http://www.ietf.org/rfc/rfc2246.txt">RFC 2246</a>]</sup>? Is the server configured for a port other than 80 or 443? is the connection proxied? etc.).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '12, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-8958" class="comments-container"></div><div id="comment-tools-8958" class="comment-tools"></div><div class="clear"></div><div id="comment-8958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8954"></span>

<div id="answer-container-8954" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8954-score" class="post-score" title="current number of votes">0</div><span id="post-8954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Normal is a very broad word when it comes to answering this question; however, HTTP (port: 80) and HTTPS (port: 443) will be used to open most webpages.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '12, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/ae897e20625df9db38d37f98126bf90e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaz0nj4ckal&#39;s gravatar image" /><p><span>jaz0nj4ckal</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaz0nj4ckal has no accepted answers">0%</span></p></div></div><div id="comments-container-8954" class="comments-container"></div><div id="comment-tools-8954" class="comment-tools"></div><div class="clear"></div><div id="comment-8954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8956"></span>

<div id="answer-container-8956" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8956-score" class="post-score" title="current number of votes">0</div><span id="post-8956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>look for packets with [SYN], [SYN, ACK] and [ACK] the tcp handshake</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '12, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/b119c1795a1d51f2d7d0aa7af9c54a9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dixglata&#39;s gravatar image" /><p><span>dixglata</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dixglata has no accepted answers">0%</span></p></div></div><div id="comments-container-8956" class="comments-container"></div><div id="comment-tools-8956" class="comment-tools"></div><div class="clear"></div><div id="comment-8956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

