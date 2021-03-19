+++
type = "question"
title = "How should I register a header field that only shows a string?"
description = '''Hi I&#x27;m creating a header item that says &quot;General Information&quot;, and I also made a subtree on this item. The thing is, I don&#x27;t know how to set its registration infoamtion in hf_register_info, to be exact, the FIELDNAME and ABBREVIATION field. This is my code for creating the item: proto_item *gi = pro...'''
date = "2017-07-20T01:01:00Z"
lastmod = "2017-07-20T18:39:00Z"
weight = 62911
keywords = [ "field", "registration" ]
aliases = [ "/questions/62911" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How should I register a header field that only shows a string?](/questions/62911/how-should-i-register-a-header-field-that-only-shows-a-string)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62911-score" class="post-score" title="current number of votes">0</div><span id="post-62911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I'm creating a header item that says "General Information", and I also made a subtree on this item. The thing is, I don't know how to set its registration infoamtion in hf_register_info, to be exact, the FIELDNAME and ABBREVIATION field.</p><p>This is my code for creating the item:</p><pre><code>proto_item *gi = proto_tree_add_string(afdx_tree, hf_gi, tvb, 0, 0, &quot;General Information&quot;);</code></pre><p>This is the hf_register_info</p><pre><code>{ &amp;hf_gi,
//      What to put here       and here
    { &quot;General Information&quot;, &quot;foo.gi&quot;,
    FT_STRING, STR_ASCII,
    NULL, 0x0,
    NULL, HFILL }
},</code></pre><p>Also, sometimes I want to handle display manually. Is calling <code>proto_tree_add_string()</code> with self-generated string the right(wireshark's) way to do it? The information I wish to present require more input data than allowed by BASE_CUSTOM, which calls <code>void func(gchar*, guint32)</code>, and only takes one input directly excerpted from the raw packet</p><p>Thank you all for your help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-registration" rel="tag" title="see questions tagged &#39;registration&#39;">registration</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jul '17, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/4222adcf6d70b2c359746d893f30c045?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nickzhang&#39;s gravatar image" /><p><span>nickzhang</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nickzhang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jul '17, 01:04</strong> </span></p></div></div><div id="comments-container-62911" class="comments-container"></div><div id="comment-tools-62911" class="comment-tools"></div><div class="clear"></div><div id="comment-62911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62921"></span>

<div id="answer-container-62921" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62921-score" class="post-score" title="current number of votes">0</div><span id="post-62921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nickzhang has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What to put here and here</p></blockquote><p>If by "here" and "here" you mean "for FIELDNAME" and "for ABBREVIATION", there's nothing special about strings - if the field is called "general information" in descriptions of the protocol, either "General information" or "General Information" is an appropriate FIELDNAME and, if the protocol's abbreviation is "foo", then "foo.gi" or "foo.general_information" would be an appropriate ABBREVIATION, and that'd be the case if it were a string or a number or....</p><blockquote><p>Also, sometimes I want to handle display manually. Is calling <code>proto_tree_add_string()</code> with self-generated string the right(wireshark's) way to do it?</p></blockquote><p>If the value of the string is exactly what appears in the packet, and you just want to change the way it's <em>displayed</em>, <code>proto_tree_add_string_format_value()</code> is probably the right way to do it. Use <code>proto_tree_add_string()</code> only if the actual <em>value</em> is something you'd need to compute from the contents of the packet rather than just being what's in the packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '17, 04:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-62921" class="comments-container"><span id="62941"></span><div id="comment-62941" class="comment"><div id="post-62941-score" class="comment-score"></div><div class="comment-text"><p>This answers my question, thank you.</p></div><div id="comment-62941-info" class="comment-info"><span class="comment-age">(20 Jul '17, 18:39)</span> <span class="comment-user userinfo">nickzhang</span></div></div></div><div id="comment-tools-62921" class="comment-tools"></div><div class="clear"></div><div id="comment-62921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

