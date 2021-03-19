+++
type = "question"
title = "Web page size"
description = '''One of our internal web pages keeps getting slower and slower and I believe it&#x27;s due to it keeps getting bigger and bigger. Anyone know of a way to easily determine a web page size? I&#x27;m using &quot;tcp.reassembled.length&quot; now but was wondering if there is a better way. thanks,'''
date = "2010-11-17T06:28:00Z"
lastmod = "2010-11-17T16:29:00Z"
weight = 984
keywords = [ "webpage", "size" ]
aliases = [ "/questions/984" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Web page size](/questions/984/web-page-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-984-score" class="post-score" title="current number of votes">0</div><span id="post-984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>One of our internal web pages keeps getting slower and slower and I believe it's due to it keeps getting bigger and bigger. Anyone know of a way to easily determine a web page size? I'm using "tcp.reassembled.length" now but was wondering if there is a better way.</p><p>thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-webpage" rel="tag" title="see questions tagged &#39;webpage&#39;">webpage</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '10, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/411e3012a5b5a15a9720252439545020?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JimL&#39;s gravatar image" /><p><span>JimL</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JimL has no accepted answers">0%</span></p></div></div><div id="comments-container-984" class="comments-container"></div><div id="comment-tools-984" class="comment-tools"></div><div class="clear"></div><div id="comment-984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="985"></span>

<div id="answer-container-985" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-985-score" class="post-score" title="current number of votes">1</div><span id="post-985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It depends... If your webpage is delivered over a single TCP session the length of the reassembled PDUs is pretty fine. If there are several TCP sessions involved, I would try an IP-based filter, if there is no other conversation between both hosts except the requested webpage</p><p>Another way to quickly lookup the size would be to filter for the TCP stream (e.g. via Stream Index) and look at</p><p><code>Statistics-&gt;Summary</code></p><p>There you see the transmitted bytes for the whole capture plus the statistics for your current display filter - of course including a little overhead from ACKs and headers...</p><p>BTW: Under <code>Statistics-&gt;Conversations</code> you can directly see lots of statistical info about transmitted bytes/packets etc. for TCP-based as well as for IP-based conversations</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '10, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Nov '10, 06:42</strong> </span></p></div></div><div id="comments-container-985" class="comments-container"><span id="991"></span><div id="comment-991" class="comment"><div id="post-991-score" class="comment-score"></div><div class="comment-text"><p>Thanks, there area several TCP sessions. I'll check out Statistics-&gt;Conversations.</p></div><div id="comment-991-info" class="comment-info"><span class="comment-age">(17 Nov '10, 11:50)</span> <span class="comment-user userinfo">JimL</span></div></div></div><div id="comment-tools-985" class="comment-tools"></div><div class="clear"></div><div id="comment-985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="986"></span>

<div id="answer-container-986" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-986-score" class="post-score" title="current number of votes">0</div><span id="post-986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's much easier to use an HTTP specific tool like Fiddler or HTTP Analyzer when troubleshooting web server's performance. You can gather the data from Wireshark (within HTTP, look for content length etc), but above tools are easier to spot issues.</p><p>You should troubleshoot this the same way as any other issue:</p><p>1) Remove any issues at the network layer. Look for any retransmissions (lost packets) or TCP window sizes (use "tcp.analysis.flags" display filter to see what's going on at a high level).<br />
</p><p>2) Remove HTTP issues by tracking response codes such as 500 server error, 304 not modified (no cache control in place so you're wasting round trips).</p><p>3) HTTP 1.0 vs 1.1: There's a reason why 1.1 was created so quickly after 1.0. Make sure you are using the optimization technique deployed in 1.1 (keepalive for example)</p><p>4) Any SSL issues? Are you wasting time by having to renegotiate SSL because of short SSL Keepalive timers?</p><p>5) Add the DELTA from PREVIOUS packet column and sort by it. Look for the biggest delays then zoom in to see what's going on.<br />
</p><p>In most of my troubleshooting experience, the problem typically lies in the backend process (web server to app/db server) or because cache control was not implemented properly. And of course the usual suspect of not having an optimized tcp stack rears its ugly head from time to time (see RFC 1323 for window scaling options)</p><p>Good luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '10, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></br></p></div></div><div id="comments-container-986" class="comments-container"><span id="992"></span><div id="comment-992" class="comment"><div id="post-992-score" class="comment-score"></div><div class="comment-text"><p>I haven't heard of Fiddler and will look into it. The network is clean, no HTTP errors and there is a hardware load balancer in front of the server doing SSL offloading. This IS an area increasing delay. Thanks for all of your ideas, I'll double check them all.</p></div><div id="comment-992-info" class="comment-info"><span class="comment-age">(17 Nov '10, 11:53)</span> <span class="comment-user userinfo">JimL</span></div></div><span id="998"></span><div id="comment-998" class="comment"><div id="post-998-score" class="comment-score"></div><div class="comment-text"><p>Fiddler is pretty nice to find out what happens while loading a web page. I can also recommend using the Firefox addon "FireBug" to see what element takes how long to load from the browser perspective, or maybe if you don't want to use a proxy tool like Fiddler. It's a little tricky to get Firebug to work though if you've never done it: 1. Install Firebug 2. Open it (Status bar "bug" icon) 3. Click and "Enable" Net Tab 4. Load web page</p><p>You'll get a nice bar chart diagram telling you what element was loaded when and how long it took</p></div><div id="comment-998-info" class="comment-info"><span class="comment-age">(17 Nov '10, 16:29)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-986" class="comment-tools"></div><div class="clear"></div><div id="comment-986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

