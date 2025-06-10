+++
type = "question"
title = "Simplest way to render a fictional map using OSM format with OSM-carto stylesheet"
description = '''I want to create a fictional map using the OSM format/technology (like the JOSM editor). I&#x27;m of course not going to submit it to the server. However, I can&#x27;t see a way to easily render the data. I don&#x27;t like the look of JOSM (using the default Carto style would be optimal.) I&#x27;ve heard about OpenGeof...'''
date = "2020-05-24T00:06:00Z"
lastmod = "2020-05-25T19:59:00Z"
weight = 74970
keywords = [ "windows", "rendering", "offline", "fictional" ]
aliases = [ "/questions/74970" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Simplest way to render a fictional map using OSM format with OSM-carto stylesheet](/questions/74970/simplest-way-to-render-a-fictional-map-using-osm-format-with-osm-carto-stylesheet)

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
<span id="post-74970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74970-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to create a fictional map using the OSM format/technology (like the JOSM editor). I'm of course not going to submit it to the server. However, I can't see a way to easily render the data. I don't like the look of JOSM (using the default Carto style would be optimal.)</p>
<p>I've heard about OpenGeofiction, but it probably wouldn't work for my needs because my project probably wouldn't be realistic enough to their standards. I also don't have a spare computer to set up my own instance of the server. QGIS looks a lot more complex than using OSM editors, but I've done some googling and it seems that it plus tilemill are the closest to what I want. Is there any simple application to render an .osm file as a styled slippy map? Or, is there a way to use tilemill with OSM-format data and styles?</p>
<p>I'm on Windows 10.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-fictional" rel="tag" title="see questions tagged &#39;fictional&#39;">fictional</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '20, 00:06</strong></p>
<img src="https://secure.gravatar.com/avatar/090f8703c27af1dad6b2585cc1f32843?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="js104&#39;s gravatar image" />
<p><span>js104</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="js104 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74970" class="comments-container">
&#10;</div>
<div id="comment-tools-74970" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74970-form-container" class="comment-form-container">
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

<span id="74977"></span>

