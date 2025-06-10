+++
type = "question"
title = "Make new wms background for Potlatch2"
description = '''I insert a new WMs Background in Potlatch2 like the other WMS - Links in Potlatch2. But it doesn`t work. Has somebody an idea? And can create a working link? There must be a Problem with the variables ({bbox}, {width},...). The wms-Server is from the Administration from Nordrhine-Westfalen, Germany....'''
date = "2017-07-27T15:04:00Z"
lastmod = "2017-07-27T16:36:00Z"
weight = 57313
keywords = [ "potlatch2", "wms", "imagery", "background" ]
aliases = [ "/questions/57313" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Make new wms background for Potlatch2](/questions/57313/make-new-wms-background-for-potlatch2)

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
<span id="post-57313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57313-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I insert a new WMs Background in Potlatch2 like the other WMS - Links in Potlatch2. But it doesn`t work. Has somebody an idea? And can create a working link? There must be a Problem with the variables ({bbox}, {width},...).</p>
<p>The wms-Server is from the Administration from Nordrhine-Westfalen, Germany. The wms Service can use free.</p>
<p><a href="https://www.wms.nrw.de/geobasis/wms_nw_dop20?VERSION=1.3.0&amp;SERVICE=WMS&amp;REQUEST=GetMap&amp;LAYERS=nw_dop20&amp;STYLES=&amp;SRS=EPSG:4326&amp;BBOX=%7Bbbox%7D&amp;WIDTH=%7Bwidth%7D&amp;HEIGHT=%7Bheight%7D&amp;FORMAT=image/png&amp;TRANSPARENT=TRUE">https://www.wms.nrw.de/geobasis/wms_nw_dop20?VERSION=1.3.0&amp;SERVICE=WMS&amp;REQUEST=GetMap&amp;LAYERS=nw_dop20&amp;STYLES=&amp;SRS=EPSG:4326&amp;BBOX={bbox}&amp;WIDTH={width}&amp;HEIGHT={height}&amp;FORMAT=image/png&amp;TRANSPARENT=TRUE</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-wms" rel="tag" title="see questions tagged &#39;wms&#39;">wms</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-background" rel="tag" title="see questions tagged &#39;background&#39;">background</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '17, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ed31c6bd7e4ebd6cb54b2af69c36fba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Street%20Fox&#39;s gravatar image" />
<p><span>Street Fox</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Street Fox has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57313" class="comments-container">
<span id="57314"></span>
<div id="comment-57314" class="comment">
<div id="post-57314-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>AFAIK Potlatch does not use WMS services, only TMS. See <a href="https://help.openstreetmap.org/questions/13868/how-to-use-wms-link-from-rectifiedwarped-map-as-background-in-potlatch-or-josm">https://help.openstreetmap.org/questions/13868/how-to-use-wms-link-from-rectifiedwarped-map-as-background-in-potlatch-or-josm</a></p>
</div>
<div id="comment-57314-info" class="comment-info">
<span class="comment-age">(27 Jul '17, 15:16)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="57315"></span>
<div id="comment-57315" class="comment">
<div id="post-57315-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But I can`t upload the Images from the WMS-Server to mapwarper. In Potlatch2 are some Backgrounds which seems like WMS Services (for example: <a href="https://gis.tirol.gv.at/arcgis/services/Service_Public/terrain/MapServer/WmsServer?FORMAT=image/png&amp;TRANSPARENT=TRUE&amp;VERSION=1.1.1&amp;SERVICE=WMS&amp;REQUEST=GetMap&amp;LAYERS=Hoehenschichtlinien">https://gis.tirol.gv.at/arcgis/services/Service_Public/terrain/MapServer/WmsServer?FORMAT=image/png&amp;TRANSPARENT=TRUE&amp;VERSION=1.1.1&amp;SERVICE=WMS&amp;REQUEST=GetMap&amp;LAYERS=Hoehenschichtlinien</a> 20m&amp;STYLES=&amp;SRS={proj}&amp;WIDTH={width}&amp;HEIGHT={height}&amp;BBOX={bbox})</p>
</div>
<div id="comment-57315-info" class="comment-info">
<span class="comment-age">(27 Jul '17, 16:16)</span> <span class="comment-user userinfo">Street Fox</span>
</div>
</div>
</div>
<div id="comment-tools-57313" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57313-form-container" class="comment-form-container">
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

<span id="57316"></span>

<div id="answer-container-57316" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57316-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can't do this because Potlatch2 does not support WMS, see the author's response on github: <a href="https://github.com/systemed/potlatch2/issues/122">link text</a>.</p>
<p>WMS entries appear in Potlatch2 because they use a common imagery json listing. None of them actually work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '17, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-57316" class="comments-container">
&#10;</div>
<div id="comment-tools-57316" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57316-form-container" class="comment-form-container">
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

