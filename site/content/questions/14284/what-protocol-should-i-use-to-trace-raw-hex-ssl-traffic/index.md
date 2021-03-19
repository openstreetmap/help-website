+++
type = "question"
title = "What protocol should I use to trace raw hex SSL traffic?"
description = '''I&#x27;m tracing three IP addresses. Address A and Address B communicate with each other using HTTPS. Address C and B communicate with each other using raw packets that are encrypted using the same certificate as the other two. Address A and C are servers. My question is, when I configure Wireshark for S...'''
date = "2012-09-14T16:28:00Z"
lastmod = "2012-09-16T12:00:00Z"
weight = 14284
keywords = [ "data", "hex", "protocol", "ssl" ]
aliases = [ "/questions/14284" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What protocol should I use to trace raw hex SSL traffic?](/questions/14284/what-protocol-should-i-use-to-trace-raw-hex-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14284-score" class="post-score" title="current number of votes">0</div><span id="post-14284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm tracing three IP addresses. Address A and Address B communicate with each other using HTTPS. Address C and B communicate with each other using raw packets that are encrypted using the same certificate as the other two. Address A and C are servers. My question is, when I configure Wireshark for SSL packets using the "SSL Decrypt Edit" form, <strong>what do I enter in the "protocol" field to trace hex data?</strong></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-hex" rel="tag" title="see questions tagged &#39;hex&#39;">hex</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '12, 16:28</strong></p><img src="https://secure.gravatar.com/avatar/90ace4ca58ca53e9c64e6713d5950cf2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tcoder&#39;s gravatar image" /><p><span>tcoder</span><br />
<span class="score" title="0 reputation points">0</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tcoder has no accepted answers">0%</span></p></div></div><div id="comments-container-14284" class="comments-container"></div><div id="comment-tools-14284" class="comment-tools"></div><div class="clear"></div><div id="comment-14284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14288"></span>

<div id="answer-container-14288" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14288-score" class="post-score" title="current number of votes">0</div><span id="post-14288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can enter "data" as protocol, this will make Wireshark not interpret the decrypted data as any protocol, but it will just be shown as "data".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '12, 23:46</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14288" class="comments-container"><span id="14305"></span><div id="comment-14305" class="comment"><div id="post-14305-score" class="comment-score"></div><div class="comment-text"><p>Thanks! Just what I needed.</p></div><div id="comment-14305-info" class="comment-info"><span class="comment-age">(16 Sep '12, 12:00)</span> <span class="comment-user userinfo">tcoder</span></div></div></div><div id="comment-tools-14288" class="comment-tools"></div><div class="clear"></div><div id="comment-14288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