<div id="answer-container-74977" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74977-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Essentially, there are two things that you need to do:</p>
<ol>
<li>Actually editing the data</li>
<li>Creating a map from it</li>
</ol>
<p>Of the two, the second is the one that you have most options with. If you're on Windows and "just want to create a map" then in addition to the options listed elsewhere <a href="https://switch2osm.org/serving-tiles/using-a-docker-container/">Docker</a> might be an option. You don't need a spare computer - all of the setup and plumbing of a Ubuntu tile server is handled by the Docker container and you don't need to worry about it.</p>
<p>With regard to the first, for a "normal map" JOSM is almost certainly still the best option. Don't worry about what things look like in there as you'll be using something else for rendering (though you can change that if you want to, as maxerickson has mentioned).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '20, 10:45</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-74977" class="comments-container">
<span id="74981"></span>
<div id="comment-74981" class="comment">
<div id="post-74981-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, I figured I would need another program to render. I'll check out docker and the other options and see which one works the best.</p>
</div>
<div id="comment-74981-info" class="comment-info">
<span class="comment-age">(24 May '20, 14:21)</span> <span class="comment-user userinfo">js104</span>
</div>
</div>
<span id="74986"></span>
<div id="comment-74986" class="comment">
<div id="post-74986-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As an aside, one thing that I wondered about when I wrote the switch2osm page for docker was how much "docker specific" info there should be there. There's lots of docker stuff all over the internet, so I wasn't sure how much "setting up docker" should ne on the switch2osm page as it wasn't anything to do with OSM per se. If you think the switch2osm pages can be improved, create an issue (or a pull request) at <a href="https://github.com/switch2osm/switch2osm.github.io/issues">https://github.com/switch2osm/switch2osm.github.io/issues</a> .</p>
</div>
<div id="comment-74986-info" class="comment-info">
<span class="comment-age">(24 May '20, 23:03)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="74996"></span>
<div id="comment-74996" class="comment">
<div id="post-74996-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, I'm not very familiar with PostgreSQL. What's the equivalent of <code>/var/lib/postgresql/12/main</code> for Windows?</p>
</div>
<div id="comment-74996-info" class="comment-info">
<span class="comment-age">(25 May '20, 15:37)</span> <span class="comment-user userinfo">js104</span>
</div>
</div>
</div>
<div id="comment-tools-74977" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74977-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74971"></span>

<div id="answer-container-74971" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74971-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as Tilemill, I'd expect anything you could do with QGIS would also be possible in JOSM, with maybe a conversion step. For a modest amount of data, the conversion step isn't a big deal (Michigan takes ~5 minutes to convert from OSM editing schema to osm2pgsql schema on my laptop).</p>
<p>JOSM does have a variety of styles available (they do tend to be mapping tools):</p>
<p><a href="https://josm.openstreetmap.de/wiki/Styles">https://josm.openstreetmap.de/wiki/Styles</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '20, 00:17</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-74971" class="comments-container">
<span id="74980"></span>
<div id="comment-74980" class="comment">
<div id="post-74980-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks good, I'll look into this and see if it works well.</p>
</div>
<div id="comment-74980-info" class="comment-info">
<span class="comment-age">(24 May '20, 14:20)</span> <span class="comment-user userinfo">js104</span>
</div>
</div>
<span id="74984"></span>
<div id="comment-74984" class="comment">
<div id="post-74984-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm... I'm having trouble installing Tilemill. When running npm install I get many errors, the first few of which state that it got a 403 when trying to download mapnik, that there aren't pre-built binaries for mapnik and node@8.15.0, and several command fails. Is it recommended/okay to use Tilemill 0.10.1 instead of 1.0.1?</p>
</div>
<div id="comment-74984-info" class="comment-info">
<span class="comment-age">(24 May '20, 16:31)</span> <span class="comment-user userinfo">js104</span>
</div>
</div>
</div>
<div id="comment-tools-74971" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74971-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74972"></span>

<div id="answer-container-74972" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74972-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Maperitive">Maperitive</a> might do what you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '20, 00:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-74972" class="comments-container">
<span id="74973"></span>
<div id="comment-74973" class="comment">
<div id="post-74973-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Unfortunately, it seems that Maperitive usese its own styling and not CartoCSS.</p>
</div>
<div id="comment-74973-info" class="comment-info">
<span class="comment-age">(24 May '20, 01:21)</span> <span class="comment-user userinfo">js104</span>
</div>
</div>
<span id="74975"></span>
<div id="comment-74975" class="comment">
<div id="post-74975-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Maperitive does not use CartoCSS but it has a number of different styles you can choose from and one of them is (an older version of) similar to CartoCSS. You can also modify the styling (Maperitive styles are simple text files). You asked for an <em>easy</em> way and that's why people have recommended Mapritive; you can achieve a genuine CartoCSS rendering but this requires the use of PostgreSQL/PostGIS and osm2pgsl to fill the database, and then you could use "kosmtik" to render the map (this uses Mapnik behind the scenes) - all this will be possible-but-challenging under Windows, and a Linux VM might be an easier way.</p>
</div>
<div id="comment-74975-info" class="comment-info">
<span class="comment-age">(24 May '20, 10:19)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="74979"></span>
<div id="comment-74979" class="comment">
<div id="post-74979-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Alright, I see. I'll try out these options today and see which one provides the most acceptable result.</p>
</div>
<div id="comment-74979-info" class="comment-info">
<span class="comment-age">(24 May '20, 14:17)</span> <span class="comment-user userinfo">js104</span>
</div>
</div>
<span id="75002"></span>
<div id="comment-75002" class="comment">
<div id="post-75002-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Alright, well so far Maperitive is the only one that has given me a map, but its rendering is still a bit weird/clunky (as an example: I have a city label right next to a town label. Only the city label shows until I zoom in, in which only the town label shows and the city is nowhere to be seen..) and it doesn't seem to be able to show some features (e.g. ferries). I'll wait to give the accept after I try out the other options.</p>
</div>
<div id="comment-75002-info" class="comment-info">
<span class="comment-age">(25 May '20, 19:59)</span> <span class="comment-user userinfo">js104</span>
</div>
</div>
</div>
<div id="comment-tools-74972" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74972-form-container" class="comment-form-container">
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

