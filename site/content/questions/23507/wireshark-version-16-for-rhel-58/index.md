+++
type = "question"
title = "Wireshark version &gt; 1.6 for RHEL 5.8"
description = '''I need to install wireshark version &amp;gt; 1.6 on RHEL 5.8, but I am not able to find any RPM on net we well as yum is providing very old versions 1.0.15. I tried compiling source code as well but there are lot of dependencies. Can anyone please refer a path where I can find the required RPM or an eas...'''
date = "2013-08-01T10:21:00Z"
lastmod = "2013-08-01T11:47:00Z"
weight = 23507
keywords = [ "rhel" ]
aliases = [ "/questions/23507" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark version &gt; 1.6 for RHEL 5.8](/questions/23507/wireshark-version-16-for-rhel-58)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23507-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to install wireshark version &gt; 1.6 on RHEL 5.8, but I am not able to find any RPM on net we well as yum is providing very old versions 1.0.15.</p><p>I tried compiling source code as well but there are lot of dependencies.</p><p>Can anyone please refer a path where I can find the required RPM or an easy way to compile and resolve all dependencies</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">rhel</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '13, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/3ac62e4a103b118d6c93f65777d77402?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RAVI_TANDON&#39;s gravatar image" /><p>RAVI_TANDON<br />
<span class="score" title="10 reputation points">10</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RAVI_TANDON has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Aug '13, 10:30</p></div></div><div id="comments-container-23507" class="comments-container"></div><div id="comment-tools-23507" class="comment-tools"></div><div class="clear"></div><div id="comment-23507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23508"></span>

<div id="answer-container-23508" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23508-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I presume when you mean "&gt; 1.6" you mean 1.8 or 1.10 (not 1.6.16, for example).</p><p>The biggest problem you have is that RHEL 5 comes with Gtk+ 2.10.4 and Wireshark 1.8 requires 2.12 or later. Upgrading your Gtk+ would be a significant undertaking but it would be the first thing you need to accomplish. A Wireshark RPM won't help you here...</p><p>You'd also need a slightly newer autoconf but this is something that can be easily compiled and thrown in /usr/local for example.</p><p>Oh, and you'll also need a newer glib2 (RHEL 5 has 2.12.3 and Wireshark 1.8 needs 2.14 or later).</p><p>There may be other things which would need to be upgraded too... Which means you'd probably be better off just using dumpcap/tshark/tcpdump for capturing on your RHEL 5 system and doing analysis on a separate (newer) system.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '13, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-23508" class="comments-container"></div><div id="comment-tools-23508" class="comment-tools"></div><div class="clear"></div><div id="comment-23508-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

