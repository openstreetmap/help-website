+++
type = "question"
title = "Display GPS position on a website with OSM (Java)"
description = '''Ok here&#x27;s the story so far... I&#x27;m a beginner programmer messing around with the GPS functionality on my browser, Google Chrome. I&#x27;m looking at different tutorials for displaying the current location of the user on a website @ W3schools and I decide to see it it were possible to do the same with Open...'''
date = "2015-06-05T13:17:00Z"
lastmod = "2015-06-05T13:31:00Z"
weight = 43416
keywords = [ "website", "browser", "html", "java", "gps" ]
aliases = [ "/questions/43416" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Display GPS position on a website with OSM (Java)](/questions/43416/display-gps-position-on-a-website-with-osm-java)

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
<span id="post-43416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43416-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Ok here's the story so far... I'm a beginner programmer messing around with the GPS functionality on my browser, Google Chrome. I'm looking at different tutorials for displaying the current location of the user on a website @ <a href="http://www.w3schools.com/html/tryit.asp?filename=tryhtml5_geolocation_map">W3schools</a> and I decide to see it it were possible to do the same with Open Street Map, instead of Google Maps. How can I utilize the OSM api to take the latitude and longitude returned from my browser? I've messed around with the default iframe offered by the OSM website, but to no avail. Any tips?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-browser" rel="tag" title="see questions tagged &#39;browser&#39;">browser</span> <span class="post-tag tag-link-html" rel="tag" title="see questions tagged &#39;html&#39;">html</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '15, 13:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ff30878c7e53e9f9d8c0a18ab24cafbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="roughlycuboid&#39;s gravatar image" />
<p><span>roughlycuboid</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="roughlycuboid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43416" class="comments-container">
&#10;</div>
<div id="comment-tools-43416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43416-form-container" class="comment-form-container">
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

<span id="43417"></span>

<div id="answer-container-43417" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43417-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For a bit of background about creating a simple browser-based map that uses map tiles from OSM, have a read of this:</p>
<p><a href="https://switch2osm.org/using-tiles/getting-started-with-leaflet/">https://switch2osm.org/using-tiles/getting-started-with-leaflet/</a></p>
<p>Leaflet (the Javascript library) supports a "locate" call - see <a href="http://leafletjs.com/reference.html">http://leafletjs.com/reference.html</a> . That allows you to centre the map display using the HTML Geolocation API.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '15, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-43417" class="comments-container">
&#10;</div>
<div id="comment-tools-43417" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43417-form-container" class="comment-form-container">
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

