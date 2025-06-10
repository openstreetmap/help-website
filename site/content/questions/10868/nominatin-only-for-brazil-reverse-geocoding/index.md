+++
type = "question"
title = "Nominatin only for brazil reverse geocoding"
description = '''Hi. here i am with one more question. I like to install nominatin on my server, but i only need this reverse geocode for Brazil. So i download what i think was a part of database, but when i try to compile that a several errors appear for missing tables... I download this file thinking that was a pa...'''
date = "2012-02-28T19:57:00Z"
lastmod = "2012-02-29T15:51:00Z"
weight = 10868
keywords = [ "brazim", "nominatim" ]
aliases = [ "/questions/10868" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatin only for brazil reverse geocoding](/questions/10868/nominatin-only-for-brazil-reverse-geocoding)

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
<span id="post-10868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10868-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. here i am with one more question.</p>
<p>I like to install nominatin on my server, but i only need this reverse geocode for Brazil.</p>
<p>So i download what i think was a part of database, but when i try to compile that a several errors appear for missing tables...</p>
<p>I download this file thinking that was a part of the entire planet database... but those errors appear:</p>
<blockquote>
<p>postgres@webgiz:/root$ osm2pgsql -lsc -O gazetteer -C 2000 -d gazetteer brazil.osm.bz2 osm2pgsql SVN version 0.69-</p>
<p>Using projection SRS 4326 (Latlong) NOTICE: table "place" does not exist, skipping NOTICE: type "keyvalue" does not exist, skipping NOTICE: type "wordscore" does not exist, skipping NOTICE: type "stringlanguagetype" does not exist, skipping NOTICE: type "keyvaluetype" does not exist, skipping NOTICE: function get_connected_ways(pg_catalog.int4[]) does not exist, skipping SELECT AddGeometryColumn('place', 'geometry', 4326, 'GEOMETRY', 2) failed: ERROR: function addgeometrycolumn(unknown, unknown, integer, unknown, integer) does not exist LINE 1: SELECT AddGeometryColumn('place', 'geometry', 4326, 'GEOMETR... ^ HINT: No function matches the given name and argument types. You might need to add explicit type casts.</p>
<p>Error occurred, cleaning up</p>
</blockquote>
<p>The link when i download this file is this: <a href="http://downloads.cloudmade.com/americas/south_america/brazil#downloads_breadcrumbs">http://downloads.cloudmade.com/americas/south_america/brazil#downloads_breadcrumbs</a></p>
<p>So i have two questions: 1)Can i use nominatin with just a Brazil DataBase? 2)When exactly i can download this file?</p>
<p>Can you help me?</p>
<p>Thanks for all attentions!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-brazim" rel="tag" title="see questions tagged &#39;brazim&#39;">brazim</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '12, 19:57</strong></p>
<img src="https://secure.gravatar.com/avatar/dfed8e249ec19c2a8d6319eba52a3a6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rspilki&#39;s gravatar image" />
<p><span>rspilki</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rspilki has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '14, 14:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-10868" class="comments-container">
&#10;</div>
<div id="comment-tools-10868" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10868-form-container" class="comment-form-container">
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

<span id="10887"></span>

<div id="answer-container-10887" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10887-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ignore the <a href="http://trac.openstreetmap.org/ticket/4216">confusing skipping warnings</a>. The actual error you need to pay attention to is</p>
<p><code>function addgeometrycolumn .... does not exist</code></p>
<p>Which means you are trying to run osm2pgsql on a plain postgres database rather than one which has been PostGIS enabled. See <a href="http://postgis.refractions.net/docs/ch02.html">PostGIS installation instructions</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Feb '12, 15:51</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-10887" class="comments-container">
&#10;</div>
<div id="comment-tools-10887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10887-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10880"></span>

<div id="answer-container-10880" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10880-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I do not know much about osm2pgsql but I can tell you that it has nothing to do with loading a brazil extract instead of the full planet. Looks more like a database setup step that need to happen before the data import step has not been done. Recheck the installation instructions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Feb '12, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-10880" class="comments-container">
&#10;</div>
<div id="comment-tools-10880" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10880-form-container" class="comment-form-container">
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

