+++
type = "question"
title = "Get all bicycle infrastructure for a city"
description = '''I am trying to write a query to get all bike lanes to display on a map for my project. I want to display all types of bike lanes(shared ,dedicated,tracks etc)  [out:json][timeout:25]; // gather results ( // query part for: “cycleway=*” // sharrow way&quot;cycleway&quot;=&quot;shared_lane&quot; ; // CONVENTIONAL BICYCLE...'''
date = "2018-07-23T23:21:00Z"
lastmod = "2018-07-24T21:57:00Z"
weight = 64879
keywords = [ "overpassapi", "bikemap", "bikepath", "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/64879" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get all bicycle infrastructure for a city](/questions/64879/get-all-bicycle-infrastructure-for-a-city)

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
<span id="post-64879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64879-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to write a query to get all bike lanes to display on a map for my project. I want to display all types of bike lanes(shared ,dedicated,tracks etc)</p>
<blockquote>
<p>[out:json][timeout:25]; // gather results ( // query part for: “cycleway=*”</p>
<p>// sharrow<br />
way<a href="%7B%7Bbbox%7D%7D">"cycleway"="shared_lane"</a> ;</p>
<p>// CONVENTIONAL BICYCLE LANE // lane on both sides of the street<br />
way<a href="%7B%7Bbbox%7D%7D">"cycleway"="lane"</a>;</p>
<p>// lane on either side<br />
way<a href="%7B%7Bbbox%7D%7D">"cycleway:left"</a>;<br />
way<a href="%7B%7Bbbox%7D%7D">"cycleway:right"</a>;</p>
<p>// dedicated bikeways<br />
way<a href="%7B%7Bbbox%7D%7D">"highway"="cycleway"</a>;</p>
<p>way<a href="%7B%7Bbbox%7D%7D">"bicycle"="designated"</a>;</p>
<p>); out body;</p>
<blockquote>
<p>; out skel qt;</p>
</blockquote>
</blockquote>
<p>Am I missing some parameters because I am not getting the same map as open cycle maps. I understand that the open cycle maps is displaying cycling routes as well. So I added the parameter</p>
<blockquote>
<p>relation<a href="%7B%7Bbbox%7D%7D">"route"="bicycle"</a>;</p>
</blockquote>
<p>But I am not very sure about what a relation is. Also it gives a lot of overlapping paths. Are all bile paths covered under a relation? Also from my understanding, this relation also has routes which would not necessarily go through a bike path. Coming back to my original question, are there any other parameters that I can add to my query to get all bike paths?</p>
<p>I found this query on overpass turbo:</p>
<blockquote>
<p>/ <em>This shows the cycleway and cycleroute network.</em> /</p>
<p>[out:json];</p>
<p>( // get cycle route relatoins<br />
relation<a href="%7B%7Bbbox%7D%7D">route=bicycle</a>;<br />
// get cycleways<br />
way<a href="%7B%7Bbbox%7D%7D">highway=cycleway</a>;<br />
way[highway=path]<a href="%7B%7Bbbox%7D%7D">bicycle=designated</a>; );</p>
<p>out body;</p>
<blockquote>
<p>; out skel qt;</p>
</blockquote>
</blockquote>
<p>But this doesn't show info about the paths like shares, one way, left,right. I want all these parameters as well to segregate the diff types of bicycle paths</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-bikemap" rel="tag" title="see questions tagged &#39;bikemap&#39;">bikemap</span> <span class="post-tag tag-link-bikepath" rel="tag" title="see questions tagged &#39;bikepath&#39;">bikepath</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '18, 23:21</strong></p>
<img src="https://secure.gravatar.com/avatar/c164cc6fe024972bdbe1d1d20525ee41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="isj126&#39;s gravatar image" />
<p><span>isj126</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="isj126 has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-64879" class="comments-container">
&#10;</div>
<div id="comment-tools-64879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64879-form-container" class="comment-form-container">
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

<span id="64898"></span>

<div id="answer-container-64898" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64898-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Bicycle routes are a list of ways (which could be normal streets, cycleways and so on) that are part of the route, not directly infrastructure itself.</p>
<p>To get all cycle infrastructure you will need to retrieve at least:</p>
<ul>
<li>all roads that have additional tags indicating cycle infrastructure (cycleway=lane and cycleway=track)</li>
<li>all highway=cycleway</li>
<li>all highway=footway and highway=path that allow bicycle use or are intended for such (bicycle=yes, bicycle=designated, bicycle=official)</li>
</ul>
<p>You will probably further need to de-duplicate roads from the first point that actually have separately mapped infrastructure from the last two items.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '18, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span> </br></br></p>
</div>
</div>
<div id="comments-container-64898" class="comments-container">
&#10;</div>
<div id="comment-tools-64898" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64898-form-container" class="comment-form-container">
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

