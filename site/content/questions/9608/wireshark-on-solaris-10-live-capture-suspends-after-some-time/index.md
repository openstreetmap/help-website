+++
type = "question"
title = "Wireshark on Solaris 10 live capture suspends after some time"
description = '''I&#x27;m finding that when running a live capture on my rge0 interface, after some time (eg 30 minutes) the display of new packets stops updating. The UI does not hang, I can interact with it and select packets etc. It&#x27;s just that no new packets are displayed and the total packet capture count remains fi...'''
date = "2012-03-17T19:34:00Z"
lastmod = "2012-03-22T12:48:00Z"
weight = 9608
keywords = [ "livecapturetcp", "solaris", "wireshark" ]
aliases = [ "/questions/9608" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark on Solaris 10 live capture suspends after some time](/questions/9608/wireshark-on-solaris-10-live-capture-suspends-after-some-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9608-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm finding that when running a live capture on my rge0 interface, after some time (eg 30 minutes) the display of new packets stops updating. The UI does not hang, I can interact with it and select packets etc. It's just that no new packets are displayed and the total packet capture count remains fixed.</p><p>On each live capture session, this behavior occurs at different times &amp; total packet counts.</p><p>I am aware of the "out of memory" issue with Wireshark but don't think this is it. Wireshark is not terminating. I've also trussed the wireshark process and the child dumpcap process and both are showing activity. I have checked I have tons of free disk space and virtual memory.</p><p>Any ideas?</p><p>Wireshark version: 1.6.4; OS: Oracle Solaris 10 [8/11 s10x_u10wos_17b X86] edition; NIC: Realtek RTL8111 Integrated Gigabit Ethernet Controller; Driver: Bundled Solaris rge(7D) driver</p></div><div id="question-tags" class="tags-container tags">livecapturetcp solaris wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '12, 19:34</strong></p><img src="https://secure.gravatar.com/avatar/c078cac56545607439662e9115340b1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SiliconLunch&#39;s gravatar image" /><p>SiliconLunch<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SiliconLunch has no accepted answers">0%</span></p></div></div><div id="comments-container-9608" class="comments-container"></div><div id="comment-tools-9608" class="comment-tools"></div><div class="clear"></div><div id="comment-9608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9705"></span>

<div id="answer-container-9705" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9705-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is it possible that even though you have tons of disk space the capture file has reached the maximum allowed size for that file system? Can you do any capture filtering to reduce the volume of data collected to see whether that has any effect on when it stops?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '12, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span></p></div></div><div id="comments-container-9705" class="comments-container"></div><div id="comment-tools-9705" class="comment-tools"></div><div class="clear"></div><div id="comment-9705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

