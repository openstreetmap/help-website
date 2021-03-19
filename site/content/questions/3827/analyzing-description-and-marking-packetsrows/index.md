+++
type = "question"
title = "analyzing, description - and marking packets/rows"
description = '''Hi...I&#x27;m back. :) Now I&#x27;m analyzing and describing protocol(s) traffic for purpose of my thesis/diploma. When a few rows are &quot;over&quot;, I&#x27;d like to mark a few packets (rows) at once. How can I do that? Combination of pressing and holding key CTRL while trying to mark more rows at once doesn&#x27;t work. BrT...'''
date = "2011-04-29T17:51:00Z"
lastmod = "2011-04-29T18:34:00Z"
weight = 3827
keywords = [ "analyze", "row", "description", "packet", "mark" ]
aliases = [ "/questions/3827" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [analyzing, description - and marking packets/rows](/questions/3827/analyzing-description-and-marking-packetsrows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3827-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi...I'm back. :)</p><p>Now I'm analyzing and describing protocol(s) traffic for purpose of my thesis/diploma. When a few rows are "over", I'd like to mark a few packets (rows) at once. How can I do that?</p><p>Combination of pressing and holding key CTRL while trying to mark more rows at once doesn't work.</p><p>BrT.</p></div><div id="question-tags" class="tags-container tags">analyze row description packet mark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '11, 17:51</strong></p><img src="https://secure.gravatar.com/avatar/13231e33ab17a93476f7b98c9d5b272a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wired&#39;s gravatar image" /><p>wired<br />
<span class="score" title="44 reputation points">44</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wired has one accepted answer">9%</span></p></div></div><div id="comments-container-3827" class="comments-container"><span id="3828"></span><div id="comment-3828" class="comment"><div id="post-3828-score" class="comment-score"></div><div class="comment-text"><p>p.s.: And I don't want to mark ALL of the packets/rows in file.</p></div><div id="comment-3828-info" class="comment-info"><span class="comment-age">(29 Apr '11, 17:53)</span> wired</div></div></div><div id="comment-tools-3827" class="comment-tools"></div><div class="clear"></div><div id="comment-3827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3834"></span>

<div id="answer-container-3834" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3834-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>AFAIK, the GUI allows marking multiple displayed packets at once, so just use a display filter for the packets of interest and then mark all.</p><p>For example, to mark rows/packets/frames 30 to 37:</p><ol><li>Enter <strong><code>frame.number &gt;= 30 &amp;&amp; frame.number &lt;= 37</code></strong> into the display filter textbox, and click <strong>Apply</strong>.</li><li>Press <strong><code>Shift+Ctrl+M</code></strong> (or use menu "Edit &gt; Mark All Displayed Packets")</li></ol><p>After marking, you can return to your previous packet perusal by clearing the display filter (i.e., click <strong>Clear</strong>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '11, 18:34</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-3834" class="comments-container"><span id="3835"></span><div id="comment-3835" class="comment"><div id="post-3835-score" class="comment-score"></div><div class="comment-text"><p>It works, but it's not pretty convenient because I'm analyzing step-by-step, row by row...well, better than nothing. (I'm marking to be sure what's already analyzed...and, when opening a file again, it's not marked anymore. :-()</p></div><div id="comment-3835-info" class="comment-info"><span class="comment-age">(29 Apr '11, 18:36)</span> wired</div></div><span id="3836"></span><div id="comment-3836" class="comment"><div id="post-3836-score" class="comment-score"></div><div class="comment-text"><p>The packet marks are not stored in the capture file or anywhere else, so all packet marks will be lost if you close the capture file.<br />
See <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkMarkPacketSection.html">Wireshark User's Guide:</a></p></div><div id="comment-3836-info" class="comment-info"><span class="comment-age">(29 Apr '11, 23:55)</span> joke</div></div><span id="3840"></span><div id="comment-3840" class="comment"><div id="post-3840-score" class="comment-score"></div><div class="comment-text"><p>Something what should be implemented in next version(s) of Wireshark.</p></div><div id="comment-3840-info" class="comment-info"><span class="comment-age">(30 Apr '11, 02:39)</span> wired</div></div><span id="3843"></span><div id="comment-3843" class="comment"><div id="post-3843-score" class="comment-score"></div><div class="comment-text"><p>Perhaps you should add it to the <a href="http://wiki.wireshark.org/WishList">Wireshark WishList</a></p></div><div id="comment-3843-info" class="comment-info"><span class="comment-age">(30 Apr '11, 10:41)</span> joke</div></div><span id="3847"></span><div id="comment-3847" class="comment"><div id="post-3847-score" class="comment-score"></div><div class="comment-text"><p>Or you could submit an enhancement bug request for it. Speaking of enhancement bug requests, <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3059">bug 3059</a> was submitted awhile ago for being able to mark multiple frames in a range at once. I haven't looked at it in awhile, but I don't think the patch was in a state suitable for inclusion at the time. Maybe someone who is interested in this feature can work on improving it so it could be included ...</p></div><div id="comment-3847-info" class="comment-info"><span class="comment-age">(30 Apr '11, 12:35)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-3834" class="comment-tools"></div><div class="clear"></div><div id="comment-3834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

