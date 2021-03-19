+++
type = "question"
title = "wireshark 1.12.8 core dump trace"
description = '''Hi, We have some issue when executing wireshark 1.12.8 in RHEL santiago. The wireshark core dumped and after gdb, bt command with that core dump, the below o/p is get #0 0x00007fdc5f57a782 in ?? () #1 0x00007fdc603b2fc0 in ?? () #2 0x00007fdc60188c46 in ?? () #3 0x00007fdc54bac070 in ?? () #4 0x0000...'''
date = "2016-02-04T05:10:00Z"
lastmod = "2016-02-04T05:10:00Z"
weight = 49814
keywords = [ "gdb", "wireshark" ]
aliases = [ "/questions/49814" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark 1.12.8 core dump trace](/questions/49814/wireshark-1128-core-dump-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49814-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, We have some issue when executing wireshark 1.12.8 in RHEL santiago. The wireshark core dumped and after gdb, bt command with that core dump, the below o/p is get</p><pre><code>#0  0x00007fdc5f57a782 in ?? ()
#1  0x00007fdc603b2fc0 in ?? ()
#2  0x00007fdc60188c46 in ?? ()
#3  0x00007fdc54bac070 in ?? ()
#4  0x0000000000000000 in ?? ()</code></pre><p>so we are not getting any function or file which is causing dump. we are modified many files of wireshark according to compliant with proprietary messages and IEs, we have make files which run fine for same changes on wireshark 1.10.6 version.</p><p>My question is more on GDB than Wireshark related. Please let me know how to trace the memory stack mentioned before.</p></div><div id="question-tags" class="tags-container tags">gdb wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '16, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/48912e037040264c21d2e543aca485e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhisek&#39;s gravatar image" /><p>Abhisek<br />
<span class="score" title="16 reputation points">16</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhisek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Feb '16, 05:36</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-49814" class="comments-container"></div><div id="comment-tools-49814" class="comment-tools"></div><div class="clear"></div><div id="comment-49814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

