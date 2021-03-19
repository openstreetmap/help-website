+++
type = "question"
title = "Post Dissector in C - is it possible?"
description = '''I have some experience of writing a post dissector using LUA. Is it possible to write an equivalent as a C plugin i.e. a dissector that receives control after all other dissectors have been executed? Thanks and regards...Paul'''
date = "2015-11-08T14:11:00Z"
lastmod = "2015-11-09T23:50:00Z"
weight = 47414
keywords = [ "postdissector" ]
aliases = [ "/questions/47414" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Post Dissector in C - is it possible?](/questions/47414/post-dissector-in-c-is-it-possible)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47414-score" class="post-score" title="current number of votes">0</div><span id="post-47414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have some experience of writing a post dissector using LUA. Is it possible to write an equivalent as a C plugin i.e. a dissector that receives control after all other dissectors have been executed?</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-postdissector" rel="tag" title="see questions tagged &#39;postdissector&#39;">postdissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '15, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Nov '15, 03:03</strong> </span></p></div></div><div id="comments-container-47414" class="comments-container"></div><div id="comment-tools-47414" class="comment-tools"></div><div class="clear"></div><div id="comment-47414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47426"></span>

<div id="answer-container-47426" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47426-score" class="post-score" title="current number of votes">1</div><span id="post-47426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PaulOfford has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, that's what <code>void register_postdissector(dissector_handle_t);</code> is intended for, see <code>epan/packet.h</code>. Currently there's limited use in the main distribution, other than PRP (but dissection disabled by default) and the MATE plugin, which may be a good example.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '15, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-47426" class="comments-container"><span id="47427"></span><div id="comment-47427" class="comment"><div id="post-47427-score" class="comment-score"></div><div class="comment-text"><p>Well that's embarrassing. I don't know how I missed that. Thanks Jaap.</p></div><div id="comment-47427-info" class="comment-info"><span class="comment-age">(09 Nov '15, 04:17)</span> <span class="comment-user userinfo">PaulOfford</span></div></div><span id="47451"></span><div id="comment-47451" class="comment"><div id="post-47451-score" class="comment-score"></div><div class="comment-text"><p>Tried it and it works a treat.</p></div><div id="comment-47451-info" class="comment-info"><span class="comment-age">(09 Nov '15, 23:50)</span> <span class="comment-user userinfo">PaulOfford</span></div></div></div><div id="comment-tools-47426" class="comment-tools"></div><div class="clear"></div><div id="comment-47426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

