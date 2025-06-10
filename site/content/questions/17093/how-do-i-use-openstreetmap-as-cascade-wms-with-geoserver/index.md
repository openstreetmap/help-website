+++
type = "question"
title = "How do i use openstreetmap  as Cascade WMS with Geoserver"
description = '''Hi All, I am using Geoserver 2.0.2 I have been informed that it is possible to use OSM as a &#x27;Cascade WMS&#x27; and then serve them out from Geoserver. When I looked up the Geoserver documentation it told me i would need a Capabillities URL, and a user name and passsword. Does anybody know where I can get...'''
date = "2012-10-22T12:31:00Z"
lastmod = "2012-10-22T15:12:00Z"
weight = 17093
keywords = [ "wms", "offline", "geoserver" ]
aliases = [ "/questions/17093" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do i use openstreetmap as Cascade WMS with Geoserver](/questions/17093/how-do-i-use-openstreetmap-as-cascade-wms-with-geoserver)

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
<span id="post-17093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17093-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All, I am using Geoserver 2.0.2 I have been informed that it is possible to use OSM as a 'Cascade WMS' and then serve them out from Geoserver. When I looked up the Geoserver documentation it told me i would need a Capabillities URL, and a user name and passsword. Does anybody know where I can get these? my purpose for this is that we are using software which looks for OSM but we are using it on non web facing machines. I can point this software to look at the server where I have Geoserver, which is web facing, and then serve the OSM maps from there. Any help would be greatly appreciated. Jason.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wms" rel="tag" title="see questions tagged &#39;wms&#39;">wms</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-geoserver" rel="tag" title="see questions tagged &#39;geoserver&#39;">geoserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '12, 12:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0f66ac4cfe29c6ae395008797514628d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NCC%20GIS%20Admin&#39;s gravatar image" />
<p><span>NCC GIS Admin</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NCC GIS Admin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17093" class="comments-container">
&#10;</div>
<div id="comment-tools-17093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17093-form-container" class="comment-form-container">
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

<span id="17097"></span>

<div id="answer-container-17097" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17097-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I understand this right, you have an application that wants to consume OSM tiles ("software which looks for OSM"), and now you want to use Geoserver to bring these tiles into the Intranet from the Internet.</p>
<p>That would be a waste of resources because as a cascading WMS, Geoserver would first assemble a coherent data source from the tiles and then cut that up again to serve them internally. You would be much better off simply installing a HTTP proxy and serving OSM tiles directly.</p>
<p>It would make sense to use Geoserver if your internal application required a WMS (which is something that OSM doesn't offer). Then Geoserver could load tiles from the Internet and make WMS responses from that. Unless Geoserver had efficient caching, however, you would likely end up making excessive requests against the OSM tile server so be sure to configure this right.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '12, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17097" class="comments-container">
<span id="17100"></span>
<div id="comment-17100" class="comment">
<div id="post-17100-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Frederik, Yes we had thought of a proxy but as you said the internal software requires a WMS. So do you have any idea how I would go about this?</p>
</div>
<div id="comment-17100-info" class="comment-info">
<span class="comment-age">(22 Oct '12, 15:12)</span> <span class="comment-user userinfo">NCC GIS Admin</span>
</div>
</div>
</div>
<div id="comment-tools-17097" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17097-form-container" class="comment-form-container">
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

