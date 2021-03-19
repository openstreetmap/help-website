+++
type = "question"
title = "ADwin Config Protocol"
description = '''Wireshark captures ADwin Congif packets. I want to learn more about this protocol. The only meaningful information is from Wireshark Wiki. That is very helpful, but not sufficient for understanding this protocol well enough to analyze it with my own code. Could anyone offer some directions?'''
date = "2016-03-13T05:49:00Z"
lastmod = "2016-03-13T06:30:00Z"
weight = 50856
keywords = [ "adwin" ]
aliases = [ "/questions/50856" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [ADwin Config Protocol](/questions/50856/adwin-config-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50856-score" class="post-score" title="current number of votes">0</div><span id="post-50856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark captures ADwin Congif packets. I want to learn more about this protocol. The only meaningful information is from <a href="https://wiki.wireshark.org/Protocols/adwin_config">Wireshark Wiki</a>. That is very helpful, but not sufficient for understanding this protocol well enough to analyze it with my own code. Could anyone offer some directions?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-adwin" rel="tag" title="see questions tagged &#39;adwin&#39;">adwin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '16, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/e23332dc51869f08737cc96395284e59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hong&#39;s gravatar image" /><p><span>Hong</span><br />
<span class="score" title="46 reputation points">46</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hong has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Mar '16, 06:26</strong> </span></p></div></div><div id="comments-container-50856" class="comments-container"></div><div id="comment-tools-50856" class="comment-tools"></div><div class="clear"></div><div id="comment-50856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50857"></span>

<div id="answer-container-50857" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50857-score" class="post-score" title="current number of votes">1</div><span id="post-50857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hong has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A brief googling has found <a href="https://cs.fit.edu/code/svn/cse2410f13team7/wireshark/epan/dissectors/packet-adwin-config.c">this C code</a> as well as a suggestion that its author is related to the company which has developed the protocol, which might explain why no better specification is publicly available. Maybe the typo (config -&gt; congif) has prevented you from finding the same?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '16, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50857" class="comments-container"><span id="50858"></span><div id="comment-50858" class="comment"><div id="post-50858-score" class="comment-score"></div><div class="comment-text"><p>Sorry for the typo. Your elucidation makes a lot of sense. The C code should be sufficient.</p></div><div id="comment-50858-info" class="comment-info"><span class="comment-age">(13 Mar '16, 06:30)</span> <span class="comment-user userinfo">Hong</span></div></div></div><div id="comment-tools-50857" class="comment-tools"></div><div class="clear"></div><div id="comment-50857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

