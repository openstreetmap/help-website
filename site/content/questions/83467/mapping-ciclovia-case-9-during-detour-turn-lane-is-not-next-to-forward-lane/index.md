+++
type = "question"
title = "Mapping ciclovia-case 9: during detour, turn lane is not next to forward lane"
description = '''Ciclovía is a concept created in Bogotá, Colombia in the 80s, where some normal streets are temporary blocked for cars to only allow bikes and pedestrians to go there. This only happens on Sundays mornings. In order to allow reduced traffic, there are detours, shared highways (dedicated lanes), and ...'''
date = "2022-02-14T03:14:00Z"
lastmod = "2022-02-24T09:30:00Z"
weight = 83467
keywords = [ "ciclovia", "highways", "mapping", "cycleway" ]
aliases = [ "/questions/83467" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping ciclovia-case 9: during detour, turn lane is not next to forward lane](/questions/83467/mapping-ciclovia-case-9-during-detour-turn-lane-is-not-next-to-forward-lane)

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
<span id="post-83467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83467-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Ciclovía is a concept created in Bogotá, Colombia in the 80s, where some normal streets are temporary blocked for cars to only allow bikes and pedestrians to go there. This only happens on Sundays mornings.</p>
<p>In order to allow reduced traffic, there are detours, shared highways (dedicated lanes), and other changes. We have created a project to map all of these conditions, initially in Bogota. This is the <a href="https://wiki.openstreetmap.org/wiki/Colombia/Project-Ciclov%C3%ADas">wiki documentation of the project</a>.</p>
<p>As part of the project, we identified several restrictions and detours cases. Here is the issue of case 9 (which is very similar to case 9a and 10).</p>
<p>This is the normal behavior of the highway:</p>
<p><img src="https://wiki.openstreetmap.org/w/images/thumb/6/6f/Case9-normal.png/862px-Case9-normal.png" alt="alt text" /></p>
<p>The mapping is simple, one highway goes up, the other goes down, and there is a turning lane, which is mapped in the a segment of the highway, with an extra lane as turning-lane. The horizontal highway is one-way, to the left.</p>
<p>This is how it looks during ciclovía (I drew the ciclovía as cycleway just for the image):</p>
<p><img src="https://wiki.openstreetmap.org/w/images/thumb/d/de/Case9-ciclovia.png/864px-Case9-ciclovia.png" alt="alt text" /></p>
<p>As you can see, the right highway is both-ways; however, the turning lane is not next to the lane that goes up.</p>
<p>This image describe the best the situation: <a href="https://www.mapillary.com/app/?pKey=439627097551960">https://www.mapillary.com/app/?pKey=439627097551960</a></p>
<p>How can we map this condition? Should I map the turning lane independently from the highway as a separated highway?</p>
<p>This is a <a href="https://github.com/MaptimeBogota/Varios/blob/main/proyecto-ciclovia/cases/cicloviaCases.osm">JOSM file to play with the highway</a> and propose a solution.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ciclovia" rel="tag" title="see questions tagged &#39;ciclovia&#39;">ciclovia</span> <span class="post-tag tag-link-highways" rel="tag" title="see questions tagged &#39;highways&#39;">highways</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-cycleway" rel="tag" title="see questions tagged &#39;cycleway&#39;">cycleway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Feb '22, 03:14</strong></p>
<img src="https://secure.gravatar.com/avatar/6998587ec6de0bab814c70777bcdd2ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AngocA&#39;s gravatar image" />
<p><span>AngocA</span><br />
<span class="score" title="281 reputation points">281</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AngocA has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Feb '22, 23:43</strong> </span></p>
</div>
</div>
<div id="comments-container-83467" class="comments-container">
<span id="83468"></span>
<div id="comment-83468" class="comment">
<div id="post-83468-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So you're not able to turn right from the rightmost road during the restrictions?</p>
</div>
<div id="comment-83468-info" class="comment-info">
<span class="comment-age">(14 Feb '22, 07:51)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="83469"></span>
<div id="comment-83469" class="comment">
<div id="post-83469-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>AngocA, your drawing indicates the road going to the left is oneway, regardless of time. The Mapillary picture suggests otherwise. Could you clarify?</p>
</div>
<div id="comment-83469-info" class="comment-info">
<span class="comment-age">(14 Feb '22, 09:13)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="83559"></span>
<div id="comment-83559" class="comment">
<div id="post-83559-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>TZorn, you are right! I will create another question for that case. It is calle 9a at <a href="https://wiki.openstreetmap.org/wiki/Colombia/Project-Ciclov%C3%ADas">https://wiki.openstreetmap.org/wiki/Colombia/Project-Ciclov%C3%ADas</a></p>
</div>
<div id="comment-83559-info" class="comment-info">
<span class="comment-age">(23 Feb '22, 23:38)</span> <span class="comment-user userinfo">AngocA</span>
</div>
</div>
</div>
<div id="comment-tools-83467" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83467-form-container" class="comment-form-container">
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

<span id="83470"></span>

<div id="answer-container-83470" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83470-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As a first step you could forget about the lanes and just tag the right carriageway as:<br />
<code>oneway=yes</code><br />
<code>oneway:conditional = no @ (Su 9:00-13:00)</code> (or whatever the exact times are)</p>
<p>The left (downward) carriageway would get:<br />
<code>oneway=yes</code><br />
<code>oneway:conditional = no @ (Su 9:00-13:00)</code><br />
<code>vehicle:conditional = no @ (Su 9:00-13:00)</code><br />
<code>bicycle:conditional = designated @ (Su 9:00-13:00)</code></p>
<p>This could be interpreted by data consumers to have enough information for proper routing.</p>
<p>Tagging the lanes correctly is getting messy and I doubt many data consumers will understand it. But of course feel free to tag something like:<br />
<code>lanes=</code><br />
<code>lanes:foward =</code><br />
<code>lanes:backward =</code><br />
<code>lanes:forward:conditonal =</code><br />
<code>lanes:backward:contitional =</code><br />
<code>oneway:lanes:conditional =</code><br />
<code>turn:lanes:conditional =</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '22, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Feb '22, 08:31</strong> </span></p>
</div>
</div>
<div id="comments-container-83470" class="comments-container">
<span id="83562"></span>
<div id="comment-83562" class="comment">
<div id="post-83562-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>With this tagging scheme, do you propose to tag the left lane as an independent highway with the given properties?</p>
</div>
<div id="comment-83562-info" class="comment-info">
<span class="comment-age">(24 Feb '22, 00:11)</span> <span class="comment-user userinfo">AngocA</span>
</div>
</div>
<span id="83575"></span>
<div id="comment-83575" class="comment">
<div id="post-83575-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For the turn lane you mean? No, that would be wrong as there is no physical deviation between the turn lane and the two main lanes.</p>
<p>I'm afraid there is currently no way in OSM to map this situation 100% correctly. Given that this is a very uncommon corner case I would approximate it as good as possible and live with it.</p>
<p>There has been a <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/driving_direction">proposal for <code>driving_direction:lanes</code></a> which could be used here but the proposal has been abandoned and the tag is poorly adopted.</p>
</div>
<div id="comment-83575-info" class="comment-info">
<span class="comment-age">(24 Feb '22, 09:30)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-83470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83470-form-container" class="comment-form-container">
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

