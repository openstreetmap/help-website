+++
type = "question"
title = "Mapping of general traffic rules"
description = '''To what extent is it common/useful to put general traffic rules (valid in a whole country) explicitly on each way/area through tags? If the maximum allowed speed outside urbanized areas is 90km/h should it be tagged or should this be implied by the country where the road is and by some general rule ...'''
date = "2011-08-28T18:06:00Z"
lastmod = "2011-08-29T15:31:00Z"
weight = 7400
keywords = [ "access", "traffic-rules" ]
aliases = [ "/questions/7400" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Mapping of general traffic rules](/questions/7400/mapping-of-general-traffic-rules)

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
<span id="post-7400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7400-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>To what extent is it common/useful to put general traffic rules (valid in a whole country) explicitly on each way/area through tags?<br />
If the maximum allowed speed outside urbanized areas is 90km/h should it be tagged or should this be implied by the country where the road is and by some general rule (in that case where can the general rule be set?) or should it be tagged everywhere (not only exceptions).<br />
If there is a certain class of roads combined with specific traffic rules/ access restrictions, should these be copied individually everywhere (making them virtually unalterable should the traffic rules change) or saved in some centralized manner?<br />
Think of something as bridleway (which would generally be a track with specific access restrictions for pedestrians, horses, cars...) but not in UK.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-traffic-rules" rel="tag" title="see questions tagged &#39;traffic-rules&#39;">traffic-rules</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '11, 18:06</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></br></p>
</div>
</div>
<div id="comments-container-7400" class="comments-container">
<span id="7420"></span>
<div id="comment-7420" class="comment">
<div id="post-7420-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think this is far too broad an issue for the Help site.</p>
<p>There have been numerous discussions about this on various talk lists (e.g., about general tagging of speed limits): and various different opinions. Broadly I think most people are happy to leave general rules out (its too much work), but as mapping data becomes more complete may add some rules, such as speedlimits.</p>
</div>
<div id="comment-7420-info" class="comment-info">
<span class="comment-age">(29 Aug '11, 12:22)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7400-form-container" class="comment-form-container">
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

<span id="7423"></span>

<div id="answer-container-7423" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7423-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LM_1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here are some hints about general traffic rules:</p>
<p>For access restriction, we tag the exceptions. If the tag access is not present, consider the highway as 'open for the public'. But some OSM highway classes are naturally considered as 'allowed' or 'forbidden' by the contributors which means that they would certainly not add a specific tag (like the "foot=no" for a motorway or "bicycle=yes" for a cycleway). For such implied restrictions, we have <a href="http://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">a wiki page</a> providing a list of worldwide and country specific default access restrictions.</p>
<p>About speed limit, many contributors don't tag the value if it's not an exception. In some cases, the speed limit can be deduced from its class. For instance, depending on the country you are, the "highway=living_street" implies a maxspeed of 15 or 20 km/h. Also "motorway" is clear enough to tag only the exceptions. We have <a href="http://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Maxspeed">another wiki page listing implied speed limits per countries</a>. In the other hand, some maxspeeds cannot be deduced like the primary, secondary, etc because they vary from inside to outside urban zones and we don't have a clear standard to specify the urban zones boundaries (which can be a mix of several landuses, etc). To avoid any doubts, some countries like Germany started to tag systematicaly all highways speed limits and more importantly, the maxspeed source. See the <a href="http://wiki.openstreetmap.org/wiki/Maxspeed">wiki page about maxspeed and implicite/explicite tagging</a>. But this will be workable for software applications only if there is a large community of contributor tagging the whole highway network. If the tag is missing, an application could fallback into the default maxspeed values per country. Also, as mentionned on the wiki, some special maps can show the progress of such tagging effort and help the community to fill the gaps (like this <a href="http://www.itoworld.com/product/data/ito_map/main?view=5&amp;lat=52.20583764584919&amp;lon=0.11938787344072233&amp;zoom=12">ITO Map</a>).</p>
<p>More generally, there is <a href="http://wiki.openstreetmap.org/wiki/Relations/Proposed/Defaults">a proposal on the wiki</a> where all local defaults for a country could be set into a special relation type 'default' (including unit of measures, default speed limits, etc). The relation has been implemented for some countries but is not used by any software application at the moment (but the concept is there).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '11, 15:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Aug '11, 09:33</strong> </span></p>
</div>
</div>
<div id="comments-container-7423" class="comments-container">
&#10;</div>
<div id="comment-tools-7423" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7423-form-container" class="comment-form-container">
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

