+++
type = "question"
title = "Dumpcap creates files that seem to be corrupt?"
description = '''I am capturing TCP SYN traffic with dumpcap. dumpcap -i 3 -f &quot;tcp[tcpflags] ==2&quot; -b filesize:1000 -w filename.pcapng The resulting files are loaded in wireshark, but wireshark finds the file to be corrupt. I get a warning: &quot;The capture file appears to have been cut short in the middle of a packet.&quot; ...'''
date = "2014-05-15T06:17:00Z"
lastmod = "2014-05-15T06:17:00Z"
weight = 32825
keywords = [ "corrupt", "dumpcap" ]
aliases = [ "/questions/32825" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dumpcap creates files that seem to be corrupt?](/questions/32825/dumpcap-creates-files-that-seem-to-be-corrupt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32825-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am capturing TCP SYN traffic with dumpcap.</p><p>dumpcap -i 3 -f "tcp[tcpflags] ==2" -b filesize:1000 -w filename.pcapng</p><p>The resulting files are loaded in wireshark, but wireshark finds the file to be corrupt. I get a warning: "The capture file appears to have been cut short in the middle of a packet."</p><p>The filesize dumpcap creates is 992 KB (1.015.808 bytes)</p><p>Version information: C:\Program Files\Wireshark&gt;dumpcap -v Dumpcap 1.10.6 (v1.10.6 from master-1.10)</p><p>Copyright 1998-2014 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GLib 2.34.1, with WinPcap (4_1_3), with libz 1.2.5, without POSIX capabilities, without libnl.</p><p>Running on 64-bit Windows 7 Service Pack 1, build 7601, without WinPcap. Intel(R) Core(TM)2 Duo CPU P8600 @ 2.40GHz, with 3996MB of physical memory.</p><p>Built using Microsoft Visual C++ 10.0 build 40219 See <a href="http://www.wireshark.org">http://www.wireshark.org</a> for more information. C:\Program Files\Wireshark&gt;</p></div><div id="question-tags" class="tags-container tags">corrupt dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '14, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/fa93107efa996eb74f342dd051bbaa3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joop&#39;s gravatar image" /><p>Joop<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joop has no accepted answers">0%</span></p></div></div><div id="comments-container-32825" class="comments-container"></div><div id="comment-tools-32825" class="comment-tools"></div><div class="clear"></div><div id="comment-32825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

