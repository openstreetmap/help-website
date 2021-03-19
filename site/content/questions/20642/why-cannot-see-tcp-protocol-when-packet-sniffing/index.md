+++
type = "question"
title = "Why cannot see  tcp protocol when packet sniffing?"
description = '''I am trying to siniff the pakets by uploading a text file to http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html. But when I start and upload that file, I can only see NBNS protocol(and 3 packets are sent).Why cannot see the tcp protocol?I have already chosen the interfaces at the begin...'''
date = "2013-04-19T14:25:00Z"
lastmod = "2013-04-22T02:25:00Z"
weight = 20642
keywords = [ "wireshark", "upload", "tcp", "nbns" ]
aliases = [ "/questions/20642" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why cannot see tcp protocol when packet sniffing?](/questions/20642/why-cannot-see-tcp-protocol-when-packet-sniffing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20642-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to siniff the pakets by uploading a text file to <a href="http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html">http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html</a>. But when I start and upload that file, I can only see NBNS protocol(and 3 packets are sent).Why cannot see the tcp protocol?I have already chosen the interfaces at the beginning and I am using wireless Internet.I also have made some Google search but couldn't find any useful thing.Thanks for any reply.</p></div><div id="question-tags" class="tags-container tags">wireshark upload tcp nbns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '13, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/353a65d8ca5a7ccfe75b52380fe8ee76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ntf&#39;s gravatar image" /><p>ntf<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ntf has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Apr '13, 21:52</p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span></p></div></div><div id="comments-container-20642" class="comments-container"></div><div id="comment-tools-20642" class="comment-tools"></div><div class="clear"></div><div id="comment-20642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20698"></span>

<div id="answer-container-20698" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20698-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Could it be the TCP Chimney as mentioned in <a href="http://wiki.wireshark.org/CaptureSetup/Offloading">http://wiki.wireshark.org/CaptureSetup/Offloading</a> ?</p><p><code>TCP Chimney Chimney offloading lets the NIC handle processing for established TCP connections. On Windows offloaded connections bypass WinPcap, which means that you won't capture TCP conversations.</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '13, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p>mrEEde2<br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-20698" class="comments-container"></div><div id="comment-tools-20698" class="comment-tools"></div><div class="clear"></div><div id="comment-20698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

