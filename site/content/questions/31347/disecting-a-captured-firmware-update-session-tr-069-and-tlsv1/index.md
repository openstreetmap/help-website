+++
type = "question"
title = "Disecting a captured firmware update session - TR-069 and TLSv1"
description = '''My locked, ISP branded modem/router runs a TR-069 daemon that periodically checks for firmware updates. I used a man-in-the-middle OpenWRT box, running tcpdump, to capture an entire TR-069 session in which a firmware update was sent from my ISP to the modem/router and installed. As I understand it, ...'''
date = "2014-04-01T07:04:00Z"
lastmod = "2014-04-02T13:48:00Z"
weight = 31347
keywords = [ "tlsv1", "tr-069" ]
aliases = [ "/questions/31347" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Disecting a captured firmware update session - TR-069 and TLSv1](/questions/31347/disecting-a-captured-firmware-update-session-tr-069-and-tlsv1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31347-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My locked, ISP branded modem/router runs a TR-069 daemon that periodically checks for firmware updates. I used a man-in-the-middle OpenWRT box, running tcpdump, to capture an entire TR-069 session in which a firmware update was sent from my ISP to the modem/router and installed.</p><p>As I understand it, TR-069 uses TLSv1 to encrypt the firmware file during transmission but I have an unencrypted copy of the same firmware, the plaintext.</p><p>How can I extract the encrypted firmware file? What other useful information can be extracted from the captured session? I have wireshark 1.11.3.</p><p>TIA!</p></div><div id="question-tags" class="tags-container tags">tlsv1 tr-069</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '14, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/c43f6ab4d44cb7f5045c0bb1c3e482ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmcdonnell&#39;s gravatar image" /><p>dmcdonnell<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmcdonnell has no accepted answers">0%</span></p></div></div><div id="comments-container-31347" class="comments-container"></div><div id="comment-tools-31347" class="comment-tools"></div><div class="clear"></div><div id="comment-31347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31435"></span>

<div id="answer-container-31435" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31435-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>As I understand it, TR-069 uses TLSv1 to encrypt the firmware file during transmission</p></blockquote><p>did you check that in the capture file? You should see SSL/TLS traffic in that case.</p><blockquote><p>but I have an unencrypted copy of the same firmware, the plaintext.</p></blockquote><p>from the capture file? If so, your whole question would be kind of pointless, so I guess you got the firmware from another source.</p><blockquote><p>How can I extract the encrypted firmware file?</p></blockquote><p>You can't if the session is encrypted with TLSv1, unless you have either access to the <strong>locked</strong> router or the update servers of the ISP to (somehow) get hold of the crypto keys. I guess neither is the case, so: Sorry, bad luck! That's what TLS was made for.</p><blockquote><p>What other useful information can be extracted from the captured session?</p></blockquote><p>that depends on the update process of your ISP. Maybe they push a new config for the router and/or the latest NSA backdoors over the encrypted TLS channel to your box. You will never know.</p><p>The only thing you could do is to use a SSL Man in the middle attack (please google that, as it's way beyond the scope of this site). But I bet, that TR-069 has some security measures in place to prevent that. So again: Sorry, no luck.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Apr '14, 13:49</p></div></div><div id="comments-container-31435" class="comments-container"><span id="31470"></span><div id="comment-31470" class="comment"><div id="post-31470-score" class="comment-score"></div><div class="comment-text"><p>@Kurt</p><p>Thank you very much for your comprehensive reply.</p><p>I thought if might be useful for researchers to have access to the pcap capture of the CWMP (TLSv1.2) firmware update session and the plaintext firmware file delivered in the session(obtained elsewhere).</p><p>pcap: <a href="https://drive.google.com/file/d/0B8w9evGfsK03Qi15Z0x4TkY1ZDQ/edit?usp=sharing">https://drive.google.com/file/d/0B8w9evGfsK03Qi15Z0x4TkY1ZDQ/edit?usp=sharing</a> firmware: <a href="https://drive.google.com/file/d/0B8w9evGfsK03MVpMTlVBTDY3WlE/edit?usp=sharing">https://drive.google.com/file/d/0B8w9evGfsK03MVpMTlVBTDY3WlE/edit?usp=sharing</a></p><p>Regards,</p><p>Dermot.</p></div><div id="comment-31470-info" class="comment-info"><span class="comment-age">(03 Apr '14, 03:41)</span> dmcdonnell</div></div></div><div id="comment-tools-31435" class="comment-tools"></div><div class="clear"></div><div id="comment-31435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

