+++
type = "question"
title = "Underground station"
description = '''Hi,  I live in Paris and i got problem with the visualization of a couple of underground metro stations like this one. As a map &quot;consumer&quot; i found &quot;ugly&quot; this &quot;rectangle&quot; under the street... I know that data is more important than the representation but still do you know a way to make it more user f...'''
date = "2022-06-14T13:51:00Z"
lastmod = "2022-06-19T11:27:00Z"
weight = 84770
keywords = [ "subway" ]
aliases = [ "/questions/84770" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Underground station](/questions/84770/underground-station)

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
<span id="post-84770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84770-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I live in Paris and i got problem with the visualization of a couple of underground metro stations like this <a href="https://www.openstreetmap.org/way/678701646">one</a>. As a map "consumer" i found "ugly" this "rectangle" under the street... I know that data is more important than the representation but still do you know a way to make it more user friendly? Thanks a lot. Djiril</p>
<p><img src="https://help.openstreetmap.org/upfiles/madeleine.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-subway" rel="tag" title="see questions tagged &#39;subway&#39;">subway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jun '22, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/84645cebdad17b9f1cf75d63a8f508a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Djiril&#39;s gravatar image" />
<p><span>Djiril</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Djiril has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-84770" class="comments-container">
<span id="84814"></span>
<div id="comment-84814" class="comment">
<div id="post-84814-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is an rather old and lengthy issue about the rendering of underground buildings: <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/552">https://github.com/gravitystorm/openstreetmap-carto/issues/552</a></p>
</div>
<div id="comment-84814-info" class="comment-info">
<span class="comment-age">(19 Jun '22, 11:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84770-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="84811"></span>

<div id="answer-container-84811" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84811-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As it's underground, I'd remove the building tag from all the stations.</p>
<p>Edit:</p>
<p><a href="https://overpass-turbo.eu/s/1jsk">https://overpass-turbo.eu/s/1jsk</a></p>
<p>I'd also remove two of the Madeleine stations as it contravenes this practice:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element">https://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element</a></p>
<p>What tags are required to return all 308 Paris Metro stations?</p>
<pre><code>nwr[railway=station] [station=subway] [network~&quot;Métro de Paris&quot;]</code></pre>
<p><a href="https://overpass-turbo.eu/s/1jst">https://overpass-turbo.eu/s/1jst</a></p>
<p>The above returns just 27 stations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '22, 16:26</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '22, 16:33</strong> </span></p>
</div>
</div>
<div id="comments-container-84811" class="comments-container">
<span id="84813"></span>
<div id="comment-84813" class="comment">
<div id="post-84813-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Why? <code>building:levels:underground=</code> is a thing. It's true underground structures is an undecided topic, but I won't discount representing it as a building. <code>=station</code> only says it's a station area, not a structure.</p>
</div>
<div id="comment-84813-info" class="comment-info">
<span class="comment-age">(19 Jun '22, 05:50)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-84811" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84811-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84773"></span>

<div id="answer-container-84773" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84773-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Djiril, good question but what do you mean by the illustration of a Paris Metro system. Which do you like better this one, <a href="https://www.openstreetmap.org/#map=19/52.51790/5.06688">https://www.openstreetmap.org/#map=19/52.51790/5.06688</a> or the station ? You could go back to nodes if you like, the earlier OSM times, but we are past that one. The original mapper of the station has just drawn a simple square the easiest way, but it is covered by the priority buildings have over other items.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '22, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/f367bf86ca89f96671e410e642a3664b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Teek&#39;s gravatar image" />
<p><span>Teek</span><br />
<span class="score" title="63 reputation points">63</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Teek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84773" class="comments-container">
&#10;</div>
<div id="comment-tools-84773" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84773-form-container" class="comment-form-container">
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

