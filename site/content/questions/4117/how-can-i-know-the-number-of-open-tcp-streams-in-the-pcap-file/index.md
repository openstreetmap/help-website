+++
type = "question"
title = "How can I know the number of open TCP streams in the pcap file?"
description = '''How can I know the number of open TCP streams in the pcap file?'''
date = "2011-05-18T04:23:00Z"
lastmod = "2011-05-18T09:39:00Z"
weight = 4117
keywords = [ "streams", "tcp" ]
aliases = [ "/questions/4117" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I know the number of open TCP streams in the pcap file?](/questions/4117/how-can-i-know-the-number-of-open-tcp-streams-in-the-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4117-score" class="post-score" title="current number of votes">0</div><span id="post-4117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I know the number of open TCP streams in the pcap file?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-streams" rel="tag" title="see questions tagged &#39;streams&#39;">streams</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '11, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/99b41a39263cf4a387d2381d86207684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlexLA&#39;s gravatar image" /><p><span>AlexLA</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlexLA has no accepted answers">0%</span></p></div></div><div id="comments-container-4117" class="comments-container"><span id="4118"></span><div id="comment-4118" class="comment"><div id="post-4118-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "open"? TCP stream that are still ongoing when the trace ended, or just any connection that had data transfers?</p></div><div id="comment-4118-info" class="comment-info"><span class="comment-age">(18 May '11, 05:13)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-4117" class="comment-tools"></div><div class="clear"></div><div id="comment-4117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4122"></span>

<div id="answer-container-4122" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4122-score" class="post-score" title="current number of votes">2</div><span id="post-4122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you just want to know how many TCP streams are in a pcap file you can use the Conversations Statistics and look at the number given on the TCP tab.</p><p>If you then want to find out how many TCP streams are still open at the end of the trace file you need to find out how many of the total TCP streams have terminated within the trace file. Filter for <code>tcp.flags.reset==1 or tcp.flags.fin==1</code> and open the conversation statistics again, select the "Limit to display filter" option at the bottom and take a look at how many TCP conversations are left. This the number of streams that have been terminated either with a reset packet or a fin packet. Substract that number from your total stream count and you should be done.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '11, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4122" class="comments-container"></div><div id="comment-tools-4122" class="comment-tools"></div><div class="clear"></div><div id="comment-4122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

