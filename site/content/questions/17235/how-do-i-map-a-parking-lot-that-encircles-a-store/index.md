+++
type = "question"
title = "How do I map a parking lot that encircles a store?"
description = '''A lot of shopping center developments have &quot;outlot&quot; stores (often restaurants), and sometimes completely stand-alone buildings will also have parking lots that entirely circle the building. I can see three plausible ways to map this:  Make the parking lot a solid rectangle (or whatever) and map the ...'''
date = "2012-10-28T19:43:00Z"
lastmod = "2012-10-28T22:10:00Z"
weight = 17235
keywords = [ "building", "topology", "parking" ]
aliases = [ "/questions/17235" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I map a parking lot that encircles a store?](/questions/17235/how-do-i-map-a-parking-lot-that-encircles-a-store)

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
<span id="post-17235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17235-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A lot of shopping center developments have "outlot" stores (often restaurants), and sometimes completely stand-alone buildings will also have parking lots that entirely circle the building. I can see three plausible ways to map this:</p>
<ol>
<li>Make the parking lot a solid rectangle (or whatever) and map the building as being contained in the parking lot</li>
<li>Make the parking lot shaped like a C-clamp and close that gap with a self-edge (i.e. faking up a 'hole' in the parking lot but keeping it topologically simple), then put the building inside the "hole"</li>
<li>Make the parking lot actually have a hole in it, and put the building inside the hole.</li>
</ol>
<p>The first is unquestionably the easiest to do, but it is semantically unsatisfying (and also doesn't render very well in some cases). The second is a bit more work, is also a little unsatisfying but at least the building isn't "in" the parking lot. The third I'm not even sure how to do in something like Potlatch, but it's certainly more technically complicated; but semantically it seems to be the best match, if it's technically possible.</p>
<p>What is the received wisdom on this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-topology" rel="tag" title="see questions tagged &#39;topology&#39;">topology</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '12, 19:43</strong></p>
<img src="https://secure.gravatar.com/avatar/4a4c8a91603aa21e05f5a441d5c13f26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blahedo&#39;s gravatar image" />
<p><span>blahedo</span><br />
<span class="score" title="736 reputation points">736</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blahedo has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-17235" class="comments-container">
&#10;</div>
<div id="comment-tools-17235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17235-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="17239"></span>

<div id="answer-container-17239" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17239-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-17239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="blahedo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your third option - make a hole in the parking lot and put the building inside the hole - is the correct and commonly used approach. Areas with holes are modelled as <strong>multipolygon relations</strong> in OSM. It's possible to create these with all of the mainstream editors.</p>
<p>Refer to the <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">Relation:multipolygon</a> wiki page for documentation, including Potlatch examples.</p>
<p>If the parking lot is directly adjacent to the building, you can re-use the building outline as the multipolygon's "inner" member.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '12, 20:33</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-17239" class="comments-container">
<span id="17241"></span>
<div id="comment-17241" class="comment">
<div id="post-17241-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, cool. Potlatch doesn't seem to be rendering it correctly but the data looks like it's in there (we'll see what Mapnik does with it).</p>
</div>
<div id="comment-17241-info" class="comment-info">
<span class="comment-age">(28 Oct '12, 22:10)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
</div>
<div id="comment-tools-17239" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17239-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17237"></span>

<div id="answer-container-17237" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17237-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Third option is the way to go. You can use <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">multipolygon relations</a> for it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '12, 20:13</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-17237" class="comments-container">
&#10;</div>
<div id="comment-tools-17237" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17237-form-container" class="comment-form-container">
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

