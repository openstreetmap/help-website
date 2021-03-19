+++
type = "question"
title = "Is Split-Packets possible in ISUP Protocol?"
description = '''ISUP Protocol data are sent as IP packets. Generally, a big IP packet can split in to 2 and we may get as 2 parts.  Will such thing happens in ISUP protocol?  I guess, normally split-packets shouldn&#x27;t happen in ISUP. If no split packets in ISUP protocol, how it is taken care?'''
date = "2013-04-17T07:47:00Z"
lastmod = "2013-04-30T02:08:00Z"
weight = 20522
keywords = [ "ip", "ss7", "isup" ]
aliases = [ "/questions/20522" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is Split-Packets possible in ISUP Protocol?](/questions/20522/is-split-packets-possible-in-isup-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20522-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>ISUP Protocol data are sent as IP packets. Generally, a big IP packet can split in to 2 and we may get as 2 parts.</p><p>Will such thing happens in ISUP protocol?</p><p>I guess, normally split-packets shouldn't happen in ISUP. If no split packets in ISUP protocol, how it is taken care?</p></div><div id="question-tags" class="tags-container tags">ip ss7 isup</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '13, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/b2940a37e14d31283e43c55dc07a1fea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manoj%20G&#39;s gravatar image" /><p>Manoj G<br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manoj G has 2 accepted answers">33%</span></p></div></div><div id="comments-container-20522" class="comments-container"></div><div id="comment-tools-20522" class="comment-tools"></div><div class="clear"></div><div id="comment-20522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20849"></span>

<div id="answer-container-20849" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20849-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Split-packets are not possible in ISUP Protocol. ISUP uses SCTP and it makes sure that packet reached is same as the packet sent. The various features of SCTP are,</p><pre><code>  - Explicit packet-oriented delivery (not stream-oriented),
  - Sequenced delivery of user messages within multiple streams,
    with an option for order-of-arrival delivery of individual
    user messages,
  - Optional multiplexing of user messages into SCTP datagrams,
  - Network-level fault tolerance through support of multi-homing
    at either or both ends of an association,
  - Resistance to flooding and masquerade attacks, and
  - Data segmentation to conform to discovered path MTU size. SCTP re-assembles the packet before it reaches the destination.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '13, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/b2940a37e14d31283e43c55dc07a1fea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manoj%20G&#39;s gravatar image" /><p>Manoj G<br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manoj G has 2 accepted answers">33%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Apr '13, 02:11</p></div></div><div id="comments-container-20849" class="comments-container"><span id="20854"></span><div id="comment-20854" class="comment"><div id="post-20854-score" class="comment-score">1</div><div class="comment-text"><p>Well, from an endpoint's perspective, yes, SCTP will give the process exactly the message that was sent by the peer. But on the wire the message may be split (I've seen some SCTP implementations split a small chunk across multiple IP packets--but only when the first packet was mostly full from bundling other packets together).</p></div><div id="comment-20854-info" class="comment-info"><span class="comment-age">(30 Apr '13, 06:10)</span> JeffMorriss ♦</div></div><span id="20857"></span><div id="comment-20857" class="comment"><div id="post-20857-score" class="comment-score"></div><div class="comment-text"><p>@JeffMorriss: Yes. It do happen. It splits multiple chunks across multiple IP packets. But underlying protocol data will not gets split since it is the part of a particular chunk. So whatever messages we want to get, we get it full.</p></div><div id="comment-20857-info" class="comment-info"><span class="comment-age">(30 Apr '13, 21:58)</span> Manoj G</div></div></div><div id="comment-tools-20849" class="comment-tools"></div><div class="clear"></div><div id="comment-20849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20526"></span>

<div id="answer-container-20526" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20526-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you asking if ISUP messages themselves can be fragmented/segmented?</p><p>I didn't think so (ISUP was designed to work within the 272-octet limit of MTP2 and thus has very small messages) but looking in ITU Q.762 there is a Segmentation message type and APM message type, either of which appear to be capable of carrying segmented ISUP messages. Wireshark's ISUP dissector has a preference whether or not to reassemble APM segments.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '13, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-20526" class="comments-container"><span id="20529"></span><div id="comment-20529" class="comment"><div id="post-20529-score" class="comment-score"></div><div class="comment-text"><p>@JeffMorriss: An IP packet may contain one or more ISUP messages or even other protocol messages also. So is it possible to have a fragmented IP Packet?</p></div><div id="comment-20529-info" class="comment-info"><span class="comment-age">(17 Apr '13, 10:38)</span> Manoj G</div></div><span id="20530"></span><div id="comment-20530" class="comment"><div id="post-20530-score" class="comment-score"></div><div class="comment-text"><p>Yes, a single IP packet can contain multiple ISUP messages (especially if SCTP is used).</p><p>Yes, an IP packet can be fragmented. IP fragmentation is, however, strongly discouraged (by the IETF) so normally your transport protocol (SCTP or TCP) figures out the (path) MTU and adjusts accordingly so that IP fragmentation is never used. If you're using UDP then whatever application or protocol is using UDP needs to do this path MTU calculation or else it will end up using IP fragmentation too.</p></div><div id="comment-20530-info" class="comment-info"><span class="comment-age">(17 Apr '13, 10:43)</span> JeffMorriss ♦</div></div><span id="20562"></span><div id="comment-20562" class="comment"><div id="post-20562-score" class="comment-score"></div><div class="comment-text"><p>@JeffMorriss: Thank you! Getting some clarity now. :)</p></div><div id="comment-20562-info" class="comment-info"><span class="comment-age">(18 Apr '13, 02:30)</span> Manoj G</div></div></div><div id="comment-tools-20526" class="comment-tools"></div><div class="clear"></div><div id="comment-20526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

