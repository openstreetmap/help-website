+++
type = "question"
title = "Cannot search on address or postcode after applying osmfilter on a map."
description = '''Hi all, I am trying to downsize / shrink the map of The Netherlands by leaving only information about a single city (Laren). I have done the following: osmconvert netherlands-latest.osm.pbf -o=netherlands-latest.o5m osmfilter netherlands-latest.o5m --keep=&quot;addr:city=Laren&quot; -o=nl-Laren.o5m  The new m...'''
date = "2017-09-08T09:11:00Z"
lastmod = "2017-09-08T14:57:00Z"
weight = 59485
keywords = [ "nominatim", "osmfilter" ]
aliases = [ "/questions/59485" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot search on address or postcode after applying osmfilter on a map.](/questions/59485/cannot-search-on-address-or-postcode-after-applying-osmfilter-on-a-map)

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
<span id="post-59485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59485-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am trying to downsize / shrink the map of The Netherlands by leaving only information about a single city (Laren).</p>
<p>I have done the following:</p>
<pre><code>osmconvert netherlands-latest.osm.pbf -o=netherlands-latest.o5m
osmfilter netherlands-latest.o5m --keep=&quot;addr:city=Laren&quot; -o=nl-Laren.o5m</code></pre>
<p>The new map of Laren is imported with the nominatim setup.php script:</p>
<pre><code>./src/utils/setup.php --osm-file /app/src/nl-Laren.o5m --all</code></pre>
<p>The above one is a part of a Dockerfile that I'm using: <a href="https://github.com/mediagis/nominatim-docker">nominatim-docker</a>. The only thing I have changed in the Dockerfile is putting the new small map of Laren.</p>
<p>However, when I use the web interface or the REST api trying to search by address or postcode I get no results. It looks like not all of the tags or object relations have been preserved after I shrinked the map with osmfilter.</p>
<p>Am I missing something when applying the osmfilter? I would like to leave only nodes related to this city.</p>
<p>Thanks in advance, Peter</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Sep '17, 09:11</strong></p>
<img src="https://secure.gravatar.com/avatar/ffa27b3528b8ca8273629ac64cf9f828?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pesho318i&#39;s gravatar image" />
<p><span>pesho318i</span><br />
<span class="score" title="27 reputation points">27</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pesho318i has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '17, 09:15</strong> </span></p>
</div>
</div>
<div id="comments-container-59485" class="comments-container">
&#10;</div>
<div id="comment-tools-59485" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59485-form-container" class="comment-form-container">
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

<span id="59487"></span>

<div id="answer-container-59487" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59487-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-59487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pesho318i has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to import essentially all (well not quite) data for the area in question to allow nominatim to build its object hierarchy, in particular not just the objects with addresses but the streets in the area too.</p>
<p>With other words instead of using osmfilter you should create an extract of the city in question with a suitable tool (you will need the a bounding box or a boundary polygon for the area in question), for example with <a href="http://osmcode.org/osmium-tool/">http://osmcode.org/osmium-tool/</a> or <a href="http://wiki.openstreetmap.org/wiki/Osmosis">http://wiki.openstreetmap.org/wiki/Osmosis</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Sep '17, 10:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '17, 11:36</strong> </span></p>
</div>
</div>
<div id="comments-container-59487" class="comments-container">
<span id="59489"></span>
<div id="comment-59489" class="comment">
<div id="post-59489-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, <a href="https://help.openstreetmap.org/users/2053/simonpoole">@SimonPoole</a>!</p>
<p>Apparently I was using the wrong tool. Osmium-tool did the job! I used a bounding box instead of polygon, that was enough for me.</p>
<p>Have a great day!</p>
</div>
<div id="comment-59489-info" class="comment-info">
<span class="comment-age">(08 Sep '17, 14:57)</span> <span class="comment-user userinfo">pesho318i</span>
</div>
</div>
</div>
<div id="comment-tools-59487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59487-form-container" class="comment-form-container">
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

