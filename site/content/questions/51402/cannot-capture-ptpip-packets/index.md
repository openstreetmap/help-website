+++
type = "question"
title = "cannot capture PTP/IP packets"
description = '''I&#x27;m using wireshark with AitPcapNX. I see packet captured but cannot find any PTP/IP packet. Most of captured packets&#x27; protocol are 802.11. Is there any setting to capture PTP/IP packets? I&#x27;d appreciate it if I&#x27;d get some advices because I really need PTP/IP packets to analyze my issue, thank you.'''
date = "2016-04-04T19:40:00Z"
lastmod = "2016-04-05T01:59:00Z"
weight = 51402
keywords = [ "ptpip", "airpcap" ]
aliases = [ "/questions/51402" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [cannot capture PTP/IP packets](/questions/51402/cannot-capture-ptpip-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51402-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using wireshark with AitPcapNX. I see packet captured but cannot find any PTP/IP packet. Most of captured packets' protocol are 802.11. Is there any setting to capture PTP/IP packets? I'd appreciate it if I'd get some advices because I really need PTP/IP packets to analyze my issue, thank you.</p></div><div id="question-tags" class="tags-container tags">ptpip airpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '16, 19:40</strong></p><img src="https://secure.gravatar.com/avatar/0506beae865889d503d6f6b5d41a43e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mokeke&#39;s gravatar image" /><p>mokeke<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mokeke has no accepted answers">0%</span></p></div></div><div id="comments-container-51402" class="comments-container"></div><div id="comment-tools-51402" class="comment-tools"></div><div class="clear"></div><div id="comment-51402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51410"></span>

<div id="answer-container-51410" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51410-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Most of captured packets' protocol are 802.11.</p></blockquote><p>That probably means that you're capturing on a "protected" network, i.e. one using WEP or WPA/WPA2 to encrypt packets, and haven't set Wireshark up to decrypt the packets. See the <a href="https://wiki.wireshark.org/HowToDecrypt802.11">how to decrypt 802.11</a> page of the Wireshark Wiki for information on what needs to be done to decrypt the packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '16, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-51410" class="comments-container"><span id="51429"></span><div id="comment-51429" class="comment"><div id="post-51429-score" class="comment-score"></div><div class="comment-text"><p>Thank you for yor reply, Guy Harris. I already tried decrypting packets with password&amp;SSID but it didn't work well; Packets still show protocol "802.11." I'm very confused now.</p></div><div id="comment-51429-info" class="comment-info"><span class="comment-age">(05 Apr '16, 18:33)</span> mokeke</div></div><span id="51430"></span><div id="comment-51430" class="comment"><div id="post-51430-score" class="comment-score"></div><div class="comment-text"><p>Read the "how to decrypt 802.11" page, paying attention to, for example, the discussion of the "EAPOL handshake" in the "Gotchas" section (in order to decrypt traffic that's not sent to or from your machine, you may need to force one of the other machines to disconnect from the network and reconnect to the network <em>while you're capturing its traffic</em>, for example by putting the machine to sleep and waking it up).</p><p>Remember, the <em>whole point of WEP and WPA/WPA2 was to make it hard to do exactly what you're trying to do!</em> The encryption is done to make it <em>hard</em> to sniff Wireless networks.</p><p>Note also that, for an AirPcap card, the decryption could be done by the card, so the way you specify the keys could be different; look for "AirPcap" on that page.</p></div><div id="comment-51430-info" class="comment-info"><span class="comment-age">(05 Apr '16, 19:15)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-51410" class="comment-tools"></div><div class="clear"></div><div id="comment-51410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

