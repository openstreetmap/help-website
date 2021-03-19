+++
type = "question"
title = "Web page content"
description = '''How can I know that all content of a web page has been fetched using Wireshark?'''
date = "2011-05-19T14:29:00Z"
lastmod = "2011-06-02T06:59:00Z"
weight = 4152
keywords = [ "http" ]
aliases = [ "/questions/4152" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Web page content](/questions/4152/web-page-content)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4152-score" class="post-score" title="current number of votes">0</div><span id="post-4152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I know that all content of a web page has been fetched using Wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '11, 14:29</strong></p><img src="https://secure.gravatar.com/avatar/0d1f835bfa8cc91838057ef65fc4d1c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="A%20B&#39;s gravatar image" /><p><span>A B</span><br />
<span class="score" title="1 reputation points">1</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="A B has no accepted answers">0%</span></p></div></div><div id="comments-container-4152" class="comments-container"></div><div id="comment-tools-4152" class="comment-tools"></div><div class="clear"></div><div id="comment-4152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4332"></span>

<div id="answer-container-4332" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4332-score" class="post-score" title="current number of votes">0</div><span id="post-4332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you use <em>host</em> as a capture filter, and you were say redirected from the initial site to another site, you would lose the redirected traffic. If you use capture filter <em>port 80</em> though, you would capture all the http traffic, assuming you are using port 80 and not https or port 443.<br />
Filter using the MAC address to ensure you get <em>all</em> traffic, including traffic which doesn't have IP headers like ARP, to and from the test system.</p><p>Hope this is helpful,</p><p>John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '11, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-4332" class="comments-container"></div><div id="comment-tools-4332" class="comment-tools"></div><div class="clear"></div><div id="comment-4332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

