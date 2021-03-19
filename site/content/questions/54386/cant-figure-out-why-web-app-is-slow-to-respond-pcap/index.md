+++
type = "question"
title = "Can&#x27;t figure out why web app is slow to respond - pcap"
description = '''Hi FOlks: My company uses a 3rd party cloud-application. When performing a function using the web interface browser, the application server doesnt seem to respond, but it really does. It takes over a minute for it to give any visual indication that it&#x27;s working, but it does complete.  The 3rd party ...'''
date = "2016-07-27T17:18:00Z"
lastmod = "2016-07-31T13:12:00Z"
weight = 54386
keywords = [ "web", "slow", "transaction" ]
aliases = [ "/questions/54386" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't figure out why web app is slow to respond - pcap](/questions/54386/cant-figure-out-why-web-app-is-slow-to-respond-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54386-score" class="post-score" title="current number of votes">0</div><span id="post-54386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi FOlks:</p><p>My company uses a 3rd party cloud-application. When performing a function using the web interface browser, the application server doesnt seem to respond, but it really does. It takes over a minute for it to give any visual indication that it's working, but it does complete.</p><p>The 3rd party vendor doesn't have any idea why it's running like this.</p><p>I used Wireshark to capture the browser&lt;-&gt;server request/response. There's some things about not being able to re-assemble the packets, but I'm not able to fully figure out what is really happening.</p><ol><li>User goes to the browser, logs into the App. WOrks fine.</li><li>User navigates to page to look up a container. Enters the container ID, presses enter.</li><li>The browser appears to do nothing. Eventually, a web busy spinner shows up (after about 40 seconds).</li><li>A few seconds after that (maybe around 1 minute total), the app responds.</li></ol><p>There are no errors. The web application actually completes the request. but it should be happening in &lt; 1 to 2 seconds, not 50-75 seconds.</p><p>The third party vendor says their server is running fine. I used Wireshark to capture a brief session. In looking at it, there's some re-assembly errors. But I honestly can't figure this out.</p><p>I'm trying to understand if there's something on our end (our internal network), or if there's something at issue with their web server/network. I'm trying to not finger point, but simply root cause.</p><p>Would anyone be willing to look at this capture and see if anything obvious stands out? I see a reassembly issue, but outside of that, I don't see anything obvious. Then again, I'm hardly an expert here.</p><p>THe web appliation never gives an error. It always completes. But in looking at the capture it almost seems like sockets between client and server are started then closed, then started on a different client ephemeral port.</p><p>The destination server in the PCAP is 192.243.221.226, port 80. My client is 192.168.1.117.</p><p>I'm not trying to prove that there's a fault on their end or an application issue. I'm just trying to see if there's some fundamental networking issue / problem first. THe web application is an IIS app on port 80.</p><p>I've uploaded the PCAP to the url in the body of this post. ANyways, I honestly can't understand what is happening. Looks like there's a re-assembly error (at #1934), an RST (#1051). But by the end of the capture, the web page finally finishes the request without error.</p><p>I could really use some help. Like I said, not trying to point fingers. Just trying to root cause.</p><p>If there's anyone who'd be willing to look at the capture and let me know what you think, I'd be so grateful.</p><p><a href="http://www64.zippyshare.com/v/FnCzHmEj/file.html">capture file</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-web" rel="tag" title="see questions tagged &#39;web&#39;">web</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-transaction" rel="tag" title="see questions tagged &#39;transaction&#39;">transaction</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '16, 17:18</strong></p><img src="https://secure.gravatar.com/avatar/3b177d137909ec089a096b0b93e7ac62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bubbawny&#39;s gravatar image" /><p><span>bubbawny</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bubbawny has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jul '16, 02:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54386" class="comments-container"></div><div id="comment-tools-54386" class="comment-tools"></div><div class="clear"></div><div id="comment-54386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54473"></span>

<div id="answer-container-54473" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54473-score" class="post-score" title="current number of votes">1</div><span id="post-54473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The answer to this problem lies in the http.data field which identifies the GMT timestamp when the web server was sending the HTTP OK messages. The client's clock doesn't seem too far away from the time-stamp at the server by looking at these packets, approximately 200 ms. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_087_hWyDSKW.png" alt="alt text" /> For non-delayed responses, the answer from the server http.time arrives between 50 - 80 ms.<br />
Not so for the first and the last requests (26) on the tcp.stream==0 which arrive 2.3 and 22 seconds after the requests.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_084.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_086_URuIsWs.png" alt="alt text" /> The timestamps in the http.date indicate that the server was already late sending those. For me clearly a slow HTTP server ( or Application server or backend systems)</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '16, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div></div><div id="comments-container-54473" class="comments-container"></div><div id="comment-tools-54473" class="comment-tools"></div><div class="clear"></div><div id="comment-54473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

