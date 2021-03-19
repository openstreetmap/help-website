+++
type = "question"
title = "Packet payload extraction from Socket connections (TCP)"
description = '''I have several packets that i was hoping to get the payload data from in a human readable format. I dont know if its even possible at this point but im hoping someone can help me to understand this. This is one of the raw packets im working with: 4500003e1ca440004006985fc0a80264c0a80202c90b138811744...'''
date = "2016-12-03T13:22:00Z"
lastmod = "2016-12-03T14:06:00Z"
weight = 57821
keywords = [ "socket", "packet", "payload" ]
aliases = [ "/questions/57821" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packet payload extraction from Socket connections (TCP)](/questions/57821/packet-payload-extraction-from-socket-connections-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57821-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have several packets that i was hoping to get the payload data from in a human readable format. I dont know if its even possible at this point but im hoping someone can help me to understand this.</p><p>This is one of the raw packets im working with:</p><p>4500003e1ca440004006985fc0a80264c0a80202c90b138811744dfafc3aa16a801820419aae00000101080ac430d02c000002eaac5083000104431251ae</p><p>I am trying to figure out the raw packet payload from this but all i can obtain are jumbled, incoherent ASCII representations. I dont know if its something i am simply doing wrong or if its even possible to do?</p><p>Would someone be able to help me either understand how to obtain the payload from this, or let me know why this wont work? The packet is sent from a Socket script over an open network, if that helps.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">socket packet payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '16, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/6661abaa9d6e16900cf6613a7f5f12c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m0nk37&#39;s gravatar image" /><p>m0nk37<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m0nk37 has no accepted answers">0%</span></p></div></div><div id="comments-container-57821" class="comments-container"></div><div id="comment-tools-57821" class="comment-tools"></div><div class="clear"></div><div id="comment-57821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57822"></span>

<div id="answer-container-57822" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57822-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>So, using <code>echo 45 ... | xxd -ps -r | od -Ax -tx1 -v | text2pcap -l 101 - some.pcap</code> I was able to create a pcap from your data. Now, feeding it it to tshark shows:</p><pre><code>Frame 1: 62 bytes on wire (496 bits), 62 bytes captured (496 bits)
Raw packet data
Internet Protocol Version 4, Src: 192.168.2.100, Dst: 192.168.2.2
Transmission Control Protocol, Src Port: 51467 (51467), Dst Port: commplex-main (5000), Seq: 1, Ack: 1, Len: 10
IPA protocol ip.access, type: unknown 0x83</code></pre><p>The TCP payload in question is:</p><pre><code>ac 50 83 00 01 04 43 12 51 ae</code></pre><p>This does not look human-readable text at all. With just one packet it is also hard to get more information out of it. When you have multiple packets and recognize a pattern, then that could suggest that some kind of message framing is involved. If it still looks like complete gibberish with high entropy, then it is possible encrypted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '16, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-57822" class="comments-container"><span id="57824"></span><div id="comment-57824" class="comment"><div id="post-57824-score" class="comment-score"></div><div class="comment-text"><p>I wasnt sure if i was doing anything wrong or not. It seems i am getting the same result that you are. Is there anything i can do in order to see if its possible to decrypt the payload? I have a pcap file also with numerous back and forth that i exported. Would that help to figure out if its possible or not?</p></div><div id="comment-57824-info" class="comment-info"><span class="comment-age">(03 Dec '16, 14:13)</span> m0nk37</div></div><span id="57825"></span><div id="comment-57825" class="comment"><div id="post-57825-score" class="comment-score"></div><div class="comment-text"><p>The data does not look very random (the distribution is not uniform), I guess that there is some framing involved. Maybe there is a fixed header followed by the length, and "04" says that there are four bytes following (43 12 51 ae). However I am not guessing based on this little information. I suggest that you have a look at all the packets that are involved. You could for example use the Follow TCP Stream option and use the "Hex" mode to see packets aligned under each other.</p><p>And if you know what application it is, then it should also give you some hints about the possible protocol.</p></div><div id="comment-57825-info" class="comment-info"><span class="comment-age">(03 Dec '16, 14:28)</span> Lekensteyn</div></div></div><div id="comment-tools-57822" class="comment-tools"></div><div class="clear"></div><div id="comment-57822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

