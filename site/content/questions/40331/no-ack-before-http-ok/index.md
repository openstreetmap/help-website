+++
type = "question"
title = "No ACK before HTTP ok"
description = '''Is it normal, or OK to NOT see an ACK from the web server before an HTTP OK is sent? Usually, I see the three-way handshake, the GET from the client, an ACK from the server and then the HTTP OK from the server. Thank you. AT'''
date = "2015-03-06T13:44:00Z"
lastmod = "2015-03-08T05:18:00Z"
weight = 40331
keywords = [ "ack", "get", "http", "wireshark" ]
aliases = [ "/questions/40331" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [No ACK before HTTP ok](/questions/40331/no-ack-before-http-ok)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40331-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it normal, or OK to NOT see an ACK from the web server before an HTTP OK is sent? Usually, I see the three-way handshake, the GET from the client, an ACK from the server and then the HTTP OK from the server.</p><p>Thank you. AT</p></div><div id="question-tags" class="tags-container tags">ack get http wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '15, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/381a470d23e2e7bf84ee3cc2e93d1bde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexltk0506&#39;s gravatar image" /><p>alexltk0506<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexltk0506 has no accepted answers">0%</span></p></div></div><div id="comments-container-40331" class="comments-container"></div><div id="comment-tools-40331" class="comment-tools"></div><div class="clear"></div><div id="comment-40331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40336"></span>

<div id="answer-container-40336" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40336-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's not normal to see <em>any</em> TCP packets that aren't ACKs, other than the initial SYN; <em>all</em> TCP packets other than the initial SYN should have the ACK bit set.</p><p>A TCP host <em>can</em> send an ACK-only packet with no data, but it doesn't <em>have</em> to do so; if, for example, a client sends a short (one-TCP-segment) HTTP request to a server, the server's TCP code could choose not to immediately respond to the TCP segment containing the request with an ACK-only packet and, if the HTTP server code responds to the request quickly enough, the ACK could be piggybacked with the response.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '15, 18:17</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-40336" class="comments-container"><span id="40338"></span><div id="comment-40338" class="comment"><div id="post-40338-score" class="comment-score"></div><div class="comment-text"><p>Thank you!</p></div><div id="comment-40338-info" class="comment-info"><span class="comment-age">(06 Mar '15, 18:36)</span> alexltk0506</div></div></div><div id="comment-tools-40336" class="comment-tools"></div><div class="clear"></div><div id="comment-40336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40364"></span>

<div id="answer-container-40364" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40364-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The (bare) ACK sent by the server after it received the GET is sent by the TCP stack on the server. Assuming the server is using delayed acking, it waits a while before sending an ACK back, as it expects it will have to send data soon. Since the client will retransmit the data if it does not receive an ACK in time, the delay before sending a bare ACK is usually 100ms or 200ms.</p><p>So if the HTTP daemon on the server is able to answer the GET request before the delayed ACK timer runs out, you will not see the extra ACK packet. If it is slower, you will see the ACK in between the GET and the HTTP OK.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '15, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40364" class="comments-container"></div><div id="comment-tools-40364" class="comment-tools"></div><div class="clear"></div><div id="comment-40364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

