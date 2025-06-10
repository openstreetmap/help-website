+++
type = "question"
title = "Extract shapefile"
description = '''Dear community, Could you please explain how it would be possible to extract and download the orange boundary as a shapefile from the following site? https://www.openstreetmap.org/relation/271888#map=12/48.7809/9.2247 Thank you!'''
date = "2019-06-27T13:53:00Z"
lastmod = "2019-06-28T14:47:00Z"
weight = 69767
keywords = [ "shapefile", "extract" ]
aliases = [ "/questions/69767" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Extract shapefile](/questions/69767/extract-shapefile)

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
<span id="post-69767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69767-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear community,</p>
<p>Could you please explain how it would be possible to extract and download the orange boundary as a shapefile from the following site? <a href="https://www.openstreetmap.org/relation/271888#map=12/48.7809/9.2247">https://www.openstreetmap.org/relation/271888#map=12/48.7809/9.2247</a></p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '19, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/5984a4e425de76c6437769c5660c335b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Neico&#39;s gravatar image" />
<p><span>Neico</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Neico has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69767" class="comments-container">
&#10;</div>
<div id="comment-tools-69767" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69767-form-container" class="comment-form-container">
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

<span id="69774"></span>

<div id="answer-container-69774" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69774-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Neico has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM does not offer conversion of data into other formats, in only offers the data in OSM's own data format.</p>
<p>The "Overpass turbo" link you have been given in the other answer (<a href="http://overpass-turbo.eu/s/KiN)">http://overpass-turbo.eu/s/KiN)</a> loads the OSM data but because it is not in the viewport, you don't immediately see it - there's a magnifying glass icon on the map that you can click to zoom to the area where the data is. Then go to "Export" and "Export as GeoJSON" and then use ogr2ogr, QGIS or other GIS software to convert GeoJSON to shape.</p>
<p>Another way to get what you want is to download relation 271888 in the JOSM editor (check "download relation members" box), then save as GeoJSON, then use ogr2ogr, QGIS or other GIS software to convert GeoJSON to shape.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '19, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jun '19, 14:38</strong> </span></p>
</div>
</div>
<div id="comments-container-69774" class="comments-container">
&#10;</div>
<div id="comment-tools-69774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69774-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69768"></span>

<div id="answer-container-69768" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69768-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could use this website: <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a> Unfortunately this only works for administrative boundaries.</p>
<p>You could use a website like <a href="https://mygeodata.cloud/converter/osm-to-shp">https://mygeodata.cloud/converter/osm-to-shp</a> (I just found this after a search), for data that you downloaded via Overpass (as raw OSM data).</p>
<p>I hope this is the query you need in Overpass: <a href="http://overpass-turbo.eu/s/KiN">http://overpass-turbo.eu/s/KiN</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '19, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jun '19, 14:19</strong> </span></p>
</div>
</div>
<div id="comments-container-69768" class="comments-container">
<span id="69769"></span>
<div id="comment-69769" class="comment">
<div id="post-69769-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. But how can I specify for the exact file? I understand it has the ID 271888. When I use the tree on the left I cannot seem to find it.</p>
</div>
<div id="comment-69769-info" class="comment-info">
<span class="comment-age">(27 Jun '19, 14:03)</span> <span class="comment-user userinfo">Neico</span>
</div>
</div>
<span id="69770"></span>
<div id="comment-69770" class="comment">
<div id="post-69770-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>oops, you are not looking for an administrative boundary, but a boundary of another type. that is not possible with this tool.</p>
</div>
<div id="comment-69770-info" class="comment-info">
<span class="comment-age">(27 Jun '19, 14:09)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="69771"></span>
<div id="comment-69771" class="comment">
<div id="post-69771-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>exactly. So I would like to know how the orange boundary from the link above can be extracted. I suppose this should be somehow possible?</p>
</div>
<div id="comment-69771-info" class="comment-info">
<span class="comment-age">(27 Jun '19, 14:12)</span> <span class="comment-user userinfo">Neico</span>
</div>
</div>
<span id="69772"></span>
<div id="comment-69772" class="comment">
<div id="post-69772-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But where exactly can I download the orange boundaries as an OSM file? (sorry I'm new to this whole field)</p>
</div>
<div id="comment-69772-info" class="comment-info">
<span class="comment-age">(27 Jun '19, 14:24)</span> <span class="comment-user userinfo">Neico</span>
</div>
</div>
<span id="69773"></span>
<div id="comment-69773" class="comment">
<div id="post-69773-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the link. But It only pulls up London and when running your code nothing happens. Or am I supposed to do something different?</p>
</div>
<div id="comment-69773-info" class="comment-info">
<span class="comment-age">(27 Jun '19, 14:30)</span> <span class="comment-user userinfo">Neico</span>
</div>
</div>
</div>
<div id="comment-tools-69768" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69768-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69780"></span>

<div id="answer-container-69780" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69780-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Easiest way I can think of is to download that relation in JOSM, CTRL+SHIFT+O ( download object) insert your id and choose relation. After that you can save it as a geojson and from there you can convert it to shp with Qgis or anything else</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '19, 14:47</strong></p>
<img src="https://secure.gravatar.com/avatar/821de102b0d4d7379085001df7ee12a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincze&#39;s gravatar image" />
<p><span>Vincze</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincze has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69780" class="comments-container">
&#10;</div>
<div id="comment-tools-69780" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69780-form-container" class="comment-form-container">
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

