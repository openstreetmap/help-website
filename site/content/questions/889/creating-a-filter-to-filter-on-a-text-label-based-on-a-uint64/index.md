+++
type = "question"
title = "Creating a filter to filter on a text label based on a UINT64"
description = '''I have a dissector that works correctly and I&#x27;m working on some usability features. Namely, I want to be able to filter on a 64 bit value using a text label.  For example, I would like to be filter on all orange objects in my protocol. e.g. myproto.id == orange where orange has an id that is 64 a bi...'''
date = "2010-11-09T14:38:00Z"
lastmod = "2010-11-20T10:06:00Z"
weight = 889
keywords = [ "filter", "dissector", "textlabel" ]
aliases = [ "/questions/889" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Creating a filter to filter on a text label based on a UINT64](/questions/889/creating-a-filter-to-filter-on-a-text-label-based-on-a-uint64)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-889-score" class="post-score" title="current number of votes">0</div><span id="post-889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a dissector that works correctly and I'm working on some usability features. Namely, I want to be able to filter on a 64 bit value using a text label.<br />
</p><p>For example, I would like to be filter on all orange objects in my protocol. e.g. myproto.id == orange where orange has an id that is 64 a bit integer.</p><p>I've looked in the manual section 9.2.3. "Improving the dissection information" and tried to follow that. But I'm getting the error "Err Field 'ID' (myproto.id) has a 'strings' value but is of type FT_UINT64 (which is not allowed to have strings)"</p><p>My code looks like</p><p>static const value_string IDnames[] = { { 1736646964, "Orange" }, { 1022267019, "Red" }, { 2033618120, "Green" }, };</p><p>My header fields looks like { &amp;hf_IDPath, { "ID ", "myproto.id", FT_UINT64, BASE_DEC, VALS(IDnames), 0x0, NULL, HFILL } },</p><p>Am I just going about this wrong way or is filtering by label on a 64 bit integer not allowed? I'm also curious about the behavior of Wireshark if it looks up the id and it isn't in the array of value_strings.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-textlabel" rel="tag" title="see questions tagged &#39;textlabel&#39;">textlabel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '10, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p><span>tlann</span><br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span> </br></p></div></div><div id="comments-container-889" class="comments-container"></div><div id="comment-tools-889" class="comment-tools"></div><div class="clear"></div><div id="comment-889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="905"></span>

<div id="answer-container-905" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-905-score" class="post-score" title="current number of votes">1</div><span id="post-905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tlann has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The value_string stuff was added to Wireshark (back when it was called Ethereal) before we had support for 64-bit integers (we didn't want to require that compilers support it then), so it didn't support 64-bit integers. This means that you can't associate a value_string table with an FT_UINT64 or an FT_INT64; so</p><p>1) you can't have protocol tree entries for those fields show a label based on the value</p><p>and</p><p>2) you can't use labels when filtering on them.</p><p>If you have a field that <em>does</em> support value_strings, and the field has a value_string, but the value of the field isn't in one of the value_string entries, the field will just be displayed with its numerical value, and possibly with the label shown as "Unknown".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '10, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-905" class="comments-container"><span id="932"></span><div id="comment-932" class="comment"><div id="post-932-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer.<br />
With 64 bit machines I could see more and more use for 64 bit value_strings in the future. Is there talk of supporting this in the future?</p></div><div id="comment-932-info" class="comment-info"><span class="comment-age">(12 Nov '10, 10:49)</span> <span class="comment-user userinfo">tlann</span></div></div><span id="1042"></span><div id="comment-1042" class="comment"><div id="post-1042-score" class="comment-score"></div><div class="comment-text"><p>Preparing a parch with a new values_string_ext_64 and the needed supporting routines(match_.. etc) and submiting it at https://bugs.wireshark.org/bugzilla would be a good start.</p></div><div id="comment-1042-info" class="comment-info"><span class="comment-age">(20 Nov '10, 10:06)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-905" class="comment-tools"></div><div class="clear"></div><div id="comment-905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

