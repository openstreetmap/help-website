+++
type = "question"
title = "Wireshark 1.10.2 on Windows XP is not showing 802.11 control frames and management frame informations."
description = '''Hi, In the packet details i am not seeing any 802.11 related IEs and informations While capturing WLAN packets using the latest versions of Wireshark on Windows XP. But it is able to decode and display 802.11 IEs when we are opening a sniffer file which was captured using older development versions ...'''
date = "2013-10-23T05:40:00Z"
lastmod = "2013-10-23T18:45:00Z"
weight = 26320
keywords = [ "wireshar1.10.2" ]
aliases = [ "/questions/26320" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.10.2 on Windows XP is not showing 802.11 control frames and management frame informations.](/questions/26320/wireshark-1102-on-windows-xp-is-not-showing-80211-control-frames-and-management-frame-informations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26320-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>In the packet details i am not seeing any 802.11 related IEs and informations While capturing WLAN packets using the latest versions of Wireshark on Windows XP. But it is able to decode and display 802.11 IEs when we are opening a sniffer file which was captured using older development versions of Wireshark.</p><p>Anyone came across this kind of issue. Please let me know how i can rectify this issue. Any suggestions would be appreciated.</p><p>Pandiya</p></div><div id="question-tags" class="tags-container tags">wireshar1.10.2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '13, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/504920a82ad8dbe70ff07effa755efb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pandiya&#39;s gravatar image" /><p>Pandiya<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pandiya has no accepted answers">0%</span></p></div></div><div id="comments-container-26320" class="comments-container"></div><div id="comment-tools-26320" class="comment-tools"></div><div class="clear"></div><div id="comment-26320-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26345"></span>

<div id="answer-container-26345" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26345-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>In the packet details i am not seeing any 802.11 related IEs and informations While capturing WLAN packets using the latest versions of Wireshark on Windows XP.</p></blockquote><p>That's not supported on Wireshark on Windows except with an AirPcap card, as WinPcap (which is what Wireshark uses to capture traffic) doesn't support it. See <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">the CaptureSetup/WLAN in the Wireshark Wiki</a> for details on capturing full 802.11 traffic (rather than pretend-Ethernet data traffic).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '13, 18:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-26345" class="comments-container"></div><div id="comment-tools-26345" class="comment-tools"></div><div class="clear"></div><div id="comment-26345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

