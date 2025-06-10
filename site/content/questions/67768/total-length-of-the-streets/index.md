+++
type = "question"
title = "total length of the streets"
description = '''I am a volunteer of the cultural public non-commercial project &quot;Тарас шевченко єднає народи&quot; (&quot;Taras Shevchenko unites the people&quot;). I was asked to calculate the total length of objects with the name &quot;Shevchenko&quot; in Ukraine. I need to write a program that:  Make a complete list of settlements in Ukr...'''
date = "2019-01-28T16:45:00Z"
lastmod = "2019-01-29T09:45:00Z"
weight = 67768
keywords = [ "maps", "javascript", "osm" ]
aliases = [ "/questions/67768" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [total length of the streets](/questions/67768/total-length-of-the-streets)

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
<span id="post-67768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67768-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am a volunteer of the cultural public non-commercial project "Тарас шевченко єднає народи" ("Taras Shevchenko unites the people"). I was asked to calculate the total length of objects with the name "Shevchenko" in Ukraine. I need to write a program that:</p>
<ol>
<li>Make a complete list of settlements in Ukraine and put them in a table.</li>
<li>In each locality will compile a list of linear objects with the name "Shevchenko" (streets, lanes, boulevards, avenues, highways, alleys) and put them in a table.</li>
<li>For each such object will find the nodes of the object and put them in a table.</li>
<li>For each such object, calculate the length of the object and add to the table.</li>
<li>Sum all the resulting lengths.</li>
</ol>
<p>I would be grateful for an explanation of how to find the necessary data in the OSM file, as well as for explaining the structure of the OSM file. I would be grateful for any help in writing up such a program. I will also be grateful for the help in finding similar programs.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maps" rel="tag" title="see questions tagged &#39;maps&#39;">maps</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '19, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/236f8899f0f89629ffbbeaf246c8d50e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anatolii%20Kharchenko&#39;s gravatar image" />
<p><span>Anatolii Kha...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anatolii Kharchenko has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67768" class="comments-container">
<span id="67770"></span>
<div id="comment-67770" class="comment">
<div id="post-67770-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<ol>
<li>is "javascript" (your tag) a requirement or just nice or unrelated?</li>
<li>Is a "OSM file" as input (in your text) a requirement or just nice or not needed?</li>
<li>Do you need do follow the 5 steps as outlined by you or would other approaches to the end result of the total length also satisfy your requirements?</li>
</ol>
</div>
<div id="comment-67770-info" class="comment-info">
<span class="comment-age">(28 Jan '19, 20:11)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67768" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67768-form-container" class="comment-form-container">
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

<span id="67774"></span>

<div id="answer-container-67774" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67774-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect the easiest way to do what you want is to actually setup a postgres/postgis database and import an <a href="http://download.geofabrik.de/europe/ukraine.html">extract of OSM data covering Ukrania</a> with <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a>.</p>
<p>Alternatively you could try to just extract the relevant data with <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">overpass api/overpass turbo</a> and sum it in a tool for example QGIS (maybe that is possible in overpass itself) see <a href="https://help.openstreetmap.org/questions/42859/find-total-length-of-ways-within-a-region-in-overpass-turbo">https://help.openstreetmap.org/questions/42859/find-total-length-of-ways-within-a-region-in-overpass-turbo</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '19, 09:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-67774" class="comments-container">
&#10;</div>
<div id="comment-tools-67774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67774-form-container" class="comment-form-container">
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

