+++
type = "question"
title = "Confusion about when Wireshark actually captures a frame in connection to LSO"
description = '''So I&#x27;ve read in a few places that Wireshark sits right between the protocol stack and the NIC capturing whatever the user want to capture and that it manages to get outgoing Ethernet frames by getting a copy from the NIC on transmission... Well, I&#x27;m all fine with that but I DO wonder one thing about...'''
date = "2014-09-25T07:14:00Z"
lastmod = "2014-09-25T08:56:00Z"
weight = 36599
keywords = [ "ethernet", "tcp", "lso" ]
aliases = [ "/questions/36599" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Confusion about when Wireshark actually captures a frame in connection to LSO](/questions/36599/confusion-about-when-wireshark-actually-captures-a-frame-in-connection-to-lso)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36599-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I've read in a few places that Wireshark sits right between the protocol stack and the NIC capturing whatever the user want to capture and that it manages to get outgoing Ethernet frames by getting a copy from the NIC on transmission... Well, I'm all fine with that but I DO wonder one thing about this...</p><p>When having Large Send Offload (LSO), TCP hands big chunks of data for the NIC to segment and transmit. Now, if the NIC would really provide Wireshark with what it's actually transmitting, we would never see frames with these large data chunks from the TCP layer and we would rather see that data the way it looks like when it reaches the other end (1518 B. frames that is in my case).</p><p>Now, this equation doesn't work... either Wireshark is getting the data after the protocol stack and then recreates the soon to be Ethernet frame before the data moves on to the NIC or there's something else going on that I don't understand... What do you think?</p></div><div id="question-tags" class="tags-container tags">ethernet tcp lso</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '14, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/eb4da28af8b7bb06278efecdb7ad9a64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fast-reflexes&#39;s gravatar image" /><p>fast-reflexes<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fast-reflexes has no accepted answers">0%</span></p></div></div><div id="comments-container-36599" class="comments-container"></div><div id="comment-tools-36599" class="comment-tools"></div><div class="clear"></div><div id="comment-36599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36601"></span>

<div id="answer-container-36601" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36601-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark does not get a copy of the packet <em>from</em> the NIC. Winpcap (on Windows sytems) provides Wireshark with a copy of the packet that is being sent <em>to</em> the NIC. So if LSO is in use, and you are capturing on the sending host, Wireshark is seeing the oversize frames before the NIC segments them into proper sized frames for transmission on the network.</p><p>To see what is transmitted on the wire, capture from the wire, not from one of the endpoints involved in the communication.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '14, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-36601" class="comments-container"><span id="36605"></span><div id="comment-36605" class="comment"><div id="post-36605-score" class="comment-score"></div><div class="comment-text"><p>Thanks! So I take it then that the Ethernet frame headers are already in place when the packet is being handed over to the NIC and that in the case of LSO, the NIC "reopens" the frame and segments its content, readjusts the relevant headers and then passes it onto the wire?</p></div><div id="comment-36605-info" class="comment-info"><span class="comment-age">(25 Sep '14, 10:52)</span> fast-reflexes</div></div><span id="36607"></span><div id="comment-36607" class="comment"><div id="post-36607-score" class="comment-score">1</div><div class="comment-text"><p>Yes, there are headers on the oversized frame that gets passed to the NIC. The NIC segments the frame into multiple smaller frames for transmission on the wire, and puts the appropriate headers on the transmitted frames.</p></div><div id="comment-36607-info" class="comment-info"><span class="comment-age">(25 Sep '14, 10:58)</span> Jim Aragon</div></div><span id="36611"></span><div id="comment-36611" class="comment"><div id="post-36611-score" class="comment-score"></div><div class="comment-text"><p>Aha! So the regular processing is that all headers (maybe except the physical ones: preamble and SFD) are on the packet as it gets passed to the NIC? I think a usual misconception might be that the NIC accepts an IP packet from "above" to which it then puts on the Ethernet headers but it makes sense that these should be in place once it is handed over to the NIC and that the NIC only takes care of the last steps involving actual transmission / handing over the data to the physical layer... That right?</p><p>Thank you very much! You helped me to greater understanding :)</p></div><div id="comment-36611-info" class="comment-info"><span class="comment-age">(25 Sep '14, 11:33)</span> fast-reflexes</div></div><span id="36612"></span><div id="comment-36612" class="comment"><div id="post-36612-score" class="comment-score"></div><div class="comment-text"><p>Actually even if you capture from the wire the host making the capture may assemble the packets if receive offloading is active.</p></div><div id="comment-36612-info" class="comment-info"><span class="comment-age">(25 Sep '14, 11:50)</span> Anders ♦</div></div></div><div id="comment-tools-36601" class="comment-tools"></div><div class="clear"></div><div id="comment-36601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

