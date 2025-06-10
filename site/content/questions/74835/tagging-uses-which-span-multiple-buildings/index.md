+++
type = "question"
title = "Tagging uses which span multiple buildings"
description = '''I am mapping in Central London where over time, many individual buildings have been amalgamated into single larger buildings. There are examples of terraced houses which have had a front door permanently locked, and an opening made in a party wall. Or multiple buildings without internal connection w...'''
date = "2020-05-15T14:42:00Z"
lastmod = "2020-05-15T23:07:00Z"
weight = 74835
keywords = [ "building", "ownership" ]
aliases = [ "/questions/74835" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Tagging uses which span multiple buildings](/questions/74835/tagging-uses-which-span-multiple-buildings)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74835-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am mapping in Central London where over time, many individual buildings have been amalgamated into single larger buildings. There are examples of terraced houses which have had a front door permanently locked, and an opening made in a party wall. Or multiple buildings without internal connection which are one hotel.</p>
<p>How should I map these buildings? To capture the urban grain correctly often terraces need to be split into their constituent buildings (for addresses as well). But how can I indicate for example that one hotel spans two consecutive buildings?</p>
<p>Or in other words, how can I indicate that two different buildings have the same ownership and use, even if they really are different buildings with different addresses?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-ownership" rel="tag" title="see questions tagged &#39;ownership&#39;">ownership</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '20, 14:42</strong></p>
<img src="https://secure.gravatar.com/avatar/19d95386711430cdb0d54618ebaeb54a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="owenward&#39;s gravatar image" />
<p><span>owenward</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="owenward has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74835" class="comments-container">
&#10;</div>
<div id="comment-tools-74835" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74835-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="74836"></span>

<div id="answer-container-74836" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74836-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="owenward has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no really good solution for such scenarios outside of using a site relation <a href="https://wiki.openstreetmap.org/wiki/Relation:site">https://wiki.openstreetmap.org/wiki/Relation:site</a></p>
<p>Unluckily it isn't very well supported, so as a tendency I would simply add a node for the amenity/shop/ whatever in a suitable location and not add such tags to the buildings themselves.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '20, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-74836" class="comments-container">
&#10;</div>
<div id="comment-tools-74836" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74836-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74844"></span>

<div id="answer-container-74844" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74844-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the two buildings are adjacent or if the space between the buildings also belongs to the hotel you can just draw a closed way around the perimeter and add the hotel tags to that way. The individual buildings would be tagged with building=hotel but without the <code>tourism=hotel</code> tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '20, 22:08</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-74844" class="comments-container">
<span id="74846"></span>
<div id="comment-74846" class="comment">
<div id="post-74846-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In OP's case, it should probably be <code>building:use=hotel</code> with <code>building=house</code> (after splitting the <code>building=terrace</code>), or whatever <code>building=*</code> it was built as.</p>
</div>
<div id="comment-74846-info" class="comment-info">
<span class="comment-age">(15 May '20, 22:57)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-74844" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74844-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74847"></span>

<div id="answer-container-74847" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74847-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Or in other words, how can I indicate that two different buildings have the same ownership and use, even if they really are different buildings with different addresses?</p>
</blockquote>
<p>You need to realize some tags represents properties (viz <code>owner=</code>), instead of making the object some feature (viz a <code>tourism=hotel</code>). Many buildings can have the same owner or operator, as in this example. Therefore, you can add <code>building:use=hotel</code> (as I commented above) no problem whatsoever, and <code>owner=*</code> (or <code>operator=</code> - be careful in their difference and verification) exhaustively, to all the appropriate buildings.</p>
<blockquote>
<p>But how can I indicate for example that one hotel spans two consecutive buildings?</p>
</blockquote>
<p>I have to admit sometimes I feel quite confused as to when I am "allowed" to use relation:site, relation:multipolygon, et al first: For the sake of purity, I have the impression one can draw new, untagged areas overlapping the individual buildings to make a <code>type=multipolygon</code> here.</p>
<p>As I understand, in principle, <code>type=multipolugon</code> can't represent hierarchies (it's only an area afterall), and <code>type=site</code> is much restricted in usage theoretically (as proposed). There are a few proposals drafted in the past decade with the aim of resolving these issues, that are even more unsupported than <code>type=site</code> (basically none, merely <code>relation</code> objects hanging around).</p>
<p>Add <code>addr:housename=</code> to the individual buildings, if applicable under your jurisdiction and community guidelines, to be the clearest possible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '20, 23:07</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 May '20, 23:15</strong> </span></p>
</div>
</div>
<div id="comments-container-74847" class="comments-container">
&#10;</div>
<div id="comment-tools-74847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74847-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

