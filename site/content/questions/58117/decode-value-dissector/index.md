+++
type = "question"
title = "Decode value dissector"
description = '''Hi I&#x27;m creating a dissector but I have some problems. I&#x27;m doing it in c. In my protocol I have the value &quot;length&quot; thais is encoded with either 1 or 2 bytes. To obtain the value of this field (designated as v) I have to consider : If v1 &amp;lt; 127 then v = v1 with one byte encoding • If v1 128 then v i...'''
date = "2016-12-14T14:53:00Z"
lastmod = "2016-12-14T18:10:00Z"
weight = 58117
keywords = [ "encoding", "proto_tree_add_item", "dissector", "newbie", "wireshark" ]
aliases = [ "/questions/58117" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decode value dissector](/questions/58117/decode-value-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58117-score" class="post-score" title="current number of votes">0</div><span id="post-58117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I'm creating a dissector but I have some problems. I'm doing it in c. In my protocol I have the value "length" thais is encoded with either 1 or 2 bytes. To obtain the value of this field (designated as v) I have to consider : If v1 &lt; 127 then v = v1 with one byte encoding • If v1 128 then v is encoded within the first and the second byte (little-endian byte order) the value of v is: how can I implement this so I can add to proto_tree the value "length2 ???</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encoding" rel="tag" title="see questions tagged &#39;encoding&#39;">encoding</span> <span class="post-tag tag-link-proto_tree_add_item" rel="tag" title="see questions tagged &#39;proto_tree_add_item&#39;">proto_tree_add_item</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '16, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/08be01e8491ba1ee291bf54aa3163886?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mat656&#39;s gravatar image" /><p><span>mat656</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mat656 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Dec '16, 05:53</strong> </span></p></div></div><div id="comments-container-58117" class="comments-container"></div><div id="comment-tools-58117" class="comment-tools"></div><div class="clear"></div><div id="comment-58117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58126"></span>

<div id="answer-container-58126" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58126-score" class="post-score" title="current number of votes">0</div><span id="post-58126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By:</p><ul><li>fetching the first byte;</li><li>if it's &lt; 127, setting the length value to the value of the byte;</li><li>if it's &gt;= 128, fetching the second byte, combining their values, and setting the length to the result;</li><li>adding the item to the field using <code>proto_tree_add_uint()</code>.</li></ul><p><code>proto_tree_add_item()</code> doesn't support the variable-length encoding used by your protocol; it only supports fixed-length big-endian and little-endian simple binary encodings.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '16, 18:10</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Dec '16, 18:10</strong> </span></p></div></div><div id="comments-container-58126" class="comments-container"></div><div id="comment-tools-58126" class="comment-tools"></div><div class="clear"></div><div id="comment-58126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

