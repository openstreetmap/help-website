+++
type = "question"
title = "HTTP Proxy"
description = '''Hello, Does Wireshark (1.8.8) have the ability to &quot;discover&quot; if an http proxy device (Websense) is being used? If so, which area of the packet might I find this information so that I can build a filter. We have multiple network segments and I&#x27;m not always sure which segments are using the proxy. We ...'''
date = "2013-07-11T04:01:00Z"
lastmod = "2013-07-16T07:16:00Z"
weight = 22844
keywords = [ "http", "proxy" ]
aliases = [ "/questions/22844" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [HTTP Proxy](/questions/22844/http-proxy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22844-score" class="post-score" title="current number of votes">0</div><span id="post-22844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Does Wireshark (1.8.8) have the ability to "discover" if an http proxy device (Websense) is being used? If so, which area of the packet might I find this information so that I can build a filter.</p><p>We have multiple network segments and I'm not always sure which segments are using the proxy. We use WCCP to "see" the http packets and then send to the Websense appliances. We do have bypass ACL's for Websense, but again, I'm not always privy to that information.</p><p>thanks, J</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '13, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/791c3a844bb1629d3a685adab364e2d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JTech_17&#39;s gravatar image" /><p><span>JTech_17</span><br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JTech_17 has no accepted answers">0%</span></p></div></div><div id="comments-container-22844" class="comments-container"></div><div id="comment-tools-22844" class="comment-tools"></div><div class="clear"></div><div id="comment-22844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22855"></span>

<div id="answer-container-22855" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22855-score" class="post-score" title="current number of votes">0</div><span id="post-22855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JTech_17 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>have the ability to "discover" if an http proxy device (Websense) is being used?</p></blockquote><p>well, it depends where you capture the traffic.</p><p>If it is near the client, see the answer of <span>@Jasper</span>. However, there is no guarantee, that the proxy adds any of those headers.</p><p>ALTERNATIVE: You can send a bogus request from the client. Chances are good, that the proxy denies those request with an error message, and by doing so exposes it's existence ;-)</p><p>A bogus request would be (use telnet www.xyz.com 80)</p><pre><code>GET / HXXP/1.0
Host: www.xyz.de</code></pre><p>Then see how the answer looks like.</p><p>If you capture near the internet router/firewall, you will be able to detect proxy request simply by it's IP address. All requests going to the proxy via WCCP will show up with the proxy IP if you capture in front of the internet router/firewall (consider DMZ setups!). All unproxied requests (WCCP did not forward the traffic to the proxy) will show up with an IP address of a client.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '13, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22855" class="comments-container"><span id="22856"></span><div id="comment-22856" class="comment"><div id="post-22856-score" class="comment-score"></div><div class="comment-text"><p>When the Proxy appliances begin to act up (high cpu, database corruption, etc.) it gives the user a poor experience when http browsing. I was hoping that I could determine a metric/filter (from the client side) that would help me detect when the appliances begin to crack...however, I have sense discovered the capture point I need. Fortunately the Proxy devices reside on one switch, to which I can use RSPAN and send a copy of the wccp forwarded packets back to my Cisco NAM. I'm very curious to see what type of info the packets contain when the Proxy begins to go tango-uniform (large delays, authen errors, etc.).</p></div><div id="comment-22856-info" class="comment-info"><span class="comment-age">(11 Jul '13, 05:41)</span> <span class="comment-user userinfo">JTech_17</span></div></div><span id="22858"></span><div id="comment-22858" class="comment"><div id="post-22858-score" class="comment-score"></div><div class="comment-text"><blockquote><p>(<strong>high cpu</strong>, database corruption, etc.) it gives the user a poor experience when http browsing. I was hoping that I could determine a metric/filter (from the client side) that would help me detect when the appliances begin to crack...</p></blockquote><p>well wouldn't it be easier to monitor those problems on the websense server itself instead if trying to detect a possible problem by looking at the network response time? Even if you want to look at the response time, why not capturing on the server itself and then use some scripts to detect a possible crack-down of the proxy!?!</p></div><div id="comment-22858-info" class="comment-info"><span class="comment-age">(11 Jul '13, 05:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="23010"></span><div id="comment-23010" class="comment"><div id="post-23010-score" class="comment-score"></div><div class="comment-text"><p>Yes, and a tech is watching for conditions that lead to the websense acting up, however, I've been tasked with determining if conditions from the client, sent/recieved packets, could help determine other parts, if any, could be the cause for poor performance.</p></div><div id="comment-23010-info" class="comment-info"><span class="comment-age">(16 Jul '13, 06:03)</span> <span class="comment-user userinfo">JTech_17</span></div></div><span id="23017"></span><div id="comment-23017" class="comment"><div id="post-23017-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I've been tasked with determining if conditions from the client, sent/recieved packets, could help determine other parts,</p></blockquote><p>Ah, I see. Any results?</p></div><div id="comment-23017-info" class="comment-info"><span class="comment-age">(16 Jul '13, 07:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-22855" class="comment-tools"></div><div class="clear"></div><div id="comment-22855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22845"></span>

<div id="answer-container-22845" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22845-score" class="post-score" title="current number of votes">1</div><span id="post-22845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might see some additional headers like "X-Forwarded-For" that you can filter on, which is added by a proxy device.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '13, 04:04</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-22845" class="comments-container"><span id="22848"></span><div id="comment-22848" class="comment"><div id="post-22848-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure I'm going to be able to determine if the client is being http proxied when capturing from the client. After a little bit more research on wccp, I believe this filter will work if I'm upstream (capturing from the router/switch side). I've added this to my personal filters list for future use. thanks, J</p></div><div id="comment-22848-info" class="comment-info"><span class="comment-age">(11 Jul '13, 04:50)</span> <span class="comment-user userinfo">JTech_17</span></div></div><span id="22851"></span><div id="comment-22851" class="comment"><div id="post-22851-score" class="comment-score"></div><div class="comment-text"><p>In addition to the "X-Forwarded-For" added by the proxy in the requests towards the server, you might also see the "Via:" header in the responses from the proxy back to the client.</p></div><div id="comment-22851-info" class="comment-info"><span class="comment-age">(11 Jul '13, 04:55)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-22845" class="comment-tools"></div><div class="clear"></div><div id="comment-22845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

