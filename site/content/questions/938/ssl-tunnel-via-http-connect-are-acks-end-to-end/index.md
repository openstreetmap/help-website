+++
type = "question"
title = "SSL Tunnel via HTTP Connect - Are ACK&#x27;s &quot;end-to-end&quot;?"
description = '''Hi. I am troubleshooting an SSL transaction that goes through a web proxy server, and I am only able to capture packets at the Client end. In this scenario, the Client uses an HTTP CONNECT to create an SSL Tunnel through the proxy server to the destination server (aka &quot;Origin Server&quot;). In my situati...'''
date = "2010-11-14T02:36:00Z"
lastmod = "2010-11-14T19:52:00Z"
weight = 938
keywords = [ "ssltunnel", "httpconnect" ]
aliases = [ "/questions/938" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SSL Tunnel via HTTP Connect - Are ACK's "end-to-end"?](/questions/938/ssl-tunnel-via-http-connect-are-acks-end-to-end)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-938-score" class="post-score" title="current number of votes">1</div><span id="post-938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I am troubleshooting an SSL transaction that goes through a web proxy server, and I am only able to capture packets at the Client end. In this scenario, the Client uses an HTTP CONNECT to create an SSL Tunnel through the proxy server to the destination server (aka "Origin Server"). In my situation, the tunnel is created successfully, and the SSL Handshake is completed successfully, but when the Client actually sends "application data" to the Origin Server, it does not get any response, and finally the Client receives a FIN, and the connection is closed.</p><p>My question is this... The application data packets sent by the client - after the SSL Handshake completes - all receive TCP ACK's. Does that indicate that the Origin Server has ACK'd those packets? Or, simply that the proxy server has ACK'd those packets?</p><p>In other words, can I use the fact that these packets are ACK'd to conclude that the Origin Server definitely received the Client's request? Or, is it possible that the proxy server ACK'd the packets, but never received an ACK from the Origin Server, or, worse yet, never SENT the packets to the Origin Server?</p><p>Thx, Feenyman99</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssltunnel" rel="tag" title="see questions tagged &#39;ssltunnel&#39;">ssltunnel</span> <span class="post-tag tag-link-httpconnect" rel="tag" title="see questions tagged &#39;httpconnect&#39;">httpconnect</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '10, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p><span>feenyman99</span><br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-938" class="comments-container"></div><div id="comment-tools-938" class="comment-tools"></div><div class="clear"></div><div id="comment-938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="939"></span>

<div id="answer-container-939" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-939-score" class="post-score" title="current number of votes">0</div><span id="post-939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="feenyman99 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I guess that all depends on the proxy you are using. If it's a proxy that does SSL inspection (by dynamically creating certificates and having the proxy-root-ca on all clients), then it's an application layer proxy which means all communication is between the client and the proxy, independently from the communication between the proxy and the origin server.</p><p>However, I think most proxies are just TCP (socks) proxies when it comes to "CONNECT". Which I would guess means that all TCP packets are just natted, but other than that not altered.</p><p>The only way to know for your particular brand of proxy is to either make a trace on both sides or ask the vendor how it processes data, but even then I would still want to double check by looking at the traces on both sides of the proxy.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '10, 05:04</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-939" class="comments-container"><span id="941"></span><div id="comment-941" class="comment"><div id="post-941-score" class="comment-score"></div><div class="comment-text"><p>Thx SYNbit! After I posted this question, I began to realize that getting a trace from the proxy server is the only sure way to get a definitive answer. It will take some doing, but I will push through my corporation's bureaucracy to get that done, and post the results here - hopefully within a week.</p></div><div id="comment-941-info" class="comment-info"><span class="comment-age">(14 Nov '10, 07:00)</span> <span class="comment-user userinfo">feenyman99</span></div></div><span id="948"></span><div id="comment-948" class="comment"><div id="post-948-score" class="comment-score">2</div><div class="comment-text"><p>Most corporate proxies that I know will not decrypt SSL. There's too much liability involved (imagine if my company decrypted my access to Chase bank and it got leaked somehow?). So it's entirely possible that you're just getting a tcp proxy. One other clue might be by looking at the IP TTL. Keep an eye on the IP TTL to see what the proxy uses by default. So ping the proxy and see what the IP TTL looks like. Then look at your internet traffic (Origin server) and see what the IP TTL looks like.</p></div><div id="comment-948-info" class="comment-info"><span class="comment-age">(14 Nov '10, 19:52)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-939" class="comment-tools"></div><div class="clear"></div><div id="comment-939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

