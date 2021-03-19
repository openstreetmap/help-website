+++
type = "question"
title = "Capture filter, tcp port and tcp portrange"
description = '''Hello guys :) I&#x27;m looking for a help. I have a problem with capture filter configuration. I want to capture just a traffic from specific tcp ports. (TCP port 23 (telnet) and tcp portrange 2066-2100) So my syntax in &quot;Capture options&quot; &quot;Capture filter&quot; field looks like this: tcp dst port 23 and tcp dst...'''
date = "2012-06-26T06:59:00Z"
lastmod = "2012-06-26T07:08:00Z"
weight = 12176
keywords = [ "capture-filter", "traffic", "telnet" ]
aliases = [ "/questions/12176" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter, tcp port and tcp portrange](/questions/12176/capture-filter-tcp-port-and-tcp-portrange)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12176-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys :)</p><p>I'm looking for a help. I have a problem with capture filter configuration.</p><p>I want to capture just a traffic from specific tcp ports. (TCP port 23 (telnet) and tcp portrange 2066-2100)</p><p>So my syntax in "Capture options" "Capture filter" field looks like this:</p><p>tcp dst port 23 and tcp dst portrange 2066-2100</p><p>and there is no capture with this command!</p><p>If I use just "tcp dst port 23" or just "tcp dst portrange 2066-2100" as a filter, I can see the output, but I can't get these filters to work together as one. Where is a problem?</p><p>Thank you for your time and for your answers. Any helpful information is highly appreciated.</p></div><div id="question-tags" class="tags-container tags">capture-filter traffic telnet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '12, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/f697d55a7a5a16d8e1582edceda33c15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jomajo&#39;s gravatar image" /><p>jomajo<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jomajo has one accepted answer">100%</span></p></div></div><div id="comments-container-12176" class="comments-container"></div><div id="comment-tools-12176" class="comment-tools"></div><div class="clear"></div><div id="comment-12176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12178"></span>

<div id="answer-container-12178" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12178-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know why, but this is working:</p><p>tcp dst portrange 2066-2100 or tcp dst port 23</p><p>:)</p><p>Oh thanks, I saw I have an answer too :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/f697d55a7a5a16d8e1582edceda33c15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jomajo&#39;s gravatar image" /><p>jomajo<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jomajo has one accepted answer">100%</span></p></div></div><div id="comments-container-12178" class="comments-container"><span id="12180"></span><div id="comment-12180" class="comment"><div id="post-12180-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I don't know why, but this is working</p></blockquote><p>see the answer of Bill Meier. <strong>OR</strong> is the key. Reason: The destination port cannot be 23 AND in the range of 2066-2100 (at the same time).</p></div><div id="comment-12180-info" class="comment-info"><span class="comment-age">(26 Jun '12, 07:39)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12178" class="comment-tools"></div><div class="clear"></div><div id="comment-12178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12177"></span>

<div id="answer-container-12177" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12177-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use ... <strong>or</strong> ...</p><p><strong>and</strong> means both conditions must be satisfied which is not going to happen if the conditions are exclusive ....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jun '12, 07:09</p></div></div><div id="comments-container-12177" class="comments-container"></div><div id="comment-tools-12177" class="comment-tools"></div><div class="clear"></div><div id="comment-12177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

