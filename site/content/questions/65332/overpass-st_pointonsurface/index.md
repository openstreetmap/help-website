+++
type = "question"
title = "Overpass ST_PointOnSurface"
description = '''There are an Overpass option or workaround to obtain ST_PointOnSurface()-equivalent instead the usual centroid? It is important to &quot;area relations&quot; (and welcome similar behaviour with ways). It returns the centroid or, when is not inside the surface, returns a point (a projection from centroid) that...'''
date = "2018-08-14T15:13:00Z"
lastmod = "2018-08-14T16:04:00Z"
weight = 65332
keywords = [ "overpass" ]
aliases = [ "/questions/65332" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass ST_PointOnSurface](/questions/65332/overpass-st_pointonsurface)

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
<span id="post-65332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65332-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are an Overpass option or workaround to obtain <a href="https://postgis.net/docs/ST_PointOnSurface.html">ST_PointOnSurface()</a>-equivalent instead the usual centroid?</p>
<p>It is important to "area <em>relations</em>" (and welcome similar behaviour with <em>ways</em>). It returns the centroid or, when is not inside the surface, returns a point (a projection from centroid) that is guaranteed to lie on the surface.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '18, 15:13</strong></p>
<img src="https://secure.gravatar.com/avatar/6963015ca2c3146e2a2a348b7fcb793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppKrauss&#39;s gravatar image" />
<p><span>ppKrauss</span><br />
<span class="score" title="95 reputation points">95</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppKrauss has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Aug '18, 15:19</strong> </span></p>
</div>
</div>
<div id="comments-container-65332" class="comments-container">
<span id="65334"></span>
<div id="comment-65334" class="comment">
<div id="post-65334-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure, but maybe here is something that you could use:</p>
<p><a href="http://gis.19327.n8.nabble.com/Overpass-API-Overpass-QL-center-and-centroid-function-td5812491.html">http://gis.19327.n8.nabble.com/Overpass-API-Overpass-QL-center-and-centroid-function-td5812491.html</a></p>
</div>
<div id="comment-65334-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 15:34)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="65335"></span>
<div id="comment-65335" class="comment">
<div id="post-65335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/11332/kocio"></a><a href="https://help.openstreetmap.org/users/11332/kocio">@kocio</a>. As we see in the discussion ,there are a lack of formal specification... Perhaps I need only to check what the Overpass command <code>center</code> is doing: is the PostGIS <code>ST_Centroid()</code> or the <code>ST_PointOnSurface()</code>? ... When I check <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">wiki/Overpass_API/Overpass_QL</a> it says <strong>"center: ... The center point is not guaranteed to lie inside the polygon"</strong>. If the Wiki is correct, my question ("there are a workaround?") make sense.</p>
</div>
<div id="comment-65335-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 15:46)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
<span id="65338"></span>
<div id="comment-65338" class="comment">
<div id="post-65338-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I hope one of these can help you:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a> <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example</a> <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide">https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide</a> <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL</a></p>
</div>
<div id="comment-65338-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 15:54)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="65339"></span>
<div id="comment-65339" class="comment">
<div id="post-65339-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/11332/kocio"></a><a href="https://help.openstreetmap.org/users/11332/kocio">@kocio</a>, I checked before about <code>center</code>, there are nothing. Only say that <code>center</code> is not the solution (and is not a centroid, is only a BBOX center). All links seems to say nothing about "<code>center</code> alternative".</p>
</div>
<div id="comment-65339-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 16:04)</span> <span class="comment-user userinfo">ppKrauss</span>
</div>
</div>
</div>
<div id="comment-tools-65332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65332-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

