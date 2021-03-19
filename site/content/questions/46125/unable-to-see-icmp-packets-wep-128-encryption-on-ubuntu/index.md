+++
type = "question"
title = "Unable to see ICMP packets WEP 128 Encryption on Ubuntu"
description = '''I am unable to see ICMP packets in a trace captured with WEP 128 encryption on my ubuntu machine. I see LLC packets instead. I am able to decrypt and see the ICMP on my windows machine perfectly fine. Both machines are running version 1.12.7. Is this a known issue?'''
date = "2015-09-24T13:38:00Z"
lastmod = "2015-09-25T13:50:00Z"
weight = 46125
keywords = [ "encryption", "icmp", "linux" ]
aliases = [ "/questions/46125" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Unable to see ICMP packets WEP 128 Encryption on Ubuntu](/questions/46125/unable-to-see-icmp-packets-wep-128-encryption-on-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46125-score" class="post-score" title="current number of votes">0</div><span id="post-46125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am unable to see ICMP packets in a trace captured with WEP 128 encryption on my ubuntu machine. I see LLC packets instead. I am able to decrypt and see the ICMP on my windows machine perfectly fine. Both machines are running version 1.12.7. Is this a known issue?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encryption" rel="tag" title="see questions tagged &#39;encryption&#39;">encryption</span> <span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '15, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/e52ed6268b16b75639b452318b810190?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adamshickAllion&#39;s gravatar image" /><p><span>adamshickAllion</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adamshickAllion has no accepted answers">0%</span></p></div></div><div id="comments-container-46125" class="comments-container"></div><div id="comment-tools-46125" class="comment-tools"></div><div class="clear"></div><div id="comment-46125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46185"></span>

<div id="answer-container-46185" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46185-score" class="post-score" title="current number of votes">1</div><span id="post-46185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="adamshickAllion has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For reference, this was a bug in Wireshark that Adam reported <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11549">here</a> and that is fixed for the upcoming 1.12.8 and 1.99.10 releases.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '15, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Sep '15, 14:03</strong> </span></p></div></div><div id="comments-container-46185" class="comments-container"></div><div id="comment-tools-46185" class="comment-tools"></div><div class="clear"></div><div id="comment-46185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

