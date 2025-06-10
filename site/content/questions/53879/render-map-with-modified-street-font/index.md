+++
type = "question"
title = "Render map with modified street font"
description = '''I&#x27;m new to OSM/Open Layers. I&#x27;d like to render a map with modified text (font family, font size) specifically for streets only. I&#x27;m a developer and happy to dive into code, I&#x27;m just not sure where to start looking. I&#x27;ve searched around on the site, and maybe I&#x27;m using the wrong terms, but haven&#x27;t fo...'''
date = "2017-01-05T19:09:00Z"
lastmod = "2017-01-05T21:21:00Z"
weight = 53879
keywords = [ "rendering", "openlayers" ]
aliases = [ "/questions/53879" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Render map with modified street font](/questions/53879/render-map-with-modified-street-font)

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
<span id="post-53879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53879-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSM/Open Layers. I'd like to render a map with modified text (font family, font size) specifically for streets only. I'm a developer and happy to dive into code, I'm just not sure where to start looking.</p>
<p>I've searched around on the site, and maybe I'm using the wrong terms, but haven't found anything yet. Any help appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '17, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/91614f89a6015e382a3afd9f74007ff3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brian%20Vogelgesang&#39;s gravatar image" />
<p><span>Brian Vogelg...</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brian Vogelgesang has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53879" class="comments-container">
&#10;</div>
<div id="comment-tools-53879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53879-form-container" class="comment-form-container">
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

<span id="53884"></span>

<div id="answer-container-53884" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53884-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Brian Vogelgesang has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap is really a geographical database rather than a specific rendering of the data, but the default layer on <a href="http://openstreetmap.org">openstreetmap.org</a> uses the openstreetmap-carto style, which is created using <a href="http://mapnik.org">Mapnik</a>. I presume this is what you would like to emulate but with a different font for streets. You might start by cloning the <a href="https://github.com/gravitystorm/openstreetmap-carto">GitHub repository</a>. Installation instructions are provided in the file <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md">INSTALL.md</a>.</p>
<p>If you'd like to create tiles and serve them using OpenLayers, you may wish to have a look at <a href="https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">switch2osm</a>.</p>
<p>There are also <a href="https://github.com/gravitystorm/openstreetmap-carto#alternatives">alternative rendering styles</a> you may wish to try instead of openstreetmap-carto.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '17, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/96c2522da1dee70df309c3bf9d279ef0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Greg&#39;s gravatar image" />
<p><span>Greg</span><br />
<span class="score" title="141 reputation points">141</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Greg has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-53884" class="comments-container">
&#10;</div>
<div id="comment-tools-53884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53884-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53888"></span>

<div id="answer-container-53888" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53888-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As Greg has already said, I'd start with the <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">switch2osm</a> site, but actually the "manually" page rather than the "from packages" one, as going through some parts of the setup manually help you to understand what's connected to what, and how to make changes to it. The "manually" page uses the <a href="https://github.com/mapbox/osm-bright">OSM Bright</a> style which is much easier to understand that OSM's "standard" style.</p>
<p>We don't, unfortunately, have a good tutorial on "editing the map style that you're using to render tiles with already" (though if someone knows of one, please edit this answer to include it).</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '17, 21:21</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-53888" class="comments-container">
&#10;</div>
<div id="comment-tools-53888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53888-form-container" class="comment-form-container">
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

