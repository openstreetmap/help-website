+++
type = "question"
title = "Using bitmask with user defined value and length"
description = '''Hi, I&#x27;m working on a protocol dissector which uses a variable-length quantity encoding. So I&#x27;ve written functions like: guint32 tvb_get_varuint32(tvbuff_t *tvb, guint8 *octet_count, guint32 offset) to peek the values from the buffer. For all other proto_tree_add_XXX functions I can pass my own value...'''
date = "2016-02-28T04:15:00Z"
lastmod = "2016-02-28T04:15:00Z"
weight = 50565
keywords = [ "variable", "bitmask", "length" ]
aliases = [ "/questions/50565" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using bitmask with user defined value and length](/questions/50565/using-bitmask-with-user-defined-value-and-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50565-score" class="post-score" title="current number of votes">0</div><span id="post-50565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm working on a protocol dissector which uses a variable-length quantity encoding. So I've written functions like:</p><p><code>guint32 tvb_get_varuint32(tvbuff_t *tvb, guint8 *octet_count, guint32 offset)</code></p><p>to peek the values from the buffer.</p><p>For all other <code>proto_tree_add_XXX</code> functions I can pass my own value and length, but for adding bitmask there is no such option. There is a <code>proto_tree_add_bitmask_len()</code> function where I can pass my length, but not my own value.</p><p>In proto.c there are non-exported functions like <code>proto_tree_add_bitmask_value()</code> where I could pass a value, but not the length.</p><p>Is there any solution to realize this without any changes to proto.c?</p><p>There is at least one existing dissector (packet-wap.c) which uses a similar VLQ encoding, but has no bitmasks in it.</p><p>Thanks for help, Thomas</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-variable" rel="tag" title="see questions tagged &#39;variable&#39;">variable</span> <span class="post-tag tag-link-bitmask" rel="tag" title="see questions tagged &#39;bitmask&#39;">bitmask</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '16, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/cc5a96007018c211be9d5fb50a76c51f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="th-wiens&#39;s gravatar image" /><p><span>th-wiens</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="th-wiens has no accepted answers">0%</span></p></div></div><div id="comments-container-50565" class="comments-container"></div><div id="comment-tools-50565" class="comment-tools"></div><div class="clear"></div><div id="comment-50565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

