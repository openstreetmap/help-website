+++
type = "question"
title = "How can I find the total data bytes sent over TCP connection excluding headers?"
description = '''Is there anyway in wireshark to do this easily? I hope it&#x27;s not something simple that I keep missing. I just need to be able to find the total number of data bytes sent of a TCP connection excluding the headers. '''
date = "2012-04-23T15:01:00Z"
lastmod = "2012-04-23T15:26:00Z"
weight = 10412
keywords = [ "databytes", "data", "tcp" ]
aliases = [ "/questions/10412" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I find the total data bytes sent over TCP connection excluding headers?](/questions/10412/how-can-i-find-the-total-data-bytes-sent-over-tcp-connection-excluding-headers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10412-score" class="post-score" title="current number of votes">0</div><span id="post-10412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there anyway in wireshark to do this easily? I hope it's not something simple that I keep missing. I just need to be able to find the total number of data bytes sent of a TCP connection excluding the headers.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-databytes" rel="tag" title="see questions tagged &#39;databytes&#39;">databytes</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '12, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/de1e752e6c999324c83795c3876e6d08?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PandaSlanda&#39;s gravatar image" /><p><span>PandaSlanda</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PandaSlanda has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '12, 15:02</strong> </span></p></div></div><div id="comments-container-10412" class="comments-container"></div><div id="comment-tools-10412" class="comment-tools"></div><div class="clear"></div><div id="comment-10412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10413"></span>

<div id="answer-container-10413" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10413-score" class="post-score" title="current number of votes">0</div><span id="post-10413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to know how much payload data was sent in a TCP connection, you can look at the sequence number in each direction.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '12, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-10413" class="comments-container"></div><div id="comment-tools-10413" class="comment-tools"></div><div class="clear"></div><div id="comment-10413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

