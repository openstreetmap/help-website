+++
type = "question"
title = "Fabricpath Dissector in V2"
description = '''I no longer see the Cisco Fabricpath Dissector (Pref/Protocols/CFP) in V2. Does anyone know if this has been moved, removed, or the name changed? I checked what I thought the obvious name changes might be.  '''
date = "2015-11-19T07:30:00Z"
lastmod = "2015-11-19T09:08:00Z"
weight = 47750
keywords = [ "fabricpath" ]
aliases = [ "/questions/47750" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Fabricpath Dissector in V2](/questions/47750/fabricpath-dissector-in-v2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47750-score" class="post-score" title="current number of votes">0</div><span id="post-47750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I no longer see the Cisco Fabricpath Dissector (Pref/Protocols/CFP) in V2. Does anyone know if this has been moved, removed, or the name changed? I checked what I thought the obvious name changes might be.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fabricpath" rel="tag" title="see questions tagged &#39;fabricpath&#39;">fabricpath</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '15, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/fc85011f4fc6b6632ab07ff82f7ebd0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cjordanva&#39;s gravatar image" /><p><span>cjordanva</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cjordanva has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-47750" class="comments-container"></div><div id="comment-tools-47750" class="comment-tools"></div><div class="clear"></div><div id="comment-47750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47751"></span>

<div id="answer-container-47751" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47751-score" class="post-score" title="current number of votes">0</div><span id="post-47751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Still there, short name is still CFP, it's in packet-mim.c. The dissector no longer has any preferences, hence it doesn't appear in the Edit -&gt; Preferences -&gt; Protocols list, but it's still in the Internals -&gt; Supported Protocols dialog.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '15, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-47751" class="comments-container"><span id="47754"></span><div id="comment-47754" class="comment"><div id="post-47754-score" class="comment-score"></div><div class="comment-text"><p>Thanks for pointing out that it is still in the internal protocols, I missed that. Although it is there when opening an FP capture I still did not see the dissected version. What I found was that although CFP was selected in Analyze/Enabled Protocols there is now a sub check box, fp_eth, that was not selected and needed to be.</p></div><div id="comment-47754-info" class="comment-info"><span class="comment-age">(19 Nov '15, 08:39)</span> <span class="comment-user userinfo">cjordanva</span></div></div><span id="47755"></span><div id="comment-47755" class="comment"><div id="post-47755-score" class="comment-score"></div><div class="comment-text"><p>I've also noticed that those sub check boxes are not originally selected for protocols I'm interested in. Not entirely sure that's very helpful.</p></div><div id="comment-47755-info" class="comment-info"><span class="comment-age">(19 Nov '15, 09:08)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-47751" class="comment-tools"></div><div class="clear"></div><div id="comment-47751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

