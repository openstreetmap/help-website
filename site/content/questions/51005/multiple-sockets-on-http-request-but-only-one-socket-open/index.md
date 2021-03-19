+++
type = "question"
title = "[closed] Multiple Sockets on HTTP request, but only one socket open"
description = '''My question is simple: I am using an embedded webserver (MQX) and have one socket for port 80. But what I see now is that within one &quot;send()&quot; I get requests with different ports over the same src and destination ip (HTTP). This means in my definition more than one socket is in use, but this is de fa...'''
date = "2016-03-17T07:56:00Z"
lastmod = "2016-03-17T07:56:00Z"
weight = 51005
keywords = [ "webserver", "http", "socket", "embedded" ]
aliases = [ "/questions/51005" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Multiple Sockets on HTTP request, but only one socket open](/questions/51005/multiple-sockets-on-http-request-but-only-one-socket-open)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51005-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My question is simple:</p><p>I am using an embedded webserver (MQX) and have one socket for port 80.</p><p>But what I see now is that within one "send()" I get requests with different ports over the same src and destination ip (HTTP). This means in my definition more than one socket is in use, but this is de facto impossible... ?!</p><p>-&gt; What is it i donot understand with HTTP? In my understanding ONE socket means ONE src-port-dst connection is possible.</p><p>Thank you very much!</p></div><div id="question-tags" class="tags-container tags">webserver http socket embedded</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '16, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/1d72f9dc6fbbc0cffbeecbb715cf345c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PeterMai&#39;s gravatar image" /><p>PeterMai<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PeterMai has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 17 Mar '16, 11:40</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-51005" class="comments-container"><span id="51011"></span><div id="comment-51011" class="comment"><div id="post-51011-score" class="comment-score"></div><div class="comment-text"><p>Sorry, can you re-word the question?</p><p>A single HTTP request and response always use a single pair of ip:port combinations - sockets, one at client side and another one at server side. So I cannot see how you could see more that one local and one remote socket in an HTTP request as the title of your question suggests.</p><p>If your "web server" really only acts as a server, I cannot see what the "single socket" setting could mean. If it acts as a client, I could imagine that multi-socket setting would mean that each new request should use its own local socket (means: open a new session) rather than keeping old ones open.</p></div><div id="comment-51011-info" class="comment-info"><span class="comment-age">(17 Mar '16, 09:17)</span> sindy</div></div></div><div id="comment-tools-51005" class="comment-tools"></div><div class="clear"></div><div id="comment-51005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Sorry IMO, this question is too far off-topic for this Q&A site." by JeffMorriss 17 Mar '16, 11:40

</div>

</div>

</div>

