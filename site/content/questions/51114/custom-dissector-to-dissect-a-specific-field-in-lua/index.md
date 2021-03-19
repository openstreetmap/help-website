+++
type = "question"
title = "Custom dissector to dissect a specific field in LUA"
description = '''Hi, I am trying to implement a custom dissector in order to dissect a field which is not dissected from original dissector (gtpv2). However i am not sure if i am able to do this in LUA. I don&#x27;t know how to write my dissector function in order to catch only the case for this specific field. Thank you...'''
date = "2016-03-23T02:04:00Z"
lastmod = "2016-03-25T10:48:00Z"
weight = 51114
keywords = [ "chained-dissector", "lua" ]
aliases = [ "/questions/51114" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Custom dissector to dissect a specific field in LUA](/questions/51114/custom-dissector-to-dissect-a-specific-field-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51114-score" class="post-score" title="current number of votes">0</div><span id="post-51114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to implement a custom dissector in order to dissect a field which is not dissected from original dissector (gtpv2).</p><p>However i am not sure if i am able to do this in LUA. I don't know how to write my dissector function in order to catch only the case for this specific field.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-chained-dissector" rel="tag" title="see questions tagged &#39;chained-dissector&#39;">chained-dissector</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '16, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/37225c04657d6faeecbba2c5073c9b45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lucas_sim&#39;s gravatar image" /><p><span>lucas_sim</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lucas_sim has no accepted answers">0%</span></p></div></div><div id="comments-container-51114" class="comments-container"><span id="51134"></span><div id="comment-51134" class="comment"><div id="post-51134-score" class="comment-score"></div><div class="comment-text"><p>Why not open a bug report and have the gtpv2 director updated to dissect the field?</p></div><div id="comment-51134-info" class="comment-info"><span class="comment-age">(23 Mar '16, 14:03)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="51137"></span><div id="comment-51137" class="comment"><div id="post-51137-score" class="comment-score"></div><div class="comment-text"><p>I modified the gtpv2 dissector and now it dissects this specific field.</p></div><div id="comment-51137-info" class="comment-info"><span class="comment-age">(23 Mar '16, 15:06)</span> <span class="comment-user userinfo">lucas_sim</span></div></div><span id="51183"></span><div id="comment-51183" class="comment"><div id="post-51183-score" class="comment-score"></div><div class="comment-text"><p>Please submit the change through gerrit to benefit all.</p></div><div id="comment-51183-info" class="comment-info"><span class="comment-age">(25 Mar '16, 07:45)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="51194"></span><div id="comment-51194" class="comment"><div id="post-51194-score" class="comment-score"></div><div class="comment-text"><p>Yes i have already applied the patch in gerrit. Thanks</p></div><div id="comment-51194-info" class="comment-info"><span class="comment-age">(25 Mar '16, 10:48)</span> <span class="comment-user userinfo">lucas_sim</span></div></div></div><div id="comment-tools-51114" class="comment-tools"></div><div class="clear"></div><div id="comment-51114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

