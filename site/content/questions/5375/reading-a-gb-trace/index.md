+++
type = "question"
title = "Reading a Gb trace"
description = '''hello, There is a little confusion on how to decode and filter the Gb over IP trace. earlier NSIP dissector was found but now there is no NSIP, though there is gprs-ns. but sometimes that is also not there. '''
date = "2011-08-01T05:53:00Z"
lastmod = "2015-02-19T11:13:00Z"
weight = 5375
keywords = [ "gprs", "gboip", "gprs-ns", "gb" ]
aliases = [ "/questions/5375" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reading a Gb trace](/questions/5375/reading-a-gb-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5375-score" class="post-score" title="current number of votes">0</div><span id="post-5375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>There is a little confusion on how to decode and filter the Gb over IP trace. earlier NSIP dissector was found but now there is no NSIP, though there is gprs-ns. but sometimes that is also not there.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gprs" rel="tag" title="see questions tagged &#39;gprs&#39;">gprs</span> <span class="post-tag tag-link-gboip" rel="tag" title="see questions tagged &#39;gboip&#39;">gboip</span> <span class="post-tag tag-link-gprs-ns" rel="tag" title="see questions tagged &#39;gprs-ns&#39;">gprs-ns</span> <span class="post-tag tag-link-gb" rel="tag" title="see questions tagged &#39;gb&#39;">gb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '11, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/9aba2429c4924d4ad4b9310df44f7d9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rahul2909&#39;s gravatar image" /><p><span>Rahul2909</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rahul2909 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Aug '11, 05:54</strong> </span></p></div></div><div id="comments-container-5375" class="comments-container"><span id="5394"></span><div id="comment-5394" class="comment"><div id="post-5394-score" class="comment-score"></div><div class="comment-text"><p>If I remember correctly previously there was two dissectors for the same protocol packet-nsip.c and packet-gprs-ns.c, packet-nsip.c was removed. If something does not work raise a bug report, include a trace file illustrating the problem. From the info above it's not possible to determine what the problem might be.</p></div><div id="comment-5394-info" class="comment-info"><span class="comment-age">(01 Aug '11, 22:54)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-5375" class="comment-tools"></div><div class="clear"></div><div id="comment-5375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39959"></span>

<div id="answer-container-39959" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39959-score" class="post-score" title="current number of votes">0</div><span id="post-39959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I used the following steps to decode Gb over IP for 2G Data captures.</p><p>Filter on UDP.</p><p>Select a packet. BSC source port is 5500 for this traffic.</p><p>Decode As: Port=5500, GPRS-NS</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '15, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/9023567c0bd9ab7aef6d78aefd489697?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20P&#39;s gravatar image" /><p><span>David P</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David P has no accepted answers">0%</span></p></div></div><div id="comments-container-39959" class="comments-container"></div><div id="comment-tools-39959" class="comment-tools"></div><div class="clear"></div><div id="comment-39959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

