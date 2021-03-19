+++
type = "question"
title = "Timestamp carried by a wireshark frame is newer than frame&#x27;s timestamp which seems incorrect"
description = '''Hello, We are monitoring NTP packets using Wireshark application (version 2.2.3). In those frames found issue that frame&#x27;s timestamp is about 1600 millisecond older than the timestamp carried by that particular timestamp and this behavior seems incorrect As Wireshark in any case shouldn&#x27;t be sent fu...'''
date = "2016-12-22T03:00:00Z"
lastmod = "2016-12-22T05:02:00Z"
weight = 58296
keywords = [ "wrongtimestamp" ]
aliases = [ "/questions/58296" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Timestamp carried by a wireshark frame is newer than frame's timestamp which seems incorrect](/questions/58296/timestamp-carried-by-a-wireshark-frame-is-newer-than-frames-timestamp-which-seems-incorrect)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58296-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, We are monitoring NTP packets using Wireshark application (version 2.2.3). In those frames found issue that frame's timestamp is about 1600 millisecond older than the timestamp carried by that particular timestamp and this behavior seems incorrect As Wireshark in any case shouldn't be sent future timestamps. This issue is observed on Windows7 Professional while same issue is not observed on windows server 2012 R2 standard.</p></div><div id="question-tags" class="tags-container tags">wrongtimestamp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '16, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/e9072572113c6c0166a8b9adca454c1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Deepak%20jindal&#39;s gravatar image" /><p>Deepak jindal<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Deepak jindal has no accepted answers">0%</span></p></div></div><div id="comments-container-58296" class="comments-container"></div><div id="comment-tools-58296" class="comment-tools"></div><div class="clear"></div><div id="comment-58296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58297"></span>

<div id="answer-container-58297" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58297-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The timestamp in the NTP data is derived from the NTP server and the round-trip between the client and the server and the timestamp of the frame is derived by the capture mechanism on the capturing host, and as such they are from different clocks and so could be different.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '16, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-58297" class="comments-container"></div><div id="comment-tools-58297" class="comment-tools"></div><div class="clear"></div><div id="comment-58297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

