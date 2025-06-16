+++
type = "question"
title = "Missing amenity name in mapnik - bug or feature?"
description = '''I recently added two pubs (that are in the same building) to the map and both showed up quite fast. But one got rendered without the name even though the name is there and there is place for it. Does this have some deeper meaning or is it a bug? If so - how should it be reported?  Permalink'''
date = "2011-07-23T20:34:00Z"
lastmod = "2011-07-24T18:37:00Z"
weight = 6521
keywords = [ "rendering", "name", "mapnik" ]
aliases = [ "/questions/6521" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Missing amenity name in mapnik - bug or feature?](/questions/6521/missing-amenity-name-in-mapnik-bug-or-feature)

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
<span id="post-6521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6521-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-6521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently added two pubs (that are in the same building) to the map and both showed up quite fast. But one got rendered without the name even though the name is there and there is place for it. Does this have some deeper meaning or is it a bug? If so - how should it be reported?</p>
<p><img src="http://b.tile.openstreetmap.org/18/143161/89796.png" alt="name missing" /></p>
<p><a href="https://www.openstreetmap.org/?lat=49.206109&amp;lon=16.602617&amp;zoom=18&amp;layers=M">Permalink</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '11, 20:34</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jul '11, 18:39</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span></p>
</div>
</div>
<div id="comments-container-6521" class="comments-container">
&#10;</div>
<div id="comment-tools-6521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6521-form-container" class="comment-form-container">
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

<span id="6522"></span>

<div id="answer-container-6522" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6522-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-6522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LM_1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is not a bug. Currently <a href="https://wiki.openstreetmap.org/wiki/Mapnik">mapnik</a> (the main renderer for OSM) isn't really smart about symbols and names that are very close to each other so it will sometimes leave the name or even the symbol out if they would overlap otherwise. You can activate the <a href="https://wiki.openstreetmap.org/wiki/Osmarender">osmarender</a> layer to see the same map rendered by an alternative program which does not have this "feature" and leads in more detailed areas to overlapping names which isn't very nice, too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '11, 20:48</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '11, 20:51</strong> </span></p>
</div>
</div>
<div id="comments-container-6522" class="comments-container">
&#10;</div>
<div id="comment-tools-6522" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6522-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6534"></span>

<div id="answer-container-6534" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6534-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not really a bug, but is due to mapnik limitations. Fortunately for all of us there is current work in progress to overcome these limitations. In his GoogleSummerofCode Project Hermann Kraus is doing the coding for better text placement: <a href="http://mapnik.org/news/2011/jul/13/new_text_placement_system/">http://mapnik.org/news/2011/jul/13/new_text_placement_system/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '11, 18:37</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-6534" class="comments-container">
&#10;</div>
<div id="comment-tools-6534" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6534-form-container" class="comment-form-container">
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

