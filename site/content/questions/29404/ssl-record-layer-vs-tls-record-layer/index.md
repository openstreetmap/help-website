+++
type = "question"
title = "SSL Record Layer vs TLS Record Layer"
description = '''Hello, I have a question about SSL and the Record Layer. In establishing an SSL connection to a vendor site, I consistently get a failure on the first client hello message. But after 15 seconds a second client hello message is resent and I receive the corresponding server hello message. The usual SY...'''
date = "2014-02-03T10:17:00Z"
lastmod = "2014-02-03T22:40:00Z"
weight = 29404
keywords = [ "tls", "ssl" ]
aliases = [ "/questions/29404" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Record Layer vs TLS Record Layer](/questions/29404/ssl-record-layer-vs-tls-record-layer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29404-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29404-score" class="post-score" title="current number of votes">0</div><span id="post-29404-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a question about SSL and the Record Layer. In establishing an SSL connection to a vendor site, I consistently get a failure on the first client hello message. But after 15 seconds a second client hello message is resent and I receive the corresponding server hello message.</p><p>The usual SYN, SYN-ACK, ACK process never changes. In the first client hello message, I see that the Record Layer is labeled as an SSL Record Layer: Handshake Protocol: Client Hello, Content Type Handshake (22), Version TLS 1.0 (0x0301) and a length of 123. The first Client Hello never receives the Server Hello message.</p><p>Approximately 15 seconds after the first Client Hello message, a second Client Hello message is sent. The difference this time is that it is labeled as a "TLS Record Layer: Handshake Protocol: Client Hello".</p><p>When I receive the Server Hello message, I see that it is responding back with TLSv1.0. In the Handshake Protocol from both Client Hello messages, TLS 1.2 is identified as the version. Since the typical SYN, SYN-ACK, ACK are occurring prior to both Client Hello messages, I am assuming that the server does not support TLS 1.2 or TLS 1.1 and that is the reason I don't receive the Server Hello message from the first Client Hello message. Is my assumption correct?</p><p>Also, is the fact that the second Client Hello message is labeled a "TLSv1" Record Label have anything to do with the server responding with its Server Hello message?</p><p>Any information or insight would be greatly appreciated. I've done quite a bit of reading on SSL/TLS and would like to know if I am understanding the protocols correctly.</p><p>Thank You,</p><p>M.R.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '14, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/9a097919f22f3c12bc73a906a139b47c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MRSoCal&#39;s gravatar image" /><p><span>MRSoCal</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MRSoCal has no accepted answers">0%</span></p></div></div><div id="comments-container-29404" class="comments-container"></div><div id="comment-tools-29404" class="comment-tools"></div><div class="clear"></div><div id="comment-29404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29414"></span>

<div id="answer-container-29414" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29414-score" class="post-score" title="current number of votes">0</div><span id="post-29414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Both ClientHello messages have the same content. the difference in the labeling comes from the fact that in the first instance the negotiation doesn't complete, therefore wireshark labels both packets differently. If you delete all packets after the Client Hello in the succeeding case, the client Hello will change to SSL also - right?<br />
</p><p>"Also, is the fact that the second Client Hello message is labeled a "TLSv1" Record Label have anything to do with the server responding with its Server Hello message?" - No, it's the other way around, it is labelled as SSL because the Server does not enter TLS negotiation.</p><p>" Handshake Protocol: Client Hello, Content Type Handshake (22), Version TLS 1.0 (0x0301) and a length of 123. " vs. " In the Handshake Protocol from both Client Hello messages, TLS 1.2 is identified as the version." - "When I receive the Server Hello message, I see that it is responding back with TLSv1.0."</p><p>If the client sends a TLS Handshake 160301 record it requests TLS_V1.0 and the server needs to accept this proposal which it obviously does. Which other TLS versions are supported cannot be told from this connection as it is the client that suggests - only - TLS V1.0</p><p>Looking at this from a distance, I'd say the server didn't get your ClientHello at all or did not expect it (at this point in time). You might be talking to two different servers behind a Load_Balancer...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '14, 22:40</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-29414" class="comments-container"></div><div id="comment-tools-29414" class="comment-tools"></div><div class="clear"></div><div id="comment-29414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

