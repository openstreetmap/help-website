+++
type = "question"
title = "TCP Zerowindow and window SIze"
description = '''Hi all, I would need your help to understand about window size behaviour. I have a trace of communication between two servers  - Web server (195.42.X.Y) - SQL database server (153.112.X.Y) here is a part of the trace  The web server is downloading data (with large packets) from the Database server w...'''
date = "2014-12-22T07:01:00Z"
lastmod = "2014-12-22T08:41:00Z"
weight = 38656
keywords = [ "window", "size" ]
aliases = [ "/questions/38656" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Zerowindow and window SIze](/questions/38656/tcp-zerowindow-and-window-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38656-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I would need your help to understand about window size behaviour.</p><p>I have a trace of communication between two servers - Web server (195.42.X.Y) - SQL database server (153.112.X.Y)</p><p>here is a part of the trace <img src="http://i60.tinypic.com/2vtsfuw.jpg" alt="alt text" /></p><p>The web server is downloading data (with large packets) from the Database server without any issue until a moment where the Web server send a "TCP Zeowindow" packet. I understand this packet/message. In previous ACK from Web server I should see the Window Size decrease but it's not really the case. And strangely in previous ACK the window size is almost 200 - 300 bytes while the server is acknowledging a bunch of large packet (1514 bytes).</p><p>So I wonder how the webserver can acknowledge so much Data / packets while its window size seems so small.</p><p>Thanks for your help</p></div><div id="question-tags" class="tags-container tags">window size</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '14, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/25fcd4b6692b20e9189d8f0b52f1663d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="any-one&#39;s gravatar image" /><p>any-one<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="any-one has no accepted answers">0%</span></p></img></div></div><div id="comments-container-38656" class="comments-container"><span id="38657"></span><div id="comment-38657" class="comment"><div id="post-38657-score" class="comment-score"></div><div class="comment-text"><p>can you upload a sanitized trace file at <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and post the link? It's a bit difficult to track TCP behavior based on screenshots.</p><p>You can use TraceWrangler to anonymize your IPs and remove payload above layer 4, see <a href="http://www.tracewrangler.com">http://www.tracewrangler.com</a></p></div><div id="comment-38657-info" class="comment-info"><span class="comment-age">(22 Dec '14, 07:24)</span> Jasper ♦♦</div></div><span id="38658"></span><div id="comment-38658" class="comment"><div id="post-38658-score" class="comment-score"></div><div class="comment-text"><p>I didn't know Tracewrangler. Nice tool :-D</p><p>here is the trace uploaded <a href="https://www.cloudshark.org/captures/d75c75501ef6">https://www.cloudshark.org/captures/d75c75501ef6</a></p><p>Web server : 49.106.38.197 SQL Server : 192.77.168.223</p></div><div id="comment-38658-info" class="comment-info"><span class="comment-age">(22 Dec '14, 08:15)</span> any-one</div></div><span id="38659"></span><div id="comment-38659" class="comment"><div id="post-38659-score" class="comment-score"></div><div class="comment-text"><p>Below you can find the requested informations</p></div><div id="comment-38659-info" class="comment-info"><span class="comment-age">(22 Dec '14, 08:15)</span> any-one</div></div></div><div id="comment-tools-38656" class="comment-tools"></div><div class="clear"></div><div id="comment-38656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38661"></span>

<div id="answer-container-38661" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38661-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In packet 446 the web server acknowledges packet 445 (which includes all segments before packet 445 as well), but advertises a Window of 99. I guess Window Scaling (see rfc 1323) is involved here, but we don't know the scale factor since the session handshake is missing, and this is also why Wireshark can't calculate the actual window size.</p><p>My guess is that the scale factor is 7, which would mean that the window of 99 is in fact 99 * 2^7, which is 12672. I deducted this from the bytes in flight in packet 455, because that's when the sender stops sending and waits for an ACK, so it's quite okay to assume that the window is full at that point.</p><p>The next ACK in packet 456 advertises a window of 0, which means that the receiver has trouble processing the amount of incoming data. It recovers in the packet 459 to 461, and the transmission continues. So the problem is the web server, because it can't deal with the packets from the database server fast enough. It's not a network problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '14, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Dec '14, 08:42</p></div></div><div id="comments-container-38661" class="comments-container"><span id="38673"></span><div id="comment-38673" class="comment"><div id="post-38673-score" class="comment-score"></div><div class="comment-text"><p>I know for sure the issue is not due to the network :-D I was just wondering why the TCP windows size was so small. So if I understand weel the scale facor is defined during the TCP triple handshake. So if I don't capture those packets Wireshark will display a wrong TCP window size value. Am I right?</p></div><div id="comment-38673-info" class="comment-info"><span class="comment-age">(23 Dec '14, 00:53)</span> any-one</div></div><span id="38674"></span><div id="comment-38674" class="comment"><div id="post-38674-score" class="comment-score"></div><div class="comment-text"><p>I found the answer :-D</p><p><a href="https://ask.wireshark.org/questions/10071/window-size-scaling-factor-1-unknown">https://ask.wireshark.org/questions/10071/window-size-scaling-factor-1-unknown</a></p><p>Thanks for your help Jasper :-D</p></div><div id="comment-38674-info" class="comment-info"><span class="comment-age">(23 Dec '14, 00:54)</span> any-one</div></div><span id="38681"></span><div id="comment-38681" class="comment"><div id="post-38681-score" class="comment-score"></div><div class="comment-text"><p>Sure, no problem. If you like my answer, please accept it with the checkmark button left to it ;-)</p></div><div id="comment-38681-info" class="comment-info"><span class="comment-age">(23 Dec '14, 03:25)</span> Jasper ♦♦</div></div></div><div id="comment-tools-38661" class="comment-tools"></div><div class="clear"></div><div id="comment-38661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

