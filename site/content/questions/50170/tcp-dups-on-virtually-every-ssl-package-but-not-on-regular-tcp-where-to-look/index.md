+++
type = "question"
title = "TCP DUPs on virtually every SSL package, but not on regular TCP. Where to look?"
description = '''Hi, What would cause TCP DUP&#x27;s (and spurious retransmissions, fast retransmissions, a cpl up to a dozen) to be received from random SSL-enabled webservers on virtually every package, WHILE REGULAR TCP/IP (non-TLS) doesn&#x27;t generate any DUP&#x27;s? Zero. If the latter would be the case, I would just have a...'''
date = "2016-02-13T03:59:00Z"
lastmod = "2016-02-13T04:26:00Z"
weight = 50170
keywords = [ "spurious", "duplicate", "retransmissions" ]
aliases = [ "/questions/50170" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP DUPs on virtually every SSL package, but not on regular TCP. Where to look?](/questions/50170/tcp-dups-on-virtually-every-ssl-package-but-not-on-regular-tcp-where-to-look)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50170-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>What would cause TCP DUP's (and spurious retransmissions, fast retransmissions, a cpl up to a dozen) to be received from random SSL-enabled webservers on virtually every package, WHILE REGULAR TCP/IP (non-TLS) doesn't generate any DUP's? Zero. If the latter would be the case, I would just have a faulty router or a low level networking issue (hardware/IP stack). I fail to see how this only concerns SSL traffic, it clogs up a nice view in Wireshark with all the DUPs.</p></div><div id="question-tags" class="tags-container tags">spurious duplicate retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '16, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/653d979a2dc2892e289024f6a619921e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="boiiingg&#39;s gravatar image" /><p>boiiingg<br />
<span class="score" title="2 reputation points">2</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="boiiingg has no accepted answers">0%</span></p></div></div><div id="comments-container-50170" class="comments-container"><span id="50174"></span><div id="comment-50174" class="comment"><div id="post-50174-score" class="comment-score"></div><div class="comment-text"><p>have you tried deduplicating your capture? See <a href="https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/">https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/</a> for more info why.</p></div><div id="comment-50174-info" class="comment-info"><span class="comment-age">(13 Feb '16, 05:30)</span> Jasper ♦♦</div></div><span id="50199"></span><div id="comment-50199" class="comment"><div id="post-50199-score" class="comment-score"></div><div class="comment-text"><p>(Thanks for <a href="https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/)">https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/)</a></p><p>Some issues I noticed:</p><ol><li>TCP DUPs all have the same Seq.no's but after testing with editcap and hexdec comparing I noticed they are not truly unique.</li><li>The difference in DUPS only lies in the IPv4 Identification field (2 bytes) and as a result the Header checksum (2 bytes). This is systematic.</li><li>Frequent errors in the expert window are: "Duplicate ACKs", "out-of-order" and "previous segment not captured"</li></ol><p>Just a shot in the dark... I wonder if Wireshark somehow tricked, seeing these packages as DUP ACKs.</p><p>Are these issues typical for a SPAN VLAN monitoring port at the ISP?</p><p>Anything else that would explain change of the ID-field in the IPv4 header while the rest of the datagram is untouched?</p></div><div id="comment-50199-info" class="comment-info"><span class="comment-age">(15 Feb '16, 00:41)</span> boiiingg</div></div><span id="50201"></span><div id="comment-50201" class="comment"><div id="post-50201-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Anything else that would explain change of the ID-field in the IPv4 header while the rest of the datagram is untouched?</p></blockquote><p>The difference in IP ID field means that the "duplicates" have been really sent by the sending machine and haven't occurred due to properties of the capturing method.</p><blockquote><p>Are these issues typical for a SPAN VLAN monitoring port at the ISP?</p></blockquote><p>If you SPAN the whole VLAN and do not / can not set additional filtering on the switch, you basically get a duplicate of each and every packet because you get one copy of the packet when it enters the switch and another copy of the same packet when it leaves the switch, so it would not explain, even if the IP ID fields would not differ, why the DUPs only exist for the SSL traffic. (There are exceptions related to total traffic volume vs. the monitoring port bandwidth and to broadcast/multicast packets, but that's a different story).</p><p>So I'd vote for the SSL stack to be responsible.</p></div><div id="comment-50201-info" class="comment-info"><span class="comment-age">(15 Feb '16, 00:54)</span> sindy</div></div><span id="50202"></span><div id="comment-50202" class="comment"><div id="post-50202-score" class="comment-score"></div><div class="comment-text"><p>I thought the SPAN VLAN would be a bit fat fetched ... I am going to run some more tests using a different SSL stack. Despite having a very popular system (Linux 3.16.0-4) with openssl 1.0.1k-3+deb8u1). Will need to reinstall the OS anyway in a cpl of days.</p></div><div id="comment-50202-info" class="comment-info"><span class="comment-age">(15 Feb '16, 00:59)</span> boiiingg</div></div></div><div id="comment-tools-50170" class="comment-tools"></div><div class="clear"></div><div id="comment-50170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50173"></span>

<div id="answer-container-50173" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50173-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If it's only SSL/TLS it could be a security device interfering with SSL/TLS like a firewall. However, without access to a capture file it's hard to say more than that!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '16, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-50173" class="comments-container"></div><div id="comment-tools-50173" class="comment-tools"></div><div class="clear"></div><div id="comment-50173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

