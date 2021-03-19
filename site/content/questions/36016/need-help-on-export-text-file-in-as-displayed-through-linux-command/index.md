+++
type = "question"
title = "Need help on export text file in &quot;as displayed&quot; through linux command"
description = '''Hi  I am using the command &quot;tshark output.pcap -V -r &amp;gt; output.txt&quot; to convert the file from pcap to text.But the display it is coming in &quot;All expanded&quot; format. I want to convert pcap to text file with packet details as &quot;As dispalyed&quot; format using tshark command.'''
date = "2014-09-04T23:54:00Z"
lastmod = "2014-09-05T00:36:00Z"
weight = 36016
keywords = [ "tshark" ]
aliases = [ "/questions/36016" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need help on export text file in "as displayed" through linux command](/questions/36016/need-help-on-export-text-file-in-as-displayed-through-linux-command)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36016-score" class="post-score" title="current number of votes">0</div><span id="post-36016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I am using the command "tshark output.pcap -V -r &gt; output.txt" to convert the file from pcap to text.But the display it is coming in "All expanded" format.</p><p>I want to convert pcap to text file with packet details as "As dispalyed" format using tshark command.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '14, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/7343ee112ff5ce3e89c692e5b9acdf93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ramkumarbarai&#39;s gravatar image" /><p><span>ramkumarbarai</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ramkumarbarai has no accepted answers">0%</span></p></div></div><div id="comments-container-36016" class="comments-container"></div><div id="comment-tools-36016" class="comment-tools"></div><div class="clear"></div><div id="comment-36016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36018"></span>

<div id="answer-container-36018" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36018-score" class="post-score" title="current number of votes">0</div><span id="post-36018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TShark is a command-line program, not a GUI program, so it has no display and can't export "as displayed", because there's no "displayed" to show; Wireshark doesn't save the list of items it's opened for use by TShark later, so TShark can't write out a text file in the form that Wireshark last displayed.</p><p>The only thing you can do is use the -O flag rather than the -V flag; the -O flag takes a comma-separated list of protocol abbreviation names, and opens up the items for those protocols.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Sep '14, 00:36</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-36018" class="comments-container"></div><div id="comment-tools-36018" class="comment-tools"></div><div class="clear"></div><div id="comment-36018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

