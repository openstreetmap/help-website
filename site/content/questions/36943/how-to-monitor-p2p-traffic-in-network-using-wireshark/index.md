+++
type = "question"
title = "How to monitor p2p traffic in network using wireshark?"
description = '''I have to monitor all the p2p traffic through my LAN. Especially skype calls and bit torrent traffic.'''
date = "2014-10-09T06:26:00Z"
lastmod = "2014-10-09T06:54:00Z"
weight = 36943
keywords = [ "bittorrent", "p2p", "skype" ]
aliases = [ "/questions/36943" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to monitor p2p traffic in network using wireshark?](/questions/36943/how-to-monitor-p2p-traffic-in-network-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36943-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have to monitor all the p2p traffic through my LAN. Especially skype calls and bit torrent traffic.</p></div><div id="question-tags" class="tags-container tags">bittorrent p2p skype</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '14, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/803340624b290b88824b7b4044b4159d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="parr&#39;s gravatar image" /><p>parr<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="parr has no accepted answers">0%</span></p></div></div><div id="comments-container-36943" class="comments-container"></div><div id="comment-tools-36943" class="comment-tools"></div><div class="clear"></div><div id="comment-36943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36944"></span>

<div id="answer-container-36944" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36944-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is probably not the tool for you, it is a packet analysis tool, not a network monitor.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '14, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36944" class="comments-container"><span id="36952"></span><div id="comment-36952" class="comment"><div id="post-36952-score" class="comment-score"></div><div class="comment-text"><p>can I identify p2p traffic using wireshark?</p></div><div id="comment-36952-info" class="comment-info"><span class="comment-age">(10 Oct '14, 02:20)</span> parr</div></div><span id="36954"></span><div id="comment-36954" class="comment"><div id="post-36954-score" class="comment-score"></div><div class="comment-text"><p>If Wireshark has a dissector for the particular p2p protocol and the traffic either runs on the ports configured for that dissector, or the dissector heuristics (if it has any) can identify the protocol amongst other traffic, then probably yes.</p><p>Note that you'll still have to handle the capture setup, as your LAN is likely to be using a switched network, or worse wireless traffic. See the Wiki pages on <a href="http://wiki.wireshark.org/CaptureSetup">capture setup</a>.</p></div><div id="comment-36954-info" class="comment-info"><span class="comment-age">(10 Oct '14, 02:37)</span> grahamb ♦</div></div></div><div id="comment-tools-36944" class="comment-tools"></div><div class="clear"></div><div id="comment-36944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

