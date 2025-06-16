+++
type = "question"
title = "ways with no tags and not part of a relation"
description = '''I want to find all streets in Brazil with no tags and not part of a relation, can someone help me?'''
date = "2017-01-15T13:44:00Z"
lastmod = "2017-02-13T20:14:00Z"
weight = 54051
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/54051" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ways with no tags and not part of a relation](/questions/54051/ways-with-no-tags-and-not-part-of-a-relation)

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
<span id="post-54051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54051-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to find all streets in Brazil with no tags and not part of a relation, can someone help me?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jan '17, 13:44</strong></p>
<img src="https://secure.gravatar.com/avatar/3f3544581ac9d97742160ff3261b1cad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erickdeoliveiraleal&#39;s gravatar image" />
<p><span>erickdeolive...</span><br />
<span class="score" title="66 reputation points">66</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erickdeoliveiraleal has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jan '17, 13:45</strong> </span></p>
</div>
</div>
<div id="comments-container-54051" class="comments-container">
&#10;</div>
<div id="comment-tools-54051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54051-form-container" class="comment-form-container">
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

<span id="54052"></span>

<div id="answer-container-54052" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54052-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question is rather at odds with the OSM data model, a way object with no tags is not a street, nor anything else.</p>
<p>If you actually want to find all streets that don't have tags outside of the highway tag and no relation membership, that can be likely done. If you want to find all way objects that have no tags and no relation membership, that can be done too, but is a different question.</p>
<p>Assuming you want to do it with the Overpass API, you should be able to get a result with a combination of the approaches used in</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Search_for_untagged_ways">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Search_for_untagged_ways</a></p>
<p>and</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Bus_relations.2C_which_are_not_part_of_a_master_relation">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Bus_relations.2C_which_are_not_part_of_a_master_relation</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '17, 14:50</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jan '17, 14:59</strong> </span></p>
</div>
</div>
<div id="comments-container-54052" class="comments-container">
<span id="54053"></span>
<div id="comment-54053" class="comment">
<div id="post-54053-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>but there are ways without tags and not part of relation on OSM, I found many here.</p>
</div>
<div id="comment-54053-info" class="comment-info">
<span class="comment-age">(15 Jan '17, 15:02)</span> <span class="comment-user userinfo">erickdeolive...</span>
</div>
</div>
<span id="54054"></span>
<div id="comment-54054" class="comment">
<div id="post-54054-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>this code can find some: <a href="http://overpass-turbo.eu/s/6X3">http://overpass-turbo.eu/s/6X3</a> but I think this doesnt take care of ways not in relations</p>
</div>
<div id="comment-54054-info" class="comment-info">
<span class="comment-age">(15 Jan '17, 15:05)</span> <span class="comment-user userinfo">erickdeolive...</span>
</div>
</div>
<span id="54055"></span>
<div id="comment-54055" class="comment">
<div id="post-54055-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I found this too <a href="http://tools.geofabrik.de/osmi/?view=tagging&amp;lon=-0.12399&amp;lat=51.51339&amp;zoom=12&amp;overlays=ways_without_tags">http://tools.geofabrik.de/osmi/?view=tagging&amp;lon=-0.12399&amp;lat=51.51339&amp;zoom=12&amp;overlays=ways_without_tags</a> I think I can live with this</p>
</div>
<div id="comment-54055-info" class="comment-info">
<span class="comment-age">(15 Jan '17, 15:06)</span> <span class="comment-user userinfo">erickdeolive...</span>
</div>
</div>
<span id="54057"></span>
<div id="comment-54057" class="comment">
<div id="post-54057-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I didn't say that such ways don't exist, just that they are not streets.</p>
</div>
<div id="comment-54057-info" class="comment-info">
<span class="comment-age">(15 Jan '17, 16:52)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="54625"></span>
<div id="comment-54625" class="comment">
<div id="post-54625-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>found it <a href="http://gis.stackexchange.com/questions/129691/search-for-untagged-ways-in-overpass-turbo">http://gis.stackexchange.com/questions/129691/search-for-untagged-ways-in-overpass-turbo</a></p>
<p>but looks like it consumes too much memory from server</p>
</div>
<div id="comment-54625-info" class="comment-info">
<span class="comment-age">(13 Feb '17, 20:14)</span> <span class="comment-user userinfo">erickdeolive...</span>
</div>
</div>
</div>
<div id="comment-tools-54052" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54052-form-container" class="comment-form-container">
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

