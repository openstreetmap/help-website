+++
type = "question"
title = "Handling missing fragments while reassembling"
description = '''I am able to reassemble fragments successfully if there is a complete message. However if there are missing fragments my dissector continues to reassemble the next message along with the message that has the missing fragments. I can calculate how many fragments there are supposed to be before I begi...'''
date = "2017-06-09T08:58:00Z"
lastmod = "2017-06-09T10:06:00Z"
weight = 61912
keywords = [ "reassembly", "fragmentation", "dissector", "reassemble", "dissection" ]
aliases = [ "/questions/61912" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Handling missing fragments while reassembling](/questions/61912/handling-missing-fragments-while-reassembling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61912-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am able to reassemble fragments successfully if there is a complete message. However if there are missing fragments my dissector continues to reassemble the next message along with the message that has the missing fragments. I can calculate how many fragments there are supposed to be before I begin reassembly but my first indication that there are missing fragments is when I come across the initial frame for the next fragmented packet. Is there a way that I can tell my reassembly to immediately stop reassembling at the previous fragment and begin a new reassembly at the current initial fragment. Either that or can I look at the next future packet to check if it is the next fragment or an initial fragment to another message?</p></div><div id="question-tags" class="tags-container tags">reassembly fragmentation dissector reassemble dissection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '17, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/ec69e82648ca5a020df1522509212989?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jpetersen&#39;s gravatar image" /><p>jpetersen<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jpetersen has no accepted answers">0%</span></p></div></div><div id="comments-container-61912" class="comments-container"></div><div id="comment-tools-61912" class="comment-tools"></div><div class="clear"></div><div id="comment-61912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61914"></span>

<div id="answer-container-61914" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61914-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The new fragment sequence should be using a new sequence id, so that the original sequence is left unreassembled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '17, 10:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61914" class="comments-container"><span id="61919"></span><div id="comment-61919" class="comment"><div id="post-61919-score" class="comment-score">1</div><div class="comment-text"><p>Thank you that worked.</p><p>For anyone facing a similar problem: I didn't have any sequence ID info in the header for the file so I just used the frame number of the initial fragment for my sequence ID.</p></div><div id="comment-61919-info" class="comment-info"><span class="comment-age">(09 Jun '17, 11:33)</span> jpetersen</div></div></div><div id="comment-tools-61914" class="comment-tools"></div><div class="clear"></div><div id="comment-61914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

