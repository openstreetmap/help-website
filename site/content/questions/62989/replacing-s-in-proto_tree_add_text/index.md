+++
type = "question"
title = "replacing %s in proto_tree_add_text"
description = '''I am new to wireshark and I am trying to upgrade a plugin that was build for 1.x to 2.x. One of those steps is replacing proto_tree_add_text() with proto_tree_add_item() if the old code is proto_tree_add_text(foo_tree, tvb, 0, -1, &quot;header ver. %s&quot;, header_array[index]);  I know I would have to start...'''
date = "2017-07-21T15:19:00Z"
lastmod = "2017-08-04T09:46:00Z"
weight = 62989
keywords = [ "proto_tree_add_text", "proto_tree_add_item", "plugin" ]
aliases = [ "/questions/62989" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [replacing %s in proto\_tree\_add\_text](/questions/62989/replacing-s-in-proto_tree_add_text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62989-score" class="post-score" title="current number of votes">0</div><span id="post-62989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to wireshark and I am trying to upgrade a plugin that was build for 1.x to 2.x. One of those steps is replacing <code>proto_tree_add_text()</code> with <code>proto_tree_add_item()</code></p><p>if the old code is</p><pre><code>proto_tree_add_text(foo_tree, tvb, 0, -1, &quot;header ver. %s&quot;, header_array[index]);</code></pre><p>I know I would have to start with</p><pre><code>static hf_register_info hf[] = {
    { &amp;foo_header,
        { &quot;header ver. &quot;, &quot;foo.header&quot;,
        FT_NONE, BASE_NONE,
        NULL, 0x0,
        NULL, HFILL }
    }
};
proto_tree_add_item(foo_tree, foo_header, tvb, 0, -1, ENC_NA);</code></pre><p>But how would I add the array into the string to display? Where is a good source to learn about using hf_register_info?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proto_tree_add_text" rel="tag" title="see questions tagged &#39;proto_tree_add_text&#39;">proto_tree_add_text</span> <span class="post-tag tag-link-proto_tree_add_item" rel="tag" title="see questions tagged &#39;proto_tree_add_item&#39;">proto_tree_add_item</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '17, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/f5b7f4029bc4724fd35867c07f85712b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="allantse&#39;s gravatar image" /><p><span>allantse</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="allantse has one accepted answer">100%</span></p></div></div><div id="comments-container-62989" class="comments-container"></div><div id="comment-tools-62989" class="comment-tools"></div><div class="clear"></div><div id="comment-62989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62994"></span>

<div id="answer-container-62994" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62994-score" class="post-score" title="current number of votes">0</div><span id="post-62994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="allantse has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>proto_tree_add_none_format(foo_tree, foo_header, tvb, 0, -1, &quot;header ver. %s&quot;, header_array[index]);</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '17, 21:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-62994" class="comments-container"><span id="63405"></span><div id="comment-63405" class="comment"><div id="post-63405-score" class="comment-score"></div><div class="comment-text"><p>thank you!</p></div><div id="comment-63405-info" class="comment-info"><span class="comment-age">(04 Aug '17, 09:32)</span> <span class="comment-user userinfo">allantse</span></div></div><span id="63408"></span><div id="comment-63408" class="comment"><div id="post-63408-score" class="comment-score"></div><div class="comment-text"><p>From the little information you have given I would consider rewriting the code and add the header information elements with proto_tree_add_item() with Hf_header_version and the appropriate length of the field.</p></div><div id="comment-63408-info" class="comment-info"><span class="comment-age">(04 Aug '17, 09:46)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-62994" class="comment-tools"></div><div class="clear"></div><div id="comment-62994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

