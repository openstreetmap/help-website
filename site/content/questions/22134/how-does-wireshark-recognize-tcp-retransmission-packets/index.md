+++
type = "question"
title = "How does Wireshark recognize TCP Retransmission packets?"
description = '''Hi guys, I just want to ask you what information that Wireshark needs to check before it recognize that packet is a retransmission packet.  If it does based on IP Identification and Transport Layer Checksum value, Wireshark needs to compare the retransmission packet&#x27;s data to previous packet&#x27;s data,...'''
date = "2013-06-18T08:41:00Z"
lastmod = "2015-03-19T17:21:00Z"
weight = 22134
keywords = [ "recognize", "retransmission", "tcp", "wireshark" ]
aliases = [ "/questions/22134" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How does Wireshark recognize TCP Retransmission packets?](/questions/22134/how-does-wireshark-recognize-tcp-retransmission-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22134-score" class="post-score" title="current number of votes">0</div><span id="post-22134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, I just want to ask you what information that Wireshark needs to check before it recognize that packet is a retransmission packet. If it does based on IP Identification and Transport Layer Checksum value, Wireshark needs to compare the retransmission packet's data to previous packet's data, does it not?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-recognize" rel="tag" title="see questions tagged &#39;recognize&#39;">recognize</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '13, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/6403b6eed27c3e6a469e7bb75cb2bc2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quang20082008&#39;s gravatar image" /><p><span>quang20082008</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quang20082008 has no accepted answers">0%</span></p></div></div><div id="comments-container-22134" class="comments-container"></div><div id="comment-tools-22134" class="comment-tools"></div><div class="clear"></div><div id="comment-22134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22135"></span>

<div id="answer-container-22135" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22135-score" class="post-score" title="current number of votes">3</div><span id="post-22135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="quang20082008 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>it compares the sequence numbers to what it has determined to be the next expected sequence number from the last packet of the the conversation into the same direction, by packet order (not by timestamp). It does not care about checksum or ip id.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '13, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-22135" class="comments-container"><span id="22319"></span><div id="comment-22319" class="comment"><div id="post-22319-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, If wireshark found it is a retransmitted packet , then is there any blocking for ack packets with the same sequence number or wireshark will drop the packets with same sequence number ?</p></div><div id="comment-22319-info" class="comment-info"><span class="comment-age">(25 Jun '13, 05:56)</span> <span class="comment-user userinfo">sachi</span></div></div><span id="22320"></span><div id="comment-22320" class="comment"><div id="post-22320-score" class="comment-score">1</div><div class="comment-text"><p>Wireshark does not drop or block packets, especially not based on sequence numbers. And careful about ACK packets: their sequence number has nothing to do with the acknowledge number. Wireshark will show/decode any packet that was captured, no matter what the sequence/acknowledge numbers are.</p></div><div id="comment-22320-info" class="comment-info"><span class="comment-age">(25 Jun '13, 06:02)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="40687"></span><div id="comment-40687" class="comment"><div id="post-40687-score" class="comment-score"></div><div class="comment-text"><p>So, could it happen that it qualifies the packet as TCP Retransmission even though the MAC source and destination are different? This is what is happening in one of my clients network, and I just find something to point my finger at...</p></div><div id="comment-40687-info" class="comment-info"><span class="comment-age">(19 Mar '15, 07:28)</span> <span class="comment-user userinfo">SNArchsCOM</span></div></div><span id="40703"></span><div id="comment-40703" class="comment"><div id="post-40703-score" class="comment-score"></div><div class="comment-text"><p>Yes. The TCP dissector does not care about MAC addresses or VLAN tags. It just looks at IP addresses and ports to identify the conversation.</p><p>In case you have the same packet twice with different Ethernet addresses you have a packet before <strong>and</strong> after it being routed. What I recommend is to filter out either the ones not routed yet, or the ones after being routed. Usually, the TTL is a good thing to filter on for this. But you can of course also filter on the MAC address pairs.</p></div><div id="comment-40703-info" class="comment-info"><span class="comment-age">(19 Mar '15, 17:21)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-22135" class="comment-tools"></div><div class="clear"></div><div id="comment-22135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

