+++
type = "question"
title = "Trying to extract countries boundaries from geofabrik extracts, getting different results, missing boundaries"
description = '''Hi, I&#x27;m trying to build a dataset with only countries boundaries out of a selected number of countries, I need all administrative levels, I have been able to find useful answers and wiki pages that have proved to be useful to create a pipeline with osmfilter and osm2pgsql. My pipeline (any suggestio...'''
date = "2017-07-25T22:30:00Z"
lastmod = "2017-07-31T12:10:00Z"
weight = 57275
keywords = [ "boundaries", "admin_level", "osmfilter", "osm2pgsql", "countries" ]
aliases = [ "/questions/57275" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Trying to extract countries boundaries from geofabrik extracts, getting different results, missing boundaries](/questions/57275/trying-to-extract-countries-boundaries-from-geofabrik-extracts-getting-different-results-missing-boundaries)

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
<span id="post-57275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57275-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm trying to build a dataset with only countries boundaries out of a selected number of countries, I need all administrative levels, I have been able to find useful answers and wiki pages that have proved to be useful to create a pipeline with osmfilter and osm2pgsql. My pipeline (any suggestion is welcome if something I'm saying is wrong) is set to filter out unwanted informations from osm files with osmfilter and then importing the files in PostgreSQL with osm2pgsql, then, I can view data with QGIS by importing layers from planet_osm_polygon tables.</p>
<p>I got issues with country borders, for example Canada and Mexico: It is my understanding that Canada and Mexico are presents in geofabrik extracts of North America (north-america-latest.osm.pbf), Canada also has it's own file canada-latest.osm.pbf that should be a subset of North America. I filter with: osmfilter in.o5m --keep-relations="boundary=administrative" --keep-nodes= --keep-ways= -o=out.osm Then add data to database: osm2pgsql -s -C 1500 -d dbdest -U osm_importer out.osm</p>
<p>Examining the data with QGIS seems that North America with an admin_level level 2 filter shows Canada border along with US but not Mexico that should be there too; Canada only data, instead, at level 2 shows nothing but Graham and Moresby Island (Pacific) and St-Pierre and Sabre Island (Atlantic)</p>
<p>I hope I don't need to do a full OSM / planet import to address this issue.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-admin_level" rel="tag" title="see questions tagged &#39;admin_level&#39;">admin_level</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-countries" rel="tag" title="see questions tagged &#39;countries&#39;">countries</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jul '17, 22:30</strong></p>
<img src="https://secure.gravatar.com/avatar/6bfcfd2dfbb00ebb62d980a63796120f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nicolape&#39;s gravatar image" />
<p><span>nicolape</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nicolape has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57275" class="comments-container">
&#10;</div>
<div id="comment-tools-57275" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57275-form-container" class="comment-form-container">
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

<span id="57276"></span>

<div id="answer-container-57276" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57276-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nicolape has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Why don't you simply use <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a> which was just a google away? (yes I'm aware that this is not really an answer to the question)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '17, 23:10</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jul '17, 23:20</strong> </span></p>
</div>
</div>
<div id="comments-container-57276" class="comments-container">
<span id="57281"></span>
<div id="comment-57281" class="comment">
<div id="post-57281-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you for your answer, I have stumbled upon that website in my journey to the boundaries :) , I'm willing to considered your solution as a fallback in case I'll be not able to "manually" filter data by myself.</p>
</div>
<div id="comment-57281-info" class="comment-info">
<span class="comment-age">(26 Jul '17, 09:31)</span> <span class="comment-user userinfo">nicolape</span>
</div>
</div>
<span id="57283"></span>
<div id="comment-57283" class="comment">
<div id="post-57283-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In any case I can see just a bit too much that could go wrong in your processing workflow, why not simply change the "default.style" so that you only import boundaries and avoid the osmfilter step?</p>
</div>
<div id="comment-57283-info" class="comment-info">
<span class="comment-age">(26 Jul '17, 10:13)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="57306"></span>
<div id="comment-57306" class="comment">
<div id="post-57306-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you again, I have changed the pipeline, now I use osm2pgsql on the country pbf file from geofabrik, I use a style file with: node,way admin_level text linear node,way boundary text linear node,way name text linear</p>
<p>Unfortunately I'm still getting partial/incomplete boundaries, for example Mexico at level 2 is missing completely the land border, it has only islands, in level 4 is missing Sonora (1673426) in land, still getting his islands. I was thinking it could be related to the US border, since in the extract is supposed to be only Mexico, but unfortunately others mexican states next to US border as Cihuahua (1673425) are correctly displayed.</p>
</div>
<div id="comment-57306-info" class="comment-info">
<span class="comment-age">(27 Jul '17, 11:27)</span> <span class="comment-user userinfo">nicolape</span>
</div>
</div>
<span id="57310"></span>
<div id="comment-57310" class="comment not_top_scorer">
<div id="post-57310-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are not by any chance importing the extracts one by one? If yes I'm surprised that it works at all. You should be pre-merging the extracts before import.</p>
</div>
<div id="comment-57310-info" class="comment-info">
<span class="comment-age">(27 Jul '17, 13:36)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="57365"></span>
<div id="comment-57365" class="comment">
<div id="post-57365-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Since you showed me the flaws in my process I moved to wambacher as you suggested in the first place, thanks to the help of Walter, he's very kind and patient, I was able to generate the boundaries for my countries.</p>
</div>
<div id="comment-57365-info" class="comment-info">
<span class="comment-age">(31 Jul '17, 10:52)</span> <span class="comment-user userinfo">nicolape</span>
</div>
</div>
<span id="57370"></span>
<div id="comment-57370" class="comment">
<div id="post-57370-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you mind explaining the problems you ran into? Ideally right here in a separate answer so that other people can profit from your experience.</p>
</div>
<div id="comment-57370-info" class="comment-info">
<span class="comment-age">(31 Jul '17, 12:10)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57276" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-57276-form-container" class="comment-form-container">
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

