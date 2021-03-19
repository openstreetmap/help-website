+++
type = "question"
title = "How do I register a field?"
description = '''Thanks! I used the private_data method and it worked perfectly. Another thing i would like to do is register the CIC i got, using proto_register function, to allow me to filter the capture files using cic as criteria. Is that possible? Sorry if this is a dumb question, my experience with wireshark i...'''
date = "2013-05-21T09:59:00Z"
lastmod = "2013-05-21T10:53:00Z"
weight = 21348
keywords = [ "field", "register" ]
aliases = [ "/questions/21348" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do I register a field?](/questions/21348/how-do-i-register-a-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21348-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Thanks!</p><p>I used the private_data method and it worked perfectly.</p><p>Another thing i would like to do is register the CIC i got, using proto_register function, to allow me to filter the capture files using cic as criteria.</p><p>Is that possible?</p><p>Sorry if this is a dumb question, my experience with wireshark is really limited.</p><p>What i did to build and show the cic is this:</p><pre><code>        cic = pinfo-&gt;private_data;

        cic = cic &lt;&lt; 8 | tvb_get_guint8(tvb, 0);

        cic_item = proto_tree_add_text(tup_tree, tvb, 0, 0, &quot;CIC: &quot;);

        proto_item_append_text(cic_item, &quot;%d&quot;, cic);</code></pre><p>Thanks again.</p></div><div id="question-tags" class="tags-container tags">field register</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '13, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/41cae5c8111115b7c81a5d2f5a624c14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Renan&#39;s gravatar image" /><p>Renan<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Renan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 21 May '13, 10:43</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-21348" class="comments-container"></div><div id="comment-tools-21348" class="comment-tools"></div><div class="clear"></div><div id="comment-21348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21351"></span>

<div id="answer-container-21351" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21351-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>(OK, that's a separate question, so I made it into a separate question; this is a Q&amp;A site, not a forum, so separate questions should be separate. The idea is that somebody who has a particular question can look here to see if it's already been answered and, if so, use the existing answer.)</p><p>The CIC appears to be a 16-bit field, displayed in decimal.</p><p>Therefore, you should:</p><ul><li>add to the list of <code>hf_</code> variables a variable named <code>hf_{protocol}_cic</code> (where {protocol} is the name of your protocol);</li><li><p>add to the list of named fields, passed to <code>proto_register_field_array()</code>, an entry</p><pre><code>{ &amp;hf_{protocol}_version, 
  { &quot;CIC&quot;, &quot;{protocol}.cic&quot;, FT_UINT16, BASE_DEC,
    NULL, 0x0, NULL, HFILL }},</code></pre></li><li><p>after you've calculated the CIC value by combining the value passed to you by the other protocol and the value extracted from your protocol's data, add it to the protocol tree with <code>proto_tree_add_uint(hf_{protocol}_cic, tup_tree, tab, 0, 0, cic);</code></p></li></ul><p>And that's it! You <em>might</em> want to pass <code>0, 1</code> rather than <code>0, 0</code>, so that the entry covers the byte from your protocol's data that's used in calculating the CIC, and you <em>might</em> want to do</p><pre><code>cic_item = proto_tree_add_uint(hf_{protocol}_cic, tup_tree, tab, 0, 0, cic);
PROTO_ITEM_SET_GENERATED(cic_item);</code></pre><p>to flag it as "generated" to indicate that it's not <em>solely</em> derived from your protocol's data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '13, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-21351" class="comments-container"><span id="21353"></span><div id="comment-21353" class="comment"><div id="post-21353-score" class="comment-score"></div><div class="comment-text"><p>My original answer-to-a-question-in-a-comment (before Guy wisely converted that comment into this new question; I'm leaving it as a comment because it's mostly redundant with Guy's more-complete answer above):</p><p>As the name implies, only protocols should be registered with <code>proto_register()</code>. To make fields filterable you need to add them with <code>proto_tree_add_item()</code> (preferred) or, for example (and which would actually be better in your case), <code>proto_tree_add_uint()</code>. The hf entry is what makes the field filterable.</p><p>(As a general note: anything you add to the tree with <code>proto_tree_add_text()</code> is not filterable; therefore that function is strongly discouraged except for some uses as described in README.developer.)</p></div><div id="comment-21353-info" class="comment-info"><span class="comment-age">(21 May '13, 11:10)</span> JeffMorriss ♦</div></div><span id="21370"></span><div id="comment-21370" class="comment"><div id="post-21370-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much Guy and Jeff, for the help. It worked great!</p><p>Just a small heads up, the <code>tree</code> argument on <code>proto_tree_add_uint()</code> comes first, like this:</p><p><code>proto_tree_add_uint(hf_{protocol}_cic, tup_tree, tab, 0, 0, cic);</code></p></div><div id="comment-21370-info" class="comment-info"><span class="comment-age">(22 May '13, 05:18)</span> Renan</div></div></div><div id="comment-tools-21351" class="comment-tools"></div><div class="clear"></div><div id="comment-21351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

