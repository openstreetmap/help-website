+++
type = "question"
title = "Does planet.osm contain a list of metro stations worldwide?"
description = '''What tables contain this data?'''
date = "2012-04-03T22:48:00Z"
lastmod = "2012-04-04T10:59:00Z"
weight = 11713
keywords = [ "planet_osm" ]
aliases = [ "/questions/11713" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Does planet.osm contain a list of metro stations worldwide?](/questions/11713/does-planetosm-contain-a-list-of-metro-stations-worldwide)

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
<span id="post-11713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11713-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What tables contain this data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Apr '12, 22:48</strong></p>
<img src="https://secure.gravatar.com/avatar/1810c63b5d062335e7ca06237dddb0a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Justin%20Tanner&#39;s gravatar image" />
<p><span>Justin Tanner</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Justin Tanner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11713" class="comments-container">
&#10;</div>
<div id="comment-tools-11713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11713-form-container" class="comment-form-container">
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

<span id="11714"></span>

<div id="answer-container-11714" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11714-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>planet.osm does contain the whole osm-database which means that also the metro stations are included. However, the metro stations - nor any other particular feature - are not stored in a particular table.</p>
<p>In order to obtain such a list, you need to know how metro stations are tagged and then extract the accordingly tagged objects from the database. You may do so by downloading the planet.osm and using e.g. <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> to filter out the metro stations. Another and possibly easier way might be to use the <a href="http://www.overpass-api.de/">overpass-api</a> to querry the database.</p>
<p>Most metro stations are possibly tagged as railway=station or railway=subway_entrance (only the entrance) or as public_transport=stop_area or public_transport=station. For most of those taggings you will get the metro station AND other public transport stations, so you will have to evaluate the context, e.g. only those on/near railway=subway. And keep in mind that you want to query nodes, ways and relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '12, 00:16</strong></p>
<img src="https://secure.gravatar.com/avatar/d732dd313768bd27c4ecc89ab4898c69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FischersFritz&#39;s gravatar image" />
<p><span>FischersFritz</span><br />
<span class="score" title="191 reputation points">191</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FischersFritz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11714" class="comments-container">
&#10;</div>
<div id="comment-tools-11714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11714-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11719"></span>

<div id="answer-container-11719" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11719-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11719-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11719-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can have a look at the <a href="http://wiki.openstreetmap.org/wiki/Map_Features">MapFeatures page</a> in the OpenStreetMap wiki and search through the page to find what your're looking for. If Metro is something underground for you the tags mentioned by FischersFritz are probably the ones you're looking for. There's also railway=tram_stop ...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '12, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/30b87850d86c99d1c4f1f72c9abaeb52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frabron&#39;s gravatar image" />
<p><span>frabron</span><br />
<span class="score" title="361 reputation points">361</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frabron has 2 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-11719" class="comments-container">
&#10;</div>
<div id="comment-tools-11719" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11719-form-container" class="comment-form-container">
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

