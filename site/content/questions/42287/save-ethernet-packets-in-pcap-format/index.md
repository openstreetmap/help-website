+++
type = "question"
title = "Save Ethernet packets in .pcap format"
description = '''Hello, I am building an application to accept output messages(Ethernet packets) from ECU(Electronic Control unit) and display it on a GUI. The GUI is build using QT designer python and the packets from the ECU will be displayed in a Tree Widget. I am using socket program to bind with the ECU. I want...'''
date = "2015-05-10T15:19:00Z"
lastmod = "2015-06-07T21:54:00Z"
weight = 42287
keywords = [ "python", "socket", "tree", "qtgui", ".pcap" ]
aliases = [ "/questions/42287" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Save Ethernet packets in .pcap format](/questions/42287/save-ethernet-packets-in-pcap-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42287-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am building an application to accept output messages(Ethernet packets) from ECU(Electronic Control unit) and display it on a GUI. The GUI is build using QT designer python and the packets from the ECU will be displayed in a Tree Widget. I am using socket program to bind with the ECU. I want to save these output in a .pcap format. Is it possible to save directly in .pcap format ? Are there any library to save the data directly ? Is there already a code implemented for this ? If yes, then how should i proceed further ?</p></div><div id="question-tags" class="tags-container tags">python socket tree qtgui .pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '15, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/85652400f627dbc4dbd4d0d09e03ecee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Praju&#39;s gravatar image" /><p>Praju<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Praju has no accepted answers">0%</span></p></div></div><div id="comments-container-42287" class="comments-container"></div><div id="comment-tools-42287" class="comment-tools"></div><div class="clear"></div><div id="comment-42287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="42313"></span>

<div id="answer-container-42313" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42313-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>It should be no problem finding a library for your favorite language</p></blockquote><p>If your favorite language is a straightforward C derivative (C itself, C++, Objective-C), the library is called libpcap on UN*X and WinPcap on Windows; just use that. The API for writing capture files is a bit clumsy if you're not writing packets from a libpcap/WinPcap live capture or file you're reading with libpcap/WinPcap, you'd want to use <code>pcap_open_dead()</code> to specify a packet format of <code>DLT_EN10MB</code> (meaning "packets that begin with an Ethernet header"), and then use <code>pcap_dump_open()</code> to open the output file, <code>pcap_dump()</code> to write packets, and <code>pcap_dump_close()</code> to finish writing out the packets and close the file.</p><p><strong><em>NOTE</em></strong>: if the output messages you receive do <em>not</em> have Ethernet headers, you can't use <code>DLT_EN10MB</code>. If they have only IP headers, use <code>DLT_RAW</code>. If they don't even have IP headers, you will need to, at minimum, put IP headers at the beginning, followed by headers for the transport protocols, e.g. TCP or UDP. I.e., do not assume that messages received at the <em>application</em> level can easily be put into pcap files without some additional work!</p><p>If your favorite language isn't a straightforward C derivative (C#, the "C" at the beginning of the name nonwithstanding, is not a straightforward C derivative in the sense that I'm using it), see, for example, <a href="https://en.wikipedia.org/wiki/Pcap#Wrapper_libraries_for_libpcap.2FWinPcap">the "Wrapper libraries" section of the Wikipedia page for pcap</a> for information about wrapper libraries for your language. With those languages, much of what I said above still applies, but the way you call those functions may be different than the way you do so from code written in straightforward C derivatives.</p><p>In the case of Python, the Wikipedia page section lists <a href="https://sourceforge.net/projects/pylibpcap/">python-libpcap</a> and <a href="http://corelabs.coresecurity.com/index.php?module=Wiki&amp;action=view&amp;type=tool&amp;name=Pcapy">pcapy</a>. Neither of them appear to have good online documentation, so I don't know whether either of them do a good job of supporting <em>writing</em> pcap files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '15, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 May '15, 14:11</p></div></div><div id="comments-container-42313" class="comments-container"></div><div id="comment-tools-42313" class="comment-tools"></div><div class="clear"></div><div id="comment-42313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42298"></span>

<div id="answer-container-42298" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42298-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The PCAP file format is a rather simple <a href="https://wiki.wireshark.org/Development/LibpcapFileFormat">file format</a>. It should be no problem finding a library for your favorite language, and/or file output routines can easily be written by hand as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '15, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-42298" class="comments-container"><span id="42302"></span><div id="comment-42302" class="comment"><div id="post-42302-score" class="comment-score"></div><div class="comment-text"><p>@jaap Thanks. I will look into it</p></div><div id="comment-42302-info" class="comment-info"><span class="comment-age">(11 May '15, 07:08)</span> Praju</div></div><span id="42309"></span><div id="comment-42309" class="comment"><div id="post-42309-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-42309-info" class="comment-info"><span class="comment-age">(11 May '15, 08:40)</span> Jaap ♦</div></div><span id="42314"></span><div id="comment-42314" class="comment"><div id="post-42314-score" class="comment-score"></div><div class="comment-text"><blockquote><p>file output routines can easily be written by hand as well.</p></blockquote><p>And <em>incorrect</em> file output routines can also be easily written by hand, so I'd suggest looking at using libpcap/WinPcap, or wrappers for them, unless there's a reason why you can't do that.</p></div><div id="comment-42314-info" class="comment-info"><span class="comment-age">(11 May '15, 14:08)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-42298" class="comment-tools"></div><div class="clear"></div><div id="comment-42298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42956"></span>

<div id="answer-container-42956" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42956-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're using C/C++ and don't want to mess with libpcap/WinPcap API directly you can use a wrapper library that wraps that functionality and provides a more convenient multi-platform object-oriented C++ API. I wrote such a library: <a href="https://github.com/seladb/PcapPlusPlus">PcapPlusPlus</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '15, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/0b6fc0687623a56d9f42c88153062754?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seladb&#39;s gravatar image" /><p>seladb<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seladb has no accepted answers">0%</span></p></div></div><div id="comments-container-42956" class="comments-container"></div><div id="comment-tools-42956" class="comment-tools"></div><div class="clear"></div><div id="comment-42956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

