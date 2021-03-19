+++
type = "question"
title = "Packets end with layer 3"
description = '''Hi, If wireshark get as an input packets header which ends with layer 3 (for example its last header is ipv4) , How can he analyzes the packet, knowing the next &quot;protocol&quot; after layer 3 is the data (payload), without display in its pdml output :  &amp;lt;proto name=&quot;**fake-field-wrapper**&quot;&amp;gt; (after &amp;l...'''
date = "2017-06-13T01:36:00Z"
lastmod = "2017-06-13T01:57:00Z"
weight = 61978
keywords = [ "fake-field-wrapper", "ipv4" ]
aliases = [ "/questions/61978" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packets end with layer 3](/questions/61978/packets-end-with-layer-3)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61978-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, If wireshark get as an input packets header which ends with layer 3 (for example its last header is ipv4) , How can he analyzes the packet, knowing the next "protocol" after layer 3 is the data (payload), without display in its pdml output : &lt;proto name="**fake-field-wrapper**"&gt;</p><p>(after &lt;proto name="ip" showname="Internet Protocol Version 4, Src: 117.19.217.140, Dst: 210.74.88.180" size="20" pos="72"&gt;)</p><p>Thanks, Aya/</p></div><div id="question-tags" class="tags-container tags">fake-field-wrapper ipv4</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '17, 01:36</strong></p><img src="https://secure.gravatar.com/avatar/3cca087c83f55798a15e19db6111ce67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aya%20dagan&#39;s gravatar image" /><p>aya dagan<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aya dagan has no accepted answers">0%</span></p></div></div><div id="comments-container-61978" class="comments-container"></div><div id="comment-tools-61978" class="comment-tools"></div><div class="clear"></div><div id="comment-61978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61979"></span>

<div id="answer-container-61979" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61979-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>IP has a "protocol" field in the header that tells what protocol comes next, e.g. 1 for ICMP, 6 for TCP and 17 for UDP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '17, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61979" class="comments-container"><span id="61987"></span><div id="comment-61987" class="comment"><div id="post-61987-score" class="comment-score"></div><div class="comment-text"><p>thank you for your answer, I know this, but I ask if a packets header terminate with ip header (layer 3) , hence after it , there is no TCP/UDP etc.. in this case, what will be this "protocol" field</p></div><div id="comment-61987-info" class="comment-info"><span class="comment-age">(13 Jun '17, 06:58)</span> aya dagan</div></div><span id="61989"></span><div id="comment-61989" class="comment"><div id="post-61989-score" class="comment-score"></div><div class="comment-text"><p>If the packet on the wire does not have a protocol on top of IPv4, then this packet shouldn't be there; there is no reason to have a network layer packet without something to transport. The IP proto number space has no value for 'there is no transport protocol on top of this IP packet'.</p><p>If the packet was captured up to the transport protocol then the IP header would contain the IP proto of this transport protocol, even thought the captured packet would not show the transport protocol fields itself.</p></div><div id="comment-61989-info" class="comment-info"><span class="comment-age">(13 Jun '17, 10:38)</span> Jaap ♦</div></div><span id="61990"></span><div id="comment-61990" class="comment"><div id="post-61990-score" class="comment-score"></div><div class="comment-text"><p>Well, for IPv6 there is in fact protocol number 59, "No Next Header", but I don't think there's something like that for IPv4...</p></div><div id="comment-61990-info" class="comment-info"><span class="comment-age">(13 Jun '17, 11:30)</span> Jasper ♦♦</div></div></div><div id="comment-tools-61979" class="comment-tools"></div><div class="clear"></div><div id="comment-61979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

