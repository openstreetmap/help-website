+++
type = "question"
title = "Insensitive network tap or wireshark 1.6.7 dropping packets?"
description = '''I have a Datacom Systems Singlestream 10/100 Link Aggregation tap (http://www.datacomsystems.com/datasheets/SS-100.pdf) between my LAN and my WAN router. I should be seeing all traffic to/from this site&#x27;s network on a laptop connected to one of the monitor ports on the tap. I have Wireshark 1.6.7 ru...'''
date = "2012-05-17T08:21:00Z"
lastmod = "2012-05-17T14:47:00Z"
weight = 11105
keywords = [ "tunnel", "tap", "dropping", "packets" ]
aliases = [ "/questions/11105" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Insensitive network tap or wireshark 1.6.7 dropping packets?](/questions/11105/insensitive-network-tap-or-wireshark-167-dropping-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11105-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Datacom Systems Singlestream 10/100 Link Aggregation tap (<a href="http://www.datacomsystems.com/datasheets/SS-100.pdf)">http://www.datacomsystems.com/datasheets/SS-100.pdf)</a> between my LAN and my WAN router. I should be seeing all traffic to/from this site's network on a laptop connected to one of the monitor ports on the tap. I have Wireshark 1.6.7 running on the laptop.</p><p>I am unable to see full traffic between a couple of devices on the LAN going to remote destinations across the WAN. For example, there are a couple of timeclocks that report to a public internet address. I see the SYN go out but no SYN/ACK coming back and then I see the ACK go back out and then a POST command and then two FIN/ACKs outbound to close the connection. I don't see any return traffic originating from the external public IP address. The transactions are using TCP.</p><p>I can ping the timeclocks and see the traffic in the packet capture but if I SSH to the timeclock I do not see that traffic captured. If I ping from the timeclock out, I can see that traffic from the timeclock AND I can see the return traffic. But Wireshark does not see anything when telnetting FROM the timeclock to a host on the WAN. The telnet session works fine so I know the traffic is going across the WAN link - AND THERE IS ONLY ONE WAY IN/OUT of this site's network.</p><p>NOTE: the only capture filter on the client is to capture traffic NOT for local MAC address - I don't want it to capture my RDP or VNC session traffic or any other traffic to/from the laptop.<br />
</p><p>I don't think that these timeclocks are using any kind of VPN tunnel or anything to get access to the network but I'm not sure how to confirm that by looking at the network traffic since the MAC addresses are changed during the pkt transfer between the LAN switch and the WAN router. But I still should see any tunnel traffic as using the local LAN IP as the tunnel source since there is only one IPv4 address on the system.</p><p>I am really at a loss of how to find out what traffic there is between the timeclocks and the WAN. I have only one network tap at this site and it is in service between the WAN router &amp; LAN switch - so removing it would take the site offline for a while. I suppose I could mirror the timeclock LAN port to another port but I would need another NIC in the wireshark system to view the traffic (I am remote to this network).</p><p>Any ideas?</p><p>Thanks for the help!</p><p>====</p><p>Laptop has only one nic - the wireless nic is disabled. The tap specified above has an aggregation port that also permits network injection so that is how I am remotely reaching the laptop &amp; doing capture at the same time.</p><p>For this site there should be no encapsulation between the LAN &amp; WAN as there are no VLANs defined at the WAN router. The LAN switch does all of the layer 3 work for local services. Silly question alert - how do I display filter for 801.1Q traffic? &lt;- google search in progress ;)</p><p>There is a McAfee firewall installed on the laptop but wireshark is a permitted application. None of the other specified interfering programs are installed/active on the laptop.</p><p>This is the first time using this laptop for capture. Remote site set it up for me.</p></div><div id="question-tags" class="tags-container tags">tunnel tap dropping packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '12, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/d1f7fabf169915dc5ba93025794b84db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Labnuke&#39;s gravatar image" /><p>Labnuke<br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Labnuke has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 May '12, 09:40</p></div></div><div id="comments-container-11105" class="comments-container"><span id="11113"></span><div id="comment-11113" class="comment"><div id="post-11113-score" class="comment-score"></div><div class="comment-text"><p>btw - all captured packets do not have any VLAN data included. Ran display filter "vlan" no packets were shown.</p></div><div id="comment-11113-info" class="comment-info"><span class="comment-age">(17 May '12, 12:28)</span> Labnuke</div></div><span id="11120"></span><div id="comment-11120" class="comment"><div id="post-11120-score" class="comment-score"></div><div class="comment-text"><p>VLAN tags are usually stripped by NICs, so they may have been on the wire, just not in your trace file. See <a href="http://wiki.wireshark.org/CaptureSetup/VLAN">http://wiki.wireshark.org/CaptureSetup/VLAN</a> for more info on that subject :-)</p></div><div id="comment-11120-info" class="comment-info"><span class="comment-age">(17 May '12, 15:04)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-11105" class="comment-tools"></div><div class="clear"></div><div id="comment-11105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11107"></span>

<div id="answer-container-11107" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11107-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I assume your laptop has 2 NICs, one for management (RDP/VNC/etc) and one for capturing (atatched to the TAP). Then it is not necessary to use your mac-capture filter, as your management traffic will not be visible on the capture interface.</p><p>Does the capture interface of your laptop make correct traces in other setups (span ports, hubs, etc)?</p><p>Are you running any <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">interfering software</a> like VPN, Host based FW, etc?</p><p>Is traffic between the LAN and WAN router using some form of encapsulation? 801.1Q vlan tagging for instance? Is so, which traffic is untagged and which traffic is tagged? Does your laptop capture vlan-tagged frames in other situations?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '12, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-11107" class="comments-container"></div><div id="comment-tools-11107" class="comment-tools"></div><div class="clear"></div><div id="comment-11107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11118"></span>

<div id="answer-container-11118" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11118-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><code>There is a McAfee firewall installed on the laptop but wireshark is a permitted application.</code></p></blockquote><p>As you do <strong>see ICMP traffic</strong> (ping time servers) but there are <strong>problems with TCP traffic</strong> (ssh, telnet), I suspect the <strong>McAfee firewall</strong> might still interfere with wireshark, although it is a "permitted application". I have seen similar problems with all kinds of Desktop firewalls - not necessarily together with Wireshark. Never trust them if their configuration says, that network access won't be blocked ;-).</p><p>Please try to <strong>disable McAfee</strong> completely, OR <strong>boot your Laptop from a Linux Bootable CDROM</strong> (or USB flash drive). If you can see TCP traffic afterwards, you know who is resonsible for the problems ;-)</p><p>If it's still the same problem, there might be something wrong with your TAP setup (cabling) or the TAP itself. Test the TAP in front on another PC on your network.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '12, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-11118" class="comments-container"><span id="11172"></span><div id="comment-11172" class="comment"><div id="post-11172-score" class="comment-score"></div><div class="comment-text"><p>The timeclocks are being changed out. When the replacement clocks arrive I will do additional testing. Thank you for the feedback.</p></div><div id="comment-11172-info" class="comment-info"><span class="comment-age">(21 May '12, 05:03)</span> Labnuke</div></div></div><div id="comment-tools-11118" class="comment-tools"></div><div class="clear"></div><div id="comment-11118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

