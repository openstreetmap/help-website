+++
type = "question"
title = "Filter data.text not working"
description = '''Under version v1.12.2 a filter on data.text (ex : &quot;data.text contains &quot;welc&quot;&quot;) is not working but under v1.10.6 it works. Is there a configuration I&#x27;m missing? Is it confimed? Is it extended to other filters? Thanks'''
date = "2014-12-09T06:28:00Z"
lastmod = "2014-12-09T06:53:00Z"
weight = 38483
keywords = [ "filter" ]
aliases = [ "/questions/38483" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filter data.text not working](/questions/38483/filter-datatext-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38483-score" class="post-score" title="current number of votes">0</div><span id="post-38483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Under version v1.12.2 a filter on data.text (ex : "data.text contains "welc"") is not working but under v1.10.6 it works. Is there a configuration I'm missing? Is it confimed? Is it extended to other filters?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '14, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/52dc6e78f31cc20b17b7e96fcdd269ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reynald&#39;s gravatar image" /><p><span>Reynald</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reynald has no accepted answers">0%</span></p></div></div><div id="comments-container-38483" class="comments-container"></div><div id="comment-tools-38483" class="comment-tools"></div><div class="clear"></div><div id="comment-38483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38485"></span>

<div id="answer-container-38485" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38485-score" class="post-score" title="current number of votes">1</div><span id="post-38485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check the preferences for the "data" dissector. To use the data.text field as a filter you must enable the preference "Show data as text".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '14, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38485" class="comments-container"><span id="38488"></span><div id="comment-38488" class="comment"><div id="post-38488-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot grahamb. This works. Do you have an explanation about why "data.text" is not looking inside the data as text ? and then we have to enable this parameter...</p></div><div id="comment-38488-info" class="comment-info"><span class="comment-age">(09 Dec '14, 06:46)</span> <span class="comment-user userinfo">Reynald</span></div></div><span id="38489"></span><div id="comment-38489" class="comment"><div id="post-38489-score" class="comment-score"></div><div class="comment-text"><p>The dissector is (currently) written that way. Unless the preference is enabled, the dissector does not add the data.text field when dissecting the data.</p><p>I guess it's an optimization of some form.</p></div><div id="comment-38489-info" class="comment-info"><span class="comment-age">(09 Dec '14, 06:53)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-38485" class="comment-tools"></div><div class="clear"></div><div id="comment-38485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38486"></span>

<div id="answer-container-38486" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38486-score" class="post-score" title="current number of votes">0</div><span id="post-38486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know why it works with 1.10.x and not with 1.12.x. Can you provide a sample capture file that shows the effect?</p><p>BTW: can you please try the following as a workaround?</p><blockquote><p>frame contains "welc"</p></blockquote><p>The false positives should be low enough to for an acceptable workaround.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '14, 06:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38486" class="comments-container"></div><div id="comment-tools-38486" class="comment-tools"></div><div class="clear"></div><div id="comment-38486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

