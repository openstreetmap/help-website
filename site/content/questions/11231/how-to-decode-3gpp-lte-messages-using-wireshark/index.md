+++
type = "question"
title = "How to decode 3GPP LTE messages using Wireshark"
description = '''Hi all, I am trying to capture the MAC, RLC, PDCP and RRC messages from a LTE usb dongle.  I&#x27;m new to wireshark but have been reading about the dissectors but I find it a bit confusing.  Could someone explain to me how to go about seeing the LTE messages using wireshark?  Regards, J'''
date = "2012-05-22T20:41:00Z"
lastmod = "2012-05-22T21:09:00Z"
weight = 11231
keywords = [ "pdcp-lte", "rrc", "rlc", "lte", "wireshark" ]
aliases = [ "/questions/11231" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode 3GPP LTE messages using Wireshark](/questions/11231/how-to-decode-3gpp-lte-messages-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11231-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am trying to capture the MAC, RLC, PDCP and RRC messages from a LTE usb dongle.</p><p>I'm new to wireshark but have been reading about the dissectors but I find it a bit confusing.</p><p>Could someone explain to me how to go about seeing the LTE messages using wireshark?</p><p>Regards,</p><p>J</p></div><div id="question-tags" class="tags-container tags">pdcp-lte rrc rlc lte wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '12, 20:41</strong></p><img src="https://secure.gravatar.com/avatar/9bf45b3be4b2ce8bb5c28d1b18563c8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pedropumpalot&#39;s gravatar image" /><p>pedropumpalot<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pedropumpalot has no accepted answers">0%</span></p></div></div><div id="comments-container-11231" class="comments-container"></div><div id="comment-tools-11231" class="comment-tools"></div><div class="clear"></div><div id="comment-11231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11234"></span>

<div id="answer-container-11234" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11234-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming your USB dongle is a "normal" USB dongle used to connect your PC to an ISP over LTE - you can't - the comunication between the dongle and the LTE network is not passed to your PC.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '12, 21:09</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-11234" class="comments-container"><span id="11243"></span><div id="comment-11243" class="comment"><div id="post-11243-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders,</p><p>I have used Tems and can decode the messages from the Sierra Wireless USB dongle.</p><p>Can you explain further why Wireshark isn't capable of decoding these messages?</p><p>What is the point of wireshark if it can't decode the messages from the device? How else would you get LTE messages onto your PC/laptop without using a wireless device?</p></div><div id="comment-11243-info" class="comment-info"><span class="comment-age">(22 May '12, 23:17)</span> pedropumpalot</div></div><span id="11254"></span><div id="comment-11254" class="comment"><div id="post-11254-score" class="comment-score"></div><div class="comment-text"><p>I think Anders point is that such a device (probably) terminates the LTE connection and then provides something that probably looks like an Ethernet connection to the host (PC/laptop). Your PC/laptop doesn't understand LTE, it understands Ethernet, so that's what it is given.</p><p>I would guess that to capture the LTE you'd need a dedicated capture device.</p><p>Simple test would be to try it out and see what you get; I'd guess the captured frames will look like, for example, TCP over IP over Ethernet.</p></div><div id="comment-11254-info" class="comment-info"><span class="comment-age">(23 May '12, 06:28)</span> JeffMorriss ♦</div></div><span id="11296"></span><div id="comment-11296" class="comment"><div id="post-11296-score" class="comment-score"></div><div class="comment-text"><blockquote><p>How else would you get LTE messages onto your PC/laptop without using a wireless device?</p></blockquote><p>By capturing them inside the LTE network or having the LTE nodes write pcap files containing different interface signals or using dedicated HW to catch the signals off the air or encapsulating LTE interface signals in UDP packets and sens them to a trace node and capture that traffic(inside the network) or...</p></div><div id="comment-11296-info" class="comment-info"><span class="comment-age">(23 May '12, 14:36)</span> Anders ♦</div></div><span id="11297"></span><div id="comment-11297" class="comment"><div id="post-11297-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I have used Tems and can decode the messages from the Sierra Wireless USB dongle.</p></blockquote><p>What sort of messages are those? And what software reads those messages?</p><blockquote><p>Can you explain further why Wireshark isn't capable of decoding these messages?</p></blockquote><p>We don't know whether Wireshark can decode them. We <em>do</em> know that Wireshark can't read them from the device, as libpcap/WinPcap and the OS mechanisms they use don't support that.</p><blockquote><p>What is the point of wireshark if it can't decode the messages from the device?</p></blockquote><p>The point is to decode those messages that it <em>can</em> read, e.g. Ethernet.</p></div><div id="comment-11297-info" class="comment-info"><span class="comment-age">(23 May '12, 17:35)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-11234" class="comment-tools"></div><div class="clear"></div><div id="comment-11234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

