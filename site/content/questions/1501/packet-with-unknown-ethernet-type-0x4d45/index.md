+++
type = "question"
title = "Packet with unknown Ethernet type 0x4d45"
description = '''Hey, I did a capture of a piece of software on my laptop loading firmware to a device. The packets look like this in list view: 687 53.047211 Dell_cb:f1:96 MegaSyst_01:b5:cf 0x4d45 Ethernet II The source (Dell..) is my laptop and the dest (Mega...) is the device. The protocol is showing up as 0x4d45...'''
date = "2010-12-28T10:41:00Z"
lastmod = "2011-01-01T18:59:00Z"
weight = 1501
keywords = [ "unknown", "type", "packet" ]
aliases = [ "/questions/1501" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packet with unknown Ethernet type 0x4d45](/questions/1501/packet-with-unknown-ethernet-type-0x4d45)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1501-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>I did a capture of a piece of software on my laptop loading firmware to a device. The packets look like this in list view:</p><p>687 53.047211 Dell_cb:f1:96 MegaSyst_01:b5:cf 0x4d45 Ethernet II</p><p>The source (Dell..) is my laptop and the dest (Mega...) is the device. The protocol is showing up as 0x4d45 (Unknown) and the type is showing up as Ethernet II.</p><p>I spoke to a friend who said that sometimes their gear shows up incorrectly in Wireshark as well.</p><p>So, my question(s) are:</p><ol><li>How can I confirm what the packet protocol and type should be? The mfr of the device is of no help on this.</li><li>Can I convert these to a known type (once I find out what the type should be) through Wireshark and if so, how?</li></ol><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">unknown type packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Dec '10, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/a4c5824428073b35c66dc9eaa2e679c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emana&#39;s gravatar image" /><p>emana<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emana has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jan '11, 13:13</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-1501" class="comments-container"><span id="1502"></span><div id="comment-1502" class="comment"><div id="post-1502-score" class="comment-score"></div><div class="comment-text"><p>If the ethertype is 0x4d45, it is what it is. Are you trying to prove that it should not be this ethertype? Or do you just want to change it, temporarily, so you can treat it as IP?</p></div><div id="comment-1502-info" class="comment-info"><span class="comment-age">(28 Dec '10, 18:34)</span> hansangb</div></div><span id="1503"></span><div id="comment-1503" class="comment"><div id="post-1503-score" class="comment-score"></div><div class="comment-text"><p>I want to confirm somehow that this is correctly reporting by Wireshark and then figure out how a file is being sent from a piece of software using this protocol. I have to write something in VB to send the same file using the same method used by the packet trace...</p></div><div id="comment-1503-info" class="comment-info"><span class="comment-age">(28 Dec '10, 19:12)</span> emana</div></div><span id="1504"></span><div id="comment-1504" class="comment"><div id="post-1504-score" class="comment-score"></div><div class="comment-text"><p>I got the mfr of the product telling me it should be port 80 TCP...it would appear that Wireshark is somehow misrepresenting the packets...any idea how to correct?</p></div><div id="comment-1504-info" class="comment-info"><span class="comment-age">(28 Dec '10, 21:07)</span> emana</div></div><span id="1505"></span><div id="comment-1505" class="comment"><div id="post-1505-score" class="comment-score"></div><div class="comment-text"><p>We would like to see such eth file on bugs.wireshark.org. Could be a file format reading issue.</p></div><div id="comment-1505-info" class="comment-info"><span class="comment-age">(28 Dec '10, 23:44)</span> Jaap ♦</div></div><span id="1513"></span><div id="comment-1513" class="comment"><div id="post-1513-score" class="comment-score"></div><div class="comment-text"><p>Emana, remember that Ethertype has nothing to do with whether port 80 is being used or not. Obviously, if TCP/IP is being used, ethertyp of 0800 (for IPv4) is what it should be set to. You can use bittwiste to change the ethertype, so you may want to give that a shot. If everything shows up correctly after you modify the ethertype to 0800, then it might be a bug (wireshark or the device).</p></div><div id="comment-1513-info" class="comment-info"><span class="comment-age">(29 Dec '10, 08:47)</span> hansangb</div></div><span id="1550"></span><div id="comment-1550" class="comment not_top_scorer"><div id="post-1550-score" class="comment-score"></div><div class="comment-text"><p>Are you able to share a bit more of the file? One (or a few) packets with all bytes?</p><p>You could do this by posting the output of "tshark -r &lt;file&gt; -c 5 -x".</p></div><div id="comment-1550-info" class="comment-info"><span class="comment-age">(31 Dec '10, 01:32)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-1501" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-1501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1582"></span>

<div id="answer-container-1582" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1582-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the traffic is really carried as TCP port 80 , but using 0x4d45 instead 0x0800 for ethertype on IP then it sounds like an attempt at security by obscurity. But the vendor should have told you that!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '11, 18:59</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1582" class="comments-container"></div><div id="comment-tools-1582" class="comment-tools"></div><div class="clear"></div><div id="comment-1582-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

