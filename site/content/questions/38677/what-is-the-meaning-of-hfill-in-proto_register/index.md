+++
type = "question"
title = "What is the meaning of HFILL in proto_register?"
description = '''While creating any plugin we have to register into wireshark. There is one method called proto_register_XXX() in this method predefined structure is used.in that one argument is HFILL . What is the meaning of that???'''
date = "2014-12-23T02:22:00Z"
lastmod = "2014-12-23T03:41:00Z"
weight = 38677
keywords = [ "ankit" ]
aliases = [ "/questions/38677" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the meaning of HFILL in proto\_register?](/questions/38677/what-is-the-meaning-of-hfill-in-proto_register)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38677-score" class="post-score" title="current number of votes">0</div><span id="post-38677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While creating any plugin we have to register into wireshark. There is one method called proto_register_XXX() in this method predefined structure is used.in that one argument is HFILL . What is the meaning of that???</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ankit" rel="tag" title="see questions tagged &#39;ankit&#39;">ankit</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '14, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p><span>ankit</span><br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></div></div><div id="comments-container-38677" class="comments-container"></div><div id="comment-tools-38677" class="comment-tools"></div><div class="clear"></div><div id="comment-38677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38682"></span>

<div id="answer-container-38682" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38682-score" class="post-score" title="current number of votes">0</div><span id="post-38682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>HFILL</code> is a macro which expands to some additional fields that are necessary for bookkeeping. You can find the definition in <code>epan/proto.h</code>:</p><pre><code>/**
 * HFILL initializes all the &quot;set by proto routines&quot; fields in a
 * _header_field_info. If new fields are added or removed, it should
 * be changed as necessary.
 */
#define HFILL -1, 0, HF_REF_TYPE_NONE, -1, NULL</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '14, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-38682" class="comments-container"></div><div id="comment-tools-38682" class="comment-tools"></div><div class="clear"></div><div id="comment-38682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

