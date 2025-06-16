+++
type = "question"
title = "Overpass area query by ID instead of by NAME"
description = '''Hi OSMappers, I&#x27;m using overpass to get all the suburbs of a city. I can do it by setting this option: area[name=&quot;CITY NAME&quot;] but what I want to is to get the infos by the ID of the city instead. Is it possible to do something like this? area[id=&quot;CITY ID&quot;] This is my actual url: http://MY-URL.com/ap...'''
date = "2017-06-11T10:26:00Z"
lastmod = "2017-06-11T14:15:00Z"
weight = 56576
keywords = [ "overpass", "overpass-api", "area" ]
aliases = [ "/questions/56576" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass area query by ID instead of by NAME](/questions/56576/overpass-area-query-by-id-instead-of-by-name)

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
<span id="post-56576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56576-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi OSMappers,</p>
<p>I'm using overpass to get all the suburbs of a city. I can do it by setting this option:</p>
<p><strong>area[name="CITY NAME"]</strong></p>
<p>but what I want to is to get the infos by the ID of the city instead. Is it possible to do something like this?</p>
<p><strong>area[id="CITY ID"]</strong></p>
<p>This is my actual url:</p>
<pre><code>http://MY-URL.com/api/interpreter?data=[out:csv(::type,&quot;place&quot;,::id,&quot;name&quot;,::lat,::lon)];area[name=&quot;CITY NAME&quot;][admin_level=8][boundary=administrative]-&gt;.RESULTS;rel(pivot.RESULTS);node[place=&quot;suburb&quot;](area.RESULTS);out;</code></pre>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jun '17, 10:26</strong></p>
<img src="https://secure.gravatar.com/avatar/e3ce7e9f39d82f7ffe0804c65aa73798?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carapace&#39;s gravatar image" />
<p><span>carapace</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carapace has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56576" class="comments-container">
&#10;</div>
<div id="comment-tools-56576" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56576-form-container" class="comment-form-container">
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

<span id="56579"></span>

<div id="answer-container-56579" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56579-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If by city id you mean an OSM id for an object representing a city, there is a mapping between OSM ids and Overpass areas. There is decent discussion of how it works in the documentation: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_area_.28area.29</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jun '17, 14:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-56579" class="comments-container">
&#10;</div>
<div id="comment-tools-56579" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56579-form-container" class="comment-form-container">
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

