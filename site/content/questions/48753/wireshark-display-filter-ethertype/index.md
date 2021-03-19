+++
type = "question"
title = "Wireshark Display Filter: ethertype"
description = '''What&#x27;s the purpose of the &#x27;ethertype&#x27; display filter? It&#x27;s not listed on the Display Filter Reference Page, but Wireshark allows you to type in this keyword during a capture session. Display filter &#x27;eth.type == 0x0800&#x27; will filter IP traffic and I&#x27;d think &#x27;ethertype == 0x0800&#x27; does the same thing (i...'''
date = "2015-12-29T16:55:00Z"
lastmod = "2015-12-30T01:29:00Z"
weight = 48753
keywords = [ "ethertype", "display-filter" ]
aliases = [ "/questions/48753" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Display Filter: ethertype](/questions/48753/wireshark-display-filter-ethertype)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48753-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What's the purpose of the 'ethertype' display filter? It's not listed on the <a href="https://www.wireshark.org/docs/dfref/#section_e">Display Filter Reference Page</a>, but Wireshark allows you to type in this keyword during a capture session.</p><p>Display filter 'eth.type == 0x0800' will filter IP traffic and I'd think 'ethertype == 0x0800' does the same thing (i.e., filter traffic by Ethertype field value), but no traffic is displayed.</p><p>As a side note, I realize Wireshark won't dissect Ethernet_II traffic without protocol "Ethertype" enabled.</p></div><div id="question-tags" class="tags-container tags">ethertype display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '15, 16:55</strong></p><img src="https://secure.gravatar.com/avatar/5b31df3735d7a8400501ab645743deef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ryan%20Moss&#39;s gravatar image" /><p>Ryan Moss<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ryan Moss has no accepted answers">0%</span></p></div></div><div id="comments-container-48753" class="comments-container"></div><div id="comment-tools-48753" class="comment-tools"></div><div class="clear"></div><div id="comment-48753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48755"></span>

<div id="answer-container-48755" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48755-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Under the hood there are several kinds of display filters you can use, among them protocol fields and protocols. You have listed two of them:</p><ul><li>eth.type : protocol field</li><li>ethertype : protocol</li></ul><p>Both protocol fields and protocols can be used in display filter expressions:</p><ul><li>eth.type == 0x0800 : field value equals 0x0800</li><li>ethertype : the ethertype protocol is present.</li></ul><p>So, using 'ethertype', or any other protocol name for that matter, in a display filter basically asserts that the protocol is present in the dissected frame.</p><p>But it also has a value. The bytes making up the protocol are the value. So to make equivalent expressions one could write:</p><ul><li>eth.type == 0x0800 : field value equals 0x0800</li><li>ethertype[12:2] == 08:00 : byte 12 and 13 are 0x08 and 0x00 respectively</li></ul><p>and even:</p><ul><li>eth[12:2] == 08:00</li></ul><p>But if there is 'eth', what is this 'ethertype' for then? Basically it's a pseudo protocol. It is needed to fan out from the wiretap library reading in frames and to use it for 'decode as'.</p><p>Oh, you can't disable it, otherwise frames wouldn't get far as dissections is concerned.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '15, 01:29</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-48755" class="comments-container"><span id="48758"></span><div id="comment-48758" class="comment"><div id="post-48758-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the explanation. Unfortunately, the display filter 'ethertype[12:2]' doesn't filter on the Ethertype field value. I've tried it with several protocols and nothing's returned. Why wouldn't the 'ethertype' protocol display filter by itself not return anything either?</p></div><div id="comment-48758-info" class="comment-info"><span class="comment-age">(30 Dec '15, 07:11)</span> Ryan Moss</div></div><span id="48759"></span><div id="comment-48759" class="comment"><div id="post-48759-score" class="comment-score"></div><div class="comment-text"><p>I'll have to test it myself on a recent Wireshark. What version do you use?</p></div><div id="comment-48759-info" class="comment-info"><span class="comment-age">(30 Dec '15, 10:37)</span> Jaap ♦</div></div><span id="48762"></span><div id="comment-48762" class="comment"><div id="post-48762-score" class="comment-score"></div><div class="comment-text"><p>Version 2.0.0 (v2.0.0-0-g9a73b82 from master-2.0) running on Mac OS X 10.11.2, build 15C50 (Darwin 15.2.0), with locale C, with libpcap version 1.5.3 - Apple version 54, with libz 1.2.5, with GnuTLS 2.12.19, with Gcrypt 1.5.0... AND</p><p>Version 1.12.8 (v1.12.8-0-g5b6e543 from master-1.12) running on 64-bit Windows 7 Service Pack 1, build 7601, with WinPcap version 4.1.3 (packet.dll version 4.1.0.2980), based on libpcap version 1.0 branch 1_0_rel0b (20091008), GnuTLS 3.2.15, Gcrypt 1.6.2, without AirPcap.</p><p>Actually, I just updated the version running on Windows 7 to Version 2.0.1 (v2.0.1-0-g59ea380 from master-2.0).</p></div><div id="comment-48762-info" class="comment-info"><span class="comment-age">(30 Dec '15, 11:41)</span> Ryan Moss</div></div></div><div id="comment-tools-48755" class="comment-tools"></div><div class="clear"></div><div id="comment-48755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

