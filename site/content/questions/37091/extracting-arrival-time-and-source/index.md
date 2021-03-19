+++
type = "question"
title = "Extracting Arrival Time and Source"
description = '''I have managed to get a reasonable specific capture filter working and now I need to get some very specific information out of the results. My Capture filter limits the traffic to a specific TCP port. How can I write out to something like a CSV file, just the following 2 fields (although they are fr...'''
date = "2014-10-15T20:22:00Z"
lastmod = "2014-10-16T06:09:00Z"
weight = 37091
keywords = [ "output", "tcp" ]
aliases = [ "/questions/37091" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Extracting Arrival Time and Source](/questions/37091/extracting-arrival-time-and-source)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37091-score" class="post-score" title="current number of votes">0</div><span id="post-37091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have managed to get a reasonable specific capture filter working and now I need to get some very specific information out of the results.</p><p>My Capture filter limits the traffic to a specific TCP port.</p><p>How can I write out to something like a CSV file, just the following 2 fields (although they are from different data levels):</p><ul><li><strong>Arrival Time</strong> from <strong>Frame</strong></li><li><strong>Source</strong> from <strong>Internet Protocol Version 4</strong></li></ul><p>Thanks in anticipation.</p><p>Alan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-output" rel="tag" title="see questions tagged &#39;output&#39;">output</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '14, 20:22</strong></p><img src="https://secure.gravatar.com/avatar/92842ce17eefb295c4cc52fe99ffc086?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alan%20Eth&#39;s gravatar image" /><p><span>Alan Eth</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alan Eth has no accepted answers">0%</span></p></div></div><div id="comments-container-37091" class="comments-container"></div><div id="comment-tools-37091" class="comment-tools"></div><div class="clear"></div><div id="comment-37091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37107"></span>

<div id="answer-container-37107" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37107-score" class="post-score" title="current number of votes">0</div><span id="post-37107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alan Eth has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Using tshark, have a look at the <code>-T fields and -e fieldname</code> options, i.e.<code>-T fields -e frame.time -e ip.src</code>. The field names for the -e options are display filter field names which can be easily determined using Wireshark by inspecting the field in the packet details display and looking at the field info at the bottom left of the status bar where the filter name is in parentheses.</p><p>If you want to do this using Wireshark, you will have to arrange that only the required columns are on display, then from the menu select File | Export Packet Dissections | As CSV, and in the options dialog uncheck "Packet details".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '14, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37107" class="comments-container"></div><div id="comment-tools-37107" class="comment-tools"></div><div class="clear"></div><div id="comment-37107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

