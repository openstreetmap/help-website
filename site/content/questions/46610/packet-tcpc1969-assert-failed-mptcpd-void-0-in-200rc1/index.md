+++
type = "question"
title = "packet-tcp.c:1969 assert failed &quot;mptcpd != ((void *)0&quot; in 2.0.0rc1"
description = '''Using Mac OS X 10.11 with wireshark download: Version 2.0.0rc1 (v2.0.0rc1-0-g3b09294 from master-2.0) I traced port 80 traffic from iTunes attempting a download and see the assert. taking the pcapng file to Linux and uses the packaged Fedora version  wireshark-1.12.7-2.fc22.x86_64 the pcap decodes w...'''
date = "2015-10-16T04:41:00Z"
lastmod = "2015-10-16T13:40:00Z"
weight = 46610
keywords = [ "bug", "mptcp" ]
aliases = [ "/questions/46610" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [packet-tcp.c:1969 assert failed "mptcpd != ((void \*)0" in 2.0.0rc1](/questions/46610/packet-tcpc1969-assert-failed-mptcpd-void-0-in-200rc1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46610-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Mac OS X 10.11 with wireshark download: Version 2.0.0rc1 (v2.0.0rc1-0-g3b09294 from master-2.0)</p><p>I traced port 80 traffic from iTunes attempting a download and see the assert.</p><p>taking the pcapng file to Linux and uses the packaged Fedora version wireshark-1.12.7-2.fc22.x86_64 the pcap decodes without error.</p></div><div id="question-tags" class="tags-container tags">bug mptcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '15, 04:41</strong></p><img src="https://secure.gravatar.com/avatar/b68cda4e0d04e1b966cfa5657bbec53d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="barryas&#39;s gravatar image" /><p>barryas<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="barryas has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '15, 13:39</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-46610" class="comments-container"></div><div id="comment-tools-46610" class="comment-tools"></div><div class="clear"></div><div id="comment-46610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="46615"></span>

<div id="answer-container-46615" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46615-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is fixed in 2.0RC2 pre release that you can find here: <a href="https://www.wireshark.org/download/automated/">https://www.wireshark.org/download/automated/</a></p><p>Sorry for the inconvenience.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '15, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-46615" class="comments-container"></div><div id="comment-tools-46615" class="comment-tools"></div><div class="clear"></div><div id="comment-46615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46612"></span>

<div id="answer-container-46612" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46612-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a bug. Please raise an entry on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a> and attach your capture to the entry.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '15, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-46612" class="comments-container"></div><div id="comment-tools-46612" class="comment-tools"></div><div class="clear"></div><div id="comment-46612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46632"></span>

<div id="answer-container-46632" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46632-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As others have said, it's a bug, and it's a 2.0-specific bug; it's not on your Linux box because you're using 1.12, not 2.0, on your Linux box, not because there's a difference here between OS X and Linux.</p><p>In particular, it's <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11598">bug 11598</a>, found on Windows, which is a duplicate of <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11593">bug 11593</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '15, 13:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '15, 17:17</p></div></div><div id="comments-container-46632" class="comments-container"></div><div id="comment-tools-46632" class="comment-tools"></div><div class="clear"></div><div id="comment-46632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

