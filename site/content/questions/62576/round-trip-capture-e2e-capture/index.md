+++
type = "question"
title = "Round Trip Capture- E2E Capture"
description = '''HI, I want to capture data using wireshark in a way that I can see all the servers/Ip my request is going through and getting the response back to my machine. Currently I only see two Ip&#x27;s ..one is my IP and second is may be webserver of my application. is there a way to capture all the servers invo...'''
date = "2017-07-06T07:43:00Z"
lastmod = "2017-07-06T08:25:00Z"
weight = 62576
keywords = [ "e2e", "roundtrips" ]
aliases = [ "/questions/62576" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Round Trip Capture- E2E Capture](/questions/62576/round-trip-capture-e2e-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62576-score" class="post-score" title="current number of votes">0</div><span id="post-62576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI, I want to capture data using wireshark in a way that I can see all the servers/Ip my request is going through and getting the response back to my machine. Currently I only see two Ip's ..one is my IP and second is may be webserver of my application. is there a way to capture all the servers involved in the request and response?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-e2e" rel="tag" title="see questions tagged &#39;e2e&#39;">e2e</span> <span class="post-tag tag-link-roundtrips" rel="tag" title="see questions tagged &#39;roundtrips&#39;">roundtrips</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '17, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/5297abbb36d8a3bc0c96de06b703e64a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sid147228&#39;s gravatar image" /><p><span>Sid147228</span><br />
<span class="score" title="9 reputation points">9</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sid147228 has no accepted answers">0%</span></p></div></div><div id="comments-container-62576" class="comments-container"></div><div id="comment-tools-62576" class="comment-tools"></div><div class="clear"></div><div id="comment-62576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62578"></span>

<div id="answer-container-62578" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62578-score" class="post-score" title="current number of votes">0</div><span id="post-62578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not from your local PC. You can use <code>traceroute</code> (<code>tracert</code> on Windows) to find through which routers the request was travelling, but it doesn't tell you anything about the path from the server back to you. Also, if the remote IP belongs e.g. to a load balancer, everything behind it is completely hidden for you, i.e. even the traceroute won't show you anything. If you administer the whole network between the client and server and you are looking for a bottleneck, then of course your possibilites are wider, but you still have to capture at different points in the network in order to get relevant information. However, capturing at client and server is the first thing to tell you whether to concentrate at transport network performance or application/server performance. Have a look at <a href="https://ask.wireshark.org/users/145/jasper">@Jasper</a>'s <a href="https://blog.packet-foo.com/2014/07/determining-tcp-initial-round-trip-time/">article on it</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '17, 08:09</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62578" class="comments-container"><span id="62579"></span><div id="comment-62579" class="comment"><div id="post-62579-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sindy. I am not a network administrator and yes our application has multiple LB across layers. We have implemented data in transit strategy to our design and want to see if data is flowing according to the implemented strategy.e.g. Between Client to LB it will be HTTPS ..from LB to App servers it will be HTTP/...similarly at different layers of the application.</p></div><div id="comment-62579-info" class="comment-info"><span class="comment-age">(06 Jul '17, 08:17)</span> <span class="comment-user userinfo">Sid147228</span></div></div><span id="62580"></span><div id="comment-62580" class="comment"><div id="post-62580-score" class="comment-score">1</div><div class="comment-text"><p>Well, in that case you are still in a good position as the servers are yours so you can capture at them. If you sync them well using NTP, you can run <code>tcpdump</code> on all the servers and the client simultaneously and then merge the files to see how the request processing went at different stages. Or just do a lot of subtraction and division when handling the files one by one.</p></div><div id="comment-62580-info" class="comment-info"><span class="comment-age">(06 Jul '17, 08:25)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-62578" class="comment-tools"></div><div class="clear"></div><div id="comment-62578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

