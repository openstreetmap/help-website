+++
type = "question"
title = "Periodic Reset cycles including TCP Dup ACKs and TCP Retransmissions"
description = '''I have a TCP communication problem between two of my servers. Every ten seconds the TCP connection is being established and then reset. The session includes Dup ACKs and Retransmissions but I couldn&#x27;t locate the root cause since I don&#x27;t observe any dropped packets neither. You can find the traces fr...'''
date = "2016-08-05T01:44:00Z"
lastmod = "2016-08-05T03:26:00Z"
weight = 54598
keywords = [ "dup-ack", "reset", "retransmissions", "tcp" ]
aliases = [ "/questions/54598" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Periodic Reset cycles including TCP Dup ACKs and TCP Retransmissions](/questions/54598/periodic-reset-cycles-including-tcp-dup-acks-and-tcp-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54598-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a TCP communication problem between two of my servers. Every ten seconds the TCP connection is being established and then reset. The session includes Dup ACKs and Retransmissions but I couldn't locate the root cause since I don't observe any dropped packets neither.</p><p>You can find the traces from both sides <a href="http://www.wikisend.com/download/837866/SRV1.pcap">here</a> and <a href="http://wikisend.com/download/600826/SRV2.pcap">here</a>.</p><p>Please note that there are some intermediate devices in between these servers although not sure I need traces from them as well. If so please let me know so that I update the post.</p></div><div id="question-tags" class="tags-container tags">dup-ack reset retransmissions tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '16, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/c3be7ca05190c6ccd7ac942b5c00242a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mert_z&#39;s gravatar image" /><p>mert_z<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mert_z has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Aug '16, 01:45</p></div></div><div id="comments-container-54598" class="comments-container"></div><div id="comment-tools-54598" class="comment-tools"></div><div class="clear"></div><div id="comment-54598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54599"></span>

<div id="answer-container-54599" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54599-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your first trace is just looking bad because of duplicate packets. Check this blog post for details:</p><p><a href="https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/">https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/</a></p><p>After deduplicating the SRV1 capture, both captures look okay - a connection established, some data exchanged, the connection staying open in case more data may be requested (resulting in "Keep Alives" when there isn't), and finally a connection teardown via reset when it turns out nothing else is needed. Looks pretty normal to me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '16, 01:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Aug '16, 01:57</p></div></div><div id="comments-container-54599" class="comments-container"><span id="54600"></span><div id="comment-54600" class="comment"><div id="post-54600-score" class="comment-score"></div><div class="comment-text"><p>Sorry, posted the wrong link. Fixed now.</p></div><div id="comment-54600-info" class="comment-info"><span class="comment-age">(05 Aug '16, 01:57)</span> Jasper ♦♦</div></div><span id="54601"></span><div id="comment-54601" class="comment"><div id="post-54601-score" class="comment-score"></div><div class="comment-text"><p>In fact, the TCP session should stay up as long as the application on the server side is up. However before sending RST, application encounters an end of stream error while trying to read the data on the socket. Thus this makes me believe that the connection is already broken before application sends the RST. Is it possible that retransmissions and duplicate acks are because of high RTT? Or some intermediate device already broke the tcp session?</p></div><div id="comment-54601-info" class="comment-info"><span class="comment-age">(05 Aug '16, 02:16)</span> mert_z</div></div><span id="54602"></span><div id="comment-54602" class="comment"><div id="post-54602-score" class="comment-score"></div><div class="comment-text"><p>No, there are <strong>no retransmissions and duplicate ACKs</strong>. These are "ghosts", not real packets. If you deduplicate your trace using <code>editcap -d srv1.pcap srv1_dedup.pcap</code> you'll see that there are no real problems.</p><p>Does the client or server application set a socket timeout when opening it? It usually has to, and I'm guessing that is why it is torn down after a while (by the client side with IP 10.238.62.53).</p><p>And honestly, your RTT is lightning fast - less than 230 microseconds at the handshake. Your problem is on the application/server side, not the network connection.</p></div><div id="comment-54602-info" class="comment-info"><span class="comment-age">(05 Aug '16, 02:31)</span> Jasper ♦♦</div></div><span id="54603"></span><div id="comment-54603" class="comment"><div id="post-54603-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for your comments. The reason why I think the problem is on the network side is the fact that same app is working successfully on another network. That's also why RST shouldn't be the result of a timeout. One interesting thing in this scenario is the RST is seen every 9 seconds sharp. I mean app has a recovery mechanism that once the TCP connection is dropped it establishes another one very quickly, however it ends with a RST again after 9 seconds. Please note that this is not seen on the other site where TCP connections are surviving successfully. Still I'm thinking of blaming some intermediate device. Any ideas on this suspicious 9 sec duration?</p></div><div id="comment-54603-info" class="comment-info"><span class="comment-age">(05 Aug '16, 03:05)</span> mert_z</div></div><span id="54604"></span><div id="comment-54604" class="comment"><div id="post-54604-score" class="comment-score"></div><div class="comment-text"><p>A consistent RST at 9 seconds looks like a timeout value set by a human for the according socket. When an application closes a socket, the TCP stack issues a reset packet. I'd expect 10 seconds though, but it can really be any value.</p><p>Regarding an intermediate device - there seems to be only one routing hop between the two, so if you can find that device (router or firewall probably), check if it has a state timeout killing the session.</p><p>So you should try to capture on both sides simultaneously to check if the reset always comes from the opposite side - this would indicate an intermediate device tearing down the connection in both directions.</p></div><div id="comment-54604-info" class="comment-info"><span class="comment-age">(05 Aug '16, 03:12)</span> Jasper ♦♦</div></div><span id="54608"></span><div id="comment-54608" class="comment not_top_scorer"><div id="post-54608-score" class="comment-score"></div><div class="comment-text"><p>I also located a capture from an intermediate firewall on which packets of these problematic session pass through. I'm also suspecting of this firewall. However I couldn't see anything suspicious looking at its ingress and egress captures. Not sure if it helps but these are the files; <a href="http://wikisend.com/download/660658/INGRESS_FW.pcap">INGRESS_FW</a> and <a href="http://wikisend.com/download/105748/EGRESS_FW.pcap">EGRESS_FW</a></p></div><div id="comment-54608-info" class="comment-info"><span class="comment-age">(05 Aug '16, 03:41)</span> mert_z</div></div><span id="54609"></span><div id="comment-54609" class="comment not_top_scorer"><div id="post-54609-score" class="comment-score"></div><div class="comment-text"><p>I think @mrEEde has a point already in working out the teardown is really coming from the client side.</p></div><div id="comment-54609-info" class="comment-info"><span class="comment-age">(05 Aug '16, 03:52)</span> Jasper ♦♦</div></div></div><div id="comment-tools-54599" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-54599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54606"></span>

<div id="answer-container-54606" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54606-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The TCP session is using TLS so you need to "Decode as" SSL<br />
<img src="https://osqa-ask.wireshark.org/upfiles/Selection_151.png" alt="alt text" /><br />
The RST packet is immediately following a CLOSE_NOTIFY so the client actively closed the SSL for good (?) reasons before tearing down the socket.<br />
</p><p>The ip.id fields of the Encrypted alert and the RST packet are incremental which suggests they have been generated by the client's IP stack and not by an external device. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_152.png" alt="alt text" /></p><p>So it is the client's application logic that decided to terminate the session.<br />
Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '16, 03:26</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-54606" class="comments-container"></div><div id="comment-tools-54606" class="comment-tools"></div><div class="clear"></div><div id="comment-54606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

