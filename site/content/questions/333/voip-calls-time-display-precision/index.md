+++
type = "question"
title = "VoIP Calls time display precision"
description = '''VoIp calls display under Telephony-&amp;gt;VoIP (on windows) rounds of the  start/stop time to the nearest millisecond. Is there a easy way to increase the precision to microseconds. Looking at the gtk/voip_calls.[ch] it looks like the data is there. any pointer to where the actual display string is for...'''
date = "2010-09-26T08:39:00Z"
lastmod = "2010-11-10T06:47:00Z"
weight = 333
keywords = [ "gtk", "voip" ]
aliases = [ "/questions/333" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [VoIP Calls time display precision](/questions/333/voip-calls-time-display-precision)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-333-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>VoIp calls display under Telephony-&gt;VoIP (on windows) rounds of the start/stop time to the nearest millisecond. Is there a easy way to increase the precision to microseconds.</p><p>Looking at the gtk/voip_calls.[ch] it looks like the data is there.</p><p>any pointer to where the actual display string is formatted ? And how to include the microsecond resolution in the 'graph' of VoIP calls?</p><p>Thanks Ramesh</p></div><div id="question-tags" class="tags-container tags">gtk voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '10, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/2fd3f495998c7891a4cc725c573ee03a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ramekris&#39;s gravatar image" /><p>ramekris<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ramekris has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Nov '10, 06:47</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-333" class="comments-container"></div><div id="comment-tools-333" class="comment-tools"></div><div class="clear"></div><div id="comment-333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="893"></span>

<div id="answer-container-893" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-893-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I haven't experimented with this but it looks like you'll have to work on the cell renderer.</p><pre><code>/* Start Time */
renderer = gtk_cell_renderer_text_new();
....
column = gtk_tree_view_column_new_with_attributes(&quot;Start Time&quot;, renderer,
    &quot;text&quot;, CALL_COL_START_TIME, 
    NULL);</code></pre><p>It seems that, according to <a href="http://scentric.net/tutorial/sec-treeview-celltext-types.html">this tutorial</a>, the renderer makes up its own mind on precision. To get a grip on that a Cell Data Function seems required, again according to <a href="http://scentric.net/tutorial/sec-treeview-col-celldatafunc.html">this tutorial</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '10, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-893" class="comments-container"></div><div id="comment-tools-893" class="comment-tools"></div><div class="clear"></div><div id="comment-893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

