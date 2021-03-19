+++
type = "question"
title = "VLAN Tagging with different versions of Wireshark"
description = '''Wireshark version 1.2.11 grabs the VLAN tag in FC_ELS frame but 1.4.6 doesn’t. Running on an ESXi5 or ESXi4, VM1 has Wireshark 1.2.11 and VM2 has Wireshark 1.4.6; both VMs are in the same VM Network in Networking using the same 10GigE adapter to access the network. VM1 platform is Ubuntu version 10....'''
date = "2012-04-11T11:44:00Z"
lastmod = "2012-04-11T11:44:00Z"
weight = 10060
keywords = [ "different", "vlan", "wireshark", "tagging", "versions" ]
aliases = [ "/questions/10060" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [VLAN Tagging with different versions of Wireshark](/questions/10060/vlan-tagging-with-different-versions-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10060-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark version 1.2.11 grabs the VLAN tag in FC_ELS frame but 1.4.6 doesn’t. Running on an ESXi5 or ESXi4, VM1 has Wireshark 1.2.11 and VM2 has Wireshark 1.4.6; both VMs are in the same VM Network in Networking using the same 10GigE adapter to access the network.<br />
VM1 platform is Ubuntu version 10.10 with Wireshark 1.2.11 VM2 platform is Ubuntu version 11.04 with Wireshark 1.4.6</p></div><div id="question-tags" class="tags-container tags">different vlan wireshark tagging versions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '12, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/b1f83ecb39abf722328306193c2a2d78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jobe&#39;s gravatar image" /><p>Jobe<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jobe has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Apr '12, 19:08</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-10060" class="comments-container"><span id="10065"></span><div id="comment-10065" class="comment"><div id="post-10065-score" class="comment-score"></div><div class="comment-text"><p>What exactly do you mean by, "<em>grabs the VLAN tag</em>"? Do you mean the packets aren't captured or the display filter you're using doesn't work or something else? If it's a display filter, what display filter are you using?</p></div><div id="comment-10065-info" class="comment-info"><span class="comment-age">(11 Apr '12, 15:36)</span> cmaynard ♦♦</div></div><span id="10067"></span><div id="comment-10067" class="comment"><div id="post-10067-score" class="comment-score"></div><div class="comment-text"><p>The FC_ELS is captured but the frame doesn't show the VLAN tag. We think it's the Ubuntu on VM2 (Wireshark 1.4.6/Ubuntu version 11.04) that is stripping off the VLAN tag. No display filter is being used.</p></div><div id="comment-10067-info" class="comment-info"><span class="comment-age">(11 Apr '12, 15:48)</span> Jobe</div></div></div><div id="comment-tools-10060" class="comment-tools"></div><div class="clear"></div><div id="comment-10060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

