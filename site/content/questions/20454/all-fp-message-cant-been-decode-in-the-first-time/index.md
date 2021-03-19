+++
type = "question"
title = "all FP message can&#x27;t been decode in the first time."
description = '''1,In debug mode,first time hit dissect_fp(),the input parameter:tree is always 0x00000000, then all FP message can&#x27;t been decode in the first time. why???'''
date = "2013-04-16T01:36:00Z"
lastmod = "2013-04-16T08:37:00Z"
weight = 20454
keywords = [ "fp", "dissect_fp", "time", "tree", "first" ]
aliases = [ "/questions/20454" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [all FP message can't been decode in the first time.](/questions/20454/all-fp-message-cant-been-decode-in-the-first-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20454-score" class="post-score" title="current number of votes">0</div><span id="post-20454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>1,In debug mode,first time hit dissect_fp(),the input parameter:tree is always 0x00000000, then all FP message can't been decode in the first time.</p><p>why???</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fp" rel="tag" title="see questions tagged &#39;fp&#39;">fp</span> <span class="post-tag tag-link-dissect_fp" rel="tag" title="see questions tagged &#39;dissect_fp&#39;">dissect_fp</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span> <span class="post-tag tag-link-tree" rel="tag" title="see questions tagged &#39;tree&#39;">tree</span> <span class="post-tag tag-link-first" rel="tag" title="see questions tagged &#39;first&#39;">first</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '13, 01:36</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p><span>smilezuzu</span><br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div></div><div id="comments-container-20454" class="comments-container"></div><div id="comment-tools-20454" class="comment-tools"></div><div class="clear"></div><div id="comment-20454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20469"></span>

<div id="answer-container-20469" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20469-score" class="post-score" title="current number of votes">0</div><span id="post-20469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark uses a two pass dissection strategy. The first (and the only linear) pass allows the dissector to setup state information, while in subsequent passes it may be asked for presentation details (a tree).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '13, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-20469" class="comments-container"><span id="20470"></span><div id="comment-20470" class="comment"><div id="post-20470-score" class="comment-score"></div><div class="comment-text"><p>It is also possible that something is under if(tree) that shouldn't be.</p></div><div id="comment-20470-info" class="comment-info"><span class="comment-age">(16 Apr '13, 08:37)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-20469" class="comment-tools"></div><div class="clear"></div><div id="comment-20469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

