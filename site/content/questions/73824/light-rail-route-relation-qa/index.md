+++
type = "question"
title = "Light rail route relation QA"
description = '''After working on metropolitan light rail routes, I&#x27;m wondering how I can verify the relations are correct. For example; https://www.openstreetmap.org/relation/8668217 I think the relation is correct, but I&#x27;m not 100% convinced. OSM Relation Analyzer doesn&#x27;t come up &quot;green&quot;. It comes up red saying, &quot;...'''
date = "2020-03-28T22:09:00Z"
lastmod = "2020-03-29T15:39:00Z"
weight = 73824
keywords = [ "route", "relation", "light_rail" ]
aliases = [ "/questions/73824" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Light rail route relation QA](/questions/73824/light-rail-route-relation-qa)

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
<span id="post-73824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73824-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After working on metropolitan light rail routes, I'm wondering how I can verify the relations are correct. For example; <a href="https://www.openstreetmap.org/relation/8668217">https://www.openstreetmap.org/relation/8668217</a></p>
<p>I think the relation is correct, but I'm not 100% convinced. OSM Relation Analyzer doesn't come up "green". It comes up red saying, "Split into several pieces. For this relation type it is required that it exists as one piece." Is it coming up red because I added stations and platforms and it thinks these elements are not physically attached to one another? When I click on the, "Analyze on map" button, I get a map of the relation with blue nodes displayed. These are alerts to errors? If they are errors, what needs to be corrected? When I click on the nodes I see, "Graph 0, Graph 1, Graph 2, etc." What does that mean?</p>
<p>I'm also attempting to use the JOSM relation window. There's nobody in my geographical area who can sit down with me and show me how to use it properly. When I click on, "sort the relation members" button. Does that mean JOSM sorts the ways so they're in the correct order after pressing the button? I assume JOSM sorts the various members based on element type in this window, e.g., platforms together, ways together, stations together? After sorting I see a tiny red dot at the top and the same red dot at the bottom of the window...meaning it's all sorted correctly now? If the platforms and stations are not sorted correctly, I assume I need to manually sort them, first station/platform at the top and then in descending order from top to bottom of the screen? Yep, a lot of questions here ;)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-light_rail" rel="tag" title="see questions tagged &#39;light_rail&#39;">light_rail</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Mar '20, 22:09</strong></p>
<img src="https://secure.gravatar.com/avatar/97e2f141b910d9a08dabfc0865382491?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chachafish&#39;s gravatar image" />
<p><span>chachafish</span><br />
<span class="score" title="411 reputation points">411</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chachafish has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-73824" class="comments-container">
&#10;</div>
<div id="comment-tools-73824" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73824-form-container" class="comment-form-container">
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

<span id="73826"></span>

<div id="answer-container-73826" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73826-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>A validation within JOSM (using SHIFT-V) shows that the role of the stations are missing in the relation. The role should probably be "stop" as explained here for the members of the relation : <a href="https://wiki.openstreetmap.org/wiki/Tag:route%3Dlight_rail">https://wiki.openstreetmap.org/wiki/Tag:route%3Dlight_rail</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '20, 04:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a588fbc312ece948db9faa4cc02b40de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zorglubu&#39;s gravatar image" />
<p><span>zorglubu</span><br />
<span class="score" title="324 reputation points">324</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zorglubu has 3 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-73826" class="comments-container">
<span id="73841"></span>
<div id="comment-73841" class="comment">
<div id="post-73841-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you :)</p>
</div>
<div id="comment-73841-info" class="comment-info">
<span class="comment-age">(29 Mar '20, 15:39)</span> <span class="comment-user userinfo">chachafish</span>
</div>
</div>
</div>
<div id="comment-tools-73826" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73826-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73827"></span>

<div id="answer-container-73827" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73827-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi chachafish, my answer is only about learning JOSM and Relations In JOSM walking-, cycling-, bus- and train routes are all treated as relations</p>
<p>1) Learn OSM <a href="https://learnosm.org/en/">https://learnosm.org/en/</a> 2) Wiki <a href="https://wiki.openstreetmap.org/wiki/JOSM">https://wiki.openstreetmap.org/wiki/JOSM</a> 3) Relations <a href="https://wiki.openstreetmap.org/wiki/Relation">https://wiki.openstreetmap.org/wiki/Relation</a></p>
<p>Polyglot is a Belgian mapper, he is the relation expert</p>
<p>Interview : <a href="https://openstreetmap.be/en/motm/2016/01/01/polyglot.html">https://openstreetmap.be/en/motm/2016/01/01/polyglot.html</a></p>
<p>Diary : <a href="https://www.openstreetmap.org/user/Polyglot/diary/38980">https://www.openstreetmap.org/user/Polyglot/diary/38980</a></p>
<p>His plugin for JOSM to edit relations <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/PT_Assistant">https://wiki.openstreetmap.org/wiki/JOSM/Plugins/PT_Assistant</a></p>
<p>hth Gys</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '20, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/5c3b258ebdc5943f1ab6008f146e7f7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gys%20de%20Jongh&#39;s gravatar image" />
<p><span>Gys de Jongh</span><br />
<span class="score" title="713 reputation points">713</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gys de Jongh has 5 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-73827" class="comments-container">
<span id="73842"></span>
<div id="comment-73842" class="comment">
<div id="post-73842-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great! Thanks :)</p>
</div>
<div id="comment-73842-info" class="comment-info">
<span class="comment-age">(29 Mar '20, 15:39)</span> <span class="comment-user userinfo">chachafish</span>
</div>
</div>
</div>
<div id="comment-tools-73827" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73827-form-container" class="comment-form-container">
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

