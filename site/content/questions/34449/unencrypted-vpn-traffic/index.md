+++
type = "question"
title = "Unencrypted VPN traffic?"
description = '''I have a VPN (default Windows XP client-server setup) running, with Wireshark on both the client box and the actual VPN. However, on both instances of Wireshark all the traffic that I sniff shows up as either PPP Comp or GRE. I haven&#x27;t been able to find a solid answer anywhere, so since I have creds...'''
date = "2014-07-07T07:39:00Z"
lastmod = "2014-07-07T08:00:00Z"
weight = 34449
keywords = [ "vpn", "wireshark" ]
aliases = [ "/questions/34449" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unencrypted VPN traffic?](/questions/34449/unencrypted-vpn-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34449-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a VPN (default Windows XP client-server setup) running, with Wireshark on both the client box and the actual VPN. However, on both instances of Wireshark all the traffic that I sniff shows up as either PPP Comp or GRE. I haven't been able to find a solid answer anywhere, so since I have creds is there a way to sniff the actual unencrypted traffic?</p><p>Both of the boxes are VMs, if that makes a difference.</p></div><div id="question-tags" class="tags-container tags">vpn wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '14, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/f202cfb304d71b60a7d589ccf3913bb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fewmitz&#39;s gravatar image" /><p>Fewmitz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fewmitz has no accepted answers">0%</span></p></div></div><div id="comments-container-34449" class="comments-container"></div><div id="comment-tools-34449" class="comment-tools"></div><div class="clear"></div><div id="comment-34449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34450"></span>

<div id="answer-container-34450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34450-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Netmon (3.4) from MS can capture traffic in the GRE tunnel (using PPTP at least). Capture on the NDSIWANBH adaptor.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '14, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-34450" class="comments-container"><span id="34453"></span><div id="comment-34453" class="comment"><div id="post-34453-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response; I'll try that. Out of curiosity does that imply that Wireshark actually can't Sniff on VPN? I've seen a few possible solutions/workarounds but none of them fit what I'm seeing.</p></div><div id="comment-34453-info" class="comment-info"><span class="comment-age">(07 Jul '14, 12:02)</span> Fewmitz</div></div><span id="34454"></span><div id="comment-34454" class="comment"><div id="post-34454-score" class="comment-score"></div><div class="comment-text"><p>On Windows, <a href="http://www.winpcap.org/">WinPCap</a> (which is what Wireshark uses to capture) isn't able to capture on the pseudo-interfaces that VPN's create. Network Monitor uses a more modern filter driver so can capture on the VPN interfaces.</p></div><div id="comment-34454-info" class="comment-info"><span class="comment-age">(07 Jul '14, 13:42)</span> grahamb ♦</div></div></div><div id="comment-tools-34450" class="comment-tools"></div><div class="clear"></div><div id="comment-34450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

