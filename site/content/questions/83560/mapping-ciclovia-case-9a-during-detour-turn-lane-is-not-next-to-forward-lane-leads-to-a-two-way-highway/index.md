+++
type = "question"
title = "Mapping ciclovia-case 9a: during detour, turn lane is not next to forward lane. Leads to a two way highway"
description = '''Ciclovía is a concept created in Bogotá, Colombia in the 80s, where some normal streets are temporary blocked for cars to only allow bikes and pedestrians to go there. This only happens on Sundays mornings. In order to allow reduced traffic, there are detours, shared highways (dedicated lanes), and ...'''
date = "2022-02-23T23:42:00Z"
lastmod = "2022-02-25T11:26:00Z"
weight = 83560
keywords = [ "ciclovia", "highways", "mapping", "cycleway" ]
aliases = [ "/questions/83560" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping ciclovia-case 9a: during detour, turn lane is not next to forward lane. Leads to a two way highway](/questions/83560/mapping-ciclovia-case-9a-during-detour-turn-lane-is-not-next-to-forward-lane-leads-to-a-two-way-highway)

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
<span id="post-83560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83560-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Ciclovía is a concept created in Bogotá, Colombia in the 80s, where some normal streets are temporary blocked for cars to only allow bikes and pedestrians to go there. This only happens on Sundays mornings.</p>
<p>In order to allow reduced traffic, there are detours, shared highways (dedicated lanes), and other changes. We have created a project to map all of these conditions, initially in Bogota. This is the <a href="https://wiki.openstreetmap.org/wiki/Colombia/Project-Ciclov%C3%ADas">wiki documentation of the project</a>.</p>
<p>As part of the project, we identified several restrictions and detours cases. Here is the issue of case 9a (which is very similar to case 9 and 10).</p>
<p>This is the normal behavior of the highway:</p>
<p><img src="https://wiki.openstreetmap.org/w/images/thumb/6/6f/Case9-normal.png/862px-Case9-normal.png" alt="alt text" /></p>
<p>The mapping is simple, one highway goes up, the other goes down, and there is a turning lane, which is mapped in the a segment of the highway, with an extra lane as turning-lane. The horizontal highway is two-way.</p>
<p>This is how it looks during ciclovía (I drew the ciclovía as cycleway just for the image):</p>
<p><img src="https://help.openstreetmap.org/upfiles/Case9a-ciclovia.png" alt="alt text" /></p>
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
<p>asked <strong>23 Feb '22, 23:42</strong></p>
<img src="https://secure.gravatar.com/avatar/6998587ec6de0bab814c70777bcdd2ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AngocA&#39;s gravatar image" />
<p><span>AngocA</span><br />
<span class="score" title="281 reputation points">281</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AngocA has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-83560" class="comments-container">
<span id="83582"></span>
<div id="comment-83582" class="comment">
<div id="post-83582-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think the situation is almost the same as your standard case 9. It's just the road to the left that needs to be tagged differently.</p>
</div>
<div id="comment-83582-info" class="comment-info">
<span class="comment-age">(25 Feb '22, 11:26)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-83560" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83560-form-container" class="comment-form-container">
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

<span id="83581"></span>

<div id="answer-container-83581" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83581-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>I guess mapping the turning lane separately is the only option. But I'm not sure I fully understand the question.</p>
<p>Good luck with your project, it looks quite complicated.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Feb '22, 19:50</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</img>
</div>
</div>
<div id="comments-container-83581" class="comments-container">
&#10;</div>
<div id="comment-tools-83581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83581-form-container" class="comment-form-container">
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

