+++
type = "question"
title = "Null / Loopback Link encapsulation conversion"
description = '''Hello All...I&#x27;m stuck. I&#x27;m on OSX 10.6 and I captured on the VPN tunnel interface (Juniper Network Connect jnc0). Wireshark is able to read the file just fine, but when I go to use &quot;advanced&quot; analysis system it tells me that the file is corrupt. I recapture, same problem. I can see that the file has...'''
date = "2011-12-08T12:12:00Z"
lastmod = "2011-12-08T23:19:00Z"
weight = 7849
keywords = [ "encapsulation", "conversion" ]
aliases = [ "/questions/7849" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Null / Loopback Link encapsulation conversion](/questions/7849/null-loopback-link-encapsulation-conversion)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7849-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All...I'm stuck.</p><p>I'm on OSX 10.6 and I captured on the VPN tunnel interface (Juniper Network Connect jnc0). Wireshark is able to read the file just fine, but when I go to use "advanced" analysis system it tells me that the file is corrupt. I recapture, same problem. I can see that the file has an encapsulation of "Null / Loopback" so I use editcap to switch to ether - well, it's NOT ether and simply changing the encapsulation identifier isn't going to fix the problem. I'm looking at bittwist and NetDude in hopes of an answer, but I'm not seeing one.</p><p>So, is there a way to convert the link layer encapsulation from Null/Loopback to ether and have it work properly?</p></div><div id="question-tags" class="tags-container tags">encapsulation conversion</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '11, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-7849" class="comments-container"><span id="7853"></span><div id="comment-7853" class="comment"><div id="post-7853-score" class="comment-score"></div><div class="comment-text"><p>Are you able to post an example somewhere? Even a trace with few packets encoded with uuencode posted here will do :-)</p></div><div id="comment-7853-info" class="comment-info"><span class="comment-age">(08 Dec '11, 15:00)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-7849" class="comment-tools"></div><div class="clear"></div><div id="comment-7849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7863"></span>

<div id="answer-container-7863" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7863-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In theory, it's possibly to construct a "fake" Ethernet header, with fake source and destination addresses, for a LINKTYPE_NULL packet, at least as long as it's an IPv4 packet (fake Ethernet type 0x0800) or an IPv6 packet (fake Ethernet type 0x86dd), and most if not all packets captured with that link-layer header type will be IPv4 or IPv6 packets.</p><p>I don't know of any program that will do that, however. It might exist, but, if so, I've never seen it. Nothing in the Wireshark suite of programs will do it.</p><p>(It's also annoying that whoever wrote the "advanced" analysis system couldn't be bothered to support LINKTYPE_NULL, or even just to say "this is a valid pcap file, but I don't handle that link-layer type"; calling it "corrupt" just because the link-layer header type was LINKTYPE_NULL is completely bogus. What software is that?)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '11, 23:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7863" class="comments-container"><span id="7869"></span><div id="comment-7869" class="comment"><div id="post-7869-score" class="comment-score"></div><div class="comment-text"><p>It's OpNet ACE. I wasn't bright enough to think of forcing an etherII header and the ether-type of 0x0800 - I think bittwist can do that. Let me play with it. All of the packets I'm interested in are IPv4 - we're diagnosing a Microsoft Lync registration issue that only affects Mac users when working remotely.</p><p>SYN - I'll work on scrubbing a piece of the file and popping it up here.</p></div><div id="comment-7869-info" class="comment-info"><span class="comment-age">(09 Dec '11, 06:35)</span> GeonJay</div></div><span id="7871"></span><div id="comment-7871" class="comment"><div id="post-7871-score" class="comment-score"></div><div class="comment-text"><p>Ok. The Null/Loopback header length is 4bytes and EtherII is 14. The tool would have to completely remove/replace the layer 2 header. I'm thinking I could use editcap's chop from beginning feature to remove layer1/2 info then add new header info - but I'm in no way a coding genius and the tool would have to autosense packet types and lengths. Ugh :(</p></div><div id="comment-7871-info" class="comment-info"><span class="comment-age">(09 Dec '11, 07:12)</span> GeonJay</div></div><span id="7883"></span><div id="comment-7883" class="comment"><div id="post-7883-score" class="comment-score"></div><div class="comment-text"><p>You should file a complaint with OPNET that they should, ideally, support at least LINKTYPE_NULL and possibly some other link-layer header types (LINKTYPE_PPP, LINKTYPE_C_HDLC, LINKTYPE_IEEE802_11, and LINKTYPE_IEEE802_11_RADIO, for example) and, if they don't, they should at <em>least</em> give a better error than "the file is corrupt" for an unsupported link-layer header type.</p></div><div id="comment-7883-info" class="comment-info"><span class="comment-age">(09 Dec '11, 10:32)</span> Guy Harris ♦♦</div></div><span id="7884"></span><div id="comment-7884" class="comment"><div id="post-7884-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately, bittwiste won't do it; <a href="http://bittwist.sourceforge.net/doc/bittwiste.1.html">the bittwiste man page</a> says "Bittwiste is designed to work only with Ethernet frame".</p><p>A pcap-based program could read a packet, discard packets where the 4-byte header (in either byte order) is neither IPv4 (2) nor any of the IPv6 values (24, 28, 30), replace the 4-byte header with {00:00:00:00:00:00,00:00:00:00:00:00,0x0800} for a value of 2 and {...,0x86dd} for the other values, leave the payload alone, and write the packet out.</p></div><div id="comment-7884-info" class="comment-info"><span class="comment-age">(09 Dec '11, 10:43)</span> Guy Harris ♦♦</div></div><span id="7890"></span><div id="comment-7890" class="comment"><div id="post-7890-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help Guy!</p></div><div id="comment-7890-info" class="comment-info"><span class="comment-age">(09 Dec '11, 14:18)</span> GeonJay</div></div></div><div id="comment-tools-7863" class="comment-tools"></div><div class="clear"></div><div id="comment-7863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

