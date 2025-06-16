+++
type = "question"
title = "English queries to OSM"
description = '''I&#x27;m building a system that tries to answer geospatial English questions such as &quot;Where is the closest restaurant&quot; or &quot;How many historic sites are in the east of Nantes?&quot;. The questions are then mapped to Overpass queries. To improve my system I need more English questions. Does anyone know of any pl...'''
date = "2016-12-07T07:31:00Z"
lastmod = "2016-12-12T09:53:00Z"
weight = 53276
keywords = [ "overpass", "english", "query" ]
aliases = [ "/questions/53276" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [English queries to OSM](/questions/53276/english-queries-to-osm)

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
<span id="post-53276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53276-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm building a system that tries to answer geospatial English questions such as "Where is the closest restaurant" or "How many historic sites are in the east of Nantes?". The questions are then mapped to Overpass queries. To improve my system I need more English questions. Does anyone know of any place/logs etc. where I might find such a collection of questions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-english" rel="tag" title="see questions tagged &#39;english&#39;">english</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Dec '16, 07:31</strong></p>
<img src="https://secure.gravatar.com/avatar/51165550639b7a05ef10e3854169b4e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carence&#39;s gravatar image" />
<p><span>carence</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carence has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53276" class="comments-container">
<span id="53313"></span>
<div id="comment-53313" class="comment">
<div id="post-53313-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was just about to ask if you already know about <a href="http://nlmaps.cl.uni-heidelberg.de/">http://nlmaps.cl.uni-heidelberg.de/</a> But of course you are since that's your thing :-D</p>
</div>
<div id="comment-53313-info" class="comment-info">
<span class="comment-age">(07 Dec '16, 19:46)</span> <span class="comment-user userinfo">tyr_asd</span>
</div>
</div>
<span id="53426"></span>
<div id="comment-53426" class="comment">
<div id="post-53426-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, that's my current working model. It's great that it can get some really complex questions right but fails on other, more simpler ones such as "Where can I go canoeing close to here" because it's never seen the word "canoeing" before. That's why I'm looking for more data that maps English word to OSM structures.</p>
</div>
<div id="comment-53426-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 07:20)</span> <span class="comment-user userinfo">carence</span>
</div>
</div>
</div>
<div id="comment-tools-53276" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53276-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="53285"></span>

<div id="answer-container-53285" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53285-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-53285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/EN">list of special phrases for Nominatim</a> could help to automatically construct such queries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '16, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-53285" class="comments-container">
<span id="53286"></span>
<div id="comment-53286" class="comment">
<div id="post-53286-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that's a great list!</p>
</div>
<div id="comment-53286-info" class="comment-info">
<span class="comment-age">(07 Dec '16, 09:32)</span> <span class="comment-user userinfo">carence</span>
</div>
</div>
<span id="53501"></span>
<div id="comment-53501" class="comment">
<div id="post-53501-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's probably worth mentioning that this list is in parts a bit outdated in that it includes some tags that are not used anymore in OSM (e.g. landuse=mine instead of landuse=quarry), see <a href="https://github.com/twain47/Nominatim/issues/103">https://github.com/twain47/Nominatim/issues/103</a></p>
</div>
<div id="comment-53501-info" class="comment-info">
<span class="comment-age">(12 Dec '16, 09:25)</span> <span class="comment-user userinfo">tyr_asd</span>
</div>
</div>
</div>
<div id="comment-tools-53285" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53285-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53496"></span>

<div id="answer-container-53496" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53496-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As <a href="https://help.openstreetmap.org/users/158/scai">@scai</a> suggested <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/EN">the list of special phrases for Nomination</a> is the correct way.</p>
<p>If still you are not able to execute then here is my suggestion. It'll be a good project <em>the list of simple questions with overpass API syntax</em> that are useful for many who want to use OSM but are unable to comprehend the complexities OSM overpass query language.</p>
<p>You can start a project on github and make a list of questions then OSM community certainly will help you to convert those queries to overpass API. Just post the github project link here once you are ready.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '16, 05:02</strong></p>
<img src="https://secure.gravatar.com/avatar/39d75f04e1a21ba653b41ac75ec1b026?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gagan&#39;s gravatar image" />
<p><span>Gagan</span><br />
<span class="score" title="305 reputation points">305</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gagan has 2 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-53496" class="comments-container">
&#10;</div>
<div id="comment-tools-53496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53496-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53502"></span>

<div id="answer-container-53502" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53502-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you're just looking for terms that translate to OSM objects (tags), you have more potential data sources:</p>
<ul>
<li>There are <strong>presets</strong> lists of OSM editors, for example here's the list maintained by the <a href="https://raw.githubusercontent.com/openstreetmap/iD/master/data/presets/presets.json">iD project</a>.</li>
<li>Another approach would be to to look at the the contents from the <strong>OSM wiki</strong> (e.g. the map features page), which can be used by using the extracts provided by the taginfo project (see <a href="http://taginfo.openstreetmap.org/download/taginfo-wiki.db.bz2">downloads</a> page).</li>
<li>Finally, you can even look at <strong>wikidata</strong> entries that have a <a href="https://www.wikidata.org/wiki/Property:P1282">OpenStreetMap tag or key</a> associated with <a href="http://tinyurl.com/jzmg8um">them</a>.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '16, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-53502" class="comments-container">
&#10;</div>
<div id="comment-tools-53502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53502-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53278"></span>

<div id="answer-container-53278" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53278-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53278-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53278-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, these questions are infinite in number. No one bothers to store them. I think.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '16, 07:34</strong></p>
<img src="https://secure.gravatar.com/avatar/100f8ccde5e9799707a5056f94fe183f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wetitpig0&#39;s gravatar image" />
<p><span>Wetitpig0</span><br />
<span class="score" title="307 reputation points">307</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wetitpig0 has 2 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-53278" class="comments-container">
&#10;</div>
<div id="comment-tools-53278" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53278-form-container" class="comment-form-container">
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

