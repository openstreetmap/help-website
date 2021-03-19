+++
type = "question"
title = "Suspected trojan with access to clipboard."
description = '''Hi there, I suspect I have a trojan on my W7Ux64 system that has access to my clipboard. I have a few PCAPNG files that I made with Wireshark that might show said clipboard upload activity. I am quite new to Wireshark and am not sure what to look for. Can anyone point me in the right direction to wh...'''
date = "2016-08-14T06:40:00Z"
lastmod = "2016-08-14T06:40:00Z"
weight = 54796
keywords = [ "trojan", "clipboard", "noob" ]
aliases = [ "/questions/54796" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Suspected trojan with access to clipboard.](/questions/54796/suspected-trojan-with-access-to-clipboard)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54796-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I suspect I have a trojan on my W7Ux64 system that has access to my clipboard. I have a few PCAPNG files that I made with Wireshark that might show said clipboard upload activity. I am quite new to Wireshark and am not sure what to look for. Can anyone point me in the right direction to what to look for in Wireshark?</p><p>Should I only look at HTTP packets?</p><p>Also bonus question: Is there anything in Windows Event Viewer that would tell me anything about clipboard activity?</p></div><div id="question-tags" class="tags-container tags">trojan clipboard noob</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '16, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/c5bfef8f8f5c73d1fd67d691f658ffff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Datura007&#39;s gravatar image" /><p>Datura007<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Datura007 has no accepted answers">0%</span></p></div></div><div id="comments-container-54796" class="comments-container"><span id="54798"></span><div id="comment-54798" class="comment"><div id="post-54798-score" class="comment-score"></div><div class="comment-text"><p>If it is a Trojan, you should be watching all ports as there is no telling which port(s) it might use, so don't limit search to just HTTP packets.</p><p>As for what to look for in WireShark, Trojans usually connect to somewhere on the internet to pass information collected from your PC. That said, look for any sessions from your PC to a Global IP address.</p><p>To reduce the number of Global IP addresses to check, stop all other programs that normally access the internet to limit the number of Global IP's you'll have to look through.</p><p>Find each IP you're going to and check it against a RBL (Real-time Black List) as well as perform reverse DNS lookups to see what your PC is talking to. Some will be kosher, others will be either unknown or flagged as malacious.</p><p>As for Windows Events... Hmmmm... I hardly doubt it, but PerfMon should be able to monitor when the Clipboard service is activated.</p><p>FWIW</p></div><div id="comment-54798-info" class="comment-info"><span class="comment-age">(14 Aug '16, 06:50)</span> wbenton</div></div></div><div id="comment-tools-54796" class="comment-tools"></div><div class="clear"></div><div id="comment-54796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

