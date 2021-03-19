+++
type = "question"
title = "L2TP DMPT header - H bit"
description = '''After V and S bits in DMPT header, we don&#x27;t find H bits [ 2 bits - Next bits after V and S]. Is there any alternatives Thanks,'''
date = "2014-12-02T08:28:00Z"
lastmod = "2014-12-03T01:10:00Z"
weight = 38280
keywords = [ "dmpt", "docsis" ]
aliases = [ "/questions/38280" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [L2TP DMPT header - H bit](/questions/38280/l2tp-dmpt-header-h-bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38280-score" class="post-score" title="current number of votes">0</div><span id="post-38280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After V and S bits in DMPT header, we don't find H bits [ 2 bits - Next bits after V and S]. Is there any alternatives</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dmpt" rel="tag" title="see questions tagged &#39;dmpt&#39;">dmpt</span> <span class="post-tag tag-link-docsis" rel="tag" title="see questions tagged &#39;docsis&#39;">docsis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '14, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/cb0d2b73451ca3fb7ae705364626b6d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sathish%20Thiruvengadam&#39;s gravatar image" /><p><span>Sathish Thir...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sathish Thiruvengadam has no accepted answers">0%</span></p></div></div><div id="comments-container-38280" class="comments-container"></div><div id="comment-tools-38280" class="comment-tools"></div><div class="clear"></div><div id="comment-38280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38283"></span>

<div id="answer-container-38283" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38283-score" class="post-score" title="current number of votes">0</div><span id="post-38283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>I just added the dissection of those H bits to the development branch. You will have to download a nightly build from <a href="https://www.wireshark.org/download/automated/">here</a> with a version number &gt;= v1.99.1rc0-775-g43e759e once available.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '14, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-38283" class="comments-container"><span id="38297"></span><div id="comment-38297" class="comment"><div id="post-38297-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal,</p><p>Thanks so much for the patch. It is working fine but with the patch, I am not able to apply filter for more than 15,000 packets. Tool closes when try to apply filter for more than 15,000 packets. In released wireshark, I am able to apply filter for more than 6,00,000 packets. Could you please provide information how to resolve it</p></div><div id="comment-38297-info" class="comment-info"><span class="comment-age">(03 Dec '14, 00:06)</span> <span class="comment-user userinfo">Sathish Thir...</span></div></div><span id="38300"></span><div id="comment-38300" class="comment"><div id="post-38300-score" class="comment-score"></div><div class="comment-text"><p>Which GUI are you using? The GTK based or the Qt based? The GTK one should behave more or less like the 1.12.X versions. The Qt based is a work in progress were developments are not finished yet.</p></div><div id="comment-38300-info" class="comment-info"><span class="comment-age">(03 Dec '14, 01:10)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-38283" class="comment-tools"></div><div class="clear"></div><div id="comment-38283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

