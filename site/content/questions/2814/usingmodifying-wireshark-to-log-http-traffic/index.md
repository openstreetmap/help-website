+++
type = "question"
title = "Using/Modifying WireShark to log http traffic"
description = '''I am new to wireshark - please can you let me know if it is possible to use or modify wireshark to run on a system and log all outgoing http traffic.  Does this feature already exist or would Wireshark need to be modified to make this happen. Please advise. Thanks MG'''
date = "2011-03-14T20:42:00Z"
lastmod = "2011-03-15T00:56:00Z"
weight = 2814
keywords = [ "sniffer", "http", "log" ]
aliases = [ "/questions/2814" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using/Modifying WireShark to log http traffic](/questions/2814/usingmodifying-wireshark-to-log-http-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2814-score" class="post-score" title="current number of votes">0</div><span id="post-2814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to wireshark - please can you let me know if it is possible to use or modify wireshark to run on a system and log all outgoing http traffic. Does this feature already exist or would Wireshark need to be modified to make this happen. Please advise. Thanks MG</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffer" rel="tag" title="see questions tagged &#39;sniffer&#39;">sniffer</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-log" rel="tag" title="see questions tagged &#39;log&#39;">log</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '11, 20:42</strong></p><img src="https://secure.gravatar.com/avatar/11daa7ada94a04c8bd053fc8c85e4ad8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gotters&#39;s gravatar image" /><p><span>gotters</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gotters has no accepted answers">0%</span></p></div></div><div id="comments-container-2814" class="comments-container"></div><div id="comment-tools-2814" class="comment-tools"></div><div class="clear"></div><div id="comment-2814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2817"></span>

<div id="answer-container-2817" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2817-score" class="post-score" title="current number of votes">0</div><span id="post-2817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can do that, simply by capturing the network traffic which would include HTTP traffic. You might want to use capture filters to limit the capture to http traffic only, for example using "<code>tcp port http</code>" and writing the files to disk using multiple files. You can do that by opening the capture options dialog. Reading the recorded trace might be a bit more complex than reading a "normal" log file, but you can export all packets to text files if you want to, or even reconstruct http content.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '11, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2817" class="comments-container"></div><div id="comment-tools-2817" class="comment-tools"></div><div class="clear"></div><div id="comment-2817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

