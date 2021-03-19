+++
type = "question"
title = "&quot;user_dlt&quot; option in tshark?"
description = '''GUI based wireshark provide USER_DLT Encapsulation.  Command based tshark provide same or even a similar option? thanks.'''
date = "2013-09-09T05:03:00Z"
lastmod = "2013-09-09T07:54:00Z"
weight = 24474
keywords = [ "user_dlt", "tshark" ]
aliases = [ "/questions/24474" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["user\_dlt" option in tshark?](/questions/24474/user_dlt-option-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24474-score" class="post-score" title="current number of votes">0</div><span id="post-24474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>GUI based wireshark provide USER_DLT Encapsulation. Command based tshark provide same or even a similar option?</p><p>thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-user_dlt" rel="tag" title="see questions tagged &#39;user_dlt&#39;">user_dlt</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '13, 05:03</strong></p><img src="https://secure.gravatar.com/avatar/87d9785e558dac3711884cc1afe5ad19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kingko&#39;s gravatar image" /><p><span>kingko</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kingko has no accepted answers">0%</span></p></div></div><div id="comments-container-24474" class="comments-container"></div><div id="comment-tools-24474" class="comment-tools"></div><div class="clear"></div><div id="comment-24474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24479"></span>

<div id="answer-container-24479" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24479-score" class="post-score" title="current number of votes">2</div><span id="post-24479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>with tshark you can use the following command line as an example:</p><pre><code>tshark.exe&quot; -o &quot;uat:user_dlts:\&quot;User 15 (DLT=162)\&quot;,\&quot;payload protocol\&quot;,\&quot;header size\&quot;,\&quot;header protocol\&quot;,\&quot;trailer size\&quot;,\&quot;trailer protocol\&quot;&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '13, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-24479" class="comments-container"><span id="24481"></span><div id="comment-24481" class="comment"><div id="post-24481-score" class="comment-score"></div><div class="comment-text"><blockquote><p>-o "uat:user_dlts:</p></blockquote><p>nice, I did not know about that feature.</p><p>Shouldn't that be part of the tshark man page? ;-)</p></div><div id="comment-24481-info" class="comment-info"><span class="comment-age">(09 Sep '13, 07:54)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24479" class="comment-tools"></div><div class="clear"></div><div id="comment-24479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

