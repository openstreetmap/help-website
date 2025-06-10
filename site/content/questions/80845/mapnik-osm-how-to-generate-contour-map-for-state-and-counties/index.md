+++
type = "question"
title = "mapnik + osm: how to generate contour map for state and counties"
description = '''Hello, I&#x27;m struggling to find info on how to generate maps with Mapnik (mml file) that only show the contour of states and counties for the US (for example), and everything else white or transparent. Any pointer welcome. Thanks!'''
date = "2021-07-07T02:00:00Z"
lastmod = "2021-07-11T17:20:00Z"
weight = 80845
keywords = [ "osm", "mapnik" ]
aliases = [ "/questions/80845" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [mapnik + osm: how to generate contour map for state and counties](/questions/80845/mapnik-osm-how-to-generate-contour-map-for-state-and-counties)

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
<span id="post-80845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80845-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm struggling to find info on how to generate maps with Mapnik (mml file) that only show the contour of states and counties for the US (for example), and everything else white or transparent.</p>
<p>Any pointer welcome. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '21, 02:00</strong></p>
<img src="https://secure.gravatar.com/avatar/af0620755ec3e0728f5fcd00a2fe0239?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pat548&#39;s gravatar image" />
<p><span>pat548</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pat548 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jul '21, 02:04</strong> </span></p>
</div>
</div>
<div id="comments-container-80845" class="comments-container">
<span id="80854"></span>
<div id="comment-80854" class="comment">
<div id="post-80854-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By contour do you mean height contours or just the administrative outlines?</p>
</div>
<div id="comment-80854-info" class="comment-info">
<span class="comment-age">(07 Jul '21, 20:37)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="80900"></span>
<div id="comment-80900" class="comment">
<div id="post-80900-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I probably used the wrong word, I don't want height, just the country or state, or county, as a simple line, nothing else.</p>
</div>
<div id="comment-80900-info" class="comment-info">
<span class="comment-age">(09 Jul '21, 13:37)</span> <span class="comment-user userinfo">pat548</span>
</div>
</div>
<span id="80909"></span>
<div id="comment-80909" class="comment">
<div id="post-80909-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is plenty of ways to achieve this. You should tell us a bit more about your goal, is it for a map on a website, is it for just a few counties, the all country? What have you tried so far?</p>
</div>
<div id="comment-80909-info" class="comment-info">
<span class="comment-age">(10 Jul '21, 09:43)</span> <span class="comment-user userinfo">yvecai</span>
</div>
</div>
<span id="80910"></span>
<div id="comment-80910" class="comment">
<div id="post-80910-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just want to generate a PNG, with transparency, for either the whole US, with states, or a single state with counties. So far, I've tried modifying the project.mml file of the openstreetmap-carto project to only show those lines, but even with a single layer, it still show the ocean and there's no transparency:</p>
<p>Layer: - id: landcover-line geometry: linestring &lt;&lt;: <em>extents Datasource: &lt;&lt;:</em> osm2pgsql table: |- (SELECT way FROM planet_osm_line WHERE man_made = 'cutline' ) AS landcover_line properties: minzoom: 5</p>
<p>I guess my main problem is I can't find any good documentation about all the options I can use here. I've looked into the reference, but without examples, it's hard to follow.</p>
</div>
<div id="comment-80910-info" class="comment-info">
<span class="comment-age">(10 Jul '21, 14:23)</span> <span class="comment-user userinfo">pat548</span>
</div>
</div>
<span id="80911"></span>
<div id="comment-80911" class="comment">
<div id="post-80911-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Correction, the layer is actually:</p>
<p>Layer: - id: admin-low-zoom geometry: linestring &lt;&lt;: <em>extents Datasource: &lt;&lt;:</em> osm2pgsql table: |- (SELECT way, admin_level FROM planet_osm_roads WHERE boundary = 'administrative' AND admin_level IN ('0', '1', '2', '3', '4') AND osm_id &lt; 0 ORDER BY admin_level DESC ) AS admin_low_zoom properties: minzoom: 4 maxzoom: 7</p>
</div>
<div id="comment-80911-info" class="comment-info">
<span class="comment-age">(10 Jul '21, 15:43)</span> <span class="comment-user userinfo">pat548</span>
</div>
</div>
</div>
<div id="comment-tools-80845" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80845-form-container" class="comment-form-container">
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

<span id="80921"></span>

<div id="answer-container-80921" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80921-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to set the background color of your map transparent, example in the xml:</p>
<p>In the style.mss, replace the <a href="https://help.openstreetmap.org/users/52/landwirt">@land</a>-color by rgba(0,0,255,0)</p>
<pre><code>Map {
  background-color: rgba(0,0,255,0);
}</code></pre>
<p>At the end, the &lt;map&gt;tag in the xml generated should look like something like this:</p>
<p><code>&lt;Map srs="..." background-color="rgba(0, 0, 255, 0)" &gt; .. &lt;/Map&gt;</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '21, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-80921" class="comments-container">
&#10;</div>
<div id="comment-tools-80921" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80921-form-container" class="comment-form-container">
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

