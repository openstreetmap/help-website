+++
type = "question"
title = "osm2pgsql does not add a relation into db"
description = '''I am using nominatim. I am working on a metro extract from https://mapzen.com/data/metro-extracts  During the nominatim setup process I add the {extract}.osm file. There is a osm_id= http://www.openstreetmap.org/relation/1942609 which I cannot find in the place and placex database using sql queries....'''
date = "2015-08-01T03:21:00Z"
lastmod = "2015-08-04T08:12:00Z"
weight = 44579
keywords = [ "nominatim", "osm2pgsql" ]
aliases = [ "/questions/44579" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql does not add a relation into db](/questions/44579/osm2pgsql-does-not-add-a-relation-into-db)

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
<span id="post-44579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44579-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using nominatim. I am working on a metro extract from <a href="https://mapzen.com/data/metro-extracts">https://mapzen.com/data/metro-extracts</a></p>
<p>During the nominatim setup process I add the {extract}.osm file. There is a osm_id= <a href="http://www.openstreetmap.org/relation/1942609">http://www.openstreetmap.org/relation/1942609</a> which I cannot find in the place and placex database using sql queries. How do I debug why this never got added to the database?</p>
<p>Even openstreetmap.org has problem with this relation. When you search for the exact name of the relation on the site "North West Delhi District", it goes to some other artifact.</p>
<p>When I hit nominatim with "osmid=1942609&amp;osmtype=R", it fails. A very similar relation and right next to it in the file "1942605" succeeds...</p>
<p>Fails : <a href="https://nominatim.openstreetmap.org/details.php?osmtype=R&amp;osmid=1942609">https://nominatim.openstreetmap.org/details.php?osmtype=R&amp;osmid=1942609</a></p>
<p>Succeeds : <a href="https://nominatim.openstreetmap.org/details.php?osmtype=R&amp;osmid=1942605">https://nominatim.openstreetmap.org/details.php?osmtype=R&amp;osmid=1942605</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '15, 03:21</strong></p>
<img src="https://secure.gravatar.com/avatar/e8920ebfd05463a0cdf49fc7bfc05258?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arahut_kyenetic&#39;s gravatar image" />
<p><span>arahut_kyenetic</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arahut_kyenetic has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Aug '15, 03:24</strong> </span></p>
</div>
</div>
<div id="comments-container-44579" class="comments-container">
&#10;</div>
<div id="comment-tools-44579" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44579-form-container" class="comment-form-container">
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

<span id="44590"></span>

<div id="answer-container-44590" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44590-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Likely the relation itself is simply broken. See:</p>
<p><a href="http://ra.osmsurround.org/analyzeRelation?relationId=1942609&amp;_noCache=on">http://ra.osmsurround.org/analyzeRelation?relationId=1942609&amp;_noCache=on</a></p>
<p>I would suggest editing it in JOSM and running the validator on it.</p>
<p>PS: as you can see there is a gap here : <a href="http://www.openstreetmap.org/relation/1942609#map=18/28.70812/77.16314">http://www.openstreetmap.org/relation/1942609#map=18/28.70812/77.16314</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '15, 07:38</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Aug '15, 08:13</strong> </span></p>
</div>
</div>
<div id="comments-container-44590" class="comments-container">
<span id="44600"></span>
<div id="comment-44600" class="comment">
<div id="post-44600-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Simon, Thanks! for the answer. That makes sense. As a follow up is there a way to run the import in a less strict fashion?</p>
</div>
<div id="comment-44600-info" class="comment-info">
<span class="comment-age">(04 Aug '15, 00:02)</span> <span class="comment-user userinfo">arahut_kyenetic</span>
</div>
</div>
<span id="44602"></span>
<div id="comment-44602" class="comment">
<div id="post-44602-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11313/arahut_kyenetic"></a><a href="http://help.openstreetmap.org/users/11313/arahut_kyenetic">@arahut_kyenetic</a> IMHO you have two options:</p>
<ul>
<li>fix the relation, wait till it it the planet / or in the extract you are importing and re-import</li>
<li>fix the relation and comsume diffs up to at least the point in time the relation is OK again.</li>
</ul>
<p>THe problem with "less strict" is that osm2pgsql would still have to build a valid geometry from what exsits (aka close the polygon) which is naturally technically possible but I don't believe anybody has implemented that.</p>
</div>
<div id="comment-44602-info" class="comment-info">
<span class="comment-age">(04 Aug '15, 08:12)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44590-form-container" class="comment-form-container">
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

