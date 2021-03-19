+++
type = "question"
title = "Netflow v9 and MPLS"
description = '''Hello, I&#x27;m using Wireshark to capture Netflow v9 flow exports of MPLS encapsulated packets. For packets that have multiple labels (e.g. L3VPN traffic), it seems that Wireshark is showing the bottom label (the one that has the bottom of stack bit set to 1), as &quot;top of stack.&quot; Is this a typo in the de...'''
date = "2014-08-27T10:58:00Z"
lastmod = "2014-09-10T10:07:00Z"
weight = 35816
keywords = [ "netflow", "mpls" ]
aliases = [ "/questions/35816" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Netflow v9 and MPLS](/questions/35816/netflow-v9-and-mpls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35816-score" class="post-score" title="current number of votes">0</div><span id="post-35816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm using Wireshark to capture Netflow v9 flow exports of MPLS encapsulated packets. For packets that have multiple labels (e.g. L3VPN traffic), it seems that Wireshark is showing the bottom label (the one that has the bottom of stack bit set to 1), as "top of stack." Is this a typo in the decoder?</p><p>I uploaded a screenshot here: <a href="http://imgur.com/4pnfk6S">http://imgur.com/4pnfk6S</a></p><p>Thanks, Chris</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-netflow" rel="tag" title="see questions tagged &#39;netflow&#39;">netflow</span> <span class="post-tag tag-link-mpls" rel="tag" title="see questions tagged &#39;mpls&#39;">mpls</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '14, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/2611257fe55cb63f7f4c8f708bca110f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mplspackets&#39;s gravatar image" /><p><span>mplspackets</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mplspackets has no accepted answers">0%</span></p></div></div><div id="comments-container-35816" class="comments-container"></div><div id="comment-tools-35816" class="comment-tools"></div><div class="clear"></div><div id="comment-35816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35824"></span>

<div id="answer-container-35824" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35824-score" class="post-score" title="current number of votes">1</div><span id="post-35824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mplspackets has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Can you confirm the actual hex (undecoded) that make up the label headers? It's a bit to navigate but it looks like the function being called on each label header starts at line 1493 of file "packet-netflow.c". That function seems to be checking that bit value to see if it's set, and I think you're right (looks like the logic is to add the text "top-of-stack" if the "bottom-of-stack" bit is set).</p><p>I suggest commenting on this in Wireshark's bugzilla page at: <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a></p><p>For reference, the code there is:</p><pre><code>proto_tree_add_mpls_label(proto_tree pdutree, tvbuff_t tvb, int offset, int length, int level)
{
    proto_item *ti;
    if( length == 3) {
        guint8 b0 = tvb_get_guint8(tvb, offset);
        guint8 b1 = tvb_get_guint8(tvb, offset + 1);
        guint8 b2 = tvb_get_guint8(tvb, offset + 2);
        ti = proto_tree_add_text(pdutree, tvb, offset, length,
                                 &quot;MPLS-Label%d: %u exp-bits: %u %s&quot;, level,
                                 ((b0&lt;&lt;12)+(b1&lt;&lt;4)+(b2&gt;&gt;4)),
                                 ((b2&gt;&gt;1)&amp;0x7),
                                 ((b2&amp;0x1)?&quot;top-of-stack&quot;:&quot;&quot;));
    } else {
        ti = proto_tree_add_text(pdutree, tvb, offset, length,
                                 &quot;MPLS-Label%d: bad length %d&quot;, level, length);
    }
    return ti;
}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '14, 17:44</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-35824" class="comments-container"><span id="36111"></span><div id="comment-36111" class="comment"><div id="post-36111-score" class="comment-score"></div><div class="comment-text"><p>Here's the hex for each label field in the flow export: <a href="http://imgur.com/a/FaTso#0">http://imgur.com/a/FaTso#0</a></p><p>I went ahead and filed a bug 10458. Thanks for your help!</p></div><div id="comment-36111-info" class="comment-info"><span class="comment-age">(09 Sep '14, 06:52)</span> <span class="comment-user userinfo">mplspackets</span></div></div><span id="36177"></span><div id="comment-36177" class="comment"><div id="post-36177-score" class="comment-score">1</div><div class="comment-text"><p>Fixed; See <a href="https://code.wireshark.org/review/#/c/4067/">https://code.wireshark.org/review/#/c/4067/</a></p></div><div id="comment-36177-info" class="comment-info"><span class="comment-age">(10 Sep '14, 10:07)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-35824" class="comment-tools"></div><div class="clear"></div><div id="comment-35824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

