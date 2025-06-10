+++
type = "question"
title = "Export to kml format a planned road drawn on OpenStreetMap"
description = '''Export to kml format a planned road drawn on OpenStreetMap How can I export to kml format this planned road: http://www.openstreetmap.org/way/421129199 drawn by somebody on openstreetmap. I have tried to use http://overpass-turbo.eu/ but I do not know what query to run to have the kml file of http:/...'''
date = "2016-10-29T16:47:00Z"
lastmod = "2016-10-29T16:47:00Z"
weight = 52731
keywords = [ "kml", "export", "road", "format" ]
aliases = [ "/questions/52731" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Export to kml format a planned road drawn on OpenStreetMap](/questions/52731/export-to-kml-format-a-planned-road-drawn-on-openstreetmap)

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
<span id="post-52731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52731-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Export to kml format a planned road drawn on OpenStreetMap</strong></p>
<p>How can I export to kml format this planned road: <a href="http://www.openstreetmap.org/way/421129199">http://www.openstreetmap.org/way/421129199</a> drawn by somebody on openstreetmap.</p>
<p>I have tried to use <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> but I do not know what query to run to have the kml file of <a href="http://www.openstreetmap.org/way/421129199">http://www.openstreetmap.org/way/421129199</a> generated.</p>
<p><strong>UPDATE:</strong></p>
<p>Finally I have found a procedure. In the left panel of <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> I wrote the sequence of commands you can see below (it is for a group of planned roads) and then pressed <strong>Run</strong> followed by <strong>Export</strong> and after that I selected <strong>as KML</strong> option.</p>
<p>way(421129199); out geom; way(255186883); out geom; way(257366617); out geom; way(254417023); out geom; way(403116840); out geom; way(420106776); out geom; way(167390508); out geom; way(233974332); out geom; way(167252854); out geom; way(283351409); out geom; way(283923219); out geom;</p>
<p>It works. The problem I still encounter is that I have a group of many planned roads like "421129199", this is, a list of numbers as "421129199". I would like to just somehow paste that list in overpass-turbo. without being obliged to add each time the keywords "way" and "out geom". Is it possible to do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-format" rel="tag" title="see questions tagged &#39;format&#39;">format</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Oct '16, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/87b667bd359ee898ecf29d0cd05337d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="simplex1&#39;s gravatar image" />
<p><span>simplex1</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="simplex1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Oct '16, 22:38</strong> </span></p>
</div>
</div>
<div id="comments-container-52731" class="comments-container">
&#10;</div>
<div id="comment-tools-52731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52731-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

