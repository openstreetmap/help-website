+++
type = "question"
title = "HTTP response time filter"
description = '''Let&#x27;s say I have a capture from a typical web server. The capture contains a lot of HTTP requests and responses.  Is it possible to create a filter to display only HTTP traffic with a response time higher than X seconds?  By &quot;response time&quot; I mean the amount of time from the client completes the HTT...'''
date = "2011-07-04T15:21:00Z"
lastmod = "2011-07-08T11:09:00Z"
weight = 4900
keywords = [ "http" ]
aliases = [ "/questions/4900" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP response time filter](/questions/4900/http-response-time-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4900-score" class="post-score" title="current number of votes">0</div><span id="post-4900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Let's say I have a capture from a typical web server. The capture contains a lot of HTTP requests and responses. Is it possible to create a filter to display only HTTP traffic with a response time higher than X seconds? By "response time" I mean the amount of time from the client completes the HTTP request to the server starts (or possibly finishes) serving the HTTP response.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '11, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/102ac441341af0e7772eb274954d1237?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aatoga&#39;s gravatar image" /><p><span>aatoga</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aatoga has no accepted answers">0%</span></p></div></div><div id="comments-container-4900" class="comments-container"></div><div id="comment-tools-4900" class="comment-tools"></div><div class="clear"></div><div id="comment-4900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4922"></span>

<div id="answer-container-4922" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4922-score" class="post-score" title="current number of votes">3</div><span id="post-4922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A while ago I have started to work on a field that would measure the time between the request and the first packet of the response, the typical server time (not including network transport). However, this is more complicated than expected due to HTTP pipelining. I hope to find some time in the future to work on this again.</p><p>In the mean time, the TCP timestamps are your best bet. You have to enable TCP timestamps in the TCP protocol preferences, but the you could use something like:</p><pre><code>http.response and tcp.time_delta&gt;X</code></pre><p>For this to work, you need to disable reassembly (so that the first response packet is listed instead of the last packet of the response). This must be done in the TCP protocol preferences too (deselect "allow subdissector to reassemble tcp streams".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '11, 00:45</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4922" class="comments-container"><span id="4961"></span><div id="comment-4961" class="comment"><div id="post-4961-score" class="comment-score"></div><div class="comment-text"><p>Thanks, this helped med a lot. Turns out I was using an ancient version of Wireshark (&lt;1.0), so I must admit I was not aware of the tcp.time_* fields and the "Calculate conversation timestamps" option. Actually, in many cases the delta between e.g. a SYN and a SYN ACK is useful as well, so I don't need to look all the way up to the HTTP level. Your tip does the trick for me :)</p></div><div id="comment-4961-info" class="comment-info"><span class="comment-age">(08 Jul '11, 11:09)</span> <span class="comment-user userinfo">aatoga</span></div></div></div><div id="comment-tools-4922" class="comment-tools"></div><div class="clear"></div><div id="comment-4922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4904"></span>

<div id="answer-container-4904" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4904-score" class="post-score" title="current number of votes">0</div><span id="post-4904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could start of with writing down what would be needed to "see" these times:</p><ol><li>first you would need a beginning: maybe starts with a HTTP request, you could use (http.request.method == "GET") your starting HTTP requests could be different</li><li>secondly there should be a moment when the file is on the client, the clients browser might answer : (http.response.code == 200)</li><li>Now to how to combine and see the time difference?</li></ol><p>You could combine both filters to this: http and (http.request.method == "GET" || http.response.code == 200) and see GET's en OK's, you could then right-click a GET &gt; set Time Reference and see how much time it took to the concerning OK, but that seems tedious...</p><p>Maybe this works better:</p><p>frame.time_delta_displayed &gt; 1 and (http.request.method == "GET" || http.response.code == 200)</p><p>This would result in displaying all GET's and OK's and see if there is a time delta bigger then 1 sec between them Your time display format should be "seconds since previous displayed packet" and you would still have to manually connect the dots...eg does this GET belong to this OK?</p><p>Marc</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '11, 05:15</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p><span>Marc</span><br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jul '11, 00:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-4904" class="comments-container"></div><div id="comment-tools-4904" class="comment-tools"></div><div class="clear"></div><div id="comment-4904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

