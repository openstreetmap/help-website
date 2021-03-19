+++
type = "question"
title = "Client closing the connection by sending FIN, ACK before server sends HTTP OK response"
description = '''Hi, We are facing a peculiar issue in our network. When trying to access mail.indiatimes.com (223.165.24.14) website 80% of time it doesn&#x27;t open. We have to keep disconnect and try again to open the web page. From the wireshark traces we can observe 3 way TCP handshake is happening. After that clien...'''
date = "2011-09-28T09:44:00Z"
lastmod = "2011-09-29T09:50:00Z"
weight = 6623
keywords = [ "ack", "fin" ]
aliases = [ "/questions/6623" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Client closing the connection by sending FIN, ACK before server sends HTTP OK response](/questions/6623/client-closing-the-connection-by-sending-fin-ack-before-server-sends-http-ok-response)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6623-score" class="post-score" title="current number of votes">0</div><span id="post-6623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We are facing a peculiar issue in our network. When trying to access mail.indiatimes.com (223.165.24.14) website 80% of time it doesn't open. We have to keep disconnect and try again to open the web page. From the wireshark traces we can observe 3 way TCP handshake is happening. After that client is sending GET HTTP request &amp; HTTP ACK is sent by web server. Now client is sending FIN, ACK to web server without waiting for HTTP OK response.</p><p>In what scenarios this will happen?</p><p>Uploaded the wireshark -&gt; http://www.4shared.com/file/hgI1MERD/ITC-Fail.html</p><p>With Regards, Balaguru S</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-fin" rel="tag" title="see questions tagged &#39;fin&#39;">fin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '11, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/df8478e4539d8fe4b003c470303cc4fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sbalagru6&#39;s gravatar image" /><p><span>sbalagru6</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sbalagru6 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>28 Sep '11, 23:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6623" class="comments-container"><span id="6632"></span><div id="comment-6632" class="comment"><div id="post-6632-score" class="comment-score"></div><div class="comment-text"><p>I reopened the question as I think it is ON-topic. We have been helping people with analyzing their protocols in the past. And I don't see why we should not continue to do so in the future.</p></div><div id="comment-6632-info" class="comment-info"><span class="comment-age">(29 Sep '11, 00:54)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-6623" class="comment-tools"></div><div class="clear"></div><div id="comment-6623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6626"></span>

<div id="answer-container-6626" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6626-score" class="post-score" title="current number of votes">0</div><span id="post-6626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This question isn't really Wireshark related so it's probably better asked elsewhere: stackexchange ?</p><p>That being said:</p><p>"From the wireshark traces we can observe 3 way TCP handshake is happening. After that client is sending GET HTTP request &amp; HTTP ACK is sent by web server. Now client is sending FIN, ACK to web server without waiting for HTTP OK response."</p><p>Looking quickly at the capture and at each of the 3 TCP "conversations", the above is somewhat incorrect:</p><ol><li>In each case, the client does wait some amount of time after sending the GET before timing out and sending the FIN.</li></ol><p>======</p><p>So: to me the real question: Is the server replying and the reply is being lost or is the server not replying.</p><p>I'm not familiar with troubleshooting GPRS connections so I can't provide any further info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '11, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Sep '11, 11:19</strong> </span></p></div></div><div id="comments-container-6626" class="comments-container"></div><div id="comment-tools-6626" class="comment-tools"></div><div class="clear"></div><div id="comment-6626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6631"></span>

<div id="answer-container-6631" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6631-score" class="post-score" title="current number of votes">0</div><span id="post-6631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are 3 TCP streams in your tracefile, each with a different pattern:</p><ol><li>In the first stream (tcp.stream eq 0), the client sends it's request, the server ACKs the request, but an answer never comes. Then after 60 seconds the client sends a FIN. If the server did send a response which got lost, it would have sent retransmissions in this interval. So either:<ul><li>the server never responded</li><li>all transmissions of the response are "blocked"</li><li>or all communication from the server to the client was lost by then.</li></ul></li><li><p>In the second stream (tcp.stream eq 1), the client sends the request. SInce it does not get an ACK, it retransmits the request until it finally gives up and sends a FIN. In this case it seems that all communication from the server to the client is lost.</p></li><li><p>In the third stream (tcp.stream eq 2), The client sends it's request, the server ACKs, but a response does not come. The client times out after 10 seconds and sends a FIN. Then the server sends a FIN back, but with a sequence number that tells us that it has been sending data before. So there is still communication, but the response from the server somehow got lost.</p></li></ol><p>When looking at the MSS values in the TCP SYN packets, the client advertises a MSS of 1420, which may or may not be lowered by intermediate devices on the way to the server. Then the server advertises a MSS of 1400 which might already have been lowered by devices in between the server and the capture point.</p><p>Combining that with the FIN/ACK in frame 26, there might be an issue in adjusting the MSS value on intermediate devices because the server seems to have sent a TCP segment of length 1401. The only way to verify this hypothesis is to make traces at multiple points in the network including one as close to the server as you can get (even if it is just the INternet exit point from the mobile network).</p><p>(In this analysis I just focussed on the TCP part of the tracefiles as I do not have any experience with mobile protocols)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '11, 00:30</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6631" class="comments-container"><span id="6635"></span><div id="comment-6635" class="comment"><div id="post-6635-score" class="comment-score"></div><div class="comment-text"><p>Hi SYNbit,</p><p>Thanks for your valuable input. We have started troubleshooting by bypassing one by one the network elements. Finally when we bypassed the traffic from Juniper SRX3400 firewall we were able to access the website without any issues. Then we put the traffic back on SRX and tried setting different tcp-mss values (1200,1300,1400,1402 &amp; 1420). But still problem is not solved.</p><p>We have raised a case with JTAC, they were also not able to find anything. JTAC has escalated the case to ATAC and they have collected some logs &amp; will come back with findings.</p><p>Now we are sure that problem with SRX firewall only (Done multiple testings bypassing firewall). Will keep you guys posted on Juniper's findings.</p><p>Really appreciate your inputs.</p><p>With Regards, Balaguru S</p></div><div id="comment-6635-info" class="comment-info"><span class="comment-age">(29 Sep '11, 08:50)</span> <span class="comment-user userinfo">sbalagru6</span></div></div><span id="6639"></span><div id="comment-6639" class="comment"><div id="post-6639-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", please see the FAQ for details)</p><p>Does your SRX do any application level filtering or IDS? There might be something in the responses from the server that triggers these filters?</p></div><div id="comment-6639-info" class="comment-info"><span class="comment-age">(29 Sep '11, 09:50)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-6631" class="comment-tools"></div><div class="clear"></div><div id="comment-6631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

