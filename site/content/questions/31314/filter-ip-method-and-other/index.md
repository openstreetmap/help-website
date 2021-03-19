+++
type = "question"
title = "Filter ip, method and other"
description = '''i&#x27;m trying to filter out the ip, the method(GET and POST), and then http data that contains a specific string. The filter looks like this: http.request.method == &quot;GET&quot; &amp;amp;&amp;amp; http.request.method == &quot;POST&quot; &amp;amp;&amp;amp; ip.src == 10.1.5.8 &amp;amp;&amp;amp; http contains &quot;facebook&quot; I want to filter the data...'''
date = "2014-03-31T08:21:00Z"
lastmod = "2014-03-31T08:34:00Z"
weight = 31314
keywords = [ "filter" ]
aliases = [ "/questions/31314" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Filter ip, method and other](/questions/31314/filter-ip-method-and-other)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31314-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i'm trying to filter out the ip, the method(GET and POST), and then http data that contains a specific string. The filter looks like this:</p><p>http.request.method == "GET" &amp;&amp; http.request.method == "POST" &amp;&amp; ip.src == 10.1.5.8 &amp;&amp; http contains "facebook"</p><p>I want to filter the data as specified by the filter, but it don't work. If I use || instead of &amp;&amp;, it works, other IPs are also shown, which is wrong. The only IP that should be listed is 10.1.5.8</p></div><div id="question-tags" class="tags-container tags">filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '14, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/6835e785b2108bd30b2a6e6490f84af9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brajzore&#39;s gravatar image" /><p>brajzore<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brajzore has no accepted answers">0%</span></p></div></div><div id="comments-container-31314" class="comments-container"></div><div id="comment-tools-31314" class="comment-tools"></div><div class="clear"></div><div id="comment-31314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31315"></span>

<div id="answer-container-31315" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31315-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The method can <strong>either</strong> be "GET" or "POST", but you're filtering using "and". Also, you need to put brackets in the right places to force the IP address being part of the transaction.</p><p>Try</p><pre><code>(http.request.method == &quot;GET&quot; or http.request.method == &quot;POST&quot;) and ip.src == 10.1.5.8 and http contains &quot;facebook&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '14, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Mar '14, 08:35</p></div></div><div id="comments-container-31315" class="comments-container"><span id="31316"></span><div id="comment-31316" class="comment"><div id="post-31316-score" class="comment-score"></div><div class="comment-text"><p>But I want to show both GET and POST data in the list? Or should I not do this? Can u explain? :)</p><p>Thank you for your answer.</p></div><div id="comment-31316-info" class="comment-info"><span class="comment-age">(31 Mar '14, 08:39)</span> brajzore</div></div><span id="31317"></span><div id="comment-31317" class="comment"><div id="post-31317-score" class="comment-score"></div><div class="comment-text"><p>With that filter, you will. "OR" in this case means "give me any HTTP request that contains GET or POST", in a boolean way - which means that if any of the two is found it will pass the filter. If you only want one of them you just specify that one, without the other.</p><p>Asking for "GET and POST" doesn't make any since, because it means "give me all requests that are GET and POST <strong>at the same time</strong>", which can never happen - it can only be one or the other.</p></div><div id="comment-31317-info" class="comment-info"><span class="comment-age">(31 Mar '14, 08:42)</span> Jasper ♦♦</div></div><span id="31318"></span><div id="comment-31318" class="comment"><div id="post-31318-score" class="comment-score"></div><div class="comment-text"><p>Okey. Thank you. So if I want the post and the get data, and the ips and the websites that the users have been visited, i should write like this:</p><p>(http.request.method == "GET" or http.request.method == "POST") and (ip.src == 10.1.5.8 or ip.src == 10.1.5.2 or ip.src == 10.1.5.3 or ip.src == 10.1.5.4 or ip.src == 10.1.5.5 or ip.src == 10.1.5.7) and (http contains "facebook" or http contains "reddit")</p></div><div id="comment-31318-info" class="comment-info"><span class="comment-age">(31 Mar '14, 08:48)</span> brajzore</div></div><span id="31319"></span><div id="comment-31319" class="comment"><div id="post-31319-score" class="comment-score"></div><div class="comment-text"><p>yes, you could do something like that. Just try things out, I think you're on the right track.</p></div><div id="comment-31319-info" class="comment-info"><span class="comment-age">(31 Mar '14, 08:57)</span> Jasper ♦♦</div></div></div><div id="comment-tools-31315" class="comment-tools"></div><div class="clear"></div><div id="comment-31315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

