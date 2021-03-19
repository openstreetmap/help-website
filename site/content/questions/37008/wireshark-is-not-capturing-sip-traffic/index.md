+++
type = "question"
title = "Wireshark is not capturing SIP traffic"
description = '''Hi i am having an HP ProBook 4430s Laptop with Windows 7 &amp;amp; Realtek PCIe GBE Family Controller LAN Card, using Wireshark 1.12.1 with wincap 4.1.3 but not able to capture SIP traffic where as when i am connecting my colleagues laptop which is having windows XP its showing SIP traffic. What may be ...'''
date = "2014-10-13T04:55:00Z"
lastmod = "2014-10-16T05:25:00Z"
weight = 37008
keywords = [ "sip" ]
aliases = [ "/questions/37008" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark is not capturing SIP traffic](/questions/37008/wireshark-is-not-capturing-sip-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37008-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi i am having an HP ProBook 4430s Laptop with Windows 7 &amp; Realtek PCIe GBE Family Controller LAN Card, using Wireshark 1.12.1 with wincap 4.1.3 but not able to capture SIP traffic where as when i am connecting my colleagues laptop which is having windows XP its showing SIP traffic. What may be the issue. Is this something related with LAN card ?</p></div><div id="question-tags" class="tags-container tags">sip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '14, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/609d46ded6f592f78583c553c043fe58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gneeraj9&#39;s gravatar image" /><p>gneeraj9<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gneeraj9 has no accepted answers">0%</span></p></div></div><div id="comments-container-37008" class="comments-container"><span id="37104"></span><div id="comment-37104" class="comment"><div id="post-37104-score" class="comment-score"></div><div class="comment-text"><p>Pls support...any one having any idea about this issue ???</p></div><div id="comment-37104-info" class="comment-info"><span class="comment-age">(16 Oct '14, 05:14)</span> gneeraj9</div></div></div><div id="comment-tools-37008" class="comment-tools"></div><div class="clear"></div><div id="comment-37008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37106"></span>

<div id="answer-container-37106" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37106-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>So many possibilities: different interface, different network controller, different driver, different driver settings, different firewall, different OS, different capture settings, different wireshark settings, etc. Start from the ground up, get any packet in and go from there, mind that any difference might have an influence.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '14, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-37106" class="comments-container"><span id="37124"></span><div id="comment-37124" class="comment"><div id="post-37124-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thanks for response but that all i have tried to explore but could not find any issue...yeah definitely hardware is different with different drivers but what may be common setting for that if you know pls let me know.</p></div><div id="comment-37124-info" class="comment-info"><span class="comment-age">(17 Oct '14, 01:15)</span> gneeraj9</div></div><span id="37129"></span><div id="comment-37129" class="comment"><div id="post-37129-score" class="comment-score"></div><div class="comment-text"><p>Have you tried capturing without any capture or display filters just looking for packets of any kind from/to the involved IP addresses? Perhaps the packets are captured but not dissected as SIP?</p></div><div id="comment-37129-info" class="comment-info"><span class="comment-age">(17 Oct '14, 03:52)</span> Anders ♦</div></div></div><div id="comment-tools-37106" class="comment-tools"></div><div class="clear"></div><div id="comment-37106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

