+++
type = "question"
title = "How to use multiple lines for one header field?"
description = '''The dissector that I&#x27;m working on includes a header that encodes a DAG. The easiest way to read a DAG in human-readable format is in a way where each node (maximum of 9 nodes) is converted to a string and placed on a different line. I am looking to implement in Wireshark something like: Destination ...'''
date = "2012-06-12T09:05:00Z"
lastmod = "2012-06-14T11:31:00Z"
weight = 11857
keywords = [ "field", "dissector", "multiple" ]
aliases = [ "/questions/11857" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to use multiple lines for one header field?](/questions/11857/how-to-use-multiple-lines-for-one-header-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11857-score" class="post-score" title="current number of votes">0</div><span id="post-11857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The dissector that I'm working on includes a header that encodes a DAG. The easiest way to read a DAG in human-readable format is in a way where each node (maximum of 9 nodes) is converted to a string and placed on a different line. I am looking to implement in Wireshark something like:</p><pre><code>Destination DAG:
     0x1-1234567890123456789012345678901234567890-1:
     0x2-123456789a123456789a123456789a123456789a-1;
     0x3-123456789b123456789b123456789b123456789b-0;</code></pre><p>Where the indentation denotes that the three nodes above are in the subtree of "Destination DAG."</p><p>Some things I have tried:</p><ul><li>proto-tree-add-string-format() with '\n' characters. However, anything after the first '\n' character is cut off from the display. Also, it looks like the Wireshark printf-like format functions want any %s arguments to be static const array of chars, not a variable.</li><li>Creating a new header field for each node. The problem here is that you can't have a header field without a name and an appended colon before the content.</li></ul><p>The closest that I have come to seeing another dissector that might be able to do this is the TCP options fields. There doesn't appear to be a field name anywhere (no colon), but the content looks static, which is not the case with my dissector.</p><pre><code>Options: (12 bytes)
    No-Operation (NOP)
    No-Operation (NOP)</code></pre><p>Is there a way to do this? Thanks in advance for any help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '12, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/e247e0fb9b9f23b4f23793ef6811d476?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cody&#39;s gravatar image" /><p><span>Cody</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cody has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jun '12, 09:11</strong> </span></p></div></div><div id="comments-container-11857" class="comments-container"></div><div id="comment-tools-11857" class="comment-tools"></div><div class="clear"></div><div id="comment-11857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11859"></span>

<div id="answer-container-11859" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11859-score" class="post-score" title="current number of votes">2</div><span id="post-11859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Cody has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><em>The problem here is that you can't have a header field without a name and an appended colon before the content.</em></p><p>Yes you can. Have a look at the <code>proto_tree_add_*_format()</code> functions. In your case, it looks like <code>proto_tree_add_string_format()</code> will do the job for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '12, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-11859" class="comments-container"><span id="11860"></span><div id="comment-11860" class="comment"><div id="post-11860-score" class="comment-score"></div><div class="comment-text"><p>Works perfectly, thank you. I got tripped up when the compiler complained about that function when it had only one argument, but I've worked out a solution.</p></div><div id="comment-11860-info" class="comment-info"><span class="comment-age">(12 Jun '12, 09:56)</span> <span class="comment-user userinfo">Cody</span></div></div><span id="11861"></span><div id="comment-11861" class="comment"><div id="post-11861-score" class="comment-score"></div><div class="comment-text"><p>Well, <code>proto_tree_add_string_format()</code> takes a minimum of 7 arguments, so by "only one argument" you presumably mean "only the format string argument".</p><p>If so, then note that the <em>ONLY</em> valid format argument for <em>any</em> printf-like function is a format string. If you want to print an arbitrary string, the way to do that is by having <code>"%s"</code> as the format string and having the arbitrary string be the <em>argument</em> to the format string, e.g.</p><pre><code>proto_tree_add_string_format(tree, hf_XXX, tvb, offset, length, &quot;%s&quot;, string);</code></pre><p><em>not</em></p><pre><code>proto_tree_add_string_format(..., offset, length, string);</code></pre></div><div id="comment-11861-info" class="comment-info"><span class="comment-age">(12 Jun '12, 15:58)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="11904"></span><div id="comment-11904" class="comment"><div id="post-11904-score" class="comment-score"></div><div class="comment-text"><p>Yes, I misspoke about the arguments, thank you. And I also tried what you suggest above with the following code:</p><pre><code>char *p =  strtok(buf, &quot;\n&quot;);

//proto_tree_add_string_format(tr, hf, tvb, off + (i * NODE_SIZE), NODE_SIZE,&quot;%s%s&quot;, p, &quot;&quot;);

proto_tree_add_string_format(tr, hf, tvb, off + (i * NODE_SIZE), NODE_SIZE, &quot;%s&quot;, p);</code></pre><p>And the call that is not commented out returns the error:</p><p><code>packet-xip.c:86:4: error: format not a string literal and no format arguments [-Werror=format-security]</code></p><p>Anything that I'm obviously missing here?</p></div><div id="comment-11904-info" class="comment-info"><span class="comment-age">(14 Jun '12, 11:15)</span> <span class="comment-user userinfo">Cody</span></div></div><span id="11905"></span><div id="comment-11905" class="comment"><div id="post-11905-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Anything that I'm obviously missing here?</p></blockquote><p>The "value" argument to <code>proto_tree_add_string_format()</code>. "add_string" means "add a string value to the protocol tree", and "format" means "but display it with the format and format arguments <em>after</em> the string value argument". Try</p><pre><code>proto_tree_add_string_format(tr, hf, tvb, off + (i * NODE_SIZE), NODE_SIZE, p, &quot;%s&quot;, p);</code></pre></div><div id="comment-11905-info" class="comment-info"><span class="comment-age">(14 Jun '12, 11:31)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-11859" class="comment-tools"></div><div class="clear"></div><div id="comment-11859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

