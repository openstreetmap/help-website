+++
type = "question"
title = "Can we use No in the filter expression?"
description = '''Hi, Can&#x27;t we use No(default Number columnn in the capturing window) as a filter(for ex: No &amp;gt;25)? A Custom protocol has a Sequence Number field.This is also added as a column in the capturing window. My Requirement is: I should apply No==25(example) first and then take the Sequence Number from tha...'''
date = "2011-10-19T22:08:00Z"
lastmod = "2011-10-20T01:11:00Z"
weight = 7000
keywords = [ "filter", "frame", "custom", "columns", "wireshark" ]
aliases = [ "/questions/7000" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can we use No in the filter expression?](/questions/7000/can-we-use-no-in-the-filter-expression)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7000-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Can't we use No(default Number columnn in the capturing window) as a filter(for ex: No &gt;25)? A Custom protocol has a Sequence Number field.This is also added as a column in the capturing window. My Requirement is: I should apply No==25(example) first and then take the Sequence Number from that row. If its not possible this way, please let me know all the other ways to obtain the Sequence Number value from a particular row. Please Help. Thanks in Advance.</p></div><div id="question-tags" class="tags-container tags">filter frame custom columns wireshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '11, 22:08</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p>Terrestrial ...<br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Oct '11, 00:22</p></div></div><div id="comments-container-7000" class="comments-container"></div><div id="comment-tools-7000" class="comment-tools"></div><div class="clear"></div><div id="comment-7000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7004"></span>

<div id="answer-container-7004" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7004-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The frame number is available as the filter "frame.number" :-)</p><p>So you can use : frame.number &gt; 25</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '11, 01:11</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Oct '11, 02:55</p></div></div><div id="comments-container-7004" class="comments-container"><span id="7002"></span><div id="comment-7002" class="comment"><div id="post-7002-score" class="comment-score"></div><div class="comment-text"><p>I 've acquired good Information from the question called <a href="http://ask.wireshark.org/questions/4891/get-frame-data-and-packet-info-from-frame-number">Get frame data and packet info from frame number?</a>. How can i access a particular field called Sequence Number from that frame?</p></div><div id="comment-7002-info" class="comment-info"><span class="comment-age">(19 Oct '11, 22:59)</span> Terrestrial ...</div></div><span id="7003"></span><div id="comment-7003" class="comment"><div id="post-7003-score" class="comment-score"></div><div class="comment-text"><p>may i know the brief details of the fields present in the structure frame_data?(only the fields that are necessary)</p></div><div id="comment-7003-info" class="comment-info"><span class="comment-age">(19 Oct '11, 23:06)</span> Terrestrial ...</div></div><span id="7016"></span><div id="comment-7016" class="comment"><div id="post-7016-score" class="comment-score"></div><div class="comment-text"><p>thanks SYNbit. Your answer solved my problem.</p></div><div id="comment-7016-info" class="comment-info"><span class="comment-age">(21 Oct '11, 00:18)</span> Terrestrial ...</div></div></div><div id="comment-tools-7004" class="comment-tools"></div><div class="clear"></div><div id="comment-7004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

