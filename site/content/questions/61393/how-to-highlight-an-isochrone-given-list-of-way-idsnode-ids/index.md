+++
type = "question"
title = "How to highlight an isochrone given list of way ids/node ids?"
description = '''Hi, I calculated an isochrone using OSM data. Now I have a list of ways/nodes which are reachable from the starting point (original OSM ids are available). How can I highlight all the ways on a map? I only found out that a single way can be highlighted with https://www.openstreetmap.org/way/&amp;lt;id&amp;gt...'''
date = "2017-12-28T09:04:00Z"
lastmod = "2018-01-08T09:00:00Z"
weight = 61393
keywords = [ "isochrone", "highlighting", "id" ]
aliases = [ "/questions/61393" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to highlight an isochrone given list of way ids/node ids?](/questions/61393/how-to-highlight-an-isochrone-given-list-of-way-idsnode-ids)

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
<span id="post-61393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61393-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I calculated an isochrone using OSM data. Now I have a list of ways/nodes which are reachable from the starting point (original OSM ids are available). How can I highlight all the ways on a map? I only found out that a single way can be highlighted with <a href="https://www.openstreetmap.org/way/">https://www.openstreetmap.org/way/</a>&lt;id&gt;.</p>
<p>I'm a beginner with OSM so any help is very much appreciated. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-isochrone" rel="tag" title="see questions tagged &#39;isochrone&#39;">isochrone</span> <span class="post-tag tag-link-highlighting" rel="tag" title="see questions tagged &#39;highlighting&#39;">highlighting</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Dec '17, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/985450e9508764783026ab5f6552e134?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mopedchen&#39;s gravatar image" />
<p><span>Mopedchen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mopedchen has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Dec '17, 07:01</strong> </span></p>
</div>
</div>
<div id="comments-container-61393" class="comments-container">
<span id="61411"></span>
<div id="comment-61411" class="comment">
<div id="post-61411-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Firstly, those are ways, not edges...</p>
<p>Secondly, is the starting point a node?</p>
</div>
<div id="comment-61411-info" class="comment-info">
<span class="comment-age">(29 Dec '17, 04:40)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
<span id="61413"></span>
<div id="comment-61413" class="comment">
<div id="post-61413-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for pointing that out. I’ve edited the question.</p>
<p>Yes, the starting point is a node.</p>
</div>
<div id="comment-61413-info" class="comment-info">
<span class="comment-age">(29 Dec '17, 07:03)</span> <span class="comment-user userinfo">Mopedchen</span>
</div>
</div>
</div>
<div id="comment-tools-61393" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61393-form-container" class="comment-form-container">
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

<span id="61416"></span>

<div id="answer-container-61416" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61416-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use <a href="http://openstreetmap.org/api.opeapi/0.6/node/#id/ways">http://openstreetmap.org/api.opeapi/0.6/node/#id/ways</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '17, 13:47</strong></p>
<img src="https://secure.gravatar.com/avatar/100f8ccde5e9799707a5056f94fe183f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wetitpig0&#39;s gravatar image" />
<p><span>Wetitpig0</span><br />
<span class="score" title="307 reputation points">307</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wetitpig0 has 2 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-61416" class="comments-container">
<span id="61535"></span>
<div id="comment-61535" class="comment">
<div id="post-61535-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately, the link doesn't work.</p>
<p>I managed to highlight the edges using QGIS and OSM data extracts from Geofabrik.</p>
</div>
<div id="comment-61535-info" class="comment-info">
<span class="comment-age">(08 Jan '18, 09:00)</span> <span class="comment-user userinfo">Mopedchen</span>
</div>
</div>
</div>
<div id="comment-tools-61416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61416-form-container" class="comment-form-container">
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

