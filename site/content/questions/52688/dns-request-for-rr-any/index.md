+++
type = "question"
title = "DNS request for RR &quot;ANY&quot;"
description = '''I&#x27;ve seen a trace where the DNS resolver asks for &quot;ANY&quot; information from the name server. Any idea about the practical case for such request ? In which context does this happen ?'''
date = "2016-05-17T12:48:00Z"
lastmod = "2016-05-17T12:50:00Z"
weight = 52688
keywords = [ "dns" ]
aliases = [ "/questions/52688" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [DNS request for RR "ANY"](/questions/52688/dns-request-for-rr-any)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52688-score" class="post-score" title="current number of votes">0</div><span id="post-52688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've seen a trace where the DNS resolver asks for "ANY" information from the name server. Any idea about the practical case for such request ? In which context does this happen ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '16, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/eac75eef24254c1c9ee690951f6c4006?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thierryn&#39;s gravatar image" /><p><span>thierryn</span><br />
<span class="score" title="21 reputation points">21</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thierryn has no accepted answers">0%</span></p></div></div><div id="comments-container-52688" class="comments-container"></div><div id="comment-tools-52688" class="comment-tools"></div><div class="clear"></div><div id="comment-52688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52689"></span>

<div id="answer-container-52689" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52689-score" class="post-score" title="current number of votes">0</div><span id="post-52689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It happens when someone wants to ask a DNS server for all available information to a domain in a single request. Most programs don't use it, but manual queries often do, because it gets results faster than querying each single type (A, AAAA, NS, MX,...) sequentially.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '16, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-52689" class="comments-container"></div><div id="comment-tools-52689" class="comment-tools"></div><div class="clear"></div><div id="comment-52689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

