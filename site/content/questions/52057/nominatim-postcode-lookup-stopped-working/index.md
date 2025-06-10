+++
type = "question"
title = "Nominatim postcode lookup stopped working"
description = '''Until recently I have been able to lookup postcodes using Nominatim. However this has stopped working recently when I search a variety of postcodes. Is this a change in the way Nominatim works or am I missing something else? Example: http://nominatim.openstreetmap.org/search.php?q=BN3+6AH This query...'''
date = "2016-09-15T10:30:00Z"
lastmod = "2016-09-18T10:47:00Z"
weight = 52057
keywords = [ "nominatim", "postcode" ]
aliases = [ "/questions/52057" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim postcode lookup stopped working](/questions/52057/nominatim-postcode-lookup-stopped-working)

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
<span id="post-52057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52057-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Until recently I have been able to lookup postcodes using Nominatim. However this has stopped working recently when I search a variety of postcodes. Is this a change in the way Nominatim works or am I missing something else?</p>
<p>Example: <a href="http://nominatim.openstreetmap.org/search.php?q=BN3+6AH">http://nominatim.openstreetmap.org/search.php?q=BN3+6AH</a></p>
<p>This query should find an area in Hove and it used to, but now instead Nominatim does not find any results.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '16, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/140fffb934f90426f52019d123175a83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sam10&#39;s gravatar image" />
<p><span>sam10</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sam10 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52057" class="comments-container">
&#10;</div>
<div id="comment-tools-52057" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52057-form-container" class="comment-form-container">
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

<span id="52095"></span>

<div id="answer-container-52095" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52095-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Postcode searches only work if there was at least one address with that addr:postcode in the database when the Nominatim database was last imported from scratch (currently December 2015). Your example postcode probably was once tagged on a pub or shop which has been deleted when it closed down. When the database was reimported in December, the postcode then disappeared also from the search index.</p>
<p>We are currently working on keeping postcodes always up-to-date with the OSM data. For progress on that front have a look at <a href="https://github.com/twain47/Nominatim/issues/403">the github issue on postcodes</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '16, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-52095" class="comments-container">
&#10;</div>
<div id="comment-tools-52095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52095-form-container" class="comment-form-container">
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

