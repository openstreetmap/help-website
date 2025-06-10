+++
type = "question"
title = "Search returning weird/unknown admin area in result (Australia)"
description = '''Hi,  I&#x27;ve found something odd with Nominatim search in Queensland Australia. If you search for &quot;Brighton, Queensland&quot; on osm.org , open.mapquest.com.au or by using this link: http://nominatim.openstreetmap.org/search?q=brighton+queensland&amp;amp;format=xml the display result is: &quot;Brighton, 4017, Cape M...'''
date = "2011-05-06T03:29:00Z"
lastmod = "2011-06-11T21:37:00Z"
weight = 5008
keywords = [ "search" ]
aliases = [ "/questions/5008" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Search returning weird/unknown admin area in result (Australia)](/questions/5008/search-returning-weirdunknown-admin-area-in-result-australia)

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
<span id="post-5008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5008-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I've found something odd with Nominatim search in Queensland Australia. If you search for "Brighton, Queensland" on <a href="http://osm.org">osm.org</a> , <a href="http://open.mapquest.com.au">open.mapquest.com.au</a> or by using this link:</p>
<p><a href="http://nominatim.openstreetmap.org/search?q=brighton+queensland&amp;format=xml">http://nominatim.openstreetmap.org/search?q=brighton+queensland&amp;format=xml</a></p>
<p>the display result is: "Brighton, 4017, Cape Moreton, Queensland, Australia"</p>
<p>Why does it have Cape Moreton in the result?</p>
<p>Brighton is part of Brisbane City Council, (the admin boundary with Moreton Bay Council is out in the Bramble Bay channel I think.)</p>
<p>Cape Moreton as a place is out on Moreton Island, so not an Admin area?</p>
<p>Geoscience Australia Gazetteer entries for Cape Moreton: <a href="http://www.ga.gov.au/bin/gazm01?placename=cape+moreton&amp;placetype=0&amp;state=QLD">http://www.ga.gov.au/bin/gazm01?placename=cape+moreton&amp;placetype=0&amp;state=QLD</a></p>
<p>Wikipedia Cape Moreton entry: <a href="http://en.wikipedia.org/wiki/Cape_Moreton">http://en.wikipedia.org/wiki/Cape_Moreton</a></p>
<p>Can anyone help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '11, 03:29</strong></p>
<img src="https://secure.gravatar.com/avatar/12ac37473087d7d6d667c276a879eec0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chas66&#39;s gravatar image" />
<p><span>chas66</span><br />
<span class="score" title="220 reputation points">220</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chas66 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5008" class="comments-container">
&#10;</div>
<div id="comment-tools-5008" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5008-form-container" class="comment-form-container">
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

<span id="5014"></span>

<div id="answer-container-5014" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5014-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This type of issue has been answered before here. Usually this is due to one of the boundaries of this administrative entities either does not exist (e.g., the place is defined by a node) or it is no longer a complete polygon. Accidental (or deliberate) deletion of this information will cause a boundary to 'spill over' into adjacent areas. Additionally some surprisingly significant areas sometimes prove never to have been added to the database.</p>
<p>Take a look at answers to the following questions: <a href="http://help.openstreetmap.org/questions/3892/nomination-reports-a-road-as-being-in-the-wrong-country">nomination-reports-a-road-as-being-in-the-wrong-country</a> <a href="http://help.openstreetmap.org/questions/4438/where-can-i-learn-about-how-nominatim-works-specifically-the-algorithm-for-listing-parent-of-objects-for-a-place-node">where-can-i-learn-about-how-nominatim-works</a>. And this forum post which was actually about the same underlying problem: <a href="http://forum.openstreetmap.org/viewtopic.php?id=11687">http://forum.openstreetmap.org/viewtopic.php?id=11687</a></p>
<p>Basically you need to check that the data for these areas is accurate and complete. There are various tools to do this. You can check the status of multipolygons using the MapQuest tool or OSM Inspector from Geofabrik. Nominatim also provides a detail browse view which will draw the polygons which it is using for a given place (e.g, <a href="http://open.mapquestapi.com/nominatim/v1/details.php?place_id=79254599">Brighton</a>).</p>
<p>Using the latter I see that Cape Moreton is tagged as place=region which Nominatim interprets as being a significant area and therefore likely to encompass a suburb. In general the place=region combination is used with too many different meanings for data consumers like Nominatim to be able to treat it consistently.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '11, 11:12</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jun '11, 14:08</strong> </span></p>
</div>
</div>
<div id="comments-container-5014" class="comments-container">
&#10;</div>
<div id="comment-tools-5014" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5014-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5687"></span>

<div id="answer-container-5687" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5687-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As SK53 says it's been asked before. here are my two related questions <a href="http://help.openstreetmap.org/questions/5198/suburbs-in-nominatim">http://help.openstreetmap.org/questions/5198/suburbs-in-nominatim</a> <a href="http://help.openstreetmap.org/questions/3919/how-can-i-find-and-modify-a-boundary">http://help.openstreetmap.org/questions/3919/how-can-i-find-and-modify-a-boundary</a> basically you need to draw a polygon to restrict the name to it's area, but, it can take a while for the polygon to take effect on/in the nominatim</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jun '11, 21:37</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-5687" class="comments-container">
&#10;</div>
<div id="comment-tools-5687" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5687-form-container" class="comment-form-container">
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

