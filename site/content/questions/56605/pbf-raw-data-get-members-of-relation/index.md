+++
type = "question"
title = "PBF raw data: Get members of relation"
description = '''Hi everyone! I&#x27;m trying to get the members (nodes) of a relation as a list. I&#x27;m using FME to read the PBF, which is basically using &quot;drv_osm&quot; from GDAL. I tried all options from the config file (osmconf_.ini) and FME itself (offers rarely any) but could not get the members. Instead, I just receive m...'''
date = "2017-06-13T16:36:00Z"
lastmod = "2017-06-15T20:42:00Z"
weight = 56605
keywords = [ "fme", "pbf", "relation", "osm_drv", "gdal" ]
aliases = [ "/questions/56605" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PBF raw data: Get members of relation](/questions/56605/pbf-raw-data-get-members-of-relation)

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
<span id="post-56605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56605-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone!</p>
<p>I'm trying to get the members (nodes) of a relation as a list. I'm using FME to read the PBF, which is basically using "drv_osm" from GDAL. I tried all options from the config file (osmconf_.ini) and FME itself (offers rarely any) but could not get the members. Instead, I just receive multilines consisting of all the ways/nodes of the relation.</p>
<p>When I use Overpass Turbo and the following query, I get the desired list of members:</p>
<p>relation(6794709); out;</p>
<p><img src="https://help.openstreetmap.org/upfiles/osm_overpassTurbo_queryRelation_zv4apu5.png" alt="alt text" /></p>
<p>Is it possible to get this Information from the PDF raw data file somehow?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-fme" rel="tag" title="see questions tagged &#39;fme&#39;">fme</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-osm_drv" rel="tag" title="see questions tagged &#39;osm_drv&#39;">osm_drv</span> <span class="post-tag tag-link-gdal" rel="tag" title="see questions tagged &#39;gdal&#39;">gdal</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '17, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/e4a051b3f251672ff56bf53262a34976?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Egaru&#39;s gravatar image" />
<p><span>Egaru</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Egaru has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-56605" class="comments-container">
<span id="56607"></span>
<div id="comment-56607" class="comment">
<div id="post-56607-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The GDAL driver makes osm data fit into a typical GDAL use case. The solution is to access the data using a library that does not attempt to abstract away the OSM data model. <a href="http://wiki.openstreetmap.org/wiki/PBF_Format">http://wiki.openstreetmap.org/wiki/PBF_Format</a> has some leads for libraries.</p>
</div>
<div id="comment-56607-info" class="comment-info">
<span class="comment-age">(13 Jun '17, 18:23)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-56605" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56605-form-container" class="comment-form-container">
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

<span id="56608"></span>

<div id="answer-container-56608" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56608-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56608-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56608-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect that you would be best served by using <a href="http://wiki.openstreetmap.org/wiki/Osmium">osmium</a> in one of it incarnations/bindings.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '17, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-56608" class="comments-container">
<span id="56636"></span>
<div id="comment-56636" class="comment">
<div id="post-56636-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, ok. So the gdal driver (which is used in FME I want to use) offers no possibility to get the members list. I'll give osmium a try, thanks!</p>
</div>
<div id="comment-56636-info" class="comment-info">
<span class="comment-age">(15 Jun '17, 20:42)</span> <span class="comment-user userinfo">Egaru</span>
</div>
</div>
</div>
<div id="comment-tools-56608" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56608-form-container" class="comment-form-container">
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

