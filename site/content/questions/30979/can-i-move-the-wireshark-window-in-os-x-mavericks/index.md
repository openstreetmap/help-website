+++
type = "question"
title = "Can I move the Wireshark window in OS X Mavericks?"
description = '''I&#x27;ve got Wireshark running in OS X Mavericks, but I don&#x27;t see how I can move the window. There&#x27;s no title bar visible. I can move it between monitors by hitting control-up arrow and dragging it between, but on either monitor the window goes flush up to the upper left and I can&#x27;t move it. Nothing in ...'''
date = "2014-03-19T22:22:00Z"
lastmod = "2014-06-19T10:24:00Z"
weight = 30979
keywords = [ "mac", "xquartz", "mavericks" ]
aliases = [ "/questions/30979" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can I move the Wireshark window in OS X Mavericks?](/questions/30979/can-i-move-the-wireshark-window-in-os-x-mavericks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30979-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've got Wireshark running in OS X Mavericks, but I don't see how I can move the window. There's no title bar visible. I can move it between monitors by hitting control-up arrow and dragging it between, but on either monitor the window goes flush up to the upper left and I can't move it. Nothing in the XQuartz menus seems to offer help along these lines. Does anyone know how to do this? (I'm a Mac and X11 noob, btw.)</p></div><div id="question-tags" class="tags-container tags">mac xquartz mavericks</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '14, 22:22</strong></p><img src="https://secure.gravatar.com/avatar/f96cc6d382fe4def22ca2a5deafec56f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="uCallHimDrJ0NES&#39;s gravatar image" /><p>uCallHimDrJ0NES<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="uCallHimDrJ0NES has no accepted answers">0%</span></p></div></div><div id="comments-container-30979" class="comments-container"><span id="30999"></span><div id="comment-30999" class="comment"><div id="post-30999-score" class="comment-score"></div><div class="comment-text"><p>What do you mean there's no title bar? You don't see a bar at the top of the Wireshark GUI with the red/yellow/green buttons on the left? I do, on my Mac Mavericks. On the Mac top toolbar (the one that has the Apple icon on the left, and should say "X11" to the right of that), select Window-&gt;Zoom. See if that shows it. If not, post your Wireshark version information here.</p></div><div id="comment-30999-info" class="comment-info"><span class="comment-age">(20 Mar '14, 09:46)</span> Hadriel</div></div><span id="33936"></span><div id="comment-33936" class="comment"><div id="post-33936-score" class="comment-score"></div><div class="comment-text"><p>Yes, I am having this same problem. I opened another related question. There is an interface anomaly problem whereby the menu bar for wireshark is opening behind Mac OSXs preventing the user from grabbing the menu bar of wireshark. This is extremely annoying.</p><p>bash-3.2$ wireshark -version 2014-06-18 10:27:15.746 defaults[43269:507] The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist 2014-06-18 10:27:15.759 defaults[43270:507] The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist wireshark 1.10.8 (v1.10.8-2-g52a5244 from master-1.10)</p><p>Copyright 1998-2014 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GTK+ 2.24.17, with Cairo 1.10.2, with Pango 1.30.1, with GLib 2.36.0, with libpcap, with libz 1.2.3, without POSIX capabilities, without libnl, with SMI 0.4.8, without c-ares, without ADNS, with Lua 5.1, without Python, with GnuTLS 2.12.19, with Gcrypt 1.5.0, with MIT Kerberos, with GeoIP, with PortAudio V19-devel (built Jul 16 2013 19:05:52), with AirPcap.</p><p>Running on Mac OS X 10.9.3, build 13D65 (Darwin 13.2.0), with locale .UTF-8, with libpcap version 1.3.0 - Apple version 41, with libz 1.2.5, GnuTLS 2.12.19, Gcrypt 1.5.0, without AirPcap. Intel(R) Xeon(R) CPU E5620 @ 2.40GHz</p><p>Built using llvm-gcc 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.9.00).</p></div><div id="comment-33936-info" class="comment-info"><span class="comment-age">(18 Jun '14, 10:27)</span> burnbrighter</div></div></div><div id="comment-tools-30979" class="comment-tools"></div><div class="clear"></div><div id="comment-30979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33960"></span>

<div id="answer-container-33960" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33960-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have more information on this - this is related to how XQuartz works with Spaces in Mavericks and perhaps multiple monitors (I have 4). Mavericks introduces the concept of individual Spaces per screen. As a workaround, you can disable this functionality in the preferences for Mission Control and uncheck "Display have separate Spaces". This solved my problem, but I don't see this as a fix and I'm not sure if this is an XQuartz problem only.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '14, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/2daaed0f953ed850693cdffc5e1866ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="burnbrighter&#39;s gravatar image" /><p>burnbrighter<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="burnbrighter has no accepted answers">0%</span></p></div></div><div id="comments-container-33960" class="comments-container"><span id="34854"></span><div id="comment-34854" class="comment"><div id="post-34854-score" class="comment-score"></div><div class="comment-text"><p>This tip works. As an addition if you uncheck "Displays have separate spaces" and then log out and back in and launch wireshark, all you have to do is then move the window to somewhere else and quick wireshark.</p><p>Then you can turn on the separate spaces setting again and next time you launch wireshark it will load where you left it.</p><p>Basically Wireshark is loading the first time with its top/left positioning "below" the menubar. So you can't move it.</p></div><div id="comment-34854-info" class="comment-info"><span class="comment-age">(23 Jul '14, 11:14)</span> PyjamaSam</div></div></div><div id="comment-tools-33960" class="comment-tools"></div><div class="clear"></div><div id="comment-33960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

