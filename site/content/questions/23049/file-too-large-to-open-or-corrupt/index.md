+++
type = "question"
title = "file too large to open or corrupt?"
description = '''Been troubleshooting a potential problem with a device that happens randomly. So I&#x27;ve been forced to capture almost 8 hours a day. The incident I was trying to record happened within the last few minutes of the day as I was about to leave/stop capturing for the day. So I have this 1.5gb cap. However...'''
date = "2013-07-16T09:47:00Z"
lastmod = "2013-07-16T09:59:00Z"
weight = 23049
keywords = [ "open_error", "runtime" ]
aliases = [ "/questions/23049" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [file too large to open or corrupt?](/questions/23049/file-too-large-to-open-or-corrupt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23049-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Been troubleshooting a potential problem with a device that happens randomly. So I've been forced to capture almost 8 hours a day.</p><p>The incident I was trying to record happened within the last few minutes of the day as I was about to leave/stop capturing for the day. So I have this 1.5gb cap. However when I try to open the file so I can run a filter, wireshark crashes. So having an FML moment.</p><p>Wireshark crashes at 86% on windows xp with this error: GLib-ERROR **: gmem.c:170: failed to allocate 81021638 bytes aborting...</p><p>When I click OK, I get a C++ Runtime Error and then wireshark closes after that.</p><p>I'm not sure what the difference would be, but I tried opening the .cap on windows server 2008 and I do not get glib error, only runtime error and it still crashes, except this time at 94%</p><p>I've tried multiple times and it always crashes at the same percentage on each machine.</p><p>Truthfully, I think I only need the last 4% or 5% or this cap anyway. The capture was recorded via my firewall (pfsense). Is there anything I can do?</p></div><div id="question-tags" class="tags-container tags">open_error runtime</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '13, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/87fc30d7b1bbbb4a2c7df57aabf071c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobbieRobski&#39;s gravatar image" /><p>RobbieRobski<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobbieRobski has no accepted answers">0%</span></p></div></div><div id="comments-container-23049" class="comments-container"></div><div id="comment-tools-23049" class="comment-tools"></div><div class="clear"></div><div id="comment-23049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23050"></span>

<div id="answer-container-23050" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23050-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes. Split the file in smaller files, using the command line tool editcap with the -c parameter, which will tell editcap how many frames per file you want. Then work with the smaller files. Editcap is installed together with Wireshark and can be found in the same directory.</p><p>The issue you're experiencing is a quite common problem. See the following pages:</p><p><a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">http://wiki.wireshark.org/KnownBugs/OutOfMemory</a></p><p><a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '13, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jul '13, 09:55</p></div></div><div id="comments-container-23050" class="comments-container"><span id="23052"></span><div id="comment-23052" class="comment"><div id="post-23052-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I guess that's what I get for still having only 4GB ram.</p><p>I was able to open it on a different workstation.</p></div><div id="comment-23052-info" class="comment-info"><span class="comment-age">(16 Jul '13, 10:10)</span> RobbieRobski</div></div></div><div id="comment-tools-23050" class="comment-tools"></div><div class="clear"></div><div id="comment-23050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23051"></span>

<div id="answer-container-23051" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23051-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The issue is likely to be an out of memory problem, see the Wiki page on <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">Out Of Memory</a>. The page offers a number of solutions, your best options would be to try a 64 bit version of Wireshark on a 64 bit OS, or use editcap (found in the same directory as the Wireshark binary) with the -c option to break the capture file into smaller chunks.</p><p>You can use <a href="http://www.wireshark.org/docs/man-pages/capinfos.html">capinfos</a> to test if the file is corrupt.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '13, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23051" class="comments-container"></div><div id="comment-tools-23051" class="comment-tools"></div><div class="clear"></div><div id="comment-23051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

