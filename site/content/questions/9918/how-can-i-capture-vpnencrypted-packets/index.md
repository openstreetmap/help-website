+++
type = "question"
title = "How can I capture VPN/encrypted packets?"
description = '''Symantec antivirus on a VPN connected Windoze machine is detecting an intrusion from a host on our VPN. Symantec can do this because the VPN client on the destination machine decrypts the messages before Symantec see it. (Right?) I am monitoring using a Mac with Wireshark on a hub which also support...'''
date = "2012-04-03T11:06:00Z"
lastmod = "2012-04-03T11:06:00Z"
weight = 9918
keywords = [ "decrypt", "vpn", "encrypt" ]
aliases = [ "/questions/9918" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I capture VPN/encrypted packets?](/questions/9918/how-can-i-capture-vpnencrypted-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9918-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Symantec antivirus on a VPN connected Windoze machine is detecting an intrusion from a host on our VPN. Symantec can do this because the VPN client on the destination machine decrypts the messages before Symantec see it. (Right?)</p><p>I am monitoring using a Mac with Wireshark on a hub which also supports the Windoze machine that's detecting the intrusion.</p><p>Because the Winders machine is on the VPN, but my monitoring Wireshark machine is not VPN connected, is there some capture filter that can decode the encrypted messages? Assume I can capture the packets which set up the VPN, and I have the RSA passcode.</p><p>The IP message header wouldn't be encrypted (else the network couldn't route it), so shouldn't I see the source host sending the packets?</p><p>Or is the source host's entire message being encrypted by the VPN server at the other end before I get it, and the VPN client removes the IP header and decrypts it, so all I can see by capturing is the destination host and the VPN source host in the packet?</p><p>(I did search 'questions' for VPN and encrypt and got zero hits for either, I'm sorry if this has been answered somewhere.)</p></div><div id="question-tags" class="tags-container tags">decrypt vpn encrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '12, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/c609362c709623fe3591a5da33a4937b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PReinie&#39;s gravatar image" /><p>PReinie<br />
<span class="score" title="15 reputation points">15</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PReinie has no accepted answers">0%</span></p></div></div><div id="comments-container-9918" class="comments-container"></div><div id="comment-tools-9918" class="comment-tools"></div><div class="clear"></div><div id="comment-9918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

