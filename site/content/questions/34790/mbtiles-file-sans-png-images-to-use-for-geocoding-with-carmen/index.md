+++
type = "question"
title = "MBTiles file sans PNG images to use for geocoding (with carmen)"
description = '''Carmen does geocoding and is known to handle OSM data (and TIGER). If I want to geocode addresses in Germany, what are the steps? I&#x27;ve found so far:  resources http://giswiki.hsr.ch/MBTiles suggestions how to create a regular MBTiles file with all rendered images inside tools http://maperitive.net/d...'''
date = "2014-07-10T08:09:00Z"
lastmod = "2014-07-10T12:46:00Z"
weight = 34790
keywords = [ "sqlite", "carmen", "mbtiles" ]
aliases = [ "/questions/34790" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MBTiles file sans PNG images to use for geocoding (with carmen)](/questions/34790/mbtiles-file-sans-png-images-to-use-for-geocoding-with-carmen)

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
<span id="post-34790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34790-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Carmen does geocoding and is known to handle OSM data (and TIGER). If I want to geocode addresses in Germany, what are the steps?</p>
<p>I've found so far:</p>
<ul>
<li>resources <a href="http://giswiki.hsr.ch/MBTiles">http://giswiki.hsr.ch/MBTiles</a></li>
<li>suggestions how to create a regular MBTiles file with all rendered images inside</li>
<li>tools <a href="http://maperitive.net/docs/Commands/GenerateMBTiles.html">http://maperitive.net/docs/Commands/GenerateMBTiles.html</a> and <a href="https://github.com/mapbox/mbutil">https://github.com/mapbox/mbutil</a></li>
<li>related questions, like <a href="/questions/24828/how-can-i-easily-convert-osm-to-mbtiles-with-default-styles">https://help.openstreetmap.org/questions/24828/how-can-i-easily-convert-osm-to-mbtiles-with-default-styles</a> and <a href="http://stackoverflow.com/questions/23965409/how-do-i-download-mbtiles-project-data-from-my-mapbox-account">http://stackoverflow.com/questions/23965409/how-do-i-download-mbtiles-project-data-from-my-mapbox-account</a></li>
</ul>
<p>But I'll only do geocoding, and do not need GB of PNG images.</p>
<p>Maybe the easiest way is still to spend XX hours of fat server power to generate the images and then just delete the images-table from the MBTiles file (since it's sqlite-based)?</p>
<p>But there ought to be a better way. And, if allowed, I'd be happy to reward a less than XX hours solution :-)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sqlite" rel="tag" title="see questions tagged &#39;sqlite&#39;">sqlite</span> <span class="post-tag tag-link-carmen" rel="tag" title="see questions tagged &#39;carmen&#39;">carmen</span> <span class="post-tag tag-link-mbtiles" rel="tag" title="see questions tagged &#39;mbtiles&#39;">mbtiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '14, 08:09</strong></p>
<img src="https://secure.gravatar.com/avatar/1566633c958fd7cd2925e25390e33ff3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sesam&#39;s gravatar image" />
<p><span>sesam</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sesam has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jul '14, 08:25</strong> </span></p>
</div>
</div>
<div id="comments-container-34790" class="comments-container">
<span id="34794"></span>
<div id="comment-34794" class="comment">
<div id="post-34794-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Would it be possible to explain the reason why you're looking at the mbtiles approach when you're interested in geocoding? Apologies if I'm completely missing the point here...</p>
</div>
<div id="comment-34794-info" class="comment-info">
<span class="comment-age">(10 Jul '14, 11:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="34795"></span>
<div id="comment-34795" class="comment">
<div id="post-34795-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes. I need to geocode massive amounts of addresses, as well as support users doing searches. Can't pay several thousand dollars, not even hundreds of dollars per month. So no services/API:s are fast/cheap enough. Carmen is fast like Google and open source, so I'm trying to get data to use with Carmen.</p>
</div>
<div id="comment-34795-info" class="comment-info">
<span class="comment-age">(10 Jul '14, 11:29)</span> <span class="comment-user userinfo">sesam</span>
</div>
</div>
</div>
<div id="comment-tools-34790" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34790-form-container" class="comment-form-container">
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

<span id="34796"></span>

<div id="answer-container-34796" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34796-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well as I understand it (purely from reading the github readme!), <a href="https://github.com/mapbox/carmen">Carmen</a> depends on vector tiles, so mbtiles based on image tiles won't be useful. I'd start by going through the various vector tile presentations at <a href="https://sotm-eu.org/">SOTM-EU</a>, but be aware it's not exactly a "mature technology" yet. See the links from <a href="https://github.com/mapbox/mapnik-vector-tile">here</a> too.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '14, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-34796" class="comments-container">
<span id="34798"></span>
<div id="comment-34798" class="comment">
<div id="post-34798-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I have trouble digging up anything on sotm-eu.org; tried search and quick-reading the summaries at <a href="https://sotm-eu.org/en/program">https://sotm-eu.org/en/program</a> so now looking through the mapnik-vector-tile repo. In the carmen repo, "openstreetmap" is mentioned once (a config of which features to import) and that might also be a place to look. Digging further...</p>
</div>
<div id="comment-34798-info" class="comment-info">
<span class="comment-age">(10 Jul '14, 12:46)</span> <span class="comment-user userinfo">sesam</span>
</div>
</div>
</div>
<div id="comment-tools-34796" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34796-form-container" class="comment-form-container">
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

