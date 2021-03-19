+++
type = "question"
title = "v2.0.4 RTAC Serial"
description = '''Hi all,  I found I cannot dissect RTAC serial message I captured in SEL RTAC device after I upgraded from v1.12.8 to v2.0.4. Is there any dissector already released that I can download and use? Thanks!'''
date = "2016-07-07T11:22:00Z"
lastmod = "2016-07-08T09:32:00Z"
weight = 53913
keywords = [ "rtac", "dissector" ]
aliases = [ "/questions/53913" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [v2.0.4 RTAC Serial](/questions/53913/v204-rtac-serial)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53913-score" class="post-score" title="current number of votes">0</div><span id="post-53913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I found I cannot dissect RTAC serial message I captured in SEL RTAC device after I upgraded from v1.12.8 to v2.0.4. Is there any dissector already released that I can download and use?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtac" rel="tag" title="see questions tagged &#39;rtac&#39;">rtac</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '16, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/6ae8a8d97d75bb45a23fd939daab36ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jli63&#39;s gravatar image" /><p><span>jli63</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jli63 has no accepted answers">0%</span></p></div></div><div id="comments-container-53913" class="comments-container"><span id="53927"></span><div id="comment-53927" class="comment"><div id="post-53927-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-53927-info" class="comment-info"><span class="comment-age">(08 Jul '16, 03:44)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="53943"></span><div id="comment-53943" class="comment"><div id="post-53943-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.cloudshark.org/captures/eae67328dff2">https://www.cloudshark.org/captures/eae67328dff2</a> Here is the sample capture I just uploaded in CloudShark for you to view.</p><p>I just don't know how to dissect and analyze the DNP message contained in the RTAC Serial layer. I used to be able to apply dissector in v1.12.8. But cannot really do that in v2.0.4.</p><p>Any help would be appreciated!</p></div><div id="comment-53943-info" class="comment-info"><span class="comment-age">(08 Jul '16, 08:47)</span> <span class="comment-user userinfo">jli63</span></div></div></div><div id="comment-tools-53913" class="comment-tools"></div><div class="clear"></div><div id="comment-53913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53944"></span>

<div id="answer-container-53944" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53944-score" class="post-score" title="current number of votes">1</div><span id="post-53944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jli63 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The data appears to be DNP3 carried over RTAC. To enable DNP3 dissection of the data, right click an RTAC packet in the packet list, and select "Decode As ...". This should give you the sub-dissector settings for RTAC serial data, and in the "Current" field, select "DNP 3.0".</p><p>Add a display filter of "dnp3" to just show the DNP3 traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '16, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53944" class="comments-container"></div><div id="comment-tools-53944" class="comment-tools"></div><div class="clear"></div><div id="comment-53944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

