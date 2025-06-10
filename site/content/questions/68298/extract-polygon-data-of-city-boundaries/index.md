+++
type = "question"
title = "Extract polygon-data of city-boundaries"
description = '''Hello,  I try to retrive the polygon-data of the boundaries of cities in germany. I need to process these data in php.  My first approach was to send a request to Nominatim and retrieve JSON data in return. See this example: https://nominatim.openstreetmap.org/search.php?q=papenburg&amp;amp;polygon_geoj...'''
date = "2019-03-06T14:59:00Z"
lastmod = "2019-03-06T15:14:00Z"
weight = 68298
keywords = [ "boundaries", "boundary", "nominatim", "polygon", "geojson" ]
aliases = [ "/questions/68298" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract polygon-data of city-boundaries](/questions/68298/extract-polygon-data-of-city-boundaries)

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
<span id="post-68298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68298-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I try to retrive the polygon-data of the boundaries of cities in germany. I need to process these data in php.</p>
<p>My first approach was to send a request to Nominatim and retrieve JSON data in return. See this example: <a href="https://nominatim.openstreetmap.org/search.php?q=papenburg&amp;polygon_geojson=1&amp;format=json">https://nominatim.openstreetmap.org/search.php?q=papenburg&amp;polygon_geojson=1&amp;format=json</a></p>
<p>But I red the usage policy of the Nominatim project and it seems to me that it is adverse to send automatic requests (out of my php script) to Nominatim. Afterwards I read about PBF Files and XML-Files and how to access the data, but it all seems to be much more complicated and I am not even sure if this would give my finally the information I need.</p>
<p>Is there any easy access to this data - or does anybody know which approach would be the best to retrieve the data I am looking for? Thank you in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '19, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/c8bc419f000b1b0c05432cb80f890c11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frlln&#39;s gravatar image" />
<p><span>frlln</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frlln has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68298" class="comments-container">
&#10;</div>
<div id="comment-tools-68298" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68298-form-container" class="comment-form-container">
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

<span id="68299"></span>

<div id="answer-container-68299" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68299-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a> In the left-pane navigation you can use right-mouse-click to select multiple levels. Countries are marked (2), states (4), cities can (6) or (7) depending on type (Bavaria markt, kreisfrei etc).</p>
<p><a href="https://overpass-turbo.eu/">https://overpass-turbo.eu/</a> is also powerful. Zoom to the desired area and search for 'relation<a href="%7B%7Bbbox%7D%7D">"admin_level"="6"</a>;' example <a href="https://overpass-turbo.eu/s/GI8">https://overpass-turbo.eu/s/GI8</a> From inside a script you can query the API directly <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '19, 15:14</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-68299" class="comments-container">
&#10;</div>
<div id="comment-tools-68299" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68299-form-container" class="comment-form-container">
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

