+++
type = "question"
title = "wireshark with SSL traffic and HTTP filter"
description = '''Hi Guys, Quetion 1: I captures the HTTPS packets.I applied the pre-master keys.Some url&#x27;s I am decrypted as HTTP request and response but some url&#x27;s I am getting &quot;ssl segment of a reassembled pdu&quot;. How to resolve this &quot;ssl segment of a reassembled pdu&quot; in wireshark. I want to see the HTTP request an...'''
date = "2016-02-08T23:38:00Z"
lastmod = "2016-02-09T06:52:00Z"
weight = 49988
keywords = [ "wireshark" ]
aliases = [ "/questions/49988" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark with SSL traffic and HTTP filter](/questions/49988/wireshark-with-ssl-traffic-and-http-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49988-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>Quetion 1:</p><p>I captures the HTTPS packets.I applied the pre-master keys.Some url's I am decrypted as HTTP request and response but some url's I am getting "ssl segment of a reassembled pdu".</p><p>How to resolve this "ssl segment of a reassembled pdu" in wireshark. I want to see the HTTP request and responce for all HTTPS packets.</p><p>Is there any option to enable or disable in wireshark.</p><p>Quetion 2:</p><p>1) For HTTP I am getting "tcp segment of a reassembled pdu". How to solve this thing to display as HTTP protocol.</p><p>Quetion 3:</p><p>1) some times for HTTP I am getting "continuation or non HTTP traffic". How to solve this thing also.</p><p>I need urgent reply.Could you please answer the above problem. Thanks for information.</p><p>Regards, Swathi.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '16, 23:38</strong></p><img src="https://secure.gravatar.com/avatar/a34282ab2b31d84bc63d5ea83c15d775?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swathi%20jakkam&#39;s gravatar image" /><p>swathi jakkam<br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swathi jakkam has no accepted answers">0%</span></p></div></div><div id="comments-container-49988" class="comments-container"></div><div id="comment-tools-49988" class="comment-tools"></div><div class="clear"></div><div id="comment-49988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50011"></span>

<div id="answer-container-50011" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50011-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Swathi,</p><p>I am afraid your description is too generic so without the capture file <em>along with the pre-master keys file</em> it is hard to say what may be issues.</p><p>So if you can, post both.</p><p>But in general: whenever a protocol data unit (PDU) of an application protocol which uses TCP as transport is bigger than the available tcp packet size, it has to be split into several TCP packets. Wireshark shows only the last packet carrying that PDU as containing that application protocol, and the dissection of the PDU is available in that last packet; all the packets before are shown as "segment of a reassembled pdu". Now there are two possible cases:</p><ul><li><p>all packets of a given PDU are available in the capture; in such case, dissection of each of the segments contains a link to the last one where the complete (reassembled) PDU is shown,</p></li><li><p>not all packets of a given PDU are available in the capture; in such case, no link is available in the individual packets because the PDU could not be reassembled.</p></li></ul><p>As for "continuation or non-http traffic", the dissector may be missing the context from the previous packets due to packet loss during capture or because you've started the capture after that http communication has already started.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '16, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50011" class="comments-container"></div><div id="comment-tools-50011" class="comment-tools"></div><div class="clear"></div><div id="comment-50011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50013"></span>

<div id="answer-container-50013" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50013-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In general if you're seeing "XXX segment of a reassembled pdu" then you're looking at a middle packet which Wireshark isn't going to show you as HTTP or HTTPS because Wireshark needs the full (reassembled) packet in order to decode it properly. Filter for <code>http</code> or <code>ssl</code> to hide these middle packets and show only the reassembled ones.</p><p>Note: it is possible that the reassembly has actually failed in which case you may not see the reassembled packet. That's common when there are TCP retransmissions or out-of-sequence or missing packets. In these cases generally the best you can do is try to get a better capture.</p><p>For "continuation or non-http traffic" this usually means Wireshark has missed some packets and is seeing the middle of the HTTP stream without having seen the beginning. This will continue until Wireshark sees another start of an HTTP stream. Again, generally the best you can do is get a better capture that doesn't miss any packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '16, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-50013" class="comments-container"></div><div id="comment-tools-50013" class="comment-tools"></div><div class="clear"></div><div id="comment-50013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

