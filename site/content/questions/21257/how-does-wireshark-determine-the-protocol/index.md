+++
type = "question"
title = "How does wireshark determine the protocol?"
description = '''We have just ventured into wireshark. We notice the protocol field. How does wireshark determines the protocol is it based on the port number or level 3 protocol numbers? For instance DNS what does it look out for?'''
date = "2013-05-19T01:25:00Z"
lastmod = "2013-05-19T02:22:00Z"
weight = 21257
keywords = [ "protocol", "wireshark" ]
aliases = [ "/questions/21257" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How does wireshark determine the protocol?](/questions/21257/how-does-wireshark-determine-the-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21257-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have just ventured into wireshark. We notice the protocol field. How does wireshark determines the protocol is it based on the port number or level 3 protocol numbers? For instance DNS what does it look out for?</p></div><div id="question-tags" class="tags-container tags">protocol wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '13, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/26750873415fcbe30ebf2fdeab499d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbie14&#39;s gravatar image" /><p>newbie14<br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbie14 has no accepted answers">0%</span></p></div></div><div id="comments-container-21257" class="comments-container"></div><div id="comment-tools-21257" class="comment-tools"></div><div class="clear"></div><div id="comment-21257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21258"></span>

<div id="answer-container-21258" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21258-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>About the same way your system is recognizing which process to send the received packets to. First of wireshark read the link layer type from the interface it is capturing from. It then knows which protocol to use for the dissection of the first octets in the packet. Let's assume ethernet. Wireshark will dissect the destination and source mac address and then it will read the ethertype field <a href="https://en.wikipedia.org/wiki/Ethernet_frame">(assuming it is a Ethernet-II frame, which is the most common</a>).</p><p>The ethertype will point to the protocol that was carried in the ethernet frame. Examples are 0x0806 for ARP or 0x0800 for IP. So assuming IP, wireshark will call the IP dissector passing along the payload from the ethernet frame. The IP dissector will dissect all the IP headers and will look at the "protocol" field to determine which dissector to pass the payload to. Examples are 1 for ICMP, 6 for TCP and 17 for UDP.</p><p>Assuming UDP, the UDP dissector will dissect the UDP header and will look at the ports to determine which dissector it will send the payload to. Since there are two ports, wireshark has some rules to determine which port to follow. It will try to map a packet to a conversation. If a packet does not belong to a conversation, the destination port will be examined first as the biggest chance is that it is a request and then the destination port is linked to the protocol in use (yes, UDP and TCP dissectors will register themselves to port numbers).</p><p>Sometimes dynamic dissecting is done by examining packets which will hint that a new session will arrive. Like the FTP PORT command will indicate that a new TCP session will be created which should be treated as FTP-DATA. So wireshark then adds a conversation with the ports from the port command to make sure the session will be interpreted as ftp-data.</p><p>There are also hearistic dissectors. They will examine the payload of the packet to determine if the data matches its protocol specification, if so, it will dissect the packet. If not, it will tell Wireshark to try another dissector.</p><p>So, wireshark uses a colelction of mechanisms to determine which protocol it should use to dissect the data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '13, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21258" class="comments-container"><span id="21260"></span><div id="comment-21260" class="comment"><div id="post-21260-score" class="comment-score"></div><div class="comment-text"><p>when you state this "It then knows which protocol to use for the dissection of the first octets in the packet." IS this protocol known or avaialable as open source? I can pretty much follow it from the level 3 once it determine the protocol it goes high to application level and try to determine the protocol if it fails then it shows the level 3 protocol? Am I right here? Is there any reference avaialable on how wireshark does its protocol dissection?</p></div><div id="comment-21260-info" class="comment-info"><span class="comment-age">(19 May '13, 03:08)</span> newbie14</div></div><span id="21261"></span><div id="comment-21261" class="comment"><div id="post-21261-score" class="comment-score">1</div><div class="comment-text"><p>With "It then knows which protocol to use for the dissection of the first octets in the packet." I meant: If the interfaces link layer type is ethernet, then wireshark knows that it needs to start with the ethernet dissector. And if the link layer type was PPP, it knows it needs to start with the PPP dissector.</p><p>Yes, if wireshark can't determine how to dissect a certain payload, it will stop dissection there. So if the TCP dissector is not able to determine the type of payload, it will show up as data and the info column will display the TCP information instead of higher-layer information.</p><p>There is no reference on how wireshark does its protocol dissection. However, you might learn from the <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/">developer documentation</a> or the source code of the dissector of interest :-)</p></div><div id="comment-21261-info" class="comment-info"><span class="comment-age">(19 May '13, 03:38)</span> SYN-bit ♦♦</div></div><span id="21262"></span><div id="comment-21262" class="comment"><div id="post-21262-score" class="comment-score"></div><div class="comment-text"><p>@Syn-Bin I went to this link <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/packet-PROTOABBREV.c?revision=48861&amp;view=markup">http://anonsvn.wireshark.org/viewvc/trunk/doc/packet-PROTOABBREV.c?revision=48861&amp;view=markup</a> is it the relevant code for protocol dissection ?</p></div><div id="comment-21262-info" class="comment-info"><span class="comment-age">(19 May '13, 07:34)</span> newbie14</div></div></div><div id="comment-tools-21258" class="comment-tools"></div><div class="clear"></div><div id="comment-21258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

