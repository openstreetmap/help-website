+++
type = "question"
title = "reverse geocoding Json format difference"
description = '''I am trying to do reverse geocoding using open street maps. I am getting 2 different Json formats in the response. For, this request The Response contains neigbourhood,suburb etc,. For,this request The Response contains county and other fields. I do see that the OSM_TYPE is differing in both the res...'''
date = "2017-03-14T07:32:00Z"
lastmod = "2017-03-14T09:23:00Z"
weight = 55051
keywords = [ "reversegeocoding" ]
aliases = [ "/questions/55051" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [reverse geocoding Json format difference](/questions/55051/reverse-geocoding-json-format-difference)

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
<span id="post-55051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55051-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to do reverse geocoding using open street maps. I am getting 2 different Json formats in the response.</p>
<p>For, <a href="http://nominatim.openstreetmap.org/reverse?json_callback=cb&amp;format=json&amp;lat=12.975360&amp;lon=80.190122&amp;zoom=27&amp;addressdetails=1">this request</a> The Response contains neigbourhood,suburb etc,.</p>
<p>For,<a href="http://nominatim.openstreetmap.org/reverse?json_callback=cb&amp;format=json&amp;lat=40.119198&amp;lon=-75.355764&amp;zoom=27&amp;osm_type=N&amp;addressdetails=1">this request</a> The Response contains county and other fields.</p>
<p>I do see that the OSM_TYPE is differing in both the response(node/way). Is there any way to restrict the type of response?I tried to add OSM_TYPE in the query string which doesn't seem to work. Is there anyother format that could be received?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Mar '17, 07:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a24776e12d0c00debee804f888f67bbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Coder123&#39;s gravatar image" />
<p><span>Coder123</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Coder123 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Mar '17, 07:33</strong> </span></p>
</div>
</div>
<div id="comments-container-55051" class="comments-container">
<span id="55054"></span>
<div id="comment-55054" class="comment">
<div id="post-55054-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>cross-posted: <a href="http://stackoverflow.com/q/42736283/1340631">http://stackoverflow.com/q/42736283/1340631</a> and <a href="http://gis.stackexchange.com/q/231747/23837">http://gis.stackexchange.com/q/231747/23837</a></p>
</div>
<div id="comment-55054-info" class="comment-info">
<span class="comment-age">(14 Mar '17, 09:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55051-form-container" class="comment-form-container">
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

<span id="55053"></span>

<div id="answer-container-55053" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55053-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Coder123 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The format of the response is the same. For the US address different address components are found than for the Indian address, e.g. for India there's also a <code>state_district</code>.</p>
<p><a href="https://github.com/OpenCageData/address-formatting/blob/master/conf/components.yaml">https://github.com/OpenCageData/address-formatting/blob/master/conf/components.yaml</a> contains a list of possible common components. Anything not in that list, e.g. <code>place_of_worship</code> can usually be seen as the name of the place.</p>
<p>The maximum zoom level you can set is 18, that's also the default. Setting it to 27 has no effect.</p>
<p>Using <code>&amp;format=jsonv2</code> will add a couple of fields in the response. Maybe they're useful for what you're trying to do.</p>
<p><code>OSM_TYPE</code> cannot be set in the request (gets ignored). Instead if you always just want roads then you can set the <code>zoom</code> parameter to a lower value like <code>16</code>..</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Mar '17, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-55053" class="comments-container">
&#10;</div>
<div id="comment-tools-55053" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55053-form-container" class="comment-form-container">
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

