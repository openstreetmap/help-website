+++
type = "question"
title = "Download 3D buildings information from URL"
description = '''Hello, I&#x27;m building a C++ desktop application feature where you can visualize 3D data and I&#x27;d like to import 3D buildings from some locations specified by the user into it. I looked at this kind of request https://wiki.openstreetmap.org/wiki/API_v0.6#Retrieving_map_data_by_bounding_box:_GET_.2Fapi.2...'''
date = "2020-11-19T16:47:00Z"
lastmod = "2020-11-23T23:49:00Z"
weight = 77623
keywords = [ "api", "3d" ]
aliases = [ "/questions/77623" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Download 3D buildings information from URL](/questions/77623/download-3d-buildings-information-from-url)

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
<span id="post-77623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77623-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm building a C++ desktop application feature where you can visualize 3D data and I'd like to import 3D buildings from some locations specified by the user into it.</p>
<p>I looked at this kind of request <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Retrieving_map_data_by_bounding_box:_GET_.2Fapi.2F0.6.2Fmap"><code>https://wiki.openstreetmap.org/wiki/API_v0.6#Retrieving_map_data_by_bounding_box:_GET_.2Fapi.2F0.6.2Fmap</code></a> but I'd like to filter it so only buildings are left in the result. Is it possible ? Since I'd like to be dependence-free (except CURL), I want to download the data given an URL and parse the .osm file myself if you guys think this is doable.</p>
<p>Is there a better way to to achieve what I'm trying to do ?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-3d" rel="tag" title="see questions tagged &#39;3d&#39;">3d</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '20, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/575a0758a02ae5fb5f40a81135538895?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Timo1111&#39;s gravatar image" />
<p><span>Timo1111</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Timo1111 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77623" class="comments-container">
&#10;</div>
<div id="comment-tools-77623" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77623-form-container" class="comment-form-container">
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

<span id="77628"></span>

<div id="answer-container-77628" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77628-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your usage sounds to me like it would fall under the second paragraph of the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#When_NOT_to_use_the_API">When NOT to use the API</a> section of that page.</p>
<p>I think the some of <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> instances have fewer restrictions. This would also allow you to request only the ways and relations that are either <code>building</code> or <code>building:part</code> and associated geometry.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '20, 23:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-77628" class="comments-container">
<span id="77665"></span>
<div id="comment-77665" class="comment">
<div id="post-77665-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry I'm late to answer, didn't have a PC this week-end.</p>
<p>I agree Overpass API seems more fitted for my needs but from what I saw I can't request buildings information only using an URL. Every request described in the documentation is using Overpass QL or Overpass XML language. Is there a REST API or should I put the OQL script in the body of a GET request ?</p>
</div>
<div id="comment-77665-info" class="comment-info">
<span class="comment-age">(23 Nov '20, 08:34)</span> <span class="comment-user userinfo">Timo1111</span>
</div>
</div>
<span id="77682"></span>
<div id="comment-77682" class="comment">
<div id="post-77682-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'm not a developer myself, but the Overpass Turbo "export" options allow you to produce a "compact form" like this:</p>
<p><code>[out:xml][timeout:25];(nwr["building"](40.764472136395,-73.979962170124,40.766089194963,-73.976062238216);nwr["building:part"](40.764472136395,-73.979962170124,40.766089194963,-73.976062238216););out;&gt;;out skel qt;</code></p>
<p>Which it then converts to a URL that looks like this: <a href="https://overpass-api.de/api/interpreter?data=%5Bout%3Axml%5D%5Btimeout%3A25%5D%3B%28nwr%5B%22building%22%5D%2840%2E764472136395%2C%2D73%2E979962170124%2C40%2E766089194963%2C%2D73%2E976062238216%29%3Bnwr%5B%22building%3Apart%22%5D%2840%2E764472136395%2C%2D73%2E979962170124%2C40%2E766089194963%2C%2D73%2E976062238216%29%3B%29%3Bout%3B%3E%3Bout%20skel%20qt%3B%0A"></a> <a href="https://overpass-api.de/api/interpreter?data=%5Bout%3Axml%5D%5Btimeout%3A25%5D%3B%28nwr%5B%22building%22%5D%2840%2E764472136395%2C%2D73%2E979962170124%2C40%2E766089194963%2C%2D73%2E976062238216%29%3Bnwr%5B%22building%3Apart%22%5D%2840%2E764472136395%2C%2D73%2E979962170124%2C40%2E766089194963%2C%2D73%2E976062238216%29%3B%29%3Bout%3B%3E%3Bout%20skel%20qt%3B%0A"><code>https://overpass-api.de/api/interpreter?data=%5Bout%3Axml%5D%5Btimeout%3A25%5D%3B%28nwr%5B%22building%22%5D%2840%2E764472136395%2C%2D73%2E979962170124%2C40%2E766089194963%2C%2D73%2E976062238216%29%3Bnwr%5B%22building%3Apart%22%5D%2840%2E764472136395%2C%2D73%2E979962170124%2C40%2E766089194963%2C%2D73%2E976062238216%29%3B%29%3Bout%3B%3E%3Bout%20skel%20qt%3B%0A</code></a></p>
<p>Which I assume is the same but percent encoded?</p>
</div>
<div id="comment-77682-info" class="comment-info">
<span class="comment-age">(23 Nov '20, 23:49)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-77628" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77628-form-container" class="comment-form-container">
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

