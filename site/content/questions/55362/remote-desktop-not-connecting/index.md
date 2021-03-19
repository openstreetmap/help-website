+++
type = "question"
title = "Remote Desktop not connecting"
description = '''Hello, I am troubleshooting a baffling situation where a windows workstation with IP 10.167.178.6 is unable to RDP into windows server at IP 10.0.129.208. There are no connectivity issue between the client and the server other than RDP. There is no ACLs on the routers between the two, and no firewal...'''
date = "2016-09-06T22:54:00Z"
lastmod = "2016-09-06T22:54:00Z"
weight = 55362
keywords = [ "rst", "tcp_retransmission", "rdp" ]
aliases = [ "/questions/55362" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Remote Desktop not connecting](/questions/55362/remote-desktop-not-connecting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55362-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am troubleshooting a baffling situation where a windows workstation with IP 10.167.178.6 is unable to RDP into windows server at IP 10.0.129.208. There are no connectivity issue between the client and the server other than RDP. There is no ACLs on the routers between the two, and no firewall.</p><p>The RDP session does connect initially and the user is prompted for for login credentials, but upon authentication the RDP just hangs. Packet capture shows TCP re-transmissions... I need help decrypting what is causing those retransmissions and the RST. I would greatly appreciate any feedback. Thank you in advance.</p><p>See link below for the pcap:</p><p><a href="https://www.cloudshark.org/captures/6ccd1d7f4690">https://www.cloudshark.org/captures/6ccd1d7f4690</a></p></div><div id="question-tags" class="tags-container tags">rst tcp_retransmission rdp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '16, 22:54</strong></p><img src="https://secure.gravatar.com/avatar/9d1f327bafc1dd9d9be9ae305eeb8417?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pc7&#39;s gravatar image" /><p>pc7<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pc7 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Sep '16, 22:55</p></div></div><div id="comments-container-55362" class="comments-container"><span id="55370"></span><div id="comment-55370" class="comment"><div id="post-55370-score" class="comment-score"></div><div class="comment-text"><p>Just a blind shot - I had a similar situation a couple of months ago. The remedy was to disable jumbo frames in the network card settings of the server. I haven't captured the traffic back then, though.</p></div><div id="comment-55370-info" class="comment-info"><span class="comment-age">(07 Sep '16, 06:20)</span> sindy</div></div><span id="55380"></span><div id="comment-55380" class="comment"><div id="post-55380-score" class="comment-score"></div><div class="comment-text"><p>Hi Sindy, thank you for the feedback. I'll look Jumbo frames.</p></div><div id="comment-55380-info" class="comment-info"><span class="comment-age">(07 Sep '16, 11:44)</span> pc7</div></div><span id="55381"></span><div id="comment-55381" class="comment"><div id="post-55381-score" class="comment-score"></div><div class="comment-text"><p>Seems that that the client did not receive all packets from the server (packet loss).For example: The ACK for Frame 4 is missing.</p><p>If I where you, I would trace as close as possible next to the server, but not onside.</p><p>Is the server on a virtual machine? Have checked the network path (CRC Counters)?</p></div><div id="comment-55381-info" class="comment-info"><span class="comment-age">(07 Sep '16, 13:53)</span> Christian_R</div></div><span id="55382"></span><div id="comment-55382" class="comment"><div id="post-55382-score" class="comment-score"></div><div class="comment-text"><p>Hi Christian_R, yes the server is a virtual machine. I will check the network for CRC counter error. Thanks</p></div><div id="comment-55382-info" class="comment-info"><span class="comment-age">(07 Sep '16, 14:00)</span> pc7</div></div><span id="55385"></span><div id="comment-55385" class="comment"><div id="post-55385-score" class="comment-score"></div><div class="comment-text"><p>Ok, good that you Check the network for CRC. But it could be that you got the packet loss inside the vm.</p></div><div id="comment-55385-info" class="comment-info"><span class="comment-age">(07 Sep '16, 15:46)</span> Christian_R</div></div></div><div id="comment-tools-55362" class="comment-tools"></div><div class="clear"></div><div id="comment-55362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

