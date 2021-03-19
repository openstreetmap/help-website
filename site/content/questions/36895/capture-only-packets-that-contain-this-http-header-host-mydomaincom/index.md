+++
type = "question"
title = "capture only packets that contain this http header-&gt; Host: mydomain.com"
description = '''hello i want to capture packets that contain this http header-&amp;gt; Host: mydomain.com if i use http.host display filter all data will be saved to disk and it becomes very large after few minutes is this possible ? or is there any kind of perl or python script written for this ?'''
date = "2014-10-07T09:23:00Z"
lastmod = "2014-10-13T10:18:00Z"
weight = 36895
keywords = [ "capture-filter" ]
aliases = [ "/questions/36895" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capture only packets that contain this http header-&gt; Host: mydomain.com](/questions/36895/capture-only-packets-that-contain-this-http-header-host-mydomaincom)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36895-score" class="post-score" title="current number of votes">0</div><span id="post-36895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello i want to capture packets that contain this http header-&gt; Host: mydomain.com if i use http.host display filter all data will be saved to disk and it becomes very large after few minutes is this possible ? or is there any kind of perl or python script written for this ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '14, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/0c9f8313e7f369d627fbe129e64c0b1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Damen%20Salvatore&#39;s gravatar image" /><p><span>Damen Salvatore</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Damen Salvatore has no accepted answers">0%</span></p></div></div><div id="comments-container-36895" class="comments-container"></div><div id="comment-tools-36895" class="comment-tools"></div><div class="clear"></div><div id="comment-36895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37018"></span>

<div id="answer-container-37018" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37018-score" class="post-score" title="current number of votes">0</div><span id="post-37018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should set a capture filter:</p><pre><code>port 80 and host mydomain.com</code></pre>So Wireshark does not capture other packets. The display filter is like the name says only for hiding packets, so if you remove the filter other packets will show up.<br />
<a href="https://www.youtube.com/watch?v=298urAvk128">Just a little Tutorial video about setting capture filters, click here.</a></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '14, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/cc56ba9bd225bd68cea09a404ecc0b6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lal12&#39;s gravatar image" /><p><span>lal12</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lal12 has 2 accepted answers">33%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Oct '14, 10:22</strong> </span></p></div></div><div id="comments-container-37018" class="comments-container"></div><div id="comment-tools-37018" class="comment-tools"></div><div class="clear"></div><div id="comment-37018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

