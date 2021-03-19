+++
type = "question"
title = "How to resolve addresses in Wireshark?"
description = '''I am trying to open a .cap file using Wireshark. I am facing problems with respect to the source and destination IP addresses. I obtained this .cap file by capturing network traffic using Microsoft Network Monitor. The .cap file when opened in Network Monitor displays the corresponding IP addresses....'''
date = "2011-04-04T10:41:00Z"
lastmod = "2011-04-05T14:06:00Z"
weight = 3326
keywords = [ "display-filter" ]
aliases = [ "/questions/3326" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to resolve addresses in Wireshark?](/questions/3326/how-to-resolve-addresses-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3326-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to open a .cap file using Wireshark. I am facing problems with respect to the source and destination IP addresses. I obtained this .cap file by capturing network traffic using Microsoft Network Monitor. The .cap file when opened in Network Monitor displays the corresponding IP addresses. How to I obtain the same in Wireshark?</p><p><img src="http://i.imgur.com/wLBuN.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '11, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/e26c7ebb23eae3f6b8a22c85915807f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bruce&#39;s gravatar image" /><p>Bruce<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bruce has no accepted answers">0%</span></p></img></div></div><div id="comments-container-3326" class="comments-container"></div><div id="comment-tools-3326" class="comment-tools"></div><div class="clear"></div><div id="comment-3326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3356"></span>

<div id="answer-container-3356" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3356-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>To see IP addresses, Wireshark has to see IP traffic. It's saying "IEEE 802.11", which means Wireshark is seeing the 802.11 headers, but it's not seeing anything past that, such as IP headers.</p><p>Is that traffic encrypted (WEP, WPA, WPA2)? If so, to see IP traffic, Wireshark needs to be able to decrypt the traffic, so you'd have to tell it the password for the network; see the <a href="http://wiki.wireshark.org/HowToDecrypt802.11">How To Decrypt 802.11</a> page in the Wireshark Wiki.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '11, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3356" class="comments-container"><span id="3397"></span><div id="comment-3397" class="comment"><div id="post-3397-score" class="comment-score"></div><div class="comment-text"><p>@Guy: Yes the traffic is encrypted. Also I should have mentioned this in the question but I connect to The Internet via a wireless AP.</p></div><div id="comment-3397-info" class="comment-info"><span class="comment-age">(07 Apr '11, 23:32)</span> Bruce</div></div></div><div id="comment-tools-3356" class="comment-tools"></div><div class="clear"></div><div id="comment-3356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3336"></span>

<div id="answer-container-3336" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3336-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That depends on name resolution settings, see <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChAdvNameResolutionSection.html#id557497">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '11, 22:32</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3336" class="comments-container"><span id="3341"></span><div id="comment-3341" class="comment"><div id="post-3341-score" class="comment-score"></div><div class="comment-text"><p>@Jaap: How do I enable ARP name resolution. I can't see it in preferences. Or did ARP name resolution fail in my case?</p></div><div id="comment-3341-info" class="comment-info"><span class="comment-age">(05 Apr '11, 05:56)</span> Bruce</div></div></div><div id="comment-tools-3336" class="comment-tools"></div><div class="clear"></div><div id="comment-3336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

