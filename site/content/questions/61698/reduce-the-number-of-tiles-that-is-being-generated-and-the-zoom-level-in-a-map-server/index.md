+++
type = "question"
title = "Reduce the number of tiles that is being generated and the zoom level in a map server."
description = '''I am trying to create a docker container which can be run on docker to host a local mapserver, the problem i am facing is even with a small country data like bhutan-latest-osm.pbf which is around 200MB large, the docker container&#x27;s size is shooting up to 4.5GB, this is just for development in actual...'''
date = "2018-01-18T10:55:00Z"
lastmod = "2018-01-22T06:37:00Z"
weight = 61698
keywords = [ "openstreetmap", "renderd", "mod_tile" ]
aliases = [ "/questions/61698" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reduce the number of tiles that is being generated and the zoom level in a map server.](/questions/61698/reduce-the-number-of-tiles-that-is-being-generated-and-the-zoom-level-in-a-map-server)

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
<span id="post-61698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61698-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to create a docker container which can be run on docker to host a local mapserver, the problem i am facing is even with a small country data like bhutan-latest-osm.pbf which is around 200MB large, the docker container's size is shooting up to 4.5GB, this is just for development in actual case i would be using the planet-latest-osm.pbf which is supposed to use up 1.5TB of secondary storage. The important thing here to note is that i would need only zooming until city level, i.e i don't want zooming till street or area level within the map. I'm a newbie to this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '18, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/40bfa18a749cf54cd08eaaa0c1e27de7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kumard&#39;s gravatar image" />
<p><span>kumard</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kumard has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61698" class="comments-container">
<span id="61701"></span>
<div id="comment-61701" class="comment">
<div id="post-61701-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think you need 1.5TB for a planet file. One of the osm2pgsql developers has <a href="http://paulnorman.ca/blog/2017/02/how-much-space-do-i-need-for-osm2pgsql/">a blog post about how much space is needed</a> and says ~&lt;600GB is needed for a planet import.</p>
</div>
<div id="comment-61701-info" class="comment-info">
<span class="comment-age">(18 Jan '18, 12:03)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
</div>
<div id="comment-tools-61698" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61698-form-container" class="comment-form-container">
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

<span id="61705"></span>

<div id="answer-container-61705" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61705-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Once you've downloaded a planet file or an extract, you can relatively easily only keep certain data that you're interested in or remove certain data that you're definitely not interested in. Have a look at <a href="https://wiki.openstreetmap.org/wiki/Category:Osmium">osmium,</a> <a href="https://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a> and <a href="https://wiki.openstreetmap.org/wiki/Category:Osmosis">osmosis</a> (and other tools linked from those pages).</p>
<p>What you can't easily do is to say "keep only those features that renderers tend to show at a particular zoom level" or "keep only enough nodes so that it still looks sensible at a particular zoom level".</p>
<p>As another data point, a mapserver that I have for <a href="http://download.geofabrik.de/europe/british-isles.html">the UK and Ireland</a> (just over 1Gb of OSM pbf data) happily fits on a 100Gb SSD, and that's with a wider range of features rendered than OSM's standard style.</p>
<p>What are you actually trying to do? Data analysis? Create a map, and if so in what map style? Routing? Something else?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '18, 20:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-61705" class="comments-container">
<span id="61710"></span>
<div id="comment-61710" class="comment">
<div id="post-61710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> I am trying to host a local map server for kibana visualizations which contain maps, the visualizations over there doesn't require city street level zooming, but the restriction over here is the size of the secondary storage is very limited. Hence i have this question.</p>
</div>
<div id="comment-61710-info" class="comment-info">
<span class="comment-age">(19 Jan '18, 04:58)</span> <span class="comment-user userinfo">kumard</span>
</div>
</div>
<span id="61763"></span>
<div id="comment-61763" class="comment">
<div id="post-61763-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>, i am just trying to dreate a map for kibana visualizations, i don't need routing info on the map</p>
</div>
<div id="comment-61763-info" class="comment-info">
<span class="comment-age">(22 Jan '18, 06:37)</span> <span class="comment-user userinfo">kumard</span>
</div>
</div>
</div>
<div id="comment-tools-61705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61705-form-container" class="comment-form-container">
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

