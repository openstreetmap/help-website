+++
type = "question"
title = "How can I modify a value within the 802.11 header of a captured packet?"
description = '''I would like to change some byte values in the 802.11 header of a captured packet and then SAVE the new modified packet. I did some research and found some programs that modify a PCAP file but these programs cannot change values in the 802.11 header and/or the program does not allow the user to save...'''
date = "2015-05-07T11:58:00Z"
lastmod = "2015-05-12T11:39:00Z"
weight = 42193
keywords = [ "text2pcap", "802.11" ]
aliases = [ "/questions/42193" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can I modify a value within the 802.11 header of a captured packet?](/questions/42193/how-can-i-modify-a-value-within-the-80211-header-of-a-captured-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42193-score" class="post-score" title="current number of votes">0</div><span id="post-42193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to change some byte values in the 802.11 header of a captured packet and then SAVE the new modified packet. I did some research and found some programs that modify a PCAP file but these programs cannot change values in the 802.11 header and/or the program does not allow the user to save the modified frame.</p><p>I also tried the following:</p><ol><li>Use tshark to convert the PCAP file to text</li><li>Modify the text file</li><li>Use text2pcap to convert the text back to PCAP</li></ol><p>However, text2pcap expects the text file to be in Ethernet 802.3 format and not 802.11. Using text2pcap would then remove all the modification made in the 802.11 section.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-text2pcap" rel="tag" title="see questions tagged &#39;text2pcap&#39;">text2pcap</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '15, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-42193" class="comments-container"></div><div id="comment-tools-42193" class="comment-tools"></div><div class="clear"></div><div id="comment-42193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42195"></span>

<div id="answer-container-42195" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42195-score" class="post-score" title="current number of votes">2</div><span id="post-42195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Amato_C has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use a hex editor.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '15, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-42195" class="comments-container"></div><div id="comment-tools-42195" class="comment-tools"></div><div class="clear"></div><div id="comment-42195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42197"></span>

<div id="answer-container-42197" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42197-score" class="post-score" title="current number of votes">2</div><span id="post-42197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In Wireshark 1.12 and later, the packet editor feature is enabled by default, although it's currently only in the GTK+ version, not the Qt version.</p><p>Select "Edit Packet" from the Edit menu, and it'll pop up the currently-selected packet in a new window.</p><p>Open up the 802.11 protocol and double-click the field you want to edit, and modify the hex bytes you want to change.</p><p>The "Save" menu item in the File menu should let you overwrite the file you have open; the "Save As" menu item in the File menu should let you save the new version to a different file. If you try to quit Wireshark, it should let you save the modified file.</p><p>Note that this is a somewhat experimental feature, so you may run into bugs, but I've successfully used it on a couple of occasions. If you find any bugs, please report them on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a> (rather than reporting them here).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '15, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 May '15, 14:42</strong> </span></p></div></div><div id="comments-container-42197" class="comments-container"><span id="42200"></span><div id="comment-42200" class="comment"><div id="post-42200-score" class="comment-score"></div><div class="comment-text"><p>That feature is greyed out. Below is the Wireshark version I am using:</p><p>Version 1.12.4 (v1.12.4-0-gb4861da from master-1.12)</p><p>Compiled (32-bit) with GTK+ 2.24.23, with Cairo 1.10.2, with Pango 1.34.0, with GLib 2.38.0, with WinPcap (4_1_3), with libz 1.2.5, with SMI 0.4.8, with c-ares 1.9.1, with Lua 5.2, without Python, with GnuTLS 3.2.15, with Gcrypt 1.6.2, with MIT Kerberos, with GeoIP, with PortAudio V19-devel (built Mar 4 2015), with AirPcap.</p><p>Running on 32-bit Windows 7 Service Pack 1, build 7601, with WinPcap version 4.1.3 (packet.dll version 4.1.0.2980), based on libpcap version 1.0 branch 1_0_rel0b (20091008), GnuTLS 3.2.15, Gcrypt 1.6.2, without AirPcap</p></div><div id="comment-42200-info" class="comment-info"><span class="comment-age">(07 May '15, 17:56)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="42213"></span><div id="comment-42213" class="comment"><div id="post-42213-score" class="comment-score"></div><div class="comment-text"><p>The feature is also greyed out on my Ubuntu machine:</p><p>Version 1.12.4</p><p>Compiled (64-bit) with GTK+ 3.10.8, with Cairo 1.13.1, with Pango 1.36.3, with GLib 2.40.2, with libpcap, with libz 1.2.8, with POSIX capabilities (Linux), with libnl 1, with SMI 0.4.8, with c-ares 1.10.0, with Lua 5.2, without Python, with GnuTLS 2.12.23, with Gcrypt 1.5.3, with MIT Kerberos, with GeoIP, with PortAudio V19-devel (built Feb 25 2014 21:09:53), without AirPcap.</p><p>Running on Linux 4.0.0-040000-generic, with locale en_US.UTF-8, with libpcap version 1.5.3, with libz 1.2.8, GnuTLS 2.12.23, Gcrypt 1.5.3.</p></div><div id="comment-42213-info" class="comment-info"><span class="comment-age">(08 May '15, 07:07)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="42338"></span><div id="comment-42338" class="comment"><div id="post-42338-score" class="comment-score">1</div><div class="comment-text"><p>Check the preferences setting, Preferences &gt; User Interface &gt; "Enable Packet Editor (Experimental)".</p></div><div id="comment-42338-info" class="comment-info"><span class="comment-age">(12 May '15, 10:18)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="42341"></span><div id="comment-42341" class="comment"><div id="post-42341-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> = That worked! I can now edit in Wireshark. Thanks!</p></div><div id="comment-42341-info" class="comment-info"><span class="comment-age">(12 May '15, 11:39)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-42197" class="comment-tools"></div><div class="clear"></div><div id="comment-42197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

