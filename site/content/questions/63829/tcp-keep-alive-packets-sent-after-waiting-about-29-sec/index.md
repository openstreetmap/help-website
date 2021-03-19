+++
type = "question"
title = "TCP Keep-Alive packets sent after waiting about 29 sec"
description = ''' We are experiencing performance issue with one of our application. I ran Wireshark on the server and captured the traffic. I noticed that after a few packets the client sends (TCP Keep-Alive) packet after it waits almost 29 sec. Can someone elaborate in the issue please?'''
date = "2017-10-11T18:38:00Z"
lastmod = "2017-10-13T00:07:00Z"
weight = 63829
keywords = [ "keep-alive", "tcp" ]
aliases = [ "/questions/63829" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TCP Keep-Alive packets sent after waiting about 29 sec](/questions/63829/tcp-keep-alive-packets-sent-after-waiting-about-29-sec)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63829-score" class="post-score" title="current number of votes">0</div><span id="post-63829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2017-10-11_at_6.29.49_PM_yEWeZrk.png" alt="alt text" /> We are experiencing performance issue with one of our application. I ran Wireshark on the server and captured the traffic. I noticed that after a few packets the client sends (TCP Keep-Alive) packet after it waits almost 29 sec. Can someone elaborate in the issue please?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-keep-alive" rel="tag" title="see questions tagged &#39;keep-alive&#39;">keep-alive</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '17, 18:38</strong></p><img src="https://secure.gravatar.com/avatar/65ebe7cef3b64da9f45fbbfcf308b40b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cnladmin&#39;s gravatar image" /><p><span>cnladmin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cnladmin has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Oct '17, 18:42</strong> </span></p></div></div><div id="comments-container-63829" class="comments-container"></div><div id="comment-tools-63829" class="comment-tools"></div><div class="clear"></div><div id="comment-63829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63831"></span>

<div id="answer-container-63831" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63831-score" class="post-score" title="current number of votes">1</div><span id="post-63831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cnladmin has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Generally 'keep-alive' packet is a probe to figure out: is other endpoint still active on this particular TCP connection?</p><p>In your case some data exchange happens between server and client, then the server sends last data packet 261194 and stops transmitting further. The client ACKs this packet, but because it doesn't receive neither more data nor connection close commands it becomes uncertain - what's happened to other end? So after timeout it sends keep-alives to ask the server: are you still alive or has you been rebooted/got stuck somehow?</p><p>The server responds with Keep-alive ACK that means: my TCP stack is still active and is maintaining this TCP connection, BUT I do not receive any data/commands from my own application layer corresponding to this connection. Later it starts to send data again.</p><p>So, reasons could be:</p><ul><li>server app process gets stuck from time to time;</li><li>server process just has nothing to send;</li><li>server overload (but timeouts are pretty stable for that reason).</li></ul><p>The next we need to know is what app type is it, maybe this is normal behavior? And also it's would be useful to monitor server app process itself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '17, 22:25</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p><span>Packet_vlad</span><br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Oct '17, 22:29</strong> </span></p></div></div><div id="comments-container-63831" class="comments-container"><span id="63854"></span><div id="comment-63854" class="comment"><div id="post-63854-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for your great answer. The application name is Bid2Win, it is a construction application for job bidding. I will monitor the app process. Do you recommend any application for the this task? or should we just use Windows process monitor?</p><p>Regards,</p></div><div id="comment-63854-info" class="comment-info"><span class="comment-age">(12 Oct '17, 13:34)</span> <span class="comment-user userinfo">cnladmin</span></div></div><span id="63862"></span><div id="comment-63862" class="comment"><div id="post-63862-score" class="comment-score"></div><div class="comment-text"><p>I myself prefer to use Procmon and TCPview utilities from Sysinternals package. In Procmon you can add filter to log only needed process and see it's activity: network, filesystem and so on. Therefore you could spot whether Bid2Win was transmitting data or not at any particular point of time. At the same time you can capture traffic with Wireshark and later do a correlation beetween the two.</p><p>Check it out also that data transfer stops for appr. 60 sec, and it looks like some timer (hardcoded or defined somewhere in settings). Maybe you'll be able to spot this number somewhere in the software.</p></div><div id="comment-63862-info" class="comment-info"><span class="comment-age">(13 Oct '17, 00:07)</span> <span class="comment-user userinfo">Packet_vlad</span></div></div></div><div id="comment-tools-63831" class="comment-tools"></div><div class="clear"></div><div id="comment-63831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

