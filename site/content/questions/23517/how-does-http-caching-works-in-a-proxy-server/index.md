+++
type = "question"
title = "How does HTTP caching works in a proxy server?"
description = '''It&#x27;s my understanding that caching is one of the main utilities of a proxy server. I&#x27;m currently trying to develop a simple one and I would like to know exactly how caching works. Intuitively I think that it&#x27;s basically an association between a request and a response. For example: for the following ...'''
date = "2013-08-02T06:44:00Z"
lastmod = "2013-08-08T06:38:00Z"
weight = 23517
keywords = [ "http-caching", "http", "proxy" ]
aliases = [ "/questions/23517" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How does HTTP caching works in a proxy server?](/questions/23517/how-does-http-caching-works-in-a-proxy-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23517-score" class="post-score" title="current number of votes">0</div><span id="post-23517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It's my understanding that caching is one of the main utilities of a proxy server. I'm currently trying to develop a simple one and I would like to know exactly how caching works.</p><p>Intuitively I think that it's basically an association between a request and a response. For example: for the following request: "GET google.com" you have the following response: "HTTP/1.0 200 OK..."</p><p>That way, whenever the proxy server receives a request for that URL he can reply with the cached response (I'm not really worried right now about when to serve the cached response and when to actually send the request to the real destination).</p><p>What I don't understand is how to establish the association between a request and a response since the HTTP response doesn't have any field saying "hey this is the response you get when you request the X URL" (or does it?).</p><p>Should I get this information by analyzing the underlying protocols? If so, how?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http-caching" rel="tag" title="see questions tagged &#39;http-caching&#39;">http-caching</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '13, 06:44</strong></p><img src="https://secure.gravatar.com/avatar/99d0d825bd23c5dda4b75085f5e2cc9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andr%C3%A9%20Louren%C3%A7o&#39;s gravatar image" /><p><span>André Lourenço</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="André Lourenço has no accepted answers">0%</span></p></div></div><div id="comments-container-23517" class="comments-container"><span id="23536"></span><div id="comment-23536" class="comment"><div id="post-23536-score" class="comment-score"></div><div class="comment-text"><p>Not really a wireshark question, you should look for answers on a support forum more appropriate, e.g. for squid.</p></div><div id="comment-23536-info" class="comment-info"><span class="comment-age">(04 Aug '13, 08:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-23517" class="comment-tools"></div><div class="clear"></div><div id="comment-23517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23644"></span>

<div id="answer-container-23644" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23644-score" class="post-score" title="current number of votes">0</div><span id="post-23644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This question is actually unrelated to Wireshark (as <span>@grahamb</span> already wrote). To understand HTTP caching, you need a profound understanding of the HTTP protocol and <strong>that's where Wireshark can help</strong> (besides online resources and books).</p><p>Wireshark Tutorial for HTTP (I did <strong>not</strong> check the quality of the content!)</p><blockquote><p><a href="http://www.youtube.com/watch?v=0wx9xfbe7B4">http://www.youtube.com/watch?v=0wx9xfbe7B4</a></p></blockquote><p>BTW: searching google for <strong>http caching explained</strong> returns these URLs and many more.</p><blockquote><p><a href="https://devcenter.heroku.com/articles/increasing-application-performance-with-http-cache-headers">https://devcenter.heroku.com/articles/increasing-application-performance-with-http-cache-headers</a><br />
<a href="http://www.mnot.net/cache_docs/">http://www.mnot.net/cache_docs/</a><br />
<a href="http://www.kaizou.org/2009/02/http-caching-explained/">http://www.kaizou.org/2009/02/http-caching-explained/</a><br />
<a href="http://tech.deepumohan.com/2012/08/http-caching-explained.html">http://tech.deepumohan.com/2012/08/http-caching-explained.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 06:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-23644" class="comments-container"></div><div id="comment-tools-23644" class="comment-tools"></div><div class="clear"></div><div id="comment-23644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

