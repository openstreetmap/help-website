+++
type = "question"
title = "No Data indication is it possible ?"
description = '''I am running some tests and need a quick visual indication. I have set up a display filter for the correct ip, i have also set a display colour for packets arriving over the specified time frame. What I want to do is display a colour or other alert if data stops completely. Example:  Data is coming ...'''
date = "2012-09-17T08:52:00Z"
lastmod = "2012-09-17T14:07:00Z"
weight = 14322
keywords = [ "data", "no" ]
aliases = [ "/questions/14322" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No Data indication is it possible ?](/questions/14322/no-data-indication-is-it-possible)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14322-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running some tests and need a quick visual indication.</p><p>I have set up a display filter for the correct ip, i have also set a display colour for packets arriving over the specified time frame.</p><p>What I want to do is display a colour or other alert if data stops completely.</p><p>Example: Data is coming in on filtered ip. (done this) A red line is shown when a packet arrives late (my time specified) (done this)</p><p>If data was coming in good and then stops, nothing happens until the next frame which catches the late packet. If the data has stopped and never restarts i will never get the red late capture and will be presented with just the captures made.</p><p>My reason for this is EMC testing by a non familiar user who need s to see a late packet (sorted) or if the data stops completely. They will not be familiar with wireshark.</p><p>Is it possible to add some kind of display filter to state if no next packet in x time then show red. At present the</p><p>frame.time_delta_displayed&gt;1 will only show when a packet does arrrive.</p><p>Hope this makes sense.</p><p>Regards</p><p>James</p></div><div id="question-tags" class="tags-container tags">data no</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '12, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/2629df170edb7fdb128f232e14e853d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="console&#39;s gravatar image" /><p>console<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="console has no accepted answers">0%</span></p></div></div><div id="comments-container-14322" class="comments-container"></div><div id="comment-tools-14322" class="comment-tools"></div><div class="clear"></div><div id="comment-14322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14339"></span>

<div id="answer-container-14339" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14339-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As Wireshark is just a network capture and dissection application, it's not cut out for performance monitoring as you require</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '12, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-14339" class="comments-container"><span id="14344"></span><div id="comment-14344" class="comment"><div id="post-14344-score" class="comment-score"></div><div class="comment-text"><p>Do you have any suggestions for free performance monitoring programs ?</p></div><div id="comment-14344-info" class="comment-info"><span class="comment-age">(18 Sep '12, 04:09)</span> console</div></div></div><div id="comment-tools-14339" class="comment-tools"></div><div class="clear"></div><div id="comment-14339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

