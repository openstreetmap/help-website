+++
type = "question"
title = "Initial SYN handshake"
description = '''During the initial SyN handshake we see a &quot;windows size&quot; field in the trace file. Is that field sent by the client (sender) or the destination (server) ? My understanding is that the initial SYN in the beginning of the three way handshake is always started from the client (sender), is that correct ?'''
date = "2013-08-13T19:45:00Z"
lastmod = "2013-08-13T22:07:00Z"
weight = 23756
keywords = [ "initial", "syn" ]
aliases = [ "/questions/23756" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Initial SYN handshake](/questions/23756/initial-syn-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23756-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>During the initial SyN handshake we see a "windows size" field in the trace file. Is that field sent by the client (sender) or the destination (server) ?</p><p>My understanding is that the initial SYN in the beginning of the three way handshake is always started from the client (sender), is that correct ?</p></div><div id="question-tags" class="tags-container tags">initial syn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '13, 19:45</strong></p><img src="https://secure.gravatar.com/avatar/f9286d33942eef728d42e015a308bb89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Robbie%20S&#39;s gravatar image" /><p>Robbie S<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Robbie S has no accepted answers">0%</span></p></div></div><div id="comments-container-23756" class="comments-container"></div><div id="comment-tools-23756" class="comment-tools"></div><div class="clear"></div><div id="comment-23756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23762"></span>

<div id="answer-container-23762" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23762-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes that is correct.</p><p>"Active opener trying to connect to the Passive Listener"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '13, 21:39</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-23762" class="comments-container"></div><div id="comment-tools-23762" class="comment-tools"></div><div class="clear"></div><div id="comment-23762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23763"></span>

<div id="answer-container-23763" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23763-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The SYN is sent by the system that is initiating the TCP connection. That is usually, but not always, the client. For example, in FTP, the FTP client will initiate a connection to the FTP server on the command channel (port 21). Each system is both a sender and a receiver. The client sends commands, and the server sends responses.</p><p>However, when files are uploaded or downloaded, a separate connection is established. In active FTP, the server connects to the client; in passive FTP the client connects to the server. Data flows in one direction only. Which system is the sender depends on whether the transfer is an upload or a download.</p><p>Both systems send their window size.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '13, 22:07</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-23763" class="comments-container"></div><div id="comment-tools-23763" class="comment-tools"></div><div class="clear"></div><div id="comment-23763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

