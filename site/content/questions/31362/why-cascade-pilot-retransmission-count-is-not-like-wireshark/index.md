+++
type = "question"
title = "why cascade pilot retransmission count is not like wireshark"
description = '''for specific tcp.stream i use (tcp.stream == 0 and tcp.analysis.retransmit) display filter  in wireshark it displays 129 packet all retransmit and correct ip source and destination  but for same capture file cascade pilot shows that there 210 retransmission packets how come??'''
date = "2014-04-01T15:45:00Z"
lastmod = "2014-04-02T13:28:00Z"
weight = 31362
keywords = [ "pilot" ]
aliases = [ "/questions/31362" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why cascade pilot retransmission count is not like wireshark](/questions/31362/why-cascade-pilot-retransmission-count-is-not-like-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31362-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>for specific tcp.stream i use (tcp.stream == 0 and tcp.analysis.retransmit) display filter</p><p>in wireshark it displays 129 packet all retransmit and correct ip source and destination</p><p>but for same capture file cascade pilot shows that there 210 retransmission packets</p><p>how come??</p></div><div id="question-tags" class="tags-container tags">pilot</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '14, 15:45</strong></p><img src="https://secure.gravatar.com/avatar/583f60448e616e6c6f8408eb6620006a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shady&#39;s gravatar image" /><p>shady<br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shady has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Apr '14, 15:47</p></div></div><div id="comments-container-31362" class="comments-container"></div><div id="comment-tools-31362" class="comment-tools"></div><div class="clear"></div><div id="comment-31362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31431"></span>

<div id="answer-container-31431" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31431-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>how come??</p></blockquote><p>maybe due to different filtering in Wireshark and Pilot?</p><p>What happens if you Export just TCP stream 0 in Wireshark and then let Wireshark and Pilot analyze the file. Do you still see a difference?</p><p>If yes: That needs to be analyzed further.<br />
If no: You probably used different filters in Wireshark and Pilot.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 13:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-31431" class="comments-container"><span id="31465"></span><div id="comment-31465" class="comment"><div id="post-31465-score" class="comment-score"></div><div class="comment-text"><p>i did what said</p><p>i noticed that in pilot analyzer under tcp error tap there (retransmission , dupl ack , lost segment )</p><p>there is difference in retransmission and lost segment</p><p>but there are the same in dupl ack</p><p>i think some thing wrong in filter</p></div><div id="comment-31465-info" class="comment-info"><span class="comment-age">(03 Apr '14, 02:35)</span> shady</div></div></div><div id="comment-tools-31431" class="comment-tools"></div><div class="clear"></div><div id="comment-31431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

