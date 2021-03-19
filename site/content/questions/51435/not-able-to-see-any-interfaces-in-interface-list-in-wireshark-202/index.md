+++
type = "question"
title = "Not able to see any interfaces in interface list in wireshark 2.0.2 ???"
description = '''I have installed wireshark 2.0.2. But I am not able to watch any interface in interface list GUI. Though i am connected with internet through LAN cable. What can be the issue? '''
date = "2016-04-06T05:50:00Z"
lastmod = "2016-04-07T01:35:00Z"
weight = 51435
keywords = [ "interface", "wireshark" ]
aliases = [ "/questions/51435" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Not able to see any interfaces in interface list in wireshark 2.0.2 ???](/questions/51435/not-able-to-see-any-interfaces-in-interface-list-in-wireshark-202)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51435-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have installed wireshark 2.0.2. But I am not able to watch any interface in interface list GUI. Though i am connected with internet through LAN cable. What can be the issue?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_oaCmb0V.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">interface wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '16, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p>ankit<br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 06 Apr '16, 05:51</p></div></div><div id="comments-container-51435" class="comments-container"><span id="51436"></span><div id="comment-51436" class="comment"><div id="post-51436-score" class="comment-score"></div><div class="comment-text"><p>Access to interfaces is provided by WinPCap, usually installed by the Wireshark installer. What does your Help -&gt; About Wireshark info show. Hint, you can copy the text from the dialog by highlighting it with your mouse and right clicking and selecting copy (or Ctrl + C).</p></div><div id="comment-51436-info" class="comment-info"><span class="comment-age">(06 Apr '16, 06:01)</span> grahamb ♦</div></div><span id="51438"></span><div id="comment-51438" class="comment"><div id="post-51438-score" class="comment-score"></div><div class="comment-text"><p>Below is the my Help -&gt; About wireshark menu info</p><p>Version 2.0.2 (v2.0.2-0-ga16e22e from master-2.0)</p><p>Copyright 1998-2016 Gerald Combs [email protected] and contributors. License GPLv2+: GNU GPL version 2 or later <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">http://www.gnu.org/licenses/old-licenses/gpl-2.0.html</a> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with Qt 5.3.2, with WinPcap (4_1_3), with libz 1.2.8, with GLib 2.42.0, with SMI 0.4.8, with c-ares 1.9.1, with Lua 5.2, with GnuTLS 3.2.15, with Gcrypt 1.6.2, with MIT Kerberos, with GeoIP, with QtMultimedia, with AirPcap.</p><p>Running on 64-bit Windows 7 Service Pack 1, build 7601, with locale C, with WinPcap version 4.1.3 (packet.dll version 4.1.0.2980), based on libpcap version 1.0 branch 1_0_rel0b (20091008), with GnuTLS 3.2.15, with Gcrypt 1.6.2, without AirPcap. Intel(R) Core(TM) i5-3340M CPU @ 2.70GHz (with SSE4.2), with 4001MB of physical memory.</p><p>Built using Microsoft Visual C++ 12.0 build 40629</p><p>Wireshark is Open Source Software released under the GNU General Public License.</p><p>Check the man page and <a href="http://www.wireshark.org">http://www.wireshark.org</a> for more information.</p></div><div id="comment-51438-info" class="comment-info"><span class="comment-age">(06 Apr '16, 09:34)</span> ankit</div></div><span id="51440"></span><div id="comment-51440" class="comment"><div id="post-51440-score" class="comment-score"></div><div class="comment-text"><p>OK, you have WinPcap installed, so for some reason it isn't returning a list of interfaces.</p><p>From a command prompt what does <code>"C:\Program Files\Wireshark\dumpcap" -D</code> give as output?</p></div><div id="comment-51440-info" class="comment-info"><span class="comment-age">(06 Apr '16, 10:27)</span> grahamb ♦</div></div><span id="51446"></span><div id="comment-51446" class="comment"><div id="post-51446-score" class="comment-score"></div><div class="comment-text"><p>Below is the output of dumpcap -D from cmd ...</p><p>Microsoft Windows [Version 6.1.7601] Copyright (c) 2009 Microsoft Corporation. All rights reserved.</p><p>C:\Program Files\Wireshark&gt;dumpcap.exe -D dumpcap: There are no interfaces on which a capture can be done</p><p>C:\Program Files\Wireshark&gt;</p></div><div id="comment-51446-info" class="comment-info"><span class="comment-age">(06 Apr '16, 21:30)</span> ankit</div></div></div><div id="comment-tools-51435" class="comment-tools"></div><div class="clear"></div><div id="comment-51435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51454"></span>

<div id="answer-container-51454" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51454-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi @grahamb,</p><p>First of all thanks for your replies... When I opened wireshark with "Run as administrator" option it is showing me the possible list of interfaces. So now I am able to capture the packets as mentioned in below image</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark1.PNG" alt="alt text" /></p><p>I got the hint of this solution from <a href="http://stackoverflow.com/questions/8255644/why-doesnt-wireshark-detect-my-interface">this link</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '16, 01:35</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p>ankit<br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></img></div></div><div id="comments-container-51454" class="comments-container"><span id="51457"></span><div id="comment-51457" class="comment"><div id="post-51457-score" class="comment-score">1</div><div class="comment-text"><p>That's very abnormal behaviour on Windows. There have been occasional reports of this, but no definite cause. I think there have been instances where somehow the installation wasn't run with elevated permissions.</p><p>It's not recommended running Wireshark with elevated permissions as malicious network traffic could cause the 3 million + lines of code in Wireshark to do something bad.</p><p>I would uninstall Wireshark and WinPcap, reboot and then reinstall, ensuring that the installer does run with elevated permissions, i.e. you should get a UAC prompt.</p></div><div id="comment-51457-info" class="comment-info"><span class="comment-age">(07 Apr '16, 02:38)</span> grahamb ♦</div></div><span id="51492"></span><div id="comment-51492" class="comment"><div id="post-51492-score" class="comment-score"></div><div class="comment-text"><p>I've seen this behavior where Wireshark is installed by administrators and used by users without admin privileges. You may be allowed to "Run as Administrator", but not as yourself. So, you might be stuck doing just that to get Wireshark to access Windows' locked down components. I agree with @grahamb; you might discuss this with your administrator as to how you can run it without elevated permissions.</p></div><div id="comment-51492-info" class="comment-info"><span class="comment-age">(07 Apr '16, 13:01)</span> coloncm</div></div><span id="51495"></span><div id="comment-51495" class="comment"><div id="post-51495-score" class="comment-score"></div><div class="comment-text"><p>@coloncm</p><p>That's an interesting thought. All the users I support have their account in the local Administrators group as this allows them to install software.</p><p>I'll check out what happens with a plain user account.</p></div><div id="comment-51495-info" class="comment-info"><span class="comment-age">(07 Apr '16, 14:28)</span> grahamb ♦</div></div></div><div id="comment-tools-51454" class="comment-tools"></div><div class="clear"></div><div id="comment-51454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

