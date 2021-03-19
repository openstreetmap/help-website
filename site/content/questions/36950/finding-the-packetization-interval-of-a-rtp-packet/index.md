+++
type = "question"
title = "finding the packetization interval of a RTP packet"
description = '''How do I create a filter to find the packetization interval for a RTP packet?  I can figure it out manually by looking at the size of the rtp payload and the codec used. For example, A 160 byte payload of G.711 has a packetization interval of 20 ms, 240 bytes of G711 has a packetization interval of ...'''
date = "2014-10-09T16:43:00Z"
lastmod = "2014-10-10T08:59:00Z"
weight = 36950
keywords = [ "sip", "rtp", "voip" ]
aliases = [ "/questions/36950" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [finding the packetization interval of a RTP packet](/questions/36950/finding-the-packetization-interval-of-a-rtp-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36950-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I create a filter to find the packetization interval for a RTP packet?</p><p>I can figure it out manually by looking at the size of the rtp payload and the codec used. For example, A 160 byte payload of G.711 has a packetization interval of 20 ms, 240 bytes of G711 has a packetization interval of 30 ms.</p><p>Also, the packetization interval can be found as a media attribute in the SIP/SDP INVITE packet, which will usually be "a=ptime:30" or "a=ptime:20".</p><p><img src="https://osqa-ask.wireshark.org/upfiles/sip-sdp.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">sip rtp voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '14, 16:43</strong></p><img src="https://secure.gravatar.com/avatar/c8c4826681cc8ca94a274bf6a1fdcfae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gsalomon&#39;s gravatar image" /><p>gsalomon<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gsalomon has no accepted answers">0%</span></p></img></div></div><div id="comments-container-36950" class="comments-container"></div><div id="comment-tools-36950" class="comment-tools"></div><div class="clear"></div><div id="comment-36950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36963"></span>

<div id="answer-container-36963" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36963-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure exactly what you want to do... a filter doesn't "find" a value, it filters the packets shown based on the values or fields you tell it to filter for.</p><ol><li>Do you want to only see SIP messages with a certain ptime attribute value? If so, you'd apply a display filter of '<code>sdp.media_attr == "ptime:10"</code>' (or whatever ptime value you want to see the value of). Of course that will only show the SIP messages with SDP containing the ptime attribute, which is not a mandatory attribute and not always included by SIP clients.</li><li>Do you want to only see RTP packets of a specific ptime value? Since RTP has no ptime field to filter by, you'd do it by the packet size as you mentioned. So you'd do something like 'udp.length == 100<code>' for an 80-byte G.711 10ms RTP payload, or 'udp.length == 180</code>' for an 160-byte G.711 20ms RTP payload, etc. (the UDP length field includes the 8 byte UDP header and 12 byte RTP header, so it's 20 bytes larger than the RTP payload)</li><li>Or is it something else you want to do?</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '14, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-36963" class="comments-container"></div><div id="comment-tools-36963" class="comment-tools"></div><div class="clear"></div><div id="comment-36963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36964"></span>

<div id="answer-container-36964" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36964-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't. Well, sorta, but it depends.</p><p>Packetizing takes place in the RTP endpoint. That's were a timer runs to collect samples into an RTP packet and set its timestamp. But, depending on the actual codec used, this may or may not lead to an RTP packet transmission. And it's only the transmitted RTP packets we can analyze.</p><p>So, assuming there's a constant packet stream (no VAD, etc) you could pick out the timestamps of subsequent RTP packets and do the math. But that requires calculation spanning multiple packets. Oke, <a href="http://wiki.wireshark.org/Mate">MATE</a> may be helpful here. Another one is already calculated: delta from previously displayed packet. If you setup a display filter just showing the RTP packets you're interested in then you can use this field. Still it's only an approximation; it's the delta of packet reception, which is somewhat correlated to packetization.</p><p>So, the real answer is in the control protocol, as you have already stated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '14, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-36964" class="comments-container"></div><div id="comment-tools-36964" class="comment-tools"></div><div class="clear"></div><div id="comment-36964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

