+++
type = "question"
title = "Losing connection"
description = '''I have a very large capture of a server losing connection from the network for a second once a day, but everything is working fine from that point according to the user. Took a large capture of the communication, and I copy and paste a few lines here. I see the same dup ack and then a retransmission...'''
date = "2013-04-14T22:22:00Z"
lastmod = "2013-04-15T09:41:00Z"
weight = 20403
keywords = [ "retransmissions", "tcp" ]
aliases = [ "/questions/20403" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Losing connection](/questions/20403/losing-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20403-score" class="post-score" title="current number of votes">0</div><span id="post-20403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a very large capture of a server losing connection from the network for a second once a day, but everything is working fine from that point according to the user. Took a large capture of the communication, and I copy and paste a few lines here. I see the same dup ack and then a retransmission. I looked at the dup ack number which all point back to 445056 frame and the retransmission give a reason of unknown packet type. What does that mean, can some explain that to me please? And what is going on with the retransmission? I checked my network from end to end an no problems were found on the wire.</p><p>Thanks for the help in advance.</p><pre><code>445056  839.680751089   0.000004609 10.97.17.12 10.97.2.123 TDS 762 [TCP Previous segment not captured] Unknown Packet Type: 108 (Not last buffer)[Unreassembled Packet]

445078  839.683686190   0.000093960 10.97.2.123 10.97.17.12 TCP 68  [TCP Dup ACK 445065#1] 49563 &gt; ms-sql-s [ACK] Seq=819300 Ack=129873434 Win=64240 Len=0
445080  839.683761089   0.000042029 10.97.2.123 10.97.17.12 TCP 68  [TCP Dup ACK 445065#3] 49563 &gt; ms-sql-s [ACK] Seq=819300 Ack=129873434 Win=64240 Len=0
445081  839.683798120   0.000037031 10.97.2.123 10.97.17.12 TCP 68  [TCP Dup ACK 445065#4] 49563 &gt; ms-sql-s [ACK] Seq=819300 Ack=129873434 Win=64240 Len=0
445083  839.683858510   0.000032081 10.97.2.123 10.97.17.12 TCP 68  [TCP Dup ACK 445065#6] 49563 &gt; ms-sql-s [ACK] Seq=819300 Ack=129873434 Win=64240 Len=0
445090  839.684140370   0.000060241 10.97.17.12 10.97.2.123 TDS 1522    [TCP Fast Retransmission] Unknown Packet Type: 108 (Not last buffer)[Unreassembled Packet]</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '13, 22:22</strong></p><img src="https://secure.gravatar.com/avatar/b616f858ccbee3de56d053f1b002a757?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ernest%20Johnson&#39;s gravatar image" /><p><span>Ernest Johnson</span><br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ernest Johnson has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Apr '13, 01:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-20403" class="comments-container"><span id="20404"></span><div id="comment-20404" class="comment"><div id="post-20404-score" class="comment-score"></div><div class="comment-text"><blockquote><p>a server losing connection from the network for a second once a day</p></blockquote><p>by '<strong>losing</strong> connection', what do you actually mean? Lost packets or a lost connection (FIN, RST, etc.)?</p></div><div id="comment-20404-info" class="comment-info"><span class="comment-age">(15 Apr '13, 00:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="20418"></span><div id="comment-20418" class="comment"><div id="post-20418-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt I thanks I got the answers there or not FIN RST just a lot of what just a lot of unknown packets and after a while it would retransmit the unknown packet. But Jasper answered it for me it is a database Protocol to WS can’t interpret</p><p>Thanks</p></div><div id="comment-20418-info" class="comment-info"><span class="comment-age">(15 Apr '13, 07:34)</span> <span class="comment-user userinfo">Ernest Johnson</span></div></div><span id="20421"></span><div id="comment-20421" class="comment"><div id="post-20421-score" class="comment-score"></div><div class="comment-text"><p>O.K.</p><p>BTW: did you read my answer? It's a possible explanation for the Retransmits.</p></div><div id="comment-20421-info" class="comment-info"><span class="comment-age">(15 Apr '13, 07:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="20425"></span><div id="comment-20425" class="comment"><div id="post-20425-score" class="comment-score"></div><div class="comment-text"><p>yes it helped</p></div><div id="comment-20425-info" class="comment-info"><span class="comment-age">(15 Apr '13, 09:41)</span> <span class="comment-user userinfo">Ernest Johnson</span></div></div></div><div id="comment-tools-20403" class="comment-tools"></div><div class="clear"></div><div id="comment-20403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20406"></span>

<div id="answer-container-20406" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20406-score" class="post-score" title="current number of votes">1</div><span id="post-20406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ernest Johnson has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"Unknown packet type" means that Wireshark could not decode it any further, which (in my experience) happens a lot if Wireshark thinks that the content is a database protocol and cannot interpret it.</p><p>The retransmission doesn't look special and comes in as expected without much time loss, so I doubt that you have a problem there. Packet loss is normal in every network; it just should not be excessive.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '13, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20406" class="comments-container"><span id="20409"></span><div id="comment-20409" class="comment"><div id="post-20409-score" class="comment-score"></div><div class="comment-text"><blockquote><p>which (in my experience) happens a lot if Wireshark thinks that the content is a database protocol and cannot interpret it.</p></blockquote><p>That's right. The only file where the string "Unknown Packet Type:" appears in the code is packet-tds.c, which is the dissector for TDS, a protocol used by MS SQL Server.</p></div><div id="comment-20409-info" class="comment-info"><span class="comment-age">(15 Apr '13, 01:28)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="20419"></span><div id="comment-20419" class="comment"><div id="post-20419-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper looking at the the full trace, there are the Unknown packet types # and after about 6 dup ack for the same number it would retransmit for the packet.</p></div><div id="comment-20419-info" class="comment-info"><span class="comment-age">(15 Apr '13, 07:39)</span> <span class="comment-user userinfo">Ernest Johnson</span></div></div></div><div id="comment-tools-20406" class="comment-tools"></div><div class="clear"></div><div id="comment-20406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20407"></span>

<div id="answer-container-20407" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20407-score" class="post-score" title="current number of votes">1</div><span id="post-20407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>a server <strong>losing connection</strong> from the network <strong>for a second</strong> once a day</p></blockquote><p>If you mean <strong>lost packets</strong>, this could be totally normal, as <span>@Jasper</span> said.<br />
</p><p>One of these 'normal processes' may be an ARP table refresh. See my answer to the following question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/12655/why-causes-arp-request-a-tcp-previous-segment-lost">http://ask.wireshark.org/questions/12655/why-causes-arp-request-a-tcp-previous-segment-lost</a></p></blockquote><p>Your <strong>one second</strong> connection loss, may be caused by an ARP table refresh. Do you see ARP packets for the involved systems (client, server, router) during that one second period?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '13, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20407" class="comments-container"></div><div id="comment-tools-20407" class="comment-tools"></div><div class="clear"></div><div id="comment-20407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

