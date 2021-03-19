+++
type = "question"
title = "15 second delay in client to server"
description = '''I have two WCF services A and B. Service A calls service B over a TCP binding with security mode set to transport. Here&#x27;s a part of network capture for one such calls. There&#x27;s a delay of around 15 seconds between two consecutive TCP Packets. This occurs frequently and I am not sure of the cause here...'''
date = "2013-06-26T21:29:00Z"
lastmod = "2013-06-26T23:02:00Z"
weight = 22384
keywords = [ "delay", "tcp", "wcf" ]
aliases = [ "/questions/22384" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [15 second delay in client to server](/questions/22384/15-second-delay-in-client-to-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22384-score" class="post-score" title="current number of votes">1</div><span id="post-22384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two WCF services A and B. Service A calls service B over a TCP binding with security mode set to transport. Here's a part of network capture for one such calls. There's a delay of around 15 seconds between two consecutive TCP Packets. This occurs frequently and I am not sure of the cause here. There can be more than one connection between the two services over different port for different calls at a given point in time. What can be the possible causes here. I will appreciate any help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-delay" rel="tag" title="see questions tagged &#39;delay&#39;">delay</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wcf" rel="tag" title="see questions tagged &#39;wcf&#39;">wcf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '13, 21:29</strong></p><img src="https://secure.gravatar.com/avatar/6e206b40657a86006c5401930d9cbc61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tenali&#39;s gravatar image" /><p><span>Tenali</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tenali has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jun '13, 20:04</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-22384" class="comments-container"></div><div id="comment-tools-22384" class="comment-tools"></div><div class="clear"></div><div id="comment-22384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22386"></span>

<div id="answer-container-22386" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22386-score" class="post-score" title="current number of votes">0</div><span id="post-22386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like the trace was taken at the server (assuming port 808 is the server). <img src="https://osqa-ask.wireshark.org/upfiles/clientdelay.png" alt="alt text" /> The excerpt starts with the server sending 1 byte after having received 117 bytes. The client "delayed_acks" this one byte and then the communication stalls.</p><p>14.796 secs later the client sends 5 + 40 bytes in two seperate data segments.</p><pre><code>   Server                   Client 
10.11.27.247:808        10.2.89.68:57400
       -----------------------&gt; (1 byte)
               ... 200ms + 14ms
       &lt;----------------------- ack

Delay  14.796 secs 
       &lt;----------------------- 5 bytes 
       &lt;----------------------- 40 bytes</code></pre><p>I would say you need to look/trace at the client side and investigate the delay.</p><p>Can you upload the (filtered on "tcp.port==57400 and tcp.port==808") trace to <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '13, 22:19</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p><span>mrEEde2</span><br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jun '13, 22:32</strong> </span></p></div></div><div id="comments-container-22386" class="comments-container"><span id="22388"></span><div id="comment-22388" class="comment"><div id="post-22388-score" class="comment-score"></div><div class="comment-text"><p>Hhm..., if this is SSL as the 'security mode set to transport' might suggest, then the client is sending a Client Hello and the server does not answer with a 'Server Hello'. Is the server SSL/TLS enabled? Without a complete trace of the session this is all guessing</p></div><div id="comment-22388-info" class="comment-info"><span class="comment-age">(26 Jun '13, 22:35)</span> <span class="comment-user userinfo">mrEEde2</span></div></div><span id="22389"></span><div id="comment-22389" class="comment"><div id="post-22389-score" class="comment-score"></div><div class="comment-text"><p>The traces were taken on client A and 808 is Server B. I am not able to upload to cloudshark it seems unavailable. SSL/TLS is enabled on server and in fact after the 15 seconds delay noted earlier the communication works fine. The client sends the request payload and the server returns in a few secs. But the 15 seconds delay happens for every new connection.</p></div><div id="comment-22389-info" class="comment-info"><span class="comment-age">(26 Jun '13, 22:50)</span> <span class="comment-user userinfo">Tenali</span></div></div><span id="22390"></span><div id="comment-22390" class="comment"><div id="post-22390-score" class="comment-score">1</div><div class="comment-text"><p>There might be some sidesteps that are delaying the flows here like DNS requests or CRL lookups that rely on a 15 seconds timeout before processing can continue.</p></div><div id="comment-22390-info" class="comment-info"><span class="comment-age">(26 Jun '13, 23:02)</span> <span class="comment-user userinfo">mrEEde2</span></div></div></div><div id="comment-tools-22386" class="comment-tools"></div><div class="clear"></div><div id="comment-22386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

