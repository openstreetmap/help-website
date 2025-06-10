+++
type = "question"
title = "Find features (e.g. man_made=chimney) exceeding a certain size limit"
description = '''I would like to find things wrongly tagged as man_made=chimney like cooling towers or even just generic industrial buildings. This would be very easy – because chimneys are always very slim – if I could query for man_made=chimney + give a minimum size, maybe 60 m^2. If it&#x27;s not directly possible wit...'''
date = "2018-05-15T08:35:00Z"
lastmod = "2018-05-16T06:10:00Z"
weight = 63484
keywords = [ "overpass", "size", "postgis", "chimney", "query" ]
aliases = [ "/questions/63484" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Find features (e.g. man_made=chimney) exceeding a certain size limit](/questions/63484/find-features-eg-man_madechimney-exceeding-a-certain-size-limit)

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
<span id="post-63484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63484-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-63484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to find things wrongly tagged as man_made=chimney like cooling towers or even just generic industrial buildings.</p>
<p>This would be very easy – because chimneys are always very slim – if I could query for man_made=chimney + give a minimum size, maybe 60 m^2.</p>
<p>If it's not directly possible with Overpass: I have no objections to use postgis (ogr2ogr).</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-chimney" rel="tag" title="see questions tagged &#39;chimney&#39;">chimney</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '18, 08:35</strong></p>
<img src="https://secure.gravatar.com/avatar/bdb6a1b49c42d8be4b8d87f3096a3622?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Druzhba&#39;s gravatar image" />
<p><span>Druzhba</span><br />
<span class="score" title="150 reputation points">150</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Druzhba has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63484" class="comments-container">
&#10;</div>
<div id="comment-tools-63484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63484-form-container" class="comment-form-container">
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

<span id="63487"></span>

<div id="answer-container-63487" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63487-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Druzhba has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass doesn't have area size filtering but you can cheat a bit and <a href="http://overpass-turbo.eu/s/yOD">use length</a>:</p>
<pre><code>[out:json][timeout:25][bbox:{{bbox}}];
way[man_made=chimney](if:length() &gt; 25);
out geom;</code></pre>
<p>Chimneys should mostly be geometries where the relationship between area and perimeter is pretty direct, so I don't think it will catch a lot of false positives.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '18, 12:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-63487" class="comments-container">
<span id="63489"></span>
<div id="comment-63489" class="comment">
<div id="post-63489-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've mapped many chimneys in Thailand, mostly those attached to crematoria, but have never added a height because I don't have the time or equipment in the field to make such measurements. I think most chimneys are, like the ones I added, simple nodes tagged man_mde=chimney so Max's query probably won't return many objects.</p>
<p>Cheers,</p>
<p>Dave</p>
</div>
<div id="comment-63489-info" class="comment-info">
<span class="comment-age">(15 May '18, 16:47)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="63491"></span>
<div id="comment-63491" class="comment">
<div id="post-63491-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5016/alaskadave">@alaskadave</a> - I think that this is about the <em>ground area</em> occupied by the feature rather than the height. There are <a href="https://taginfo.openstreetmap.org/tags/man_made=chimney">32k nodes, but still 7k ways</a>, which is still a significant number.</p>
<p>(I'm mentioning this because I referred to this answer in reply to an entirely separate question over at the <a href="https://forum.openstreetmap.org/viewtopic.php?id=62222">forum</a>).</p>
</div>
<div id="comment-63491-info" class="comment-info">
<span class="comment-age">(15 May '18, 17:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63492"></span>
<div id="comment-63492" class="comment">
<div id="post-63492-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Aha. Thanks for the clarification.</p>
<p>I didn't think about ground area at all so I didn't do any checking for ways vs nodes before I answered. Even knowing that, the query will produce data for only 7K out of a total of 40K objects.</p>
</div>
<div id="comment-63492-info" class="comment-info">
<span class="comment-age">(15 May '18, 17:21)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="63500"></span>
<div id="comment-63500" class="comment">
<div id="post-63500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Dave: You can "guesstimate" the height if the Bing or DG as shadows. If you have the shadow of say known height close by. eg a two story block say 6 meters by a chimney with double or triple shadow chimney will be 12 to 18 meters. I realise that Thailand might be fairley shadow free but in the UK 50 degrees north we always have shadows.</p>
</div>
<div id="comment-63500-info" class="comment-info">
<span class="comment-age">(16 May '18, 06:10)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-63487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63487-form-container" class="comment-form-container">
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

