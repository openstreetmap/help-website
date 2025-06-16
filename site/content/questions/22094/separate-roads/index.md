+++
type = "question"
title = "Separate roads?"
description = '''Can someone tell me how to fix these roads -&amp;gt;https://www.openstreetmap.org/?lat=61.96632&amp;amp;lon=26.97533&amp;amp;zoom=16&amp;amp;layers=M You can see that there is many separate roads called Henkisalmentie. How can i combine the roads in to one road. I tried to combine them in JOSM and Potlatch but I cou...'''
date = "2013-05-04T16:47:00Z"
lastmod = "2013-05-04T19:20:00Z"
weight = 22094
keywords = [ "merge", "combine", "road", "separate" ]
aliases = [ "/questions/22094" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Separate roads?](/questions/22094/separate-roads)

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
<span id="post-22094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22094-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can someone tell me how to fix these roads -&gt;<a href="https://www.openstreetmap.org/?lat=61.96632&amp;lon=26.97533&amp;zoom=16&amp;layers=M">https://www.openstreetmap.org/?lat=61.96632&amp;lon=26.97533&amp;zoom=16&amp;layers=M</a></p>
<p>You can see that there is many separate roads called Henkisalmentie. How can i combine the roads in to one road. I tried to combine them in JOSM and Potlatch but I couldn't do it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-combine" rel="tag" title="see questions tagged &#39;combine&#39;">combine</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-separate" rel="tag" title="see questions tagged &#39;separate&#39;">separate</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '13, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/e27726a8f06d67072ad90c8d932e6ff3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rainis&#39;s gravatar image" />
<p><span>Rainis</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rainis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22094" class="comments-container">
<span id="22099"></span>
<div id="comment-22099" class="comment">
<div id="post-22099-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is no need to combine them (which is impossible anyway as already explained). If these streets share the same name and are connected to each other via shared nodes (or are at least in the near surrounding) it is clear that they are in fact the same road.</p>
</div>
<div id="comment-22099-info" class="comment-info">
<span class="comment-age">(04 May '13, 19:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22094" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22094-form-container" class="comment-form-container">
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

<span id="22097"></span>

<div id="answer-container-22097" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22097-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-22097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The simple answer is you can't.</p>
<p>The OSM data model does not have a concept of a road merely that of abstract linear features (ways). A street which consists of several interconnected sections must perforce be represented by several ways sharing a common tag <code>name=*</code>. This has numerous advantages because there is no need to create a huge infrastructure to deal with the multitude of special cases which would arise if we tried to have a road primitive (dual carriageways, roundabouts, main highways with service roads, <a href="http://osm.org/go/euuShWgaz-">unimaginative street naming</a> and so on).</p>
<p>You could use the <a href="https://wiki.openstreetmap.org/wiki/Relation:associatedStreet">associatedStreet</a> relation to explicitly show that all these ways belong to a single named street.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '13, 17:35</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-22097" class="comments-container">
&#10;</div>
<div id="comment-tools-22097" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22097-form-container" class="comment-form-container">
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

