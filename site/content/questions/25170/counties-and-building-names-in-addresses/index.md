+++
type = "question"
title = "Counties and Building Names In Addresses"
description = '''When Filling in an address for a retail building should the key addr:housename be used? Would it be better to use the building:name and leave that? Also, what should the county be under addr:province, addr:state or something else like aadr:county? To clarify this is in the case where the building ha...'''
date = "2013-08-10T18:09:00Z"
lastmod = "2013-08-10T21:15:00Z"
weight = 25170
keywords = [ "adresses" ]
aliases = [ "/questions/25170" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Counties and Building Names In Addresses](/questions/25170/counties-and-building-names-in-addresses)

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
<span id="post-25170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25170-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When Filling in an address for a retail building should the key addr:housename be used? Would it be better to use the building:name and leave that? Also, what should the county be under addr:province, addr:state or something else like aadr:county?</p>
<p>To clarify this is in the case where the building has a name which is not it's official address name (if that makes sense)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-adresses" rel="tag" title="see questions tagged &#39;adresses&#39;">adresses</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '13, 18:09</strong></p>
<img src="https://secure.gravatar.com/avatar/981c43f1f8dee2453ed3aaa01cd5e27f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_P&#39;s gravatar image" />
<p><span>John_P</span><br />
<span class="score" title="226 reputation points">226</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_P has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Aug '13, 18:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-25170" class="comments-container">
&#10;</div>
<div id="comment-tools-25170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25170-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="25179"></span>

<div id="answer-container-25179" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25179-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="John_P has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>When Filling in an address for a retail building should the key addr:housename be used? Would it be better to use the building:name and leave that?</p>
</blockquote>
<p>There is some overlap between the tags <code>name=</code> and <code>addr:housename=</code>. Usually you use <code>name</code> if the name refers to the organization/users of the building, and <code>housename</code> if the building itself has a special name - especially if that name is also used as the building's address. So <code>housename</code> might be appropriate in your case.</p>
<blockquote>
<p>Also, what should the county be under addr:province, addr:state or something else like aadr:county?</p>
</blockquote>
<p>Generally there's no need to fill in things like county, state etc.. These administrative areas usually exist as areas in the OSM data, so it's easy to calculate which one an address belongs to.</p>
<p>Normally it's enough to fill in <code>addr:housenumber</code>, <code>addr:street</code> and <code>addr:postcode</code>, the rest can be derived.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '13, 21:15</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-25179" class="comments-container">
&#10;</div>
<div id="comment-tools-25179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25179-form-container" class="comment-form-container">
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

