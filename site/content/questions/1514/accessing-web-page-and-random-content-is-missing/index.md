+++
type = "question"
title = "accessing web page and random content is missing"
description = '''I am trying to establish a cause for this. I have two sites I get partial loads with different content missing. An example would be that sometimes the CSS file fails to be applied on some loads but not others. Another example would be that 6 out the ten images will fail to display but if I reload th...'''
date = "2010-12-29T09:20:00Z"
lastmod = "2010-12-29T11:13:00Z"
weight = 1514
keywords = [ "content", "random", "missing" ]
aliases = [ "/questions/1514" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [accessing web page and random content is missing](/questions/1514/accessing-web-page-and-random-content-is-missing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1514-score" class="post-score" title="current number of votes">0</div><span id="post-1514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to establish a cause for this. I have two sites I get partial loads with different content missing. An example would be that sometimes the CSS file fails to be applied on some loads but not others. Another example would be that 6 out the ten images will fail to display but if I reload the page 4 random images will not display. I am trying to prove that my ISP could be causing this as I have the same issue at home (Same ISP) and if I use my VPN I do not have the same issue. I am trying to establish whether my browsers requests for the content are firstly successful and secondly receiving the appropriate response. I see no failures in my capture does this imply that all requests are being met?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-content" rel="tag" title="see questions tagged &#39;content&#39;">content</span> <span class="post-tag tag-link-random" rel="tag" title="see questions tagged &#39;random&#39;">random</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '10, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/537cdf147df5455a04ee0f16700700cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silark&#39;s gravatar image" /><p><span>silark</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silark has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Dec '10, 09:21</strong> </span></p></div></div><div id="comments-container-1514" class="comments-container"></div><div id="comment-tools-1514" class="comment-tools"></div><div class="clear"></div><div id="comment-1514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1517"></span>

<div id="answer-container-1517" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1517-score" class="post-score" title="current number of votes">0</div><span id="post-1517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark isn't an http parser. To wireshark, not having consistent cache-controls (which sounds like your problem) isn't an error. Since http uses TCP, pkt loss would not exhibit the behavior that you are seeing. Two ways to go about it are: 1) Use http analyzers available on the web (HTTP Analyzer, Fiddler etc) 2) Use "follow tcp stream" and look at all the http semantics to see if something is not right. You can also try using Statistics, HTTP option to see if that helps.</p><p>My guess is that cache controls are inconsistent.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '10, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-1517" class="comments-container"></div><div id="comment-tools-1517" class="comment-tools"></div><div class="clear"></div><div id="comment-1517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

