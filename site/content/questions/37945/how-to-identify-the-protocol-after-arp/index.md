+++
type = "question"
title = "How to identify the protocol after ARP"
description = '''I&#x27;ve a pcap file with several ARP packets. If there is a protocol after ARP, how can wireshark identify it? If it is an IP packet, I can see the next protocol in the protocol field. But ARP does not have this field.'''
date = "2014-11-18T04:53:00Z"
lastmod = "2014-11-18T05:00:00Z"
weight = 37945
keywords = [ "arp", "ip" ]
aliases = [ "/questions/37945" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to identify the protocol after ARP](/questions/37945/how-to-identify-the-protocol-after-arp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37945-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I've a pcap file with several ARP packets. If there is a protocol after ARP, how can wireshark identify it?</p><p>If it is an IP packet, I can see the next protocol in the protocol field. But ARP does not have this field.</p></div><div id="question-tags" class="tags-container tags">arp ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '14, 04:53</strong></p><img src="https://secure.gravatar.com/avatar/05b012c8242a790bf2d6885eb0420756?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Struci&#39;s gravatar image" /><p>Struci<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Struci has no accepted answers">0%</span></p></div></div><div id="comments-container-37945" class="comments-container"></div><div id="comment-tools-37945" class="comment-tools"></div><div class="clear"></div><div id="comment-37945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37946"></span>

<div id="answer-container-37946" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37946-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Arp is a standalone protocol, it's not a transport layer for other protocols. See <a href="https://tools.ietf.org/html/std37">Internet Standard 37</a> and the Wikipedia <a href="http://en.wikipedia.org/wiki/Address_Resolution_Protocol">page</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '14, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37946" class="comments-container"><span id="37947"></span><div id="comment-37947" class="comment"><div id="post-37947-score" class="comment-score"></div><div class="comment-text"><p>Thanks grahamb. And you can identify ARP by the type field of ethernet, right?. And how can you identify an protocol after ARP? Or how can I know how many padding bytes there are after the ARP protocol?</p></div><div id="comment-37947-info" class="comment-info"><span class="comment-age">(18 Nov '14, 05:46)</span> Struci</div></div><span id="37948"></span><div id="comment-37948" class="comment"><div id="post-37948-score" class="comment-score"></div><div class="comment-text"><p>The padding issue is more difficult. Wireshark has a display filter field eth.padding that contains the padding bytes, but nothing I know of to actually say the length of that padding.</p><p>You seem to be implying that you have Ethernet frames contain ARP traffic followed by something else. If so can you post an example capture illustrating this somewhere,. e.g. <a href="http://cloudshark.org">CloudShark</a>, Dropbox, Google Drive, and post the link back by editing your question?</p></div><div id="comment-37948-info" class="comment-info"><span class="comment-age">(18 Nov '14, 06:11)</span> grahamb ♦</div></div><span id="37981"></span><div id="comment-37981" class="comment"><div id="post-37981-score" class="comment-score"></div><div class="comment-text"><blockquote><p>And you can identify ARP by the type field of ethernet, right?</p></blockquote><p>RIght.</p><blockquote><p>And how can you identify an protocol after ARP?</p></blockquote><p>As Graham said, there <em>isn't</em> a protocol after ARP within a given Ethernet frame - there's the Ethernet header, there's the ARP packet, there's the padding, and that's it. The same applies for other link-layer protocols such as 802.11, except that the other protocols don't have a minimum frame length, so there's no padding.</p><blockquote><p>Or how can I know how many padding bytes there are after the ARP protocol?</p></blockquote><p>Yes, the only stuff after ARP would, on Ethernet, be padding. You find out how many padding bytes there are by:</p><ul><li>finding out how big the entire Ethernet packet is;</li><li>subtracting 14 from that value for the Ethernet header (and, <em>if</em> the packet you have includes the FCS, subtract another 4 bytes for the FCS);</li><li>parsing the ARP packet to figure out how big it is (add the size of the fixed-length portion of the ARP packet to the lengths of the addresses in the packet);</li><li>subtracting the size of the ARP packet from the result of the previous subtraction.</li></ul></div><div id="comment-37981-info" class="comment-info"><span class="comment-age">(19 Nov '14, 15:52)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-37946" class="comment-tools"></div><div class="clear"></div><div id="comment-37946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

