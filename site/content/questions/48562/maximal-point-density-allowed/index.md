+++
type = "question"
title = "Maximal point density allowed"
description = '''Is there a maximal point density that is allowed in the OSM database? I mean whether there is a rule that would say that the distance between two points that belong the same object (road, building, road lane marking etc.) can not be smaller than a given value (like 1, 10, 100 cm etc.)? The reason I ...'''
date = "2016-03-08T10:18:00Z"
lastmod = "2016-03-08T10:25:00Z"
weight = 48562
keywords = [ "point", "rule", "rtk", "density" ]
aliases = [ "/questions/48562" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Maximal point density allowed](/questions/48562/maximal-point-density-allowed)

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
<span id="post-48562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48562-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a maximal point density that is allowed in the OSM database? I mean whether there is a rule that would say that the distance between two points that belong the same object (road, building, road lane marking etc.) can not be smaller than a given value (like 1, 10, 100 cm etc.)?</p>
<p>The reason I am asking is because I am looking for a place where I could donate a precise geodata obtained with RTK precise positioning. My data would mainly deal with the main road marking types like solid-lane-divider and solid-road-edge that fall under the <a href="http://wiki.openstreetmap.org/wiki/Key:road_marking">road_marking key</a>.</p>
<p>My goal is for the data to be as precise as possible, but the final density would still be open for discussion. For instance, it probably would make sense for the road lanes point density to vary as needed by the lane shape (more dense in curves) maybe resulting in an average density of some 25 cm.</p>
<p>Has the OSM community ever dealt with precise geospatial data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-point" rel="tag" title="see questions tagged &#39;point&#39;">point</span> <span class="post-tag tag-link-rule" rel="tag" title="see questions tagged &#39;rule&#39;">rule</span> <span class="post-tag tag-link-rtk" rel="tag" title="see questions tagged &#39;rtk&#39;">rtk</span> <span class="post-tag tag-link-density" rel="tag" title="see questions tagged &#39;density&#39;">density</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '16, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-48562" class="comments-container">
&#10;</div>
<div id="comment-tools-48562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48562-form-container" class="comment-form-container">
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

<span id="48563"></span>

<div id="answer-container-48563" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48563-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-48563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, we have delt with precise geospatial data, and NO, road markings are defintely not something you should be using it for (essentially one user invented the key you referred to without any discussion with anybody). While there are numerous features and use cases where micro-mapping might result in useful information at this point in time, the non-abstracted, exact position of road markings is not one.</p>
<p>If you want to do something helpful, please add <a href="http://wiki.openstreetmap.org/wiki/Lanes">lane tagging</a> (from which road marking can be derived if necessary).</p>
<p>PS: see <a href="http://wiki.openstreetmap.org/wiki/Proposed_features/Street_area">http://wiki.openstreetmap.org/wiki/Proposed_features/Street_area</a> for useful detailed mapping of shoulder areas and similar.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '16, 10:25</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Mar '16, 11:09</strong> </span></p>
</div>
</div>
<div id="comments-container-48563" class="comments-container">
&#10;</div>
<div id="comment-tools-48563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48563-form-container" class="comment-form-container">
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

