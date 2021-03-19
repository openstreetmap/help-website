+++
type = "question"
title = "wireshark doesn&#x27;t show protocol of bmp (BGP monitor protocol)"
description = '''I have download a Sample Captures of bmp (BGP monitor protocol) use wireshark analysis,but display nothing of bmp packet,my wireshark is support bmp,the version of wireshark is 2.4.0, I have also capture bmp packet of my lab,but also display nothing,is somebody also have this problems?'''
date = "2017-10-23T22:57:00Z"
lastmod = "2017-10-23T23:13:00Z"
weight = 64136
keywords = [ "bgp", "bmp" ]
aliases = [ "/questions/64136" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark doesn't show protocol of bmp (BGP monitor protocol)](/questions/64136/wireshark-doesnt-show-protocol-of-bmp-bgp-monitor-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64136-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have download a Sample Captures of bmp (BGP monitor protocol) use wireshark analysis,but display nothing of bmp packet,my wireshark is support bmp,the version of wireshark is 2.4.0, I have also capture bmp packet of my lab,but also display nothing,is somebody also have this problems?</p></div><div id="question-tags" class="tags-container tags">bgp bmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '17, 22:57</strong></p><img src="https://secure.gravatar.com/avatar/99a1e8295ab72ef8e99f88794aae3b11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eladlv&#39;s gravatar image" /><p>eladlv<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eladlv has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Oct '17, 09:28</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-64136" class="comments-container"></div><div id="comment-tools-64136" class="comment-tools"></div><div class="clear"></div><div id="comment-64136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64138"></span>

<div id="answer-container-64138" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64138-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Either:</p><ol><li>Set the correct port number in the BMP protocol preferences, or</li><li>Use the "Decode as..." option to assign the BMP dissector to that TCP stream.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '17, 23:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-64138" class="comments-container"><span id="64139"></span><div id="comment-64139" class="comment"><div id="post-64139-score" class="comment-score"></div><div class="comment-text"><p>Thank you，this problem is solved!</p></div><div id="comment-64139-info" class="comment-info"><span class="comment-age">(23 Oct '17, 23:49)</span> eladlv</div></div><span id="64144"></span><div id="comment-64144" class="comment"><div id="post-64144-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-64144-info" class="comment-info"><span class="comment-age">(24 Oct '17, 04:30)</span> Jaap ♦</div></div></div><div id="comment-tools-64138" class="comment-tools"></div><div class="clear"></div><div id="comment-64138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

