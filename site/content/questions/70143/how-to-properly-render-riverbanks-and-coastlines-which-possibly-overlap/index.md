+++
type = "question"
title = "How to properly render riverbanks and coastlines which possibly overlap?"
description = '''I would like to extend the OSM carto style to render coastlines, riverbanks and other edges of water features with a line. This is quite easy to achieve by just adding another layer for ocean and water features which render lines on top of the polygon-fill layers. This looks nice and works as expect...'''
date = "2019-07-21T11:06:00Z"
lastmod = "2019-07-21T11:06:00Z"
weight = 70143
keywords = [ "osmosis", "rendering", "osm2pgsql", "mapnik" ]
aliases = [ "/questions/70143" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to properly render riverbanks and coastlines which possibly overlap?](/questions/70143/how-to-properly-render-riverbanks-and-coastlines-which-possibly-overlap)

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
<span id="post-70143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70143-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to extend the OSM carto style to render coastlines, riverbanks and other edges of water features with a line. This is quite easy to achieve by just adding another layer for ocean and water features which render lines on top of the polygon-fill layers.</p>
<p>This looks nice and works as expected, except for parts where the water areas join. In OSM this happens along rivers and when rivers meet coastlines. I thought about trying to make this work using a stylesheet alone, and it can almost be done by drawing the casing first like is done with lines, but not quite, there are still artifacts at the joins, and it's difficult to get the layer ordering right.</p>
<p>It seems like the best way would be to preprocess the data and produce another set of ways that really do represent banks. That means that if any natural=water/waterway=riverbank/natural=coastline overlap, just remove both ways.</p>
<p>Is this a sensible approach? What tool can I use to preprocess the data in this way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '19, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/9f432fe9a39bc9081698062b4d33d135?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Borbus&#39;s gravatar image" />
<p><span>Borbus</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Borbus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70143" class="comments-container">
&#10;</div>
<div id="comment-tools-70143" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70143-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

