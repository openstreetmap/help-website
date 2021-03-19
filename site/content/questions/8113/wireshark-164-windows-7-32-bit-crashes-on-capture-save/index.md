+++
type = "question"
title = "Wireshark 1.6.4 Windows 7 32-bit Crashes on Capture Save"
description = '''Am running 1.6.4 under 32-bit Windows and doing wireless captures using AirPcap cards across 1,6,11. Am using the aggregator virtual adapter that combines these. System captures properly, but when I go to save the capture the file (e.g. 71 MB) the file saves, and the a close dialog pops up on screen...'''
date = "2011-12-23T09:09:00Z"
lastmod = "2011-12-23T09:23:00Z"
weight = 8113
keywords = [ "airpcap" ]
aliases = [ "/questions/8113" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.6.4 Windows 7 32-bit Crashes on Capture Save](/questions/8113/wireshark-164-windows-7-32-bit-crashes-on-capture-save)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8113-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Am running 1.6.4 under 32-bit Windows and doing wireless captures using AirPcap cards across 1,6,11. Am using the aggregator virtual adapter that combines these. System captures properly, but when I go to save the capture the file (e.g. 71 MB) the file saves, and the a close dialog pops up on screen but never goes away. I have to kill the app and reboot to start a new capture. The saved capture seems OK. I have plenty of free disk space on this machine, also 3 GB of RAM and nothing else running at the time.</p><p>Any help is appreciated. It's important that I am able to capture on the 3 USB AirPcap devices at the same time.</p></div><div id="question-tags" class="tags-container tags">airpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '11, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/8a6a04f8e78617cf25a7cc58a9a5877c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kendor&#39;s gravatar image" /><p>Kendor<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kendor has no accepted answers">0%</span></p></div></div><div id="comments-container-8113" class="comments-container"></div><div id="comment-tools-8113" class="comment-tools"></div><div class="clear"></div><div id="comment-8113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8115"></span>

<div id="answer-container-8115" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8115-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds like <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3046">bug 3046</a>, which has been fixed and is scheduled for 1.6.5, so look for it when it comes out. In the meantime, you can close the dialog using the <code>ALT+F4</code> work-around mentioned by Johannes Lange in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3046#c18">comment 18</a> of that bug report. Alternatively, you could upgrade to one of the <a href="http://www.wireshark.org/download/automated/win32/">automated</a> releases from the unstable development branch if you wish.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '11, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-8115" class="comments-container"></div><div id="comment-tools-8115" class="comment-tools"></div><div class="clear"></div><div id="comment-8115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

