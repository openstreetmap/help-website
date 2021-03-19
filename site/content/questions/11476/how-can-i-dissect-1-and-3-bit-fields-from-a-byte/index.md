+++
type = "question"
title = "How can I dissect 1- and 3-bit fields from a byte?"
description = '''Hi, I am trying to dissect a byte field for protocol with following byte structure. ============= |T|S|TSG|RES| ============= |1|1| 3 | 3 | ============= T bit 1 bit S bit 1 bit TSG 3 bit RES 3 bit I was trying to get 1 byte unsigned int, AND with the MASKs for the bits and right shift operation. (t...'''
date = "2012-05-30T11:36:00Z"
lastmod = "2013-02-28T12:22:00Z"
weight = 11476
keywords = [ "development", "dissector" ]
aliases = [ "/questions/11476" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I dissect 1- and 3-bit fields from a byte?](/questions/11476/how-can-i-dissect-1-and-3-bit-fields-from-a-byte)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11476-score" class="post-score" title="current number of votes">0</div><span id="post-11476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to dissect a byte field for protocol with following byte structure.</p><pre><code>=============
|T|S|TSG|RES|
=============
|1|1| 3 | 3 |
=============</code></pre><p><code>T</code> bit 1 bit<br />
<code>S</code> bit 1 bit<br />
<code>TSG</code> 3 bit<br />
<code>RES</code> 3 bit</p><p>I was trying to get 1 byte unsigned int, AND with the <code>MASK</code>s for the bits and right shift operation.</p><pre><code>(tvb_get_guint8(tvb,stlv_offset+46)) &amp;&amp; 0x80) &gt;&gt; 7
(tvb_get_guint8(tvb,stlv_offset+46)) &amp;&amp; 0x40) &gt;&gt; 6
(tvb_get_guint8(tvb,stlv_offset+46)) &amp;&amp; 0x38) &gt;&gt; 3</code></pre><p>I am using above functions as an argument to add_text like:</p><pre><code>proto_tree_add_text(stlv_tree, tvb, stlv_offset+46, 1, &quot;Termination Capable: %d&quot;,    
                   ((tvb_get_guint8(tvb,stlv_offset+46)) &amp;&amp; 0x80)&gt;&gt;7));</code></pre><p>But this is giving me all 0 values, and messes my further dissecting. I am fairly new to Wireshark development, but I was thinking I could just get int, bitwise and, then right shift to get the correct bits.</p><p>Is there a better way to do this?<br />
I have a C program wherein I receive a byte array and I do the same thing, extracting bytes and using masks to get the correct bit values, which works. The same logic is not working in Wireshark code.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '12, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/20a66c2b7cc93d2a68ebcfd0c819ab9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prafulla&#39;s gravatar image" /><p><span>prafulla</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prafulla has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 May '12, 12:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></br></p></div></div><div id="comments-container-11476" class="comments-container"></div><div id="comment-tools-11476" class="comment-tools"></div><div class="clear"></div><div id="comment-11476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11480"></span>

<div id="answer-container-11480" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11480-score" class="post-score" title="current number of votes">2</div><span id="post-11480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Read about <code>proto_tree_add_bitmask()</code> in <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.developer?revision=42602&amp;view=markup"><code>README.developer</code></a>. There are plenty of dissectors that make use this function; <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-icmp.c?revision=42393&amp;view=markup"><code>packet-icmp.c</code></a> is one example.</p><p>By the way, you should try to avoid <code>proto_tree_add_text()</code> as much as possible, because any fields added to the tree using that function won't be filterable.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '12, 12:20</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></p></div></div><div id="comments-container-11480" class="comments-container"></div><div id="comment-tools-11480" class="comment-tools"></div><div class="clear"></div><div id="comment-11480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18991"></span>

<div id="answer-container-18991" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18991-score" class="post-score" title="current number of votes">0</div><span id="post-18991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is stlv_offset a byte offset or bit offset?</p><p>I run into into a similar situation where tvb _ read_bits8 always seems to return 0, it turns out that I forget to multiply the running byte offset with 8.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/fac9c2b6b25428ab66486fd1f9bcbaf8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Johann&#39;s gravatar image" /><p><span>Johann</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Johann has no accepted answers">0%</span></p></div></div><div id="comments-container-18991" class="comments-container"></div><div id="comment-tools-18991" class="comment-tools"></div><div class="clear"></div><div id="comment-18991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

