+++
type = "question"
title = "proto_tree_add_item new line"
description = '''The proto_tree_add_item displays each filter in a newline in the CLI. Is there a way to display the filters in the same line. Ex.   proto_tree_add_uint(tree, hf_s1, tvb, 0, 1, s1);   proto_tree_add_uint(tree, hf_s2, tvb, 0, 1, s2);  I want them to be s1 and s2 to be displayed in the same line as   s...'''
date = "2015-09-28T04:03:00Z"
lastmod = "2015-09-28T14:32:00Z"
weight = 46215
keywords = [ "command-line", "tshark", "packet", "wireshark" ]
aliases = [ "/questions/46215" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [proto\_tree\_add\_item new line](/questions/46215/proto_tree_add_item-new-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46215-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46215-score" class="post-score" title="current number of votes">0</div><span id="post-46215-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The proto_tree_add_item displays each filter in a newline in the CLI. Is there a way to display the filters in the same line.</p><p>Ex.</p><pre><code>    proto_tree_add_uint(tree, hf_s1, tvb, 0, 1, s1);    
    proto_tree_add_uint(tree, hf_s2, tvb, 0, 1, s2);</code></pre><p>I want them to be s1 and s2 to be displayed in the same line as</p><pre><code>    s1 : 12,  s2 : 13</code></pre><p>rather than</p><pre><code>   s1 : 12
   s2 : 13</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-command-line" rel="tag" title="see questions tagged &#39;command-line&#39;">command-line</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '15, 04:03</strong></p><img src="https://secure.gravatar.com/avatar/5c6557bd7c8696a17e1c44bae9cd4217?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samprit&#39;s gravatar image" /><p><span>samprit</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samprit has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Sep '15, 03:01</strong> </span></p></div></div><div id="comments-container-46215" class="comments-container"></div><div id="comment-tools-46215" class="comment-tools"></div><div class="clear"></div><div id="comment-46215-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46220"></span>

<div id="answer-container-46220" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46220-score" class="post-score" title="current number of votes">0</div><span id="post-46220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not for a filter (I think you actually mean an hf item). The text for each entry can be built from multiple packets in the frame, or synthesise out of thin air if you wish though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '15, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-46220" class="comments-container"><span id="46221"></span><div id="comment-46221" class="comment"><div id="post-46221-score" class="comment-score"></div><div class="comment-text"><p>Yes, I meant an hf item. How to display different hf items in the same line in CLI.</p></div><div id="comment-46221-info" class="comment-info"><span class="comment-age">(28 Sep '15, 07:46)</span> <span class="comment-user userinfo">samprit</span></div></div></div><div id="comment-tools-46220" class="comment-tools"></div><div class="clear"></div><div id="comment-46220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46236"></span>

<div id="answer-container-46236" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46236-score" class="post-score" title="current number of votes">0</div><span id="post-46236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The only way to display multiple fields on the same line is to use the <code>-T fields</code> option to TShark, for example</p><pre><code>tshark -r inputfile -T fields -e ip.src -e ip.dst -e ip.ttl</code></pre><p>which will show the IPv4 source address, destination address, and TTL on the same line. If any of those fields are missing, it will show a blank, so, for example, non-IPv4 packets will show a blank line.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '15, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-46236" class="comments-container"></div><div id="comment-tools-46236" class="comment-tools"></div><div class="clear"></div><div id="comment-46236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

