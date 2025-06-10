+++
type = "question"
title = "How to get nodes into a closed way in a single Overpass query"
description = '''For example: I have the way(52360447). It is the building. The are several nodes (organisations) into this building.  I was tried to get this nodes by next query: [timeout:10][out:json]; (way(52360447)-&amp;gt;.x;node(around.x:10)[&#x27;name&#x27;];); out tags geom; But, result this query has one wrong organisati...'''
date = "2016-11-14T10:16:00Z"
lastmod = "2016-11-15T06:24:00Z"
weight = 52932
keywords = [ "overpass" ]
aliases = [ "/questions/52932" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to get nodes into a closed way in a single Overpass query](/questions/52932/how-to-get-nodes-into-a-closed-way-in-a-single-overpass-query)

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
<span id="post-52932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52932-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For example: I have the way(52360447). It is the building. The are several nodes (organisations) into this building. I was tried to get this nodes by next query: [timeout:10][out:json]; (way(52360447)-&gt;.x;node(around.x:10)['name'];); out tags geom;</p>
<p>But, result this query has one wrong organisation from a neighboring building. And I understand why! How can I get those nodes (organisations) only from this buildings(way)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '16, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/23da3eafe6f6c0646ba3b2ec1fd0e302?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Denis_giswork&#39;s gravatar image" />
<p><span>Denis_giswork</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Denis_giswork has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52932" class="comments-container">
<span id="52946"></span>
<div id="comment-52946" class="comment">
<div id="post-52946-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>take a look at <a href="https://help.openstreetmap.org/questions/47548/overpass-ql-return-all-parks-with-playgrounds-within-polygon">https://help.openstreetmap.org/questions/47548/overpass-ql-return-all-parks-with-playgrounds-within-polygon</a></p>
<p>I guess the feature is still not available on the main public servers, I didn't check if it is still available on the dev server mentioned in the answer.</p>
</div>
<div id="comment-52946-info" class="comment-info">
<span class="comment-age">(14 Nov '16, 18:35)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="52965"></span>
<div id="comment-52965" class="comment">
<div id="post-52965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks maxerickson! I had seen this link. But those variants don't work for my example. I don't know why( This variant must be working (in my opinion): [bbox:{{bbox}}] [out:json][timeout:1800];</p>
<p>way(52360447); map_to_area-&gt;.a; ( node(area.a); ); out; But no((( Maybe you're right! It's not available yet...</p>
</div>
<div id="comment-52965-info" class="comment-info">
<span class="comment-age">(15 Nov '16, 06:24)</span> <span class="comment-user userinfo">Denis_giswork</span>
</div>
</div>
</div>
<div id="comment-tools-52932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52932-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

