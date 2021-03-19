+++
type = "question"
title = "col_set_str method does not work on plugin"
description = '''Hello, i have recentrly tried to write a plugin for my wireshark in C following the manuals in the doc/ directory (readme.dissector, readme.plugins). Everything works fine, my dissector is registered and also the tree elements are added to the display. However the col_set_str method does not provide...'''
date = "2016-02-25T02:21:00Z"
lastmod = "2016-02-26T04:53:00Z"
weight = 50499
keywords = [ "column", "dissector", "plugins" ]
aliases = [ "/questions/50499" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [col\_set\_str method does not work on plugin](/questions/50499/col_set_str-method-does-not-work-on-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50499-score" class="post-score" title="current number of votes">0</div><span id="post-50499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>i have recentrly tried to write a plugin for my wireshark in C following the manuals in the doc/ directory (readme.dissector, readme.plugins). Everything works fine, my dissector is registered and also the tree elements are added to the display. However the col_set_str method does not provide any visible results in the col_set_str.</p><p>The method call looks like this:</p><pre><code>col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;foo&quot;);
col_clear(pinfo-&gt;cinfo, COL_INFO);</code></pre><p>The method gets called 100% since other method calls after col_set_str are executed normally. I also tried registering my dissector via register_postdissector instead adding it to the tcp-port-table however the results are still the same.</p><p>Has anyone made similar experiences so far or could help me out?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-column" rel="tag" title="see questions tagged &#39;column&#39;">column</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '16, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/ce595bcaea627c29ed0222d44eccb874?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wodka&#39;s gravatar image" /><p><span>Wodka</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wodka has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Feb '16, 02:24</strong> </span></p></div></div><div id="comments-container-50499" class="comments-container"><span id="50503"></span><div id="comment-50503" class="comment"><div id="post-50503-score" class="comment-score"></div><div class="comment-text"><p>Are your col statements under if(tree)? That will not work.</p></div><div id="comment-50503-info" class="comment-info"><span class="comment-age">(25 Feb '16, 04:05)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="50526"></span><div id="comment-50526" class="comment"><div id="post-50526-score" class="comment-score"></div><div class="comment-text"><p>Nope, i am using the method right under the declarations of the proto_tree and proto_item variables.</p><p>static int dissect_foo(tvbuff_t <em>tvb, packet_info</em> pinfo, proto_tree <em>tree, void</em> data <em>U</em>) {</p><pre><code>proto_tree *protocol_subtree;
    proto_item *protocol_item;

    /* Set the Protocol column to the constant string of foo */
col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;foo&quot;);</code></pre><p>.....</p></div><div id="comment-50526-info" class="comment-info"><span class="comment-age">(25 Feb '16, 23:32)</span> <span class="comment-user userinfo">Wodka</span></div></div><span id="50531"></span><div id="comment-50531" class="comment"><div id="post-50531-score" class="comment-score"></div><div class="comment-text"><p>So what is shown in the protocol column? The protocol your protocol is running on top of or? How is your protocol dissector called? By adding it to the TCP or UDP port table?</p></div><div id="comment-50531-info" class="comment-info"><span class="comment-age">(26 Feb '16, 03:55)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="50533"></span><div id="comment-50533" class="comment"><div id="post-50533-score" class="comment-score"></div><div class="comment-text"><p>I call it on top of the TCP Dissector, adding it to a certain port. The column string still is the TCP string.</p></div><div id="comment-50533-info" class="comment-info"><span class="comment-age">(26 Feb '16, 04:35)</span> <span class="comment-user userinfo">Wodka</span></div></div><span id="50535"></span><div id="comment-50535" class="comment"><div id="post-50535-score" class="comment-score"></div><div class="comment-text"><p>I used col_str() myself in a custom plugin running on top of TCP without any issue with both Wireshark 1.12.X and Wireshark 2.X. As you are the very first one to report such issue, and as we do not have much info yet, that would be helpful if you could execute the code step by step with a debugger to see what could be wrong as I fear no one will be able to help you without more info.</p></div><div id="comment-50535-info" class="comment-info"><span class="comment-age">(26 Feb '16, 04:53)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-50499" class="comment-tools"></div><div class="clear"></div><div id="comment-50499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

