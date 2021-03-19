+++
type = "question"
title = "How to know the sender of the ACK"
description = '''I&#x27;d like to know the sender of the ACK received.  I mean, if the ACK received is from the layer itself (TCP, etc..) or from the server I&#x27;ve just contacted (e.g. they received the package, and they sent me an ACK confirming they received it.) In the ACK data, how can I know this kind of information. ...'''
date = "2012-11-19T09:34:00Z"
lastmod = "2012-11-19T19:35:00Z"
weight = 16059
keywords = [ "ack", "packets" ]
aliases = [ "/questions/16059" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to know the sender of the ACK](/questions/16059/how-to-know-the-sender-of-the-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16059-score" class="post-score" title="current number of votes">0</div><span id="post-16059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to know the sender of the ACK received.</p><p>I mean, if the ACK received is from the layer itself (TCP, etc..) or from the server I've just contacted (e.g. they received the package, and they sent me an ACK confirming they received it.)</p><p>In the ACK data, how can I know this kind of information. Could it be the source port?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '12, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/356e94abf22a9f5ddeee7910f6c232cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rogcg&#39;s gravatar image" /><p><span>rogcg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rogcg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Nov '12, 09:35</strong> </span></p></div></div><div id="comments-container-16059" class="comments-container"></div><div id="comment-tools-16059" class="comment-tools"></div><div class="clear"></div><div id="comment-16059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16065"></span>

<div id="answer-container-16065" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16065-score" class="post-score" title="current number of votes">0</div><span id="post-16065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You receive ACKs from the TCP stack of the receiving node. Packets sent from the client are Acknowledged by the TCP stack of the server and vice versa. Acknowledge numbers are based on the sequence number plus the payload size of the packet received. The have nothing to do with ports, except that sequences are kept per TCP session, which is based on ports.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '12, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16065" class="comments-container"><span id="16069"></span><div id="comment-16069" class="comment"><div id="post-16069-score" class="comment-score"></div><div class="comment-text"><p>so how can I know whos is the sender? All ACK's will be received from TCP stack, even if the client is sending it, the TCP stack will acknowledge it to me? So I'm not able to know if it's comming from the TCP layer or the client itself?</p></div><div id="comment-16069-info" class="comment-info"><span class="comment-age">(19 Nov '12, 10:21)</span> <span class="comment-user userinfo">rogcg</span></div></div><span id="16081"></span><div id="comment-16081" class="comment"><div id="post-16081-score" class="comment-score"></div><div class="comment-text"><blockquote><p>even if the client is sending it, the TCP stack will acknowledge it to me?</p></blockquote><p>it's not the client application that is sending the data. It's the TCP/IP stack of the OS (unless you have client software that operates at a real low level).</p><p>The client opens a TCP connection and then it reads/write from/to that connection by calling OS system calls.</p><p>I'm sure you will find the following tutorial about network programming interesting. I picked just the first link from a google search.</p><blockquote><p><code>http://beej.us/guide/bgnet/output/html/multipage/index.html</code></p></blockquote></div><div id="comment-16081-info" class="comment-info"><span class="comment-age">(19 Nov '12, 11:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16092"></span><div id="comment-16092" class="comment"><div id="post-16092-score" class="comment-score"></div><div class="comment-text"><p>I.e., the application/library/daemon code on the client or the server sends data by writing it to the networking stack; the networking stack encapsulates it in TCP segments, encapsulates those into IP datagrams, and sends them over a network.</p><p>The TCP stack also either sends ACKs in packets by themselves or in a data segment - the application/library/daemon code on the client or the server has nothing to do with sending those ACKs (again, unless you have client or server software that operates at a real low level).</p></div><div id="comment-16092-info" class="comment-info"><span class="comment-age">(19 Nov '12, 19:35)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-16065" class="comment-tools"></div><div class="clear"></div><div id="comment-16065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

