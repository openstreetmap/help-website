+++
type = "question"
title = "icmp replies come back but the switch says the target is unreachable..."
description = '''have you ever seen this ? From a switch (on the same VLAN etc), I send ping to a target server. The ICMP reply comes back (I can see it in the wireshark trace file). Unfortunately in the CLI of the switch, this is like it gets no Echo reply !! And of course I take the PCAP on the switch itself, so I...'''
date = "2016-10-17T03:47:00Z"
lastmod = "2016-10-17T05:02:00Z"
weight = 56448
keywords = [ "icmp", "echo" ]
aliases = [ "/questions/56448" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [icmp replies come back but the switch says the target is unreachable...](/questions/56448/icmp-replies-come-back-but-the-switch-says-the-target-is-unreachable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56448-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>have you ever seen this ? From a switch (on the same VLAN etc), I send ping to a target server. The ICMP reply comes back (I can see it in the wireshark trace file). Unfortunately in the CLI of the switch, this is like it gets no Echo reply !! And of course I take the PCAP on the switch itself, so I'm sure the Echo reply gets back to the switch.</p><p>Have tried everything : - change the target IP address of the server - change the network adapater of the target server - change the port on which the server is connected</p><p>I only have this problem with this particular server. All other servers work perfectly in the same network environment.</p><p>The switch is a Cisco Nexus switch.</p><p>any idea ?</p></div><div id="question-tags" class="tags-container tags">icmp echo</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '16, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/eac75eef24254c1c9ee690951f6c4006?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thierryn&#39;s gravatar image" /><p>thierryn<br />
<span class="score" title="21 reputation points">21</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thierryn has no accepted answers">0%</span></p></div></div><div id="comments-container-56448" class="comments-container"><span id="56450"></span><div id="comment-56450" class="comment"><div id="post-56450-score" class="comment-score"></div><div class="comment-text"><p>The idea would be that you can see the response packet in the capture but the switch does not recognize it as a response to its particular echo request due to mismatch of some field.</p><p>Can you publish the trace file?</p></div><div id="comment-56450-info" class="comment-info"><span class="comment-age">(17 Oct '16, 04:30)</span> sindy</div></div><span id="56451"></span><div id="comment-56451" class="comment"><div id="post-56451-score" class="comment-score"></div><div class="comment-text"><p>Yes sure, but how can I upload a tracefile ? (sorry for this stupid question but I do not see any file upload possibility).</p></div><div id="comment-56451-info" class="comment-info"><span class="comment-age">(17 Oct '16, 04:33)</span> thierryn</div></div><span id="56452"></span><div id="comment-56452" class="comment"><div id="post-56452-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I do not see any file upload possibility</p></blockquote><p>Correct, there is none. You have to upload your file to Cloudshark or to any plain file publishing service (Dropbox, Google Drive, Microsoft Onedrive, ...) and edit your question with a login-free link to it.</p></div><div id="comment-56452-info" class="comment-info"><span class="comment-age">(17 Oct '16, 04:35)</span> sindy</div></div><span id="56453"></span><div id="comment-56453" class="comment"><div id="post-56453-score" class="comment-score"></div><div class="comment-text"><p>OK, thanks.</p><p>there it is : <a href="https://www.dropbox.com/s/aoeydiup6cbovh8/5_fresenius2.pcap?dl=0">https://www.dropbox.com/s/aoeydiup6cbovh8/5_fresenius2.pcap?dl=0</a></p></div><div id="comment-56453-info" class="comment-info"><span class="comment-age">(17 Oct '16, 04:40)</span> thierryn</div></div></div><div id="comment-tools-56448" class="comment-tools"></div><div class="clear"></div><div id="comment-56448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56454"></span>

<div id="answer-container-56454" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56454-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, the IP and ICMP contents of the Ethernet frames is fine, but look at the MAC addresses. The echo request from IP address <code>192.168.26.1</code> is sent with source MAC address <code>00:46:36:80:fc:04</code> (vendor unknown although bit 6 of the MAC address indicates that it is globally unique), but the echo response to the same IP, <code>192.168.26.1</code>, has <code>4c:00:82:a1:c0:83</code> as destination MAC address (some Cisco box). So the responding server's ARP table maps <code>192.168.26.1</code> to <code>4c:00:82:a1:c0:83</code>, which means that the switch which has sent the request never gets the response.</p><p>Have a look at your IP address assignments and MAC addresses of different pieces of your equipment. Maybe there is a static record in that particular server's ARP table?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '16, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56454" class="comments-container"><span id="56457"></span><div id="comment-56457" class="comment"><div id="post-56457-score" class="comment-score"></div><div class="comment-text"><p>ohhh, stupid am I. Was only focused on the ICMP part. Thanks !!</p></div><div id="comment-56457-info" class="comment-info"><span class="comment-age">(17 Oct '16, 05:08)</span> thierryn</div></div></div><div id="comment-tools-56454" class="comment-tools"></div><div class="clear"></div><div id="comment-56454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

