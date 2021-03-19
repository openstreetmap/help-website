+++
type = "question"
title = "Gratuitous ARP has unknown manufactures &quot;Target MAC address"
description = '''I have two 3Com switches (SuperStack 4 Switch 5500-El) that are sending out GARPs on a regular basis throughout the day. The weird thing is, besides the fact that they are GARPing regularly, is that the &quot;Target MAC address&quot; under the &quot;Address Resolution Protocol (request/gratuitous ARP) is a mac add...'''
date = "2016-03-25T11:18:00Z"
lastmod = "2016-03-25T12:20:00Z"
weight = 51195
keywords = [ "arp", "garp", "gratuitous" ]
aliases = [ "/questions/51195" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Gratuitous ARP has unknown manufactures "Target MAC address](/questions/51195/gratuitous-arp-has-unknown-manufactures-target-mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51195-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two 3Com switches (SuperStack 4 Switch 5500-El) that are sending out GARPs on a regular basis throughout the day. The weird thing is, besides the fact that they are GARPing regularly, is that the "Target MAC address" under the "Address Resolution Protocol (request/gratuitous ARP) is a mac address whose manufacturers octets are unknown. The "Target MAC address" is different for each of the switches. The switch located at IP 192.168.56.241 has ae:59:16:83:e9:c5 for its "Target MAC address" and The switch located at IP 192.168.56.242 has 81:41:0c:62:70:bb for its "Target MAC address" I thought that the mac address listed under "Target MAC address" was supposed to be a broadcast, 0.0.0.0 or ff.ff.ff.ff. Is this an indicator of malicious activity, or am I missing something obvious?</p></div><div id="question-tags" class="tags-container tags">arp garp gratuitous</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '16, 11:18</strong></p><img src="https://secure.gravatar.com/avatar/1e255b843a59ef2b041ab3f5b3f859ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bruce%20Garoutte&#39;s gravatar image" /><p>Bruce Garoutte<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bruce Garoutte has no accepted answers">0%</span></p></div></div><div id="comments-container-51195" class="comments-container"></div><div id="comment-tools-51195" class="comment-tools"></div><div class="clear"></div><div id="comment-51195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51196"></span>

<div id="answer-container-51196" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51196-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe this article could help you: <a href="http://crnetpackets.com/2015/08/28/special-type-of-arp-packets/">http://crnetpackets.com/2015/08/28/special-type-of-arp-packets/</a></p><p>And could you provide us a pcap with this packet?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '16, 12:20</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-51196" class="comments-container"><span id="51197"></span><div id="comment-51197" class="comment"><div id="post-51197-score" class="comment-score"></div><div class="comment-text"><p>The article pretty much sums up what I have read elsewhere, so I am still at a loss to explain this.</p><p><a href="https://mydata.industrialfinishes.com/?linkid=KZi4zr6VWWX3n/zRowesmJv737vgnfzJ/oDODS6ncAGbVD1e5e81qg">pcap can be retrieved from here</a></p><p>Thank you</p></div><div id="comment-51197-info" class="comment-info"><span class="comment-age">(25 Mar '16, 12:36)</span> Bruce Garoutte</div></div><span id="51198"></span><div id="comment-51198" class="comment"><div id="post-51198-score" class="comment-score"></div><div class="comment-text"><p>I converted your answer to a comment. As it is more a comment, to my answer.</p><p>Yes I have no fast answer for this... Maybe the answer is at the system...</p><p>But at least we can see that the knows how a correct gratious arp does work</p><p><img src="https://osqa-ask.wireshark.org/upfiles/25-03-_2016_21-14-17.png" alt="alt text" /></p></div><div id="comment-51198-info" class="comment-info"><span class="comment-age">(25 Mar '16, 13:14)</span> Christian_R</div></div><span id="51202"></span><div id="comment-51202" class="comment"><div id="post-51202-score" class="comment-score"></div><div class="comment-text"><p>OK, thanks for the conversion. I'm not sure how to upload a picture here, so I attached it to the "Your Answer". If you open the packet, and peak inside, there is still the unknown mac address residing in the "Target MAC address" area. My concern is whether this might be a "man in the middle" type of attack signature since it (1) does not conform to the RFC and (2) the mac address of 81:41:0c:62:70:bb appears to not belong to any manufacturer as far as I could find.</p></div><div id="comment-51202-info" class="comment-info"><span class="comment-age">(25 Mar '16, 13:31)</span> Bruce Garoutte</div></div><span id="51203"></span><div id="comment-51203" class="comment"><div id="post-51203-score" class="comment-score"></div><div class="comment-text"><p><a href="https://osqa-ask.wireshark.org/upfiles/Gratuitous_ARP_for_.56.242-A.PNG">Frame inspection showing unknown mac address</a></p></div><div id="comment-51203-info" class="comment-info"><span class="comment-age">(25 Mar '16, 13:31)</span> Bruce Garoutte</div></div><span id="51210"></span><div id="comment-51210" class="comment"><div id="post-51210-score" class="comment-score"></div><div class="comment-text"><p>This could be... You should find out if these special Gratious ARPs<br />
has been sent by the 3COM devices or not...<br />
If not...<br />
You should search out these target mac devices in your network<br />
(but maybe they are defined somewhere on the 3COM devices).</p></div><div id="comment-51210-info" class="comment-info"><span class="comment-age">(25 Mar '16, 14:25)</span> Christian_R</div></div><span id="51213"></span><div id="comment-51213" class="comment not_top_scorer"><div id="post-51213-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I thought that the mac address listed under "Target MAC address" was supposed to be a broadcast, 0.0.0.0 or ff.ff.ff.ff.</p></blockquote><p>The "target MAC address" in the ARP part of the frame is supposed to be <em>the same</em> like the "destination MAC address" in the Ethernet header of the frame. So <em>both</em> should be the broadcast one in case of ARP requests (including GARP request) and <em>both</em> should be the same individual MAC address in case of ARP response (or of a request which is sent to an already known L3 target which can also happen).</p><p>However, if sender and target L3 (IPv4 in this case) addresses are the same, which is the case with gratuitous ARP, the target MAC address is not really relevant.</p><p>You cannot find any of your two weird addresses among manufacturer assigned prefixes because one of them has bit 1 of the first byte set (0xae &amp; 0x2 = 0x2), meaning it is a privately assigned one, and the other one has bit 0 set (0x81 &amp; 0x1 = 0x1) meaning it is a multicast address, yet multicast MAC addresses starting with 0x81 are currently not assigned for any purpose.</p><p>So I would suspect rather a bug of the switches than some malware running on them; however, there might be some other machine sending GARP and spoofing the MAC address of the switch as the source one, in an attempt to steal the traffic towards the admin interface of the switch (and probably even unaware that it was an admin interface of a switch). And there would have to be a bug in that malware, causing the target address to be this weird.</p><p>I'm afraid that in order to find out which of these two cases is true, you would have to shut down all ports of one of the switches, except a single one to which your sniffing machine would be connected, and see whether the corresponding GARP packets still come. If yes, the switch itself sends them; if not, start enabling the ports one by one to find out from which connected box they come.</p></div><div id="comment-51213-info" class="comment-info"><span class="comment-age">(25 Mar '16, 15:32)</span> sindy</div></div><span id="51240"></span><div id="comment-51240" class="comment not_top_scorer"><div id="post-51240-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the suggestions. I have done just that. It appears that these switches do use GARP to ensure there is only one layer three device on the network. The unknown mac address does not exist on our network, nor anywhere on this planet according to the three Mac address look-ups I used, including Wiresharks. After reading the appropriate area in the setup manual, there appeared to not be a setting for the Target MAC address, so that part is still a mystery to me.</p><p>Thank you for all your help on this. If I find a reason for the unknown MAC, I'll update this post.</p></div><div id="comment-51240-info" class="comment-info"><span class="comment-age">(28 Mar '16, 12:56)</span> Bruce Garoutte</div></div></div><div id="comment-tools-51196" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-51196-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

