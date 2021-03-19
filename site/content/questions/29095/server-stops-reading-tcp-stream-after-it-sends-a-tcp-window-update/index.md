+++
type = "question"
title = "Server stops reading TCP stream after it sends a TCP Window update"
description = '''Hello all, we have very strange behaviour with our web application. When certain clients do a HTTP POST request to our JBOSS 4.2 application server (running behind an apache), they sometimes(!) never get a reply from the server. In all these cases, the wireshark dumpfile shows that a TCP Window Upda...'''
date = "2014-01-22T07:16:00Z"
lastmod = "2014-02-07T00:13:00Z"
weight = 29095
keywords = [ "tcpdump", "tcp" ]
aliases = [ "/questions/29095" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Server stops reading TCP stream after it sends a TCP Window update](/questions/29095/server-stops-reading-tcp-stream-after-it-sends-a-tcp-window-update)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29095-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>we have very strange behaviour with our web application. When certain clients do a HTTP POST request to our JBOSS 4.2 application server (running behind an apache), they sometimes(!) never get a reply from the server. In all these cases, the wireshark dumpfile shows that a TCP Window Update is sent from server to client while the client sends the POST data. The server then sends consecutively a lot more of these window updates (which are markes as TCP DUP ACK in wireshark), and the client tries to do multiple retransmits of the POST data. But it never gets an ACK from the server. This goes on until the retransmission times out and the client sends a RST.</p><p>Here are example dumps of one TCP stream for this bahaviour:</p><p><a href="http://www.cloudshark.org/captures/0c9860e1507b">http://www.cloudshark.org/captures/0c9860e1507b</a></p><p><a href="http://www.cloudshark.org/captures/18eff2081f27">http://www.cloudshark.org/captures/18eff2081f27</a></p><p>Thanks for any help.</p><p>Markus</p></div><div id="question-tags" class="tags-container tags">tcpdump tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '14, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/5e3461642182a27f9c35bc81e6284e4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msh&#39;s gravatar image" /><p>msh<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msh has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jan '14, 08:07</p></div></div><div id="comments-container-29095" class="comments-container"></div><div id="comment-tools-29095" class="comment-tools"></div><div class="clear"></div><div id="comment-29095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="29517"></span>

<div id="answer-container-29517" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29517-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for your help. We now found a setting that solves the problem. In our Apache Webserver, KeepAlive was turned off. It seems that certain browsers (newer Firefox browsers and their forks like Iceweasel) have problems with this setting when running on certain operating systems (Linux Mint, Debian Wheezy, Mac OS X...). Other browsers or Firefox on Windows work fine anyway.</p><p>When KeepAlive is turned on, the problem disappears. Still have no explanation for this, maybe a bug in the Firefox client? But at least we could fix it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '14, 00:13</strong></p><img src="https://secure.gravatar.com/avatar/5e3461642182a27f9c35bc81e6284e4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msh&#39;s gravatar image" /><p>msh<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msh has one accepted answer">100%</span></p></div></div><div id="comments-container-29517" class="comments-container"></div><div id="comment-tools-29517" class="comment-tools"></div><div class="clear"></div><div id="comment-29517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29123"></span>

<div id="answer-container-29123" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29123-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at the timestamp options all packets after the three-way-handshake come in with a 'wrong' fixed TS_echo . There must be some proxy between the client and the server that is intercepting your tcp segments after the 3-way handshake and exchanges (messes up) - at least - the timestamps in the tcp options. It might be the 4s+ delay between the 3-way-HS and the POSt request that is making this fail...</p><p>As to the MSS, the client adheres to the offering of 1380 and never sends segments larger than 1368 <img src="https://osqa-ask.wireshark.org/upfiles/Selection_031.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '14, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-29123" class="comments-container"></div><div id="comment-tools-29123" class="comment-tools"></div><div class="clear"></div><div id="comment-29123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29096"></span>

<div id="answer-container-29096" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29096-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Um, did you see that the client sends a FIN flag in its first packet after the three way handshake is complete? That is kind of a "Hello, Nevermind" behavior from the client. I am pretty sure that you can stop looking at any packet after packet 4, because basically the client declares the conversation over in packet 4. DUP Acks, Window update etc. have no meaning. You need to find out why the client establishes the session only to finish it instantly. This is not a server problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '14, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-29096" class="comments-container"><span id="29097"></span><div id="comment-29097" class="comment"><div id="post-29097-score" class="comment-score"></div><div class="comment-text"><p>Jasper, thank you for the quick answer. However, there are other examples where no FIN flag is set: <a href="http://www.cloudshark.org/captures/0c9860e1507b">http://www.cloudshark.org/captures/0c9860e1507b</a></p><p>Thank you for any more ideas or help</p></div><div id="comment-29097-info" class="comment-info"><span class="comment-age">(22 Jan '14, 08:07)</span> msh</div></div><span id="29098"></span><div id="comment-29098" class="comment"><div id="post-29098-score" class="comment-score"></div><div class="comment-text"><p>Ok, the second trace is different. Here the server never gets anything after the Three Way Handshake, it keeps ACKing the initial SYN packet. From the timings I deduct you capture very close (or even on) the client. You now need to do a simultaneous capture at client <strong>and</strong> server to see why the client packets never get acknowledged. My guess is that they never arrive at the server.</p><p>The most common cause for the behavior in your trace is an MTU problem: small packets (Three Way Handshake) get through okay, while large packets don't. Often, routers are configured not to send "ICMP destination unreachable - fragmentation needed" to protect themselves from DoS attacks, so you do not even get a notice back that the packets are too large.</p><p>My advice: figure out if the client receives the packets at all, and reconfigure the client to stop using the TCP timestamp option, which wastes a lot of bytes but doesn't help in most situations.</p><p><strong>Edited:</strong> I was wrong about the MSS being ignored, so I removed that part to avoid spreading wrong information. @mrEEde did it right when saying it never exceeds 1380. Obviously my math was bad last night :-)</p></div><div id="comment-29098-info" class="comment-info"><span class="comment-age">(22 Jan '14, 08:17)</span> Jasper ♦♦</div></div></div><div id="comment-tools-29096" class="comment-tools"></div><div class="clear"></div><div id="comment-29096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

