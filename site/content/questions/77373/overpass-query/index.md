+++
type = "question"
title = "Overpass : Query"
description = '''Hello,  A school will have a number of buildings and they will be located close by. I tried with overpass the query which can select only one of these buildings and skip the rest. But not Proper working. Can you tell me the query for that ....  https://overpass-turbo.eu/s/ZEM  [out:json] [timeout:25...'''
date = "2020-11-03T12:11:00Z"
lastmod = "2020-11-03T19:16:00Z"
weight = 77373
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/77373" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass : Query](/questions/77373/overpass-query)

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
<span id="post-77373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77373-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,<br />
A school will have a number of buildings and they will be located close by. I tried with overpass the query which can select only one of these buildings and skip the rest. But not Proper working. Can you tell me the query for that ....<br />
<a href="https://overpass-turbo.eu/s/ZEM">https://overpass-turbo.eu/s/ZEM</a><br />
<code> [out:json] [timeout:25]; way({{bbox}})[amenity=school]; map_to_area -&gt;.area; ( ( node </code><a href="%7B%7Bbbox%7D%7D"><code>"building"="school"</code></a><code>; way </code><a href="%7B%7Bbbox%7D%7D"><code>"building"="school"</code></a><code>; )-&gt;.scl; ( ( node ["building"="school"]</code><a href="%7B%7Bbbox%7D%7D"><code>"amenity"!~"."</code></a><code>; way ["building"="school"]</code><a href="%7B%7Bbbox%7D%7D"><code>"amenity"!~"."</code></a><code>; ); - ( // All nodes+ways with building=school and no amenity=* tag in area node ["building"="school"]</code><a href="area.area"><code>"amenity"!~"."</code></a><code>; way ["building"="school"]</code><a href="area.area"><code>"amenity"!~"."</code></a><code>;</code><br />
<code>);)-&gt;.samp1; ( node.samp1(around.scl:100); way.samp1(around.scl:100); )-&gt;.near; (.samp1; - .near;); ); out center; </code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Nov '20, 12:11</strong></p>
<img src="https://secure.gravatar.com/avatar/fc9c2a007c6f81684415bb1f16f2991c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VIPINDAS%20K&#39;s gravatar image" />
<p><span>VIPINDAS K</span><br />
<span class="score" title="125 reputation points">125</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VIPINDAS K has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-77373" class="comments-container">
<span id="77374"></span>
<div id="comment-77374" class="comment">
<div id="post-77374-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To start with, the {bbox} you provided there is no amenity=school so your first two lines will return nothing. Which building are you attempting to single out?</p>
</div>
<div id="comment-77374-info" class="comment-info">
<span class="comment-age">(03 Nov '20, 12:49)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="77377"></span>
<div id="comment-77377" class="comment">
<div id="post-77377-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>school building (outside the tag "amenity = school")</p>
</div>
<div id="comment-77377-info" class="comment-info">
<span class="comment-age">(03 Nov '20, 13:38)</span> <span class="comment-user userinfo">VIPINDAS K</span>
</div>
</div>
</div>
<div id="comment-tools-77373" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77373-form-container" class="comment-form-container">
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

<span id="77380"></span>

<div id="answer-container-77380" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77380-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I /think/ you may have over complicated things. It's unclear if you wan one or all those outside</p>
<p>Edit:</p>
<p><a href="https://overpass-turbo.eu/s/ZH6">https://overpass-turbo.eu/s/ZH6</a></p>
<pre><code>[bbox:{{bbox}}];
(
  nw[building=school];
  -
  (
    way[amenity=school];map_to_area;
    nw(area)[building=school];
  );
)-&gt;.Outside;  
foreach .Outside (
  way.Outside(around:100);
  way._(if:count(ways) == 1);
  out center;
);</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '20, 14:54</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Nov '20, 17:10</strong> </span></p>
</div>
</div>
<div id="comments-container-77380" class="comments-container">
<span id="77381"></span>
<div id="comment-77381" class="comment">
<div id="post-77381-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is exactly what is needed. But select only one school building and deselect the school building around it (within 100 meters). Is this possible?</p>
</div>
<div id="comment-77381-info" class="comment-info">
<span class="comment-age">(03 Nov '20, 15:07)</span> <span class="comment-user userinfo">VIPINDAS K</span>
</div>
</div>
<span id="77382"></span>
<div id="comment-77382" class="comment">
<div id="post-77382-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So you want all school buildings outside the perimeter of the school amenity, that are at least 100m away from other school buildings. Is that correct?</p>
</div>
<div id="comment-77382-info" class="comment-info">
<span class="comment-age">(03 Nov '20, 15:19)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="77384"></span>
<div id="comment-77384" class="comment">
<div id="post-77384-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. (Select only one school building within 100 meter and skip the rest)</p>
</div>
<div id="comment-77384-info" class="comment-info">
<span class="comment-age">(03 Nov '20, 15:25)</span> <span class="comment-user userinfo">VIPINDAS K</span>
</div>
</div>
<span id="77386"></span>
<div id="comment-77386" class="comment">
<div id="post-77386-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've updated the routine</p>
</div>
<div id="comment-77386-info" class="comment-info">
<span class="comment-age">(03 Nov '20, 17:11)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="77388"></span>
<div id="comment-77388" class="comment">
<div id="post-77388-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much for your help .... Let there be 5 school buildings in one place (around 100 meters), select only one of them(and deselect the other school buildings). This is not possible in this query ... Can you include that too ....</p>
</div>
<div id="comment-77388-info" class="comment-info">
<span class="comment-age">(03 Nov '20, 19:16)</span> <span class="comment-user userinfo">VIPINDAS K</span>
</div>
</div>
</div>
<div id="comment-tools-77380" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77380-form-container" class="comment-form-container">
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

