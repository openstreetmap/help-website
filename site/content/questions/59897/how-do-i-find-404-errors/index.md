+++
type = "question"
title = "How do I find 404 errors?"
description = '''There is a sporadic issue I&#x27;m troubleshooting and I&#x27;m somewhat new to detailed capture filtering. I ran a tcpdump on a loadbalancer, and analyzing the pcap file output produced, we are looking to find a forwarded request to servers in a pool from the load balancer. The end client is getting sporadic...'''
date = "2017-03-07T10:58:00Z"
lastmod = "2017-03-07T12:05:00Z"
weight = 59897
keywords = [ "filter", "capture", "404", "pcap", "uri" ]
aliases = [ "/questions/59897" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I find 404 errors?](/questions/59897/how-do-i-find-404-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59897-score" class="post-score" title="current number of votes">0</div><span id="post-59897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>There is a sporadic issue I'm troubleshooting and I'm somewhat new to detailed capture filtering. I ran a tcpdump on a loadbalancer, and analyzing the pcap file output produced, we are looking to find a forwarded request to servers in a pool from the load balancer. The end client is getting sporadic 404 not found errors, and they appear to be coming from the pool members, based on logs, but we need to prove that and find out why it's happening. We suspect it is because the forwarded URI is malformed leaving the load balancer going to the pool members, but I can't seem to filter properly to see if that's true or not. They are https requests, but should be unencrypted between the LB and pool hosts. I need to know how to find out what the URI looks like going to the pool members and anything about the 404 errors coming back. Can someone assist?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-404" rel="tag" title="see questions tagged &#39;404&#39;">404</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-uri" rel="tag" title="see questions tagged &#39;uri&#39;">uri</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '17, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/19a1636cc5e1b53b71bb7d0b31f6249f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aj1&#39;s gravatar image" /><p><span>aj1</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aj1 has no accepted answers">0%</span></p></div></div><div id="comments-container-59897" class="comments-container"></div><div id="comment-tools-59897" class="comment-tools"></div><div class="clear"></div><div id="comment-59897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59901"></span>

<div id="answer-container-59901" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59901-score" class="post-score" title="current number of votes">1</div><span id="post-59901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can try to filter for the response codes you're looking for, in your case 404:</p><pre><code>http.response.code==404</code></pre><p>If there are non-encrypted HTTP requests/replies in your capture you should be able to see them. After that you can use the popup menu on each of the resulting packets and "Follow TCP stream" to see a whole conversation, inclusing the HTTP request.</p><p>If the filter doesn't give you any results you can try</p><pre><code>http.response.code</code></pre><p>to check if there are any response codes in clear text at all. If not, you probably do not have HTTP connections in your capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '17, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-59901" class="comments-container"></div><div id="comment-tools-59901" class="comment-tools"></div><div class="clear"></div><div id="comment-59901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

