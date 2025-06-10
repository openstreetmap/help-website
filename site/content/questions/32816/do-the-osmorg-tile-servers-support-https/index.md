+++
type = "question"
title = "Do the osm.org tile servers support HTTPS?"
description = '''I am using OpenLayer to load OpenStreetMap. Using this js : http://www.openlayers.org/api/OpenLayers.js which doesn&#x27;t support https and hence the map is not load. I have a app which has a requirement to use all url having https support. Is there any way to Use the HTTPS SDK of OpenLayer or OpenStree...'''
date = "2014-05-02T15:38:00Z"
lastmod = "2014-05-05T10:09:00Z"
weight = 32816
keywords = [ "openstreetmap", "openlayers", "https" ]
aliases = [ "/questions/32816" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Do the osm.org tile servers support HTTPS?](/questions/32816/do-the-osmorg-tile-servers-support-https)

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
<span id="post-32816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32816-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using OpenLayer to load OpenStreetMap. Using this js : <a href="http://www.openlayers.org/api/OpenLayers.js">http://www.openlayers.org/api/OpenLayers.js</a> which doesn't support https and hence the map is not load. I have a app which has a requirement to use all url having https support. Is there any way to Use the HTTPS SDK of OpenLayer or OpenStreetMap and Load the Map ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '14, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/7793b4b476478c6637ae563bf9166ff6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vivek%20Tankaria&#39;s gravatar image" />
<p><span>Vivek Tankaria</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vivek Tankaria has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 May '14, 16:35</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-32816" class="comments-container">
&#10;</div>
<div id="comment-tools-32816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32816-form-container" class="comment-form-container">
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

<span id="32818"></span>

<div id="answer-container-32818" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32818-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-32818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenLayers is a separate project, and not part of OpenStreetMap. But yes, you can use the javascript over https by downloading it and serving it from your own servers.</p>
<p>The map tiles from OpenStreetMap are available over https.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '14, 17:08</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 May '14, 17:09</strong> </span></p>
</div>
</div>
<div id="comments-container-32818" class="comments-container">
<span id="32858"></span>
<div id="comment-32858" class="comment">
<div id="post-32858-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi Andy,</p>
<p>Thanks for your quick reply. Alternative to hosting the library on a server and use it . I downloaded the library and just included the OpenLayers.js , marker image and required css file in the app and the map loads perfect.</p>
</div>
<div id="comment-32858-info" class="comment-info">
<span class="comment-age">(05 May '14, 10:09)</span> <span class="comment-user userinfo">Vivek Tankaria</span>
</div>
</div>
</div>
<div id="comment-tools-32818" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32818-form-container" class="comment-form-container">
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

