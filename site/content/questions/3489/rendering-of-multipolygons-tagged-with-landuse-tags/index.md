+++
type = "question"
title = "Rendering of multipolygons tagged with landuse tags"
description = '''I have been updating the map of my local area to better use the capabilities of the multipolygon relations and I have run into some apparent rendering bugs. Relation 1441560 is tagged with landuse=residential and type=multipolygon and relation 1444850 is similarly tagged. Both relations are closed a...'''
date = "2011-03-02T20:05:00Z"
lastmod = "2011-03-09T18:53:00Z"
weight = 3489
keywords = [ "rendering", "landuse", "residential", "multipolygon" ]
aliases = [ "/questions/3489" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering of multipolygons tagged with landuse tags](/questions/3489/rendering-of-multipolygons-tagged-with-landuse-tags)

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
<span id="post-3489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3489-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been updating the map of my local area to better use the capabilities of the multipolygon relations and I have run into some apparent rendering bugs. Relation 1441560 is tagged with landuse=residential and type=multipolygon and relation 1444850 is similarly tagged. Both relations are closed and thus, in theory, should show up in the default OSM view and be rendered as a grey background to the map.</p>
<p>However relation 1441560 shows up as grey as expected and relation 1444850 does not show up grey as expected. What might be causing this rendering difference and how should it be fixed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-residential" rel="tag" title="see questions tagged &#39;residential&#39;">residential</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '11, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/af12631e82ba0646269cf40b15363c27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Newton&#39;s gravatar image" />
<p><span>David Newton</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Newton has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3489" class="comments-container">
&#10;</div>
<div id="comment-tools-3489" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3489-form-container" class="comment-form-container">
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

<span id="3490"></span>

<div id="answer-container-3490" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3490-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Contary to your expectations relation 1444850 does not appear to be closed, and has two segments, the smaller of which is closed. It is always a good idea to check a relation using <a href="http://ra.osmsurround.org/analyze.jsp?relationId=1444850">Relation Analyser</a>, but it is usually possible to resolve relation problems by using JOSM.</p>
<p>Dowload only the relation using the option "Download Object", and use the relation panel (on RHS of screen) to find ways in the relation which do not join as expected. JOSM can automatically sort the members of the relation and this often highlights where the problem lies. Once the precise area is known download all ways in that surrounding bounding box and fix connectivity. Repeat until your relation is as you expect.</p>
<p>In your case you have a) to joined Cross lane to the landuse=residential way to its NE and b) you have a small extra circular way around the Guide Dogs for the Blind building. The latter may be intentional, but you certainly need to join Cross Lane to the other way to complete your relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '11, 20:26</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-3490" class="comments-container">
<span id="3491"></span>
<div id="comment-3491" class="comment">
<div id="post-3491-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the help. I see the very small gap that two immensely close together nodes caused. I will deal with that and see what happens with the rendering. The Guide Dogs portion was deliberate, and I will have to see what I might find in the multipolygon I have created of that site's business use.</p>
</div>
<div id="comment-3491-info" class="comment-info">
<span class="comment-age">(02 Mar '11, 22:31)</span> <span class="comment-user userinfo">David Newton</span>
</div>
</div>
</div>
<div id="comment-tools-3490" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3490-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3492"></span>

<div id="answer-container-3492" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3492-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I notice relation 1444850 is tagged as <code>landuse=residential</code>, <code>type=landuse</code>. It should be tagged as <code>type=multipolygon</code> (and <code>landuse=residential</code>).</p>
<p>Also, it probably won't affect rendering, but its usually helpful to specify the roles for the members of your relation. I think this should be <code>outer</code> for all of the parts in these examples.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '11, 23:23</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-3492" class="comments-container">
<span id="3659"></span>
<div id="comment-3659" class="comment">
<div id="post-3659-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It definitely needed the relation to be tagged as type=multipolygon for it to render correctly. Doing so caused the grey background of the residential area to appear and also the green of the park background of other relations in the area. It appears the problem with the Guide Dogs site was a mis-spelling of commercial as commmercial.</p>
</div>
<div id="comment-3659-info" class="comment-info">
<span class="comment-age">(09 Mar '11, 18:53)</span> <span class="comment-user userinfo">David Newton</span>
</div>
</div>
</div>
<div id="comment-tools-3492" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3492-form-container" class="comment-form-container">
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

