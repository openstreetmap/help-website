+++
type = "question"
title = "How to modified display format of a given field within dissector tree pane?"
description = '''Hi, I recently used the asn2wrs to create a new asn1 dissector (thanks for that wonderful tool). The problem I have is that I would like to modify how an integer value is displayed in the wireshark pane for a specific field. For example, the value that is displayed is “70390700” which is the good va...'''
date = "2014-11-06T08:48:00Z"
lastmod = "2014-11-07T11:08:00Z"
weight = 37622
keywords = [ "asn2wrs", "asn1", "ft_ipv4", "dissectors" ]
aliases = [ "/questions/37622" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to modified display format of a given field within dissector tree pane?](/questions/37622/how-to-modified-display-format-of-a-given-field-within-dissector-tree-pane)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37622-score" class="post-score" title="current number of votes">0</div><span id="post-37622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I recently used the asn2wrs to create a new asn1 dissector (thanks for that wonderful tool).</p><p>The problem I have is that I would like to modify how an integer value is displayed in the wireshark pane for a specific field. For example, the value that is displayed is “70390700” which is the good value but I would like to display it to the user in a different way because it represents an ip address.</p><p>70390700 (decimal value) = 04 32 13 AC (hex value) –&gt; 4 50 19 172, and I would like to have “172.19.50.4” displayed into the wireshark pane.</p><p>Can you give me some help on how I could achieve that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-asn2wrs" rel="tag" title="see questions tagged &#39;asn2wrs&#39;">asn2wrs</span> <span class="post-tag tag-link-asn1" rel="tag" title="see questions tagged &#39;asn1&#39;">asn1</span> <span class="post-tag tag-link-ft_ipv4" rel="tag" title="see questions tagged &#39;ft_ipv4&#39;">ft_ipv4</span> <span class="post-tag tag-link-dissectors" rel="tag" title="see questions tagged &#39;dissectors&#39;">dissectors</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '14, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/10d514b16f65d7a9e8c47e1378e9534c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="badam71&#39;s gravatar image" /><p><span>badam71</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="badam71 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Nov '14, 10:25</strong> </span></p></div></div><div id="comments-container-37622" class="comments-container"></div><div id="comment-tools-37622" class="comment-tools"></div><div class="clear"></div><div id="comment-37622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37627"></span>

<div id="answer-container-37627" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37627-score" class="post-score" title="current number of votes">1</div><span id="post-37627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use the #TYPE_ATTR directive,see the sources for examples.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '14, 13:46</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-37627" class="comments-container"><span id="37650"></span><div id="comment-37650" class="comment"><div id="post-37650-score" class="comment-score"></div><div class="comment-text"><p>I added the following lines to my .cnf:</p><p>#.TYPE_ATTR Ip4AddressType TYPE = FT_IPv4 DISPLAY = BASE_NONE STRINGS = NULL</p><p>But the IP address is still displayed as "4.50.19.172" instead of "172.19.50.4".</p></div><div id="comment-37650-info" class="comment-info"><span class="comment-age">(07 Nov '14, 06:12)</span> <span class="comment-user userinfo">badam71</span></div></div><span id="37651"></span><div id="comment-37651" class="comment"><div id="post-37651-score" class="comment-score"></div><div class="comment-text"><p>Hmm it's the endianess thet's the problem you will have to replace the generated dissection by your own in the .cnf file.</p></div><div id="comment-37651-info" class="comment-info"><span class="comment-age">(07 Nov '14, 06:46)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="37656"></span><div id="comment-37656" class="comment"><div id="post-37656-score" class="comment-score"></div><div class="comment-text"><p>I am not sure how do do that... My dissector (automatically generated) looks like this in the packet-foo.c file.</p><pre><code>static int
dissect_foo_Ip4AddressType(tvbuff_t *tvb _U_, int offset _U_, asn1_ctx_t *actx _U_, proto_tree *tree _U_, int hf_index _U_) {
  offset = dissect_per_octet_string(tvb, offset, actx, tree, hf_index,
                                       NO_BOUND, NO_BOUND, FALSE, NULL);

  return offset;
}</code></pre></div><div id="comment-37656-info" class="comment-info"><span class="comment-age">(07 Nov '14, 10:05)</span> <span class="comment-user userinfo">badam71</span></div></div><span id="37659"></span><div id="comment-37659" class="comment"><div id="post-37659-score" class="comment-score"></div><div class="comment-text"><p>I found that the "dissect_per_octet_string()" function was using ENC_BIG_ENDIAN. For now I solved this issue by adding a special case for the type "FT_IPv4" which will now use ENC_LITTLE_ENDIAN instead.</p></div><div id="comment-37659-info" class="comment-info"><span class="comment-age">(07 Nov '14, 11:08)</span> <span class="comment-user userinfo">badam71</span></div></div></div><div id="comment-tools-37627" class="comment-tools"></div><div class="clear"></div><div id="comment-37627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

