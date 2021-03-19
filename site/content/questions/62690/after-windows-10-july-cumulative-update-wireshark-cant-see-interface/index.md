+++
type = "question"
title = "After Windows 10 july cumulative update , wireshark can&#x27;t see interface"
description = '''It was working before this update.  I&#x27;ve tried winpcap 4.1.3 and win10pcap to no avail.  At the moment, I&#x27;ve winpcap 4.1.3 installed on my system and verified that npf is running; but wireshark cant see the network interface, although it doesn&#x27;t throw any error or complain. Thanks in advance.'''
date = "2017-07-11T19:55:00Z"
lastmod = "2017-07-12T02:13:00Z"
weight = 62690
keywords = [ "wiresharkwindows10", "winpcap", "npf", "windows10", "update" ]
aliases = [ "/questions/62690" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [After Windows 10 july cumulative update , wireshark can't see interface](/questions/62690/after-windows-10-july-cumulative-update-wireshark-cant-see-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62690-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It was working before this update.</p><p>I've tried winpcap 4.1.3 and win10pcap to no avail.</p><p>At the moment, I've winpcap 4.1.3 installed on my system and verified that npf is running; but wireshark cant see the network interface, although it doesn't throw any error or complain.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">wiresharkwindows10 winpcap npf windows10 update</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '17, 19:55</strong></p><img src="https://secure.gravatar.com/avatar/772164a97adeb03ba348fde40b66c747?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="strategen&#39;s gravatar image" /><p>strategen<br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="strategen has no accepted answers">0%</span></p></div></div><div id="comments-container-62690" class="comments-container"><span id="62697"></span><div id="comment-62697" class="comment"><div id="post-62697-score" class="comment-score"></div><div class="comment-text"><p>Works for me after that update (WinPcap). What output do you get from the command line <code>path\to\dumpcap.exe -D</code>?</p></div><div id="comment-62697-info" class="comment-info"><span class="comment-age">(12 Jul '17, 03:34)</span> grahamb ♦</div></div></div><div id="comment-tools-62690" class="comment-tools"></div><div class="clear"></div><div id="comment-62690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62696"></span>

<div id="answer-container-62696" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62696-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried using <a href="https://nmap.org/npcap/">npcap</a> as a replacement for winpcap?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '17, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-62696" class="comments-container"><span id="62711"></span><div id="comment-62711" class="comment"><div id="post-62711-score" class="comment-score"></div><div class="comment-text"><p>Npcap solved the issue. Thanks for your suggestions.</p></div><div id="comment-62711-info" class="comment-info"><span class="comment-age">(12 Jul '17, 09:27)</span> strategen</div></div><span id="62721"></span><div id="comment-62721" class="comment"><div id="post-62721-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-62721-info" class="comment-info"><span class="comment-age">(12 Jul '17, 13:23)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-62696" class="comment-tools"></div><div class="clear"></div><div id="comment-62696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

