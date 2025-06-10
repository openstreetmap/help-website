+++
type = "question"
title = "Best way to get all cities of a specific area?"
description = '''I&#x27;m just starting to play with the databases (Nominatim, Mapnik), but I&#x27;m a little bit confused about such an easy task: &quot;How to get a list of all cities in Germany?&quot; Nominatim: It could be so easy, but of course it is not. If I search all states of Germany, I get a only 13 back (of 16!). Why? Becau...'''
date = "2012-04-27T12:10:00Z"
lastmod = "2012-05-03T09:41:00Z"
weight = 12388
keywords = [ "nominatim", "postgresql", "mapnik", "postgis", "database" ]
aliases = [ "/questions/12388" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Best way to get all cities of a specific area?](/questions/12388/best-way-to-get-all-cities-of-a-specific-area)

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
<span id="post-12388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12388-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm just starting to play with the databases (Nominatim, Mapnik), but I'm a little bit confused about such an easy task: <em>"How to get a list of all cities in Germany?"</em></p>
<p><strong>Nominatim:</strong> It could be so easy, but of course it is not. If I search all states of Germany, I get a only 13 back (of 16!). Why? Because the others do have "Deutschland" instead of "Germany" in their "isin"-column or just nothing.</p>
<p><strong>Mapnik:</strong> I suppose the "savest" way would be to find all city-Points inside the "Germany"-polygon? But I can't even find the Germany-polygon. I only found the Germany-point. How do I do this?</p>
<p>Or am I doing it totally wrong? What would be your approach?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '12, 12:10</strong></p>
<img src="https://secure.gravatar.com/avatar/49f0c5218671e039c889fc520ea55a92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="np00&#39;s gravatar image" />
<p><span>np00</span><br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="np00 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Apr '12, 12:11</strong> </span></p>
</div>
</div>
<div id="comments-container-12388" class="comments-container">
&#10;</div>
<div id="comment-tools-12388" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12388-form-container" class="comment-form-container">
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

<span id="12389"></span>

<div id="answer-container-12389" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12389-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="np00 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Several possible approaches:</p>
<ol>
<li>Import data into database then make queries, like you tried.</li>
<li>Don't import data but instead use someone else's database - see XAPI or Overpass. (The latter can indeed limit a search to a boundary polygon, and an easy way of finding the Germany relation is typing "openstreetmap relation germany" into Google.)</li>
<li>Don't use a database at all; download a suitable extract (e.g. from download.geofabrik.de), cut out an area if required using osmosis or similar (not required if you want all of Germany since there's already an extract for that), and then use osmosis or osmfilter to extract the objects you need.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '12, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12389" class="comments-container">
<span id="12390"></span>
<div id="comment-12390" class="comment">
<div id="post-12390-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Because I'm planning to get used to the databases, I will focus on the first approach.</p>
<p>Is my assumtion for the mapnik-database true? Could you help/lead me with that?</p>
<p>Thanks for the quick response!</p>
</div>
<div id="comment-12390-info" class="comment-info">
<span class="comment-age">(27 Apr '12, 12:30)</span> <span class="comment-user userinfo">np00</span>
</div>
</div>
<span id="12520"></span>
<div id="comment-12520" class="comment">
<div id="post-12520-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Mapnik is out of point here. Mapnik is the software used for rendering the data from a postgis database. You need to import the OSM data in a postgis database.</p>
</div>
<div id="comment-12520-info" class="comment-info">
<span class="comment-age">(03 May '12, 09:41)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
</div>
<div id="comment-tools-12389" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12389-form-container" class="comment-form-container">
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

