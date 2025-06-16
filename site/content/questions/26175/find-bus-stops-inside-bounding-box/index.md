+++
type = "question"
title = "Find bus stops inside bounding box"
description = '''I&#x27;m building a mobile application. One of the features shows bus stops on a map. When the user zooms in far enough, bus stops should load for the area they are looking at. I have found part of the API that should help me do this: /api/0.6/map?bbox=left,bottom,right,top This should be called every ti...'''
date = "2013-09-07T13:26:00Z"
lastmod = "2013-09-09T11:31:00Z"
weight = 26175
keywords = [ "mobile", "bus", "api", "busstops", "bbox" ]
aliases = [ "/questions/26175" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Find bus stops inside bounding box](/questions/26175/find-bus-stops-inside-bounding-box)

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
<span id="post-26175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26175-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm building a mobile application. One of the features shows bus stops on a map. When the user zooms in far enough, bus stops should load for the area they are looking at.</p>
<p>I have found part of the API that should help me do this:</p>
<p>/api/0.6/map?bbox=left,bottom,right,top</p>
<p>This should be called every time the user pans around the map so that it loads a fresh set of bus stops for that area. My problem is, when I do this I'm receiving way too much data that is not related to the bus stops. I need to see nodes only by user: NaPTAN (104459). Is there a way I can filter down the results like this? Essentially I need to be loading the bus stops every time the user pans across the map, for this to be productive the bus stops need to have been loaded ideally &gt; 500 milliseconds and &lt; 1 second. It would also probably be better to receive the files in JSON format rather than XML as this will save a chunk of bytes increasing download speed.</p>
<p>If anyone can give me advice on the best way to do this I'd really appreciate it!</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Sep '13, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/798374ef5cfa2acd48be598c543fdcd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jskidd3&#39;s gravatar image" />
<p><span>jskidd3</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jskidd3 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26175" class="comments-container">
&#10;</div>
<div id="comment-tools-26175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26175-form-container" class="comment-form-container">
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

<span id="26183"></span>

<div id="answer-container-26183" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26183-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-26183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jskidd3 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> allows to specify complex filters. It is also faster and more suited than the main API which is actually for editing and not for running bulk queries. Another option is to download the data in advance to store it locally. This way you are completely independent from the API and don't have to comply with the usage policy.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '13, 19:39</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-26183" class="comments-container">
&#10;</div>
<div id="comment-tools-26183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26183-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26177"></span>

<div id="answer-container-26177" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26177-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-26177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>you should not use API 0.6 for that, see it's <a href="https://wiki.openstreetmap.org/wiki/API_usage_policy">usage policy</a> - it is intended for editing only, and for such queries. There are alternative ways mentioned on the page, from setting up your own server syncing data with master openstreetmap servers, to using third party services.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '13, 17:22</strong></p>
<img src="https://secure.gravatar.com/avatar/666391973130e371bf8092f70c43df28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matija%20Nalis&#39;s gravatar image" />
<p><span>Matija Nalis</span><br />
<span class="score" title="750 reputation points">750</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matija Nalis has 2 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-26177" class="comments-container">
&#10;</div>
<div id="comment-tools-26177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26177-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26226"></span>

<div id="answer-container-26226" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26226-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As already stated Overpass should help you. Have a look how overpass-turbo does it:</p>
<p>If you only need the coordinates: <a href="http://overpass-turbo.eu/s/10g">http://overpass-turbo.eu/s/10g</a></p>
<p>If you need more details: <a href="http://overpass-turbo.eu/s/10h">http://overpass-turbo.eu/s/10h</a></p>
<p>You will probably have to consider whether you really want to query for each single pan (or if it would be better to query a bigger bbox and only requery if the user leaves the bbox).</p>
<p>/al</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '13, 11:31</strong></p>
<img src="https://secure.gravatar.com/avatar/5501080a7333d6383d6c545f076eaeba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_al&#39;s gravatar image" />
<p><span>_al</span><br />
<span class="score" title="860 reputation points">860</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_al has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-26226" class="comments-container">
&#10;</div>
<div id="comment-tools-26226" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26226-form-container" class="comment-form-container">
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

