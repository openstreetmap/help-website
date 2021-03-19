+++
type = "question"
title = "Semi-ETHERNET-compatible proprietary 802.3 protocol problems"
description = '''Hi all,  I work for a large company which had developed and maintained its own internal and proprietary 802.3 protocol since the late 90s. This protocol is kinda-sorta-compliant to early ETHERNET standards, so we could still use our desktop wired network adapters to eavesdrop on our traffic, and iro...'''
date = "2014-12-30T14:52:00Z"
lastmod = "2014-12-30T14:52:00Z"
weight = 38813
keywords = [ "ethertype", "proprietary", "packet", "802.3", "truncated" ]
aliases = [ "/questions/38813" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Semi-ETHERNET-compatible proprietary 802.3 protocol problems](/questions/38813/semi-ethernet-compatible-proprietary-8023-protocol-problems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38813-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I work for a large company which had developed and maintained its own internal and proprietary 802.3 protocol since the late 90s.</p><p>This protocol is <em>kinda-sorta-compliant</em> to early ETHERNET standards, so we could still use our desktop wired network adapters to eavesdrop on our traffic, and iron out the bugs as needed. -- well, at least as long as I've worked here, since the mid 90s.</p><p>Anyway, what used to work before (with WIRESHARK on MSWindows and up until last October), now DOESNT work. Pre Oct-2014 our network drivers in our laptops worked perfectly with Wireshark, and we could always sniff all 802.3 traffic between our boxes.</p><p>NOW, (since some WINDOWS update in mid-Oct-2014), Wireshark is not being passed ALL of our packet data.<br />
</p><p>The issue is this (I speculate)...</p><p>In our proprietary 802.3 std comms, the ETHERTYPE/PACKETSIZE field (word at offset 12) is coincidentally <em>ALWAYS</em> a hardcoded constant value of 0x0080 (128 decimal). And in reality, our network packets are always transmitted with a constant payload size of 1400 bytes,</p><p>And, happily, my network adapter never cared. Even though the (non-)Ethernet header always had a hardcoded LENGTH value of 128 at offset=12, the Windows Ethernet driver ALWAYS returned ALL the actual packet data to Wireshark -- all 1400 bytes of payload in addition to the enveloping info, etc. And so we could see all the data and everything, and life was good.</p><p>(and coincidentally, since our packets were NEVER smaller than 128 bytes, no packets were ever rejected as RUNTs)</p><p>Anyway, something happened to our network driver software (in Windows), which PROHIBITS passing through the packet data beyond 128 bytes worth of data -- or what my network driver probably now thinks is possible malicious code.</p><p>Now, when I Wireshark this interface, I get ONLY the first 128 bytes of payload (142 bytes including envelope stuff).</p><p>AND SO... (now for the MONEY STATEMENT)...</p><p>What can I do about this? Does anyone know if this is a WINDOWS KERNAL ISSUE, or simply a Windows Registry Issue.<br />
</p><p>Needless to say, I am considered just another mindless drone in a corporate cubicle-farm by my IT department. I do NOT have admin privs on my company issued laptop, and frankly, it has taken me almost 2 months now (off-n-on) to educate myself to this meager level.</p><p>So, if I can solicit for some dialog and education here, and also learn the proper vocabulary, I can approach the wizards behind the curtain, and see if they can enable me and my co-workers with whatever I need to get this fixed again. Believe it or not, this does have some pretty serious ramifications to me and my group. I gotta get this worked out.</p><p>Thanks for reading, and please reply with any knowledge you might be able to contribute. Even if it might seem too trivial or primary for the other oracles here. I confess I'm a NOOB. But I want to learn.</p><p>-David B</p></div><div id="question-tags" class="tags-container tags">ethertype proprietary packet 802.3 truncated</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '14, 14:52</strong></p><img src="https://secure.gravatar.com/avatar/736fae666aeef8a4072e3b20e2e18bdf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davidjaybrown&#39;s gravatar image" /><p>davidjaybrown<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davidjaybrown has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-38813" class="comments-container"></div><div id="comment-tools-38813" class="comment-tools"></div><div class="clear"></div><div id="comment-38813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

