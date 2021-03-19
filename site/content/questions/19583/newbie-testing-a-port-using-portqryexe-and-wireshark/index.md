+++
type = "question"
title = "Newbie : Testing a port using Portqry.exe and Wireshark"
description = '''Hello All,  I am a newbie in networking and wireshark. To test a port, I am using portqry.exe on a sender server and capturing packets on the receving PC. Please advise if my suspicion of a network issue is reasonable. Thanks.  portqry.exe -n 10.20.30.40 -e 68 -p udp -sp 4011  - I understand portqry...'''
date = "2013-03-17T00:05:00Z"
lastmod = "2013-03-17T00:05:00Z"
weight = 19583
keywords = [ "portqry", "udp" ]
aliases = [ "/questions/19583" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Newbie : Testing a port using Portqry.exe and Wireshark](/questions/19583/newbie-testing-a-port-using-portqryexe-and-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19583-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I am a newbie in networking and wireshark.</p><p>To test a port, I am using portqry.exe on a sender server and capturing packets on the receving PC.</p><p>Please advise if my suspicion of a network issue is reasonable. Thanks.</p><ul><li>portqry.exe -n 10.20.30.40 -e 68 -p udp -sp 4011 - I understand portqry sends a dummy packet to host (-n) at port (-e) from port(-sp) using protocol (-p) - 10.20.30.40 is a random PC in some other Adsite</li><li>Wireshark captures packets at 10.20.30.40; no capture filters set</li><li><p>when portqry.exe executed from : (a) W2K8 WDS server (boot image server) : No packets were received by 10.20.30.40 (b) a random XP PC in same subnet of WDS server : No packets were received by 10.20.30.40 (c) a random WDS W2K8 server from ANOTHER Adsite : UDP Packet received fine.</p></li><li><p>If I change the portqry.exe protocol from udp to tcp, then packet is received fine from all WDS/XP/Server above.</p></li><li>Windows Firewall on W2K8 servers is disabled.</li><li>HP Switches</li></ul><p>Based on the above, can I conclude that UDP packets that originate from the first Adsite with source port as 4011 do not reach their destination due to a network issue?</p></div><div id="question-tags" class="tags-container tags">portqry udp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '13, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/33b6d240392d83aef87df5a43442235a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aruntechie123&#39;s gravatar image" /><p>aruntechie123<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aruntechie123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Mar '13, 01:52</p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-19583" class="comments-container"></div><div id="comment-tools-19583" class="comment-tools"></div><div class="clear"></div><div id="comment-19583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

