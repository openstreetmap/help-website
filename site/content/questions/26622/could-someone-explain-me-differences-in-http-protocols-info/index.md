+++
type = "question"
title = "Could someone explain me differences in HTTP protocol&#x27;s info?"
description = '''Excuse me, if this question will be totally &quot;noob&quot; , but I am actually a newbie in capturing packets with Wireshark. But back to my question. I&#x27;m currently capturing packets ingoing and outgoing from my iPad. I filtered them to show only HTTP protocols. And now I get hundreds of different protocols ...'''
date = "2013-11-01T12:42:00Z"
lastmod = "2013-11-03T03:03:00Z"
weight = 26622
keywords = [ "post", "http", "notify", "protocols", "get" ]
aliases = [ "/questions/26622" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Could someone explain me differences in HTTP protocol's info?](/questions/26622/could-someone-explain-me-differences-in-http-protocols-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26622-score" class="post-score" title="current number of votes">0</div><span id="post-26622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Excuse me, if this question will be totally "noob" , but I am actually a newbie in capturing packets with Wireshark. But back to my question. I'm currently capturing packets ingoing and outgoing from my iPad. I filtered them to show only HTTP protocols. And now I get hundreds of different protocols with info. And the info tab near this protocols says it's 'POST', 'NOTIFY' or 'GET' . Ok I tried to find some information about all this three types. I got that 'GET' are protocols that is going to me. In that case 'POST' will be protocols that are going from me. What's with 'NOTIFY' then? Like I said, I'm just starting my adventure here, so would really appreciate any help, hints, advice !</p><p>Thanks in advance!</p><p>JustZet</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-post" rel="tag" title="see questions tagged &#39;post&#39;">post</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-notify" rel="tag" title="see questions tagged &#39;notify&#39;">notify</span> <span class="post-tag tag-link-protocols" rel="tag" title="see questions tagged &#39;protocols&#39;">protocols</span> <span class="post-tag tag-link-get" rel="tag" title="see questions tagged &#39;get&#39;">get</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '13, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/f3b560d7df61bdde10d08873911d57e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JustZet&#39;s gravatar image" /><p><span>JustZet</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JustZet has no accepted answers">0%</span></p></div></div><div id="comments-container-26622" class="comments-container"></div><div id="comment-tools-26622" class="comment-tools"></div><div class="clear"></div><div id="comment-26622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26623"></span>

<div id="answer-container-26623" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26623-score" class="post-score" title="current number of votes">1</div><span id="post-26623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JustZet has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"GET", "POST", "NOTIFY" etc are not protocols, they're HTTP requests. HTTP requests are commands that the client sends to the server, and which will trigger a response from the server. The difference between "GET" (the most common request type) and "POST" is that GET by design requests content without modifying server state, while "POST" transfers form values that are processed on the server side.</p><p>"NOTIFY" is probably part of the SSDP (Simple Service Discovery Protocol) which uses HTTP requests to do Universal Plug &amp; Play detection of other services available in the network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '13, 15:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-26623" class="comments-container"><span id="26624"></span><div id="comment-26624" class="comment"><div id="post-26624-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot Jasper!</p></div><div id="comment-26624-info" class="comment-info"><span class="comment-age">(02 Nov '13, 04:02)</span> <span class="comment-user userinfo">JustZet</span></div></div><span id="26630"></span><div id="comment-26630" class="comment"><div id="post-26630-score" class="comment-score"></div><div class="comment-text"><p>One (grammatical) "correction", "GET", "POST", "NOTIFY" are actually "request methods" which of course make it possible to make HTTP requests.</p><p>You can find more info on the character of each request method in chapter 9 of the <a href="http://tools.ietf.org/html/rfc2616#section-9">HTTP 1.1 RFC</a>.</p></div><div id="comment-26630-info" class="comment-info"><span class="comment-age">(03 Nov '13, 03:03)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-26623" class="comment-tools"></div><div class="clear"></div><div id="comment-26623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

