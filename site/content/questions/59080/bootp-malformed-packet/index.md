+++
type = "question"
title = "BOOTP [Malformed Packet]"
description = '''Hello Guys I&#x27;m troubleshooting an issue where boop server responses are being dropped at some point in the topology In a capture taken from the interface where the bootp server is attached I see the below message: 428 Unknown BOOTP message type (0) [Malformed Packet] I&#x27;m guessing it means corruption...'''
date = "2017-01-26T08:30:00Z"
lastmod = "2017-01-26T20:46:00Z"
weight = 59080
keywords = [ "bootp" ]
aliases = [ "/questions/59080" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [BOOTP \[Malformed Packet\]](/questions/59080/bootp-malformed-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59080-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Guys</p><p>I'm troubleshooting an issue where boop server responses are being dropped at some point in the topology In a capture taken from the interface where the bootp server is attached I see the below message:</p><p>428 Unknown BOOTP message type (0) [Malformed Packet]</p><p>I'm guessing it means corruption but can any of you let me know what it means o where can I find more information about it.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">bootp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '17, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/9bdaed5d9e2e5230501055b67a48cc04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JuniperGuy&#39;s gravatar image" /><p>JuniperGuy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JuniperGuy has no accepted answers">0%</span></p></div></div><div id="comments-container-59080" class="comments-container"></div><div id="comment-tools-59080" class="comment-tools"></div><div class="clear"></div><div id="comment-59080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59092"></span>

<div id="answer-container-59092" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59092-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The BOOTP protocol, as described by <a href="https://tools.ietf.org/html/rfc951">RFC 951</a>, has an opcode field in it; the RFC specifies that it can either have the value 1 for a request and 2 for a reply. 0 is not a valid value for the opcode, so Wireshark reports the packet as having an unknown message type.</p><p><a href="https://tools.ietf.org/html/rfc2131">RFC 2131</a> describes DHCP; <a href="https://tools.ietf.org/html/rfc2131#section-3">section 3 "The Client-Server Protocol"</a> says</p><pre><code> DHCP uses the BOOTP message format defined in RFC 951 and given in
 table 1 and figure 1.  The &#39;op&#39; field of each DHCP message sent from
 a client to a server contains BOOTREQUEST. BOOTREPLY is used in the
&#39;op&#39; field of each DHCP message sent from a server to a client.</code></pre><p>so, again, the only valid opcode values are 1 and 2.</p><p>Either a client is sending out a BOOTP/DHCP message with an invalid opcode, and no server is sending a reply to that, or the server is sending out the message with the invalid opcode, and the client is ignoring it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '17, 20:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-59092" class="comments-container"></div><div id="comment-tools-59092" class="comment-tools"></div><div class="clear"></div><div id="comment-59092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59081"></span>

<div id="answer-container-59081" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59081-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>BOOTP is the Wireshark name for DHCP. Both protocols run on the same UDP ports (67 and 68). DHCP is based on the BOOTP frame format and added a few option.</p><p>A DHCP or BOOTP message starts with a fixed block of parameters and is followed by a series of options. Each option is a tuple of a numeric identifier, a length and a value field.</p><p>Virtually every DHCP message should have the option 53 present. This is the message type. The majority of DHCP frames have a types of Discover, Offer, Request or Acknowledge, but there are more.</p><p>The error message indicates that the dissector encountered the option number 0. As Wireshark does not know about this option number you get your error message.</p><p>Either the frame was corrupted during transmission or the sender (or DHCP relay agent) has a bug in it's DHCP implementation. A tracefile or at least screenshot would grately aid my curiosity.</p><p>Good hunting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '17, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jan '17, 20:35</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-59081" class="comments-container"><span id="59086"></span><div id="comment-59086" class="comment"><div id="post-59086-score" class="comment-score"></div><div class="comment-text"><p>Thank you packethunter</p><p>Unfortunately I can't provide the pcap but your answer definitively helps<br />
</p></div><div id="comment-59086-info" class="comment-info"><span class="comment-age">(26 Jan '17, 12:59)</span> JuniperGuy</div></div><span id="59091"></span><div id="comment-59091" class="comment"><div id="post-59091-score" class="comment-score"></div><div class="comment-text"><p>Presumably when you said "TFTP" you meant "DHCP". I'll fix the answer.</p></div><div id="comment-59091-info" class="comment-info"><span class="comment-age">(26 Jan '17, 20:35)</span> Guy Harris ♦♦</div></div><span id="59110"></span><div id="comment-59110" class="comment"><div id="post-59110-score" class="comment-score"></div><div class="comment-text"><p>How embarrasing.</p><p>Please excuse me while I go and hide behind my network cabinet for the rest of the day. And thank you for fixing the answer.</p></div><div id="comment-59110-info" class="comment-info"><span class="comment-age">(27 Jan '17, 09:04)</span> packethunter</div></div></div><div id="comment-tools-59081" class="comment-tools"></div><div class="clear"></div><div id="comment-59081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

