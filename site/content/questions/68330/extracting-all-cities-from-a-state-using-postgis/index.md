+++
type = "question"
title = "Extracting all cities from a state using PostGIS"
description = '''I have written a PostGIS query on a database with OSM data of the state of Baden-Württemberg. SELECT * FROM public.planet_osm_polygon WHERE boundary = &#x27;administrative&#x27; AND admin_level = &#x27;8&#x27;;  So it turns out that not all cities/towns have an admin_level tag of 8. Is there any way we can further cons...'''
date = "2019-03-08T05:19:00Z"
lastmod = "2019-03-10T07:46:00Z"
weight = 68330
keywords = [ "osm", "postgresql", "postgis" ]
aliases = [ "/questions/68330" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Extracting all cities from a state using PostGIS](/questions/68330/extracting-all-cities-from-a-state-using-postgis)

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
<span id="post-68330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68330-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have written a PostGIS query on a database with OSM data of the state of Baden-Württemberg.</p>
<pre><code>SELECT * FROM public.planet_osm_polygon WHERE boundary = &#39;administrative&#39; AND admin_level = &#39;8&#39;;</code></pre>
<p>So it turns out that not all cities/towns have an admin_level tag of 8. Is there any way we can further constrain the query to filter out only the towns/cities?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '19, 05:19</strong></p>
<img src="https://secure.gravatar.com/avatar/0f1df60051a6f0ba2d7aeaac57441c49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sujay&#39;s gravatar image" />
<p><span>Sujay</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sujay has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Mar '19, 05:20</strong> </span></p>
</div>
</div>
<div id="comments-container-68330" class="comments-container">
<span id="68331"></span>
<div id="comment-68331" class="comment">
<div id="post-68331-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/314806/extracting-all-cities-from-a-state-using-postgis">https://gis.stackexchange.com/questions/314806/extracting-all-cities-from-a-state-using-postgis</a></p>
</div>
<div id="comment-68331-info" class="comment-info">
<span class="comment-age">(08 Mar '19, 08:00)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68330-form-container" class="comment-form-container">
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

<span id="68352"></span>

<div id="answer-container-68352" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68352-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sujay has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Posting your question in multiple places at once is impolite. It can lead to several people answering your question, without knowing that it has been answered already elsewhere. It means that you just think of yourself (maximizing your chance of getting an answer) and you don't care if you waste the time of others. Think about that before you do it next time!</p>
<p>The reason that not all cities in Germany have an admin_level of 8 is that there are some "kreisfreie Städte" which use admin_level 6 (and, outside of Baden-Württemberg, even two "Stadtstaaten" which use admin_level 4).</p>
<p>Finding the cities that do not have an admin_level 8 tag but instead an admin_level 6 tag could be done like this:</p>
<pre><code>SELECT a.*
FROM planet_osm_polygon a
LEFT OUTER JOIN planet_osm_polygon b
ON ST_COVERS(a.way,b.way) AND b.boundary=&#39;administrative&#39; AND b.admin_level=&#39;8&#39;
WHERE a.boundary=&#39;administrative&#39; AND a.admin_level=&#39;6&#39; AND b.osm_id IS NULL</code></pre>
<p>The "left outer join" instructs PostgreSQL to find pairs of adminlevel 6/8 entities where the adminlevel 6 entity covers the adminlevel 8 entity, and to set the adminlevel 8 entity to NULL if none is found matching this criterion. Then, we only select those adminlevel 6 entities where the adminlevel 8 part is NULL, i.e. those that have no "children" on admin_level 8.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '19, 23:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '19, 23:49</strong> </span></p>
</div>
</div>
<div id="comments-container-68352" class="comments-container">
<span id="68353"></span>
<div id="comment-68353" class="comment">
<div id="post-68353-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much for your answer Frederik! I'm sorry, I will make sure not to post it in multiple places from next time. Thanks again.</p>
</div>
<div id="comment-68353-info" class="comment-info">
<span class="comment-age">(10 Mar '19, 07:46)</span> <span class="comment-user userinfo">Sujay</span>
</div>
</div>
</div>
<div id="comment-tools-68352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68352-form-container" class="comment-form-container">
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

