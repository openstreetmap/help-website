+++
type = "question"
title = "correlating traces"
description = '''Hello, I need to correlate 2 separate traces, one taken on my network and the other on my client&#x27;s network. There are packet drops and retransmissions in between our networks , with at least a half dozen of the client&#x27;s switches/routers before my end-point router on the client&#x27;s network. Is there an...'''
date = "2014-12-05T13:59:00Z"
lastmod = "2014-12-06T16:01:00Z"
weight = 38376
keywords = [ "compare_two_traces" ]
aliases = [ "/questions/38376" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [correlating traces](/questions/38376/correlating-traces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38376-score" class="post-score" title="current number of votes">0</div><span id="post-38376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I need to correlate 2 separate traces, one taken on my network and the other on my client's network. There are packet drops and retransmissions in between our networks , with at least a half dozen of the client's switches/routers before my end-point router on the client's network. Is there an article/tutorial/youtube/Sharkfest presentation that can assist me? Thanks<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compare_two_traces" rel="tag" title="see questions tagged &#39;compare_two_traces&#39;">compare_two_traces</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '14, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/5f5299714626c91721c62ac2e42793e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IND&#39;s gravatar image" /><p><span>IND</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IND has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-38376" class="comments-container"></div><div id="comment-tools-38376" class="comment-tools"></div><div class="clear"></div><div id="comment-38376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38382"></span>

<div id="answer-container-38382" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38382-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38382-score" class="post-score" title="current number of votes">1</div><span id="post-38382-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are they the same exact session captured at these two locations?</p><p>If so, one way would be</p><ul><li>Zoom in on one session (eg: right-click and 'follow TCP session') in one trace file</li><li>Go to file -&gt; 'export specified packets' and save it as its own capture file.</li><li>Do the same from the second trace you're comparing.</li><li>Open one of the session-specific capture files, and hit ctrl+shift+m to 'mark' all the packets in that trace.</li><li>Go to File -&gt; Merge and merge the two traces together. Sort them chronologically (default)</li></ul><p>From that, you should have an apples-to-apples comparison where two complete sets of the packets relating to that session are in one file, with one file's packets "marked" and the other's not. At this level you can (for example) right-click the IP ID field of an IP header and add it as a column, looking for any lack of duplicates. You could also look at the protocol stats with 'frame.marked==1' compared to '!frame.marked==1', or put those two into an IO graph and compare any criteria you want for these traces.</p><p>Could you possibly upload the trace files and post the URL (if the data isn't confidential)?: <a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '14, 16:42</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Dec '14, 16:43</strong> </span></p></div></div><div id="comments-container-38382" class="comments-container"><span id="38400"></span><div id="comment-38400" class="comment"><div id="post-38400-score" class="comment-score"></div><div class="comment-text"><p>Thank you, let me work with your recommendation.Ivan</p></div><div id="comment-38400-info" class="comment-info"><span class="comment-age">(06 Dec '14, 16:01)</span> <span class="comment-user userinfo">IND</span></div></div></div><div id="comment-tools-38382" class="comment-tools"></div><div class="clear"></div><div id="comment-38382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

