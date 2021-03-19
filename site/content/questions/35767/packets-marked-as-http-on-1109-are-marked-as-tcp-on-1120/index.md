+++
type = "question"
title = "Packets marked as http on 1.10.9 are marked as tcp on 1.12.0"
description = '''I have a capture that I was looking at in Wireshark 1.10.9 and after upgrading to Wireshark 1.12.0 certain packets that were marked with a protocol of http are now being marked as tcp instead. In both cases I have the tcp preference “Allow sub dissector to reassemble TCP streams” disabled. I have al...'''
date = "2014-08-26T11:22:00Z"
lastmod = "2014-08-26T11:46:00Z"
weight = 35767
keywords = [ "http", "tcp" ]
aliases = [ "/questions/35767" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Packets marked as http on 1.10.9 are marked as tcp on 1.12.0](/questions/35767/packets-marked-as-http-on-1109-are-marked-as-tcp-on-1120)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35767-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture that I was looking at in Wireshark 1.10.9 and after upgrading to Wireshark 1.12.0 certain packets that were marked with a protocol of http are now being marked as tcp instead.</p><p>In both cases I have the tcp preference “Allow sub dissector to reassemble TCP streams” disabled.</p><p>I have also uploaded this capture to cloudshark.org if anyone would like to download it and view it with reassembly turned off:</p><p><a href="https://www.cloudshark.org/captures/dd61015908de">https://www.cloudshark.org/captures/dd61015908de</a></p><p>The packets that have changed from HTTP in version 1.10.9 to TCP in version 1.12.0 are: 7, 8, 11, 12, 14, 15, 17 and 18.</p><p>I’ve looked through the release notes for Wireshark 1.12.0 and I wasn’t able to find anything that seemed related to this.</p><p>Does anyone have any insight on what may have changed between versions?</p></div><div id="question-tags" class="tags-container tags">http tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '14, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/65cd0a920d19fa6ee7fb900733947753?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tomp&#39;s gravatar image" /><p>tomp<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tomp has no accepted answers">0%</span></p></div></div><div id="comments-container-35767" class="comments-container"></div><div id="comment-tools-35767" class="comment-tools"></div><div class="clear"></div><div id="comment-35767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35768"></span>

<div id="answer-container-35768" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35768-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a known bug. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10335">Bug 10335</a> on the Wireshark Bugzilla.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '14, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-35768" class="comments-container"></div><div id="comment-tools-35768" class="comment-tools"></div><div class="clear"></div><div id="comment-35768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

