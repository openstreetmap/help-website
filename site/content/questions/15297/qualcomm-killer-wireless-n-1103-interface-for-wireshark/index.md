+++
type = "question"
title = "Qualcomm Killer Wireless N 1103 interface for wireshark"
description = '''Hey, do you have a &quot;How to&quot; to code an interface for a network card. Qualcomm Killer Wireless N 1103 isn&#x27;t supported and i want to get it work. Thx Mojita'''
date = "2012-10-26T10:51:00Z"
lastmod = "2012-10-26T16:35:00Z"
weight = 15297
keywords = [ "networkinterfaces" ]
aliases = [ "/questions/15297" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Qualcomm Killer Wireless N 1103 interface for wireshark](/questions/15297/qualcomm-killer-wireless-n-1103-interface-for-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15297-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, do you have a "How to" to code an interface for a network card.</p><p>Qualcomm Killer Wireless N 1103 isn't supported and i want to get it work.</p><p>Thx Mojita</p></div><div id="question-tags" class="tags-container tags">networkinterfaces</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '12, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/a3954cbca7d185957735227e1c651629?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mojita&#39;s gravatar image" /><p>mojita<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mojita has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Oct '12, 13:40</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-15297" class="comments-container"></div><div id="comment-tools-15297" class="comment-tools"></div><div class="clear"></div><div id="comment-15297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15298"></span>

<div id="answer-container-15298" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15298-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're using Windows, see <a href="http://msdn.microsoft.com/en-us/library/windows/hardware/ff557563(v=vs.85).aspx">the Network Devices page on MSDN</a>, and the pages below it. Note that this could be a problem with the driver for the adapter, but it's probably a problem with WinPcap, and to fix that you'd have to modify WinPcap to support NDIS 6 and the "native Wi-Fi" mechanism.</p><p>If you're using Linux, see <a href="http://linuxwireless.org/en/developers">the Linux Wireless Web site</a>.</p><p>For various flavors of BSD, check out the documentation for it.</p><p>I.e., the software in question is at least two layers below any of the Wireshark code, so there's no Wireshark how-to guide for developing it, and, if it's an issue with the driver, will involve writing kernel-mode code for whatever operating system you're using, which is not going to be easy if you're not already familiar with writing kernel-mode code for the operating system in question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '12, 16:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Oct '12, 13:40</p></div></div><div id="comments-container-15298" class="comments-container"><span id="15334"></span><div id="comment-15334" class="comment"><div id="post-15334-score" class="comment-score"></div><div class="comment-text"><p>Thank you! I will check your links. No, I've never done this before but maybe i can learn it. Of course I will try Linux then. Have a nice day!</p><p>(Converted to a comment per the format of <a href="http://ask.wireshark.org">ask.wireshark.org</a>. Please see the FAQ).</p></div><div id="comment-15334-info" class="comment-info"><span class="comment-age">(29 Oct '12, 05:05)</span> mojita</div></div></div><div id="comment-tools-15298" class="comment-tools"></div><div class="clear"></div><div id="comment-15298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

