+++
type = "question"
title = "Converting 1.6.2 propietary plugins to latest Wireshark release."
description = '''Is there a way to decompile propietary plugins from a 32bit platform version 1.6.2 and compile them AGAIN to a 64 bit 1.10.3 release or even 32 bit? This is what I have:  Version 1.6.2 (SVN Rev 38931 from /trunk-1.6) Copyright 1998-2011 Gerald Combs gerald@wireshark.org and contributors. This is fre...'''
date = "2013-12-05T08:51:00Z"
lastmod = "2013-12-05T08:59:00Z"
weight = 27826
keywords = [ "propietary", "plugins" ]
aliases = [ "/questions/27826" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Converting 1.6.2 propietary plugins to latest Wireshark release.](/questions/27826/converting-162-propietary-plugins-to-latest-wireshark-release)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27826-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to decompile propietary plugins from a 32bit platform version 1.6.2 and compile them AGAIN to a 64 bit 1.10.3 release or even 32 bit?</p><p>This is what I have:</p><p>Version 1.6.2 (SVN Rev 38931 from /trunk-1.6)</p><p>Copyright 1998-2011 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (32-bit) with GTK+ 2.22.1, with GLib 2.26.1, with WinPcap (version unknown), with libz 1.2.5, without POSIX capabilities, without libpcre, with SMI 0.4.8, with c-ares 1.7.1, with Lua 5.1, without Python, with GnuTLS 2.10.3, with Gcrypt 1.4.6, with MIT Kerberos, with GeoIP, with PortAudio V19-devel (built Sep 7 2011), with AirPcap.</p><p>Running on 64-bit Windows 7 Service Pack 1, build 7601, with WinPcap version 4.1.2 (packet.dll version 4.1.0.2001), based on libpcap version 1.0 branch 1_0_rel0b (20091008), GnuTLS 2.10.3, Gcrypt 1.4.6, without AirPcap.</p><p>Built using Microsoft Visual C++ 9.0 build 21022</p></div><div id="question-tags" class="tags-container tags">propietary plugins</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '13, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/c3b287adb5ffa1e43a080f39d76590d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hugeyeti&#39;s gravatar image" /><p>hugeyeti<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hugeyeti has no accepted answers">0%</span></p></div></div><div id="comments-container-27826" class="comments-container"></div><div id="comment-tools-27826" class="comment-tools"></div><div class="clear"></div><div id="comment-27826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27827"></span>

<div id="answer-container-27827" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27827-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The short answer: no.</p><p>The longer answer: The terms of the GPL license used by Wireshark require that you be able to get a copy of the dissector source.</p><p>I suggest that you contact the supplier of the "proprietary dissector" and request the source of the dissector.</p><p>(Of course, once you have the source, some work may/will be required to update the dissector for use with the newer version of Wireshark).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '13, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '13, 09:12</p></div></div><div id="comments-container-27827" class="comments-container"><span id="27828"></span><div id="comment-27828" class="comment"><div id="post-27828-score" class="comment-score"></div><div class="comment-text"><p>Oh good. I'll go ahead and request the source of the dissector. Thank you.</p><p>(Answer converted to a comment in keeping with the way ask.wireshark.org works; Please see the FAQ)</p></div><div id="comment-27828-info" class="comment-info"><span class="comment-age">(05 Dec '13, 09:05)</span> hugeyeti</div></div><span id="27829"></span><div id="comment-27829" class="comment"><div id="post-27829-score" class="comment-score"></div><div class="comment-text"><p>If you should run into any problems getting the source, please let us know.</p></div><div id="comment-27829-info" class="comment-info"><span class="comment-age">(05 Dec '13, 09:09)</span> Bill Meier ♦♦</div></div><span id="27830"></span><div id="comment-27830" class="comment"><div id="post-27830-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-27830-info" class="comment-info"><span class="comment-age">(05 Dec '13, 09:10)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-27827" class="comment-tools"></div><div class="clear"></div><div id="comment-27827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

