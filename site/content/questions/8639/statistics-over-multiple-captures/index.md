+++
type = "question"
title = "Statistics over multiple captures"
description = '''Is there a simple way to grab statistics from multiple captures without having to merge them into a single capture file? In particular I want to generate statistics from Protocol Hierarchy and HTTP Packet Counter. I&#x27;ve been able to do this with tshark using  tshark -q -z http,tree -z io,phs -r file....'''
date = "2012-01-26T15:13:00Z"
lastmod = "2012-01-26T15:13:00Z"
weight = 8639
keywords = [ "multiple-files", "merge", "statistics", "tshark" ]
aliases = [ "/questions/8639" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Statistics over multiple captures](/questions/8639/statistics-over-multiple-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8639-score" class="post-score" title="current number of votes">0</div><span id="post-8639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a simple way to grab statistics from multiple captures without having to merge them into a single capture file? In particular I want to generate statistics from Protocol Hierarchy and HTTP Packet Counter. I've been able to do this with tshark using</p><pre><code>tshark -q -z http,tree -z io,phs -r file.cap.gz</code></pre><p>but it only works for a single file. I've been merging them, but now my merged files are big enough to cause OutOfMemory errors. So is there a way to grab statistics over all the files like this? Or do I need to run the statistics on each capture separately and combine the results myself?</p><p>Thanks for any insights!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multiple-files" rel="tag" title="see questions tagged &#39;multiple-files&#39;">multiple-files</span> <span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '12, 15:13</strong></p><img src="https://secure.gravatar.com/avatar/52c6078760d2bc4d0238604270db8186?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eHalcyon&#39;s gravatar image" /><p><span>eHalcyon</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eHalcyon has no accepted answers">0%</span></p></div></div><div id="comments-container-8639" class="comments-container"></div><div id="comment-tools-8639" class="comment-tools"></div><div class="clear"></div><div id="comment-8639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

