+++
type = "question"
title = "alternate for proto_tree_add_text()"
description = '''proto_tree_add_text(header_tree, tvb, startValue, 3, &quot;%s: %d&quot;, val_to_str(Tag, value_string_array, &quot;Unknown Tag:(0x%02x)&quot;),value);  the convert_proto_tree_add_text.pl isn&#x27;t considering the &quot;%s: and %d&quot;  it is only considering %s: and the result is invalid!  i need the alternate for the same function...'''
date = "2017-05-02T23:31:00Z"
lastmod = "2017-05-02T23:31:00Z"
weight = 61180
keywords = [ "proto_tree_add_text", "dissector", "proto_tree_add_item" ]
aliases = [ "/questions/61180" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [alternate for proto\_tree\_add\_text()](/questions/61180/alternate-for-proto_tree_add_text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61180-score" class="post-score" title="current number of votes">0</div><span id="post-61180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>proto_tree_add_text(header_tree, tvb, startValue, 3, &quot;%s: %d&quot;, val_to_str(Tag, value_string_array, &quot;Unknown Tag:(0x%02x)&quot;),value);</code></pre><p>the convert_proto_tree_add_text.pl isn't considering the "<code>%s:</code> and <code>%d</code>"</p><p>it is only considering <code>%s:</code> and the result is invalid!</p><p>i need the alternate for the same function using proto_tree_add_item()</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proto_tree_add_text" rel="tag" title="see questions tagged &#39;proto_tree_add_text&#39;">proto_tree_add_text</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-proto_tree_add_item" rel="tag" title="see questions tagged &#39;proto_tree_add_item&#39;">proto_tree_add_item</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '17, 23:31</strong></p><img src="https://secure.gravatar.com/avatar/600778689935688cd4eaaa966e880cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DhanuShalz&#39;s gravatar image" /><p><span>DhanuShalz</span><br />
<span class="score" title="36 reputation points">36</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DhanuShalz has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 May '17, 03:02</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-61180" class="comments-container"></div><div id="comment-tools-61180" class="comment-tools"></div><div class="clear"></div><div id="comment-61180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

