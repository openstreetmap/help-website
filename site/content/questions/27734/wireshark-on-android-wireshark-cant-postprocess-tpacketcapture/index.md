+++
type = "question"
title = "wireshark on android: wireshark can&#x27;t postprocess tPacketCapture"
description = '''I have installed tPacketCapture on my Android phone (Nexus Phone Android kitkat). I transferred the file to my laptop and launched wireshark. Wireshark was consuming all the availlabe RAM (more than 6GB) when loading a 27MB file. I had to kill the wireshark process.  Anyone aware of this issue? And ...'''
date = "2013-12-03T12:41:00Z"
lastmod = "2013-12-03T14:32:00Z"
weight = 27734
keywords = [ "android", "tpacketcapture", "bug", "wireshark" ]
aliases = [ "/questions/27734" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark on android: wireshark can't postprocess tPacketCapture](/questions/27734/wireshark-on-android-wireshark-cant-postprocess-tpacketcapture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27734-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have installed tPacketCapture on my Android phone (Nexus Phone Android kitkat). I transferred the file to my laptop and launched wireshark. Wireshark was consuming all the availlabe RAM (more than 6GB) when loading a 27MB file. I had to kill the wireshark process. Anyone aware of this issue? And do you know if tPacketCapture works properly.. when it does not crash wireshark?</p></div><div id="question-tags" class="tags-container tags">android tpacketcapture bug wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '13, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/d0f06d34a341e69557b9fba37a267a6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pierre0001&#39;s gravatar image" /><p>pierre0001<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pierre0001 has no accepted answers">0%</span></p></div></div><div id="comments-container-27734" class="comments-container"></div><div id="comment-tools-27734" class="comment-tools"></div><div class="clear"></div><div id="comment-27734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27736"></span>

<div id="answer-container-27736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27736-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>do you know if tPacketCapture works properly.. when it does not crash wireshark?</p></blockquote><p>No, but others seem to have had success. Search for tag 'android' on this site.</p><p>It may be that you've encountered a wireshark bug.</p><p>To help diagnose the issue (and obtain a capture file small enough to attach to a wireshark bug report), please do the following:</p><ol><li>On your PC: Use <code>capinfos</code> (from the commandline) to get info about the capture file;</li><li>(If the file is read OK) determine the number of packets in the file from the <code>capinfos</code> output.</li><li>Split the file into two parts using <code>editcap</code> (See below).</li><li>Open, in turn, each of the two files with Wireshark. (Hopefully) one of the files will still show the problem.</li><li>Repeat steps 1-4 on the bad file and etc until you've a (bad) file of manageable size (or until the issue no longer occurs).</li><li><p>Submit a Wireshark bug report at <a href="http://bugs.wireshark.org">bugs.wireshark.org</a> and attach the smallest bad file obtained (hopefully under 1 Meg). You can mark the bug as private if the capture file contains private data. (Click on advanced fields in the bug report).</p><p>Commands:</p><p><code>capinfos filename</code></p><p><code>editcap -c n filename split-filename</code> // 'n' is the number of packets to split by</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '13, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '13, 14:44</p></div></div><div id="comments-container-27736" class="comments-container"></div><div id="comment-tools-27736" class="comment-tools"></div><div class="clear"></div><div id="comment-27736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

