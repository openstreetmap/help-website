+++
type = "question"
title = "Utility to &quot;anonymize&quot; capture files?"
description = '''I often run across capture data that would make excellent teaching aids, but (for obvious reasons) I am not allowed to use &quot;real customer&quot; data for such purposes. Does anyone know of a pcap editor that would allow me to do things like arbitrary search-and-replace of IP/MAC addresses, obfuscate URLs ...'''
date = "2010-11-06T22:45:00Z"
lastmod = "2010-11-08T20:14:00Z"
weight = 844
keywords = [ "teaching", "utilities" ]
aliases = [ "/questions/844" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Utility to "anonymize" capture files?](/questions/844/utility-to-anonymize-capture-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-844-score" class="post-score" title="current number of votes">1</div><span id="post-844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I often run across capture data that would make excellent teaching aids, but (for obvious reasons) I am not allowed to use "real customer" data for such purposes. Does anyone know of a pcap editor that would allow me to do things like arbitrary search-and-replace of IP/MAC addresses, obfuscate URLs (like changing "GET /real/file/path/here.htm" to "GET /dead/beef/feed/blah.htm", and the like?</p><p>I REALLY don't want to break out the old binary file editor...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-teaching" rel="tag" title="see questions tagged &#39;teaching&#39;">teaching</span> <span class="post-tag tag-link-utilities" rel="tag" title="see questions tagged &#39;utilities&#39;">utilities</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '10, 22:45</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-844" class="comments-container"></div><div id="comment-tools-844" class="comment-tools"></div><div class="clear"></div><div id="comment-844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="847"></span>

<div id="answer-container-847" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-847-score" class="post-score" title="current number of votes">1</div><span id="post-847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wesmorgan1 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For Ethernet, IP, and TCP portion, you can use "bittwist" The only thing it can't handle is dot1q headers. So for that, I actually just use UltraEdit (or any other hex capable editor) to nuke the dot1q header.</p><p>I can't help you on munging the HTTP part, though.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '10, 09:06</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></p></div></div><div id="comments-container-847" class="comments-container"><span id="868"></span><div id="comment-868" class="comment"><div id="post-868-score" class="comment-score"></div><div class="comment-text"><p>I think bittwiste (note the 'e' at the end) is what Hansang is referring to. See bittwist.sourceforge.net for both Bittwist and Bittwiste information.</p><p>I'd avoid a binary file editor, but consider a hex editor - if you don't care about the checksums being recalculated you can do some search/replace operations throughout the trace file and catch the IP addresses embedded past the IP header as well.</p></div><div id="comment-868-info" class="comment-info"><span class="comment-age">(08 Nov '10, 20:14)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div></div><div id="comment-tools-847" class="comment-tools"></div><div class="clear"></div><div id="comment-847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

