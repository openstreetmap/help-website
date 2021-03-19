+++
type = "question"
title = "TCP Stream - FIN, ACK question"
description = '''I have traced a TCP stream sent over my LAN. Everything runs quick until the FIN, ACK from server to client (there is a 2 second delay here). I&#x27;m not sure if the issue is server side or client side, any ideas? http://picthost.net/v.php?id=0e1b3f755b766b166e39822e4d652664'''
date = "2014-02-24T07:59:00Z"
lastmod = "2014-02-25T07:41:00Z"
weight = 30132
keywords = [ "tcp" ]
aliases = [ "/questions/30132" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Stream - FIN, ACK question](/questions/30132/tcp-stream-fin-ack-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30132-score" class="post-score" title="current number of votes">0</div><span id="post-30132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have traced a TCP stream sent over my LAN. Everything runs quick until the FIN, ACK from server to client (there is a 2 second delay here). I'm not sure if the issue is server side or client side, any ideas?</p><p><a href="http://picthost.net/v.php?id=0e1b3f755b766b166e39822e4d652664">http://picthost.net/v.php?id=0e1b3f755b766b166e39822e4d652664</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '14, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/65e9a8f212300a3afe98bcb1052e3a37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markc1&#39;s gravatar image" /><p><span>markc1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markc1 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Feb '14, 08:06</strong> </span></p></div></div><div id="comments-container-30132" class="comments-container"></div><div id="comment-tools-30132" class="comment-tools"></div><div class="clear"></div><div id="comment-30132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30141"></span>

<div id="answer-container-30141" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30141-score" class="post-score" title="current number of votes">0</div><span id="post-30141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>without knowing the upper layer application protocol it is hard to say.</p><p>The client sends 8 bytes to the server and immediately closes the connection again. So what is in the payload and how should the server react upon the data? Obviously it just doesn't do anything and closes its end of the connection after 2 seconds (timer popping?)</p><p>What exactly is <em>'the issue'</em> ?<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '14, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-30141" class="comments-container"><span id="30146"></span><div id="comment-30146" class="comment"><div id="post-30146-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the reply. The client app is a vb.net application sending data via a TCP client (I close the connection after sending). I don't monitor any responses from the server on the client app. The server is a Perle IOLAN box (converts tcp stream to serial) that basically takes the input stream and puts out via a serial port that in turn connects to a PLC. The issue is the 2 second 'lag'. It just seems strange that all AKS prior to the FIN, ACK take milliseconds and then there seems to be some delay. Maybe this is normal, I'm not sure. The whole think does work end to end but the total round trip is just taking too long. I can provide more info if this would help?</p></div><div id="comment-30146-info" class="comment-info"><span class="comment-age">(24 Feb '14, 11:34)</span> <span class="comment-user userinfo">markc1</span></div></div><span id="30149"></span><div id="comment-30149" class="comment"><div id="post-30149-score" class="comment-score"></div><div class="comment-text"><p>The ACKs are sent from the TCP stack whereas the FIN requires a close() socket call from the server application. So it is not too strange to see (sub-)ms responsetimes in the same ethernet LAN and a - purposely? - delayed closing of the tcp connection from the server.</p></div><div id="comment-30149-info" class="comment-info"><span class="comment-age">(24 Feb '14, 12:02)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="30157"></span><div id="comment-30157" class="comment"><div id="post-30157-score" class="comment-score"></div><div class="comment-text"><p>So is it fair to say that the server is causing the 'delay'? I have limited control over the server side but just need to clarify that there is nothing I can do on the client side to affect the FIN?</p></div><div id="comment-30157-info" class="comment-info"><span class="comment-age">(24 Feb '14, 13:38)</span> <span class="comment-user userinfo">markc1</span></div></div><span id="30162"></span><div id="comment-30162" class="comment"><div id="post-30162-score" class="comment-score"></div><div class="comment-text"><p>Yes, that's right.</p></div><div id="comment-30162-info" class="comment-info"><span class="comment-age">(24 Feb '14, 21:09)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="30181"></span><div id="comment-30181" class="comment"><div id="post-30181-score" class="comment-score"></div><div class="comment-text"><p>You can try to send a FIN and 'shortly' after that a RESET. If the server accepts that behavior (meaning it does not drop the sent data), your local socket might get closed faster (and the remote socket as well).</p></div><div id="comment-30181-info" class="comment-info"><span class="comment-age">(25 Feb '14, 07:41)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-30141" class="comment-tools"></div><div class="clear"></div><div id="comment-30141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

