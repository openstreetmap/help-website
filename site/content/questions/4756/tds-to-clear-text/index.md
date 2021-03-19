+++
type = "question"
title = "TDS to clear-text"
description = '''Hi, I want to convert a TDS stream to clear-text or similar. Does anyone have a hint how to solve this? /Stef'''
date = "2011-06-26T01:48:00Z"
lastmod = "2011-06-27T07:47:00Z"
weight = 4756
keywords = [ "tds", "ms-sql-s", "1433", "tcp" ]
aliases = [ "/questions/4756" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TDS to clear-text](/questions/4756/tds-to-clear-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4756-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to convert a TDS stream to clear-text or similar. Does anyone have a hint how to solve this?</p><p>/Stef</p></div><div id="question-tags" class="tags-container tags">tds ms-sql-s 1433 tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '11, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/47133309c7463618993903d614f7312d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stefan741&#39;s gravatar image" /><p>stefan741<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stefan741 has no accepted answers">0%</span></p></div></div><div id="comments-container-4756" class="comments-container"></div><div id="comment-tools-4756" class="comment-tools"></div><div class="clear"></div><div id="comment-4756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4764"></span>

<div id="answer-container-4764" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4764-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>When I view SQL data, which is transmitted via TDS, (Tabular Data Stream protocol), I am able to view the text by 1st selecting the Stream, (right click on one of the packets in the stream, then "Follow TCP Stream", then select "Hex Dump" as the format option in the bottom right of the TCP Stream window. The TCP Stream window includes hexidecimal data and on the right shows the text conversion of the data as you scroll down.</p><p>Hope this is helpful,</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '11, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p>John_Modlin<br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div></div><div id="comments-container-4764" class="comments-container"><span id="4765"></span><div id="comment-4765" class="comment"><div id="post-4765-score" class="comment-score"></div><div class="comment-text"><p>Okay, thats what I got too (I guess). But it actually still seems to be a mess. I would like to extract either just the table content or some kind of structured output (tables + content).</p></div><div id="comment-4765-info" class="comment-info"><span class="comment-age">(27 Jun '11, 06:16)</span> stefan741</div></div></div><div id="comment-tools-4764" class="comment-tools"></div><div class="clear"></div><div id="comment-4764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4768"></span>

<div id="answer-container-4768" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4768-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>While not completely formatted, you can use use the TDS display filter, then Edit Menu, Mark All Displayed Packets, then File | Print, Output to File, Packet Format: "Packet Bytes" only, deselect Packet Summary line and Packet details. This will create a text file without the summary header information, only the bytes. This still isn't columnized like SQL records. LUA might be helpful, but I haven't played that much with LUA to advise more.</p><p>Hope this helps some,</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '11, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p>John_Modlin<br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div></div><div id="comments-container-4768" class="comments-container"></div><div id="comment-tools-4768" class="comment-tools"></div><div class="clear"></div><div id="comment-4768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

