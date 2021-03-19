+++
type = "question"
title = "Diameter End-2-End question"
description = '''I am using WS on a Diameter trace. I am looking for records that do not have a matching end-to-end value. In the trace file the Diameter packets are identified with a [Request in: xxx] tag or the tag [Answer In: yyy] where xxx and yyy are record numbers. My objective is to find all orphaned Diameter...'''
date = "2013-10-01T11:02:00Z"
lastmod = "2013-10-02T06:07:00Z"
weight = 25481
keywords = [ "diameterend2end" ]
aliases = [ "/questions/25481" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Diameter End-2-End question](/questions/25481/diameter-end-2-end-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25481-score" class="post-score" title="current number of votes">0</div><span id="post-25481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using WS on a Diameter trace. I am looking for records that do not have a matching end-to-end value. In the trace file the Diameter packets are identified with a [Request in: xxx] tag or the tag [Answer In: yyy] where xxx and yyy are record numbers. My objective is to find all orphaned Diameter records, meaning the records that do not have a matching end-to-end value or do not have matching Tags (mated Request – Answer). I am looking for Request messages that do not have an response.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameterend2end" rel="tag" title="see questions tagged &#39;diameterend2end&#39;">diameterend2end</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '13, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/bb7eccec0a05bdb4bc4c8c5eda35231b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="plaurie&#39;s gravatar image" /><p><span>plaurie</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="plaurie has no accepted answers">0%</span></p></div></div><div id="comments-container-25481" class="comments-container"></div><div id="comment-tools-25481" class="comment-tools"></div><div class="clear"></div><div id="comment-25481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25487"></span>

<div id="answer-container-25487" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25487-score" class="post-score" title="current number of votes">3</div><span id="post-25487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JeffMorriss has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This display filter should do the trick:</p><p><code>diameter.flags.request == 1 &amp;&amp; !diameter.answer_in</code></p><p>That's asking for all Diameter Request messages that Wireshark didn't find/link an answer to.</p><p>(Since you appear to be new here: if this answers your question, please Accept the answer by clicking on the check box next to the answer.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '13, 17:40</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-25487" class="comments-container"><span id="25488"></span><div id="comment-25488" class="comment"><div id="post-25488-score" class="comment-score"></div><div class="comment-text"><p>Thank You Jeff, I worked like a charm.</p></div><div id="comment-25488-info" class="comment-info"><span class="comment-age">(01 Oct '13, 18:49)</span> <span class="comment-user userinfo">plaurie</span></div></div><span id="25507"></span><div id="comment-25507" class="comment"><div id="post-25507-score" class="comment-score"></div><div class="comment-text"><p>You're welcome. I went ahead and Accepted this answer for you (by clicking on the checkbox). That way this question doesn't show up in the list of "unanswered questions."</p></div><div id="comment-25507-info" class="comment-info"><span class="comment-age">(02 Oct '13, 06:07)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-25487" class="comment-tools"></div><div class="clear"></div><div id="comment-25487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

