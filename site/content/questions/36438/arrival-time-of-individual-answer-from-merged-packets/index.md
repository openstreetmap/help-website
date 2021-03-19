+++
type = "question"
title = "Arrival time of individual answer from merged packets"
description = '''Hi, I am placed 400 diameter calls and capturing them in wirehsark. Now I need to extract information from capture as below.  Extract sent time of all Diameter request. Extract arrival time of all Diameter request.  All the initial request sent are sent in individual frames so there is one packet fo...'''
date = "2014-09-18T20:38:00Z"
lastmod = "2014-09-19T12:43:00Z"
weight = 36438
keywords = [ "arrivaltime" ]
aliases = [ "/questions/36438" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Arrival time of individual answer from merged packets](/questions/36438/arrival-time-of-individual-answer-from-merged-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36438-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am placed 400 diameter calls and capturing them in wirehsark. Now I need to extract information from capture as below.</p><ol><li>Extract sent time of all Diameter request.</li><li>Extract arrival time of all Diameter request.</li></ol><p>All the initial request sent are sent in individual frames so there is one packet for one request sent. Hence I am able to extract arrival time using PDML. Its because, I have 4000 different arrival times for 4000 different initial requests sent.</p><p>But, the answers come from server as merged packets. So I have 1 arrival time for 4 different packets merged inside single. So I have only 1500 arrival times for 4000 different diameter answers received.</p><p>Now, I need to map arrival times to the sent requests. Is there any way to extract such information?</p><p>Note that, I dont want response time. I want frame sent time and arrival time.</p><p>In short, I dont want merge packets. Is there any way I can split packets to individual and then extract arrival time?</p><p>Let me know please if need more clarification.</p><p>Thank you for your support in advance. Please help.</p><p>Thanks, Vidhi.</p></div><div id="question-tags" class="tags-container tags">arrivaltime</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '14, 20:38</strong></p><img src="https://secure.gravatar.com/avatar/b794b90289cddde7dadc03e91012c605?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vidhi&#39;s gravatar image" /><p>Vidhi<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vidhi has no accepted answers">0%</span></p></div></div><div id="comments-container-36438" class="comments-container"></div><div id="comment-tools-36438" class="comment-tools"></div><div class="clear"></div><div id="comment-36438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36468"></span>

<div id="answer-container-36468" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36468-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On wireshark 1.12 try the exported PDU function.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '14, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-36468" class="comments-container"></div><div id="comment-tools-36468" class="comment-tools"></div><div class="clear"></div><div id="comment-36468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

