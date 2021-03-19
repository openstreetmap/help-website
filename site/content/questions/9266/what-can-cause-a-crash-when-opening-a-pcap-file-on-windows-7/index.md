+++
type = "question"
title = "What can cause a crash when opening a pcap file on Windows 7?"
description = '''I run Wireshark on Windows 7 and try to open a pcap file (captured on Windows XP), but Wireshark crashes when I try to open the file. What could be the problem?'''
date = "2012-02-28T01:26:00Z"
lastmod = "2012-02-28T09:03:00Z"
weight = 9266
keywords = [ "crash", "windows7", "pcap" ]
aliases = [ "/questions/9266" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What can cause a crash when opening a pcap file on Windows 7?](/questions/9266/what-can-cause-a-crash-when-opening-a-pcap-file-on-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9266-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I run Wireshark on Windows 7 and try to open a pcap file (captured on Windows XP), but Wireshark crashes when I try to open the file. What could be the problem?</p></div><div id="question-tags" class="tags-container tags">crash windows7 pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '12, 01:26</strong></p><img src="https://secure.gravatar.com/avatar/ce79034142dc613a1a30949664b84723?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic&#39;s gravatar image" /><p>Nic<br />
<span class="score" title="14 reputation points">14</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Feb '12, 09:09</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9266" class="comments-container"></div><div id="comment-tools-9266" class="comment-tools"></div><div class="clear"></div><div id="comment-9266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9270"></span>

<div id="answer-container-9270" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9270-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Lot's of possibilies; It's difficult to know which without being able to do a test with the capture file.</p><p>What error message do you get when Wireshark crashes ?</p><p>Please open a bug at bugs.wireshark,.org and attach the file to the bug. If necessary, you can mark the attachment private so that only Wireshark core developers will have access.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '12, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Feb '12, 09:05</p></div></div><div id="comments-container-9270" class="comments-container"><span id="9271"></span><div id="comment-9271" class="comment"><div id="post-9271-score" class="comment-score"></div><div class="comment-text"><p>If I don't include my own plugin I can open the file. What could be different between the build of the plugin on Windows XP to Windows7?</p><p>(Converted to a comment in keeping with the way <a href="http://ask.wireshrk.org">ask.wireshrk.org</a> works; Please see the FAQ).</p></div><div id="comment-9271-info" class="comment-info"><span class="comment-age">(28 Feb '12, 10:18)</span> Nic</div></div><span id="9283"></span><div id="comment-9283" class="comment"><div id="post-9283-score" class="comment-score"></div><div class="comment-text"><p>Aha ....</p><p>Are you using the same version of Wireshark on both systems ?</p><p>If not, have you recompiled the plugin for the version of Wireshark you are using on Windows 7 ?</p><p>There's no promise that a plugin compiled for one version of Wireshark will work with another version. That is, the plugin needs to be re-compiled from source for each major version of Wireshark.</p><p>If you are using the same version of Wireshark on both systems (or you've recompiled the plugin to match the Wireshark version), then you'll probably need to use a debugger to see why your plugin is failing.</p></div><div id="comment-9283-info" class="comment-info"><span class="comment-age">(29 Feb '12, 17:17)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-9270" class="comment-tools"></div><div class="clear"></div><div id="comment-9270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

