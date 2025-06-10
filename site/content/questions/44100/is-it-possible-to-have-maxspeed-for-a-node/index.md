+++
type = "question"
title = "Is it possible to have maxspeed for a node ?"
description = '''Hi All, My idea is to calculate the max speed by using the open street apis giving latitude and longitude as inputs I am able to do it when the osm type is &quot;way&quot; . But for some of the latitude and longitude the osm type returned is &quot;node&quot; instead of &quot;way&quot; (It may be relation also) for which i am not...'''
date = "2015-07-10T08:19:00Z"
lastmod = "2015-07-10T14:43:00Z"
weight = 44100
keywords = [ "a", "node", "maxspeed", "for" ]
aliases = [ "/questions/44100" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to have maxspeed for a node ?](/questions/44100/is-it-possible-to-have-maxspeed-for-a-node)

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
<span id="post-44100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44100-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>My idea is to calculate the max speed by using the open street apis giving latitude and longitude as inputs I am able to do it when the osm type is "way" . But for some of the latitude and longitude the osm type returned is "node" instead of "way" (It may be relation also) for which i am not able to calculate the max speed . Is there a possibility that a particular node can have a max speed associated ?</p>
<p>Any thoughts ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-a" rel="tag" title="see questions tagged &#39;a&#39;">a</span> <span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-for" rel="tag" title="see questions tagged &#39;for&#39;">for</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '15, 08:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f5272d3a2e54ebca28981adbb4a3105f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gauravk&#39;s gravatar image" />
<p><span>Gauravk</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gauravk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44100" class="comments-container">
&#10;</div>
<div id="comment-tools-44100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44100-form-container" class="comment-form-container">
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

<span id="44102"></span>

<div id="answer-container-44102" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44102-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Which API are you using exactly? You shouldn't use the <a href="https://wiki.openstreetmap.org/wiki/API">main API</a> for such queries, instead use <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> which is both faster and more flexible.</p>
<p>With Overpass API you can specify the types of <a href="https://wiki.openstreetmap.org/wiki/Elements">elements</a> to query for. This means you can query just for ways if you like, see an <a href="http://overpass-turbo.eu/s/alx">example on overpass turbo</a>.</p>
<p>For answering your original question: A <a href="http://wiki.openstreetmap.org/wiki/Key:maxspeed">maxspeed tag</a> on a node doesn't really make sense because it lacks one important information: where does it start and where does it end? So this is no typical tagging scheme and can be completely ignored. The only useful meaning is combining it with a <a href="https://wiki.openstreetmap.org/wiki/Key:traffic_sign">traffic_sign tag</a>. But in this case it mainly refers to a traffic sign which is mostly useful for other mappers and less useful for routers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '15, 11:09</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-44102" class="comments-container">
<span id="44116"></span>
<div id="comment-44116" class="comment">
<div id="post-44116-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your response.</p>
<p>I use <a href="http://nominatim.openstreetmap.org/reverse">http://nominatim.openstreetmap.org/reverse</a> to get the osm_id by giving the latitude and longitude</p>
<p>Then using <a href="http://overpass-api.de/api/interpreter?data=way(osm_id);out;">http://overpass-api.de/api/interpreter?data=way(osm_id);out;</a> i get the maxspeed or highway type only if the first url gives a "way" type .</p>
</div>
<div id="comment-44116-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 14:43)</span> <span class="comment-user userinfo">Gauravk</span>
</div>
</div>
</div>
<div id="comment-tools-44102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44102-form-container" class="comment-form-container">
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

