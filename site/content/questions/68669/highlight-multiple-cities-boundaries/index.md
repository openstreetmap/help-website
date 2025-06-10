+++
type = "question"
title = "Highlight multiple cities boundaries"
description = '''Hello from Italy! I&#x27;m pretty new in OSM. I&#x27;m trying to highlight the boundaries of an area determineted by a list of cities. I know that every city have a relation number and I know how to extract the boundaries of a single city (using nominatim or geojson.io that looks better for me), but how can I...'''
date = "2019-04-05T23:05:00Z"
lastmod = "2019-04-24T08:15:00Z"
weight = 68669
keywords = [ "boundaries", "highlight", "boundary", "geojson" ]
aliases = [ "/questions/68669" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Highlight multiple cities boundaries](/questions/68669/highlight-multiple-cities-boundaries)

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
<span id="post-68669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68669-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello from Italy! I'm pretty new in OSM.</p>
<p>I'm trying to highlight the boundaries of an area determineted by a list of cities. I know that every city have a relation number and I know how to extract the boundaries of a single city (using nominatim or geojson.io that looks better for me), but how can I combine multiple cities in one single map?</p>
<p>LIST EXAMPLE:</p>
<p>Milano (relation 44915) Corsico (relation 44993) Rho (relation 44993)</p>
<p>Sometimes the list is longer than 30 cities.</p>
<p>Is there a way to make this? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-highlight" rel="tag" title="see questions tagged &#39;highlight&#39;">highlight</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Apr '19, 23:05</strong></p>
<img src="https://secure.gravatar.com/avatar/8fd10e3924e41387d5ccd750c71b2eef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="volo86&#39;s gravatar image" />
<p><span>volo86</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="volo86 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68669" class="comments-container">
&#10;</div>
<div id="comment-tools-68669" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68669-form-container" class="comment-form-container">
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

<span id="68682"></span>

<div id="answer-container-68682" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68682-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass-API is a straightforward way to <a href="http://overpass-turbo.eu/s/HLY">retrieve the data</a>, using a simple script that just asks for each relation:</p>
<pre><code>(
  rel(44915);
  rel(44993);
  rel(45188);
);
out geom;</code></pre>
<p>Overpass Turbo adds several export formats for data retrieved from Overpass-API, check the export button there. You could pick a suitable one and load that into geojson.io or such.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '19, 13:06</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-68682" class="comments-container">
<span id="68701"></span>
<div id="comment-68701" class="comment">
<div id="post-68701-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>oh thanks! it was so easy (for who know what is doing). Thanks again! Any hint about how to automatically retrieve relation id starting from city name?</p>
</div>
<div id="comment-68701-info" class="comment-info">
<span class="comment-age">(08 Apr '19, 08:20)</span> <span class="comment-user userinfo">volo86</span>
</div>
</div>
<span id="68702"></span>
<div id="comment-68702" class="comment">
<div id="post-68702-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>City name to relation ID can be done via a <a href="https://wiki.openstreetmap.org/wiki/Search_engines">geocoder</a>, for example <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a>.</p>
</div>
<div id="comment-68702-info" class="comment-info">
<span class="comment-age">(08 Apr '19, 09:12)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="68708"></span>
<div id="comment-68708" class="comment">
<div id="post-68708-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok, I understand that but I was wondering if is possibile to write the same code using the name of the city instead of the relation id (or create a spreadsheet where in column A I write the name of the city and in column B appear the rel id)</p>
</div>
<div id="comment-68708-info" class="comment-info">
<span class="comment-age">(08 Apr '19, 16:08)</span> <span class="comment-user userinfo">volo86</span>
</div>
</div>
<span id="68712"></span>
<div id="comment-68712" class="comment">
<div id="post-68712-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Something like <a href="http://overpass-turbo.eu/s/HO5">http://overpass-turbo.eu/s/HO5</a></p>
<p>The assumption that the cities you are looking for all have an admin_level=8 tag may break down.</p>
<p>The .searchArea stuff restricts the results to matches inside of Italy.</p>
</div>
<div id="comment-68712-info" class="comment-info">
<span class="comment-age">(08 Apr '19, 17:23)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-68682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68682-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68907"></span>

<div id="answer-container-68907" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68907-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am practicing with turbo overpass but I can't understand how to manage city names with the apostrophe or composed of two or more words (for example "Villa Sant'Angelo"). If I write "rel [admin_level = 8] [name = Villa Sant'Angelo] (area.searchArea);" overpass gives me an error. any suggestions? thank you</p>
<p>Edit: I understand that I need to replace spaces with underscore, but the problem remain for apostrophe.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '19, 08:15</strong></p>
<img src="https://secure.gravatar.com/avatar/8fd10e3924e41387d5ccd750c71b2eef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="volo86&#39;s gravatar image" />
<p><span>volo86</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="volo86 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '19, 08:27</strong> </span></p>
</div>
</div>
<div id="comments-container-68907" class="comments-container">
&#10;</div>
<div id="comment-tools-68907" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68907-form-container" class="comment-form-container">
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

