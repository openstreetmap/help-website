+++
type = "question"
title = "How to get the street new name and old name and add the same id to each"
description = '''I need to get the street new name and old name and street name in other language and have conexion between its in form: +---------+----------------------------+------------------+ | city | street name | street_id | +---------+----------------------------+------------------+ | NewYork | new street na...'''
date = "2016-11-17T13:56:00Z"
lastmod = "2016-12-08T16:50:00Z"
weight = 53000
keywords = [ "city", "streets" ]
aliases = [ "/questions/53000" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get the street new name and old name and add the same id to each](/questions/53000/how-to-get-the-street-new-name-and-old-name-and-add-the-same-id-to-each)

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
<span id="post-53000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53000-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to get the street new name and old name and street name in other language and have conexion between its in form:</p>
<pre><code>+---------+----------------------------+------------------+
| city    | street name                |  street_id       |
+---------+----------------------------+------------------+
| NewYork | new street name            | 7                |
+---------+----------------------------+------------------+
| NewYork | old street name            | 7 (the same id)  |
+---------+----------------------------+------------------+
| NewYork | other language street name | 7 (the same id)  |
+---------+----------------------------+------------------+</code></pre>
<p>I get streets and city with</p>
<p>select * from planet_osm_line where ( planet_osm_line.highway='living_street' or planet_osm_line.highway='motorway' or planet_osm_line.highway='primary' or planet_osm_line.highway='proposed' or planet_osm_line.highway='raceway' or planet_osm_line.highway='residential' or planet_osm_line.highway='road' or planet_osm_line.highway='secondary' or planet_osm_line.highway='tertiary' or planet_osm_line.highway='track' or planet_osm_line.highway='trunk' or planet_osm_line.highway='unclassified' or planet_osm_line.route='road' or planet_osm_line.highway='service' or planet_osm_line.highway='cycleway' ) order by planet_osm_line.osm_id;</p>
<p>And whe i seach street by id i get old and new street name and name of that street in other languages!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-streets" rel="tag" title="see questions tagged &#39;streets&#39;">streets</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Nov '16, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/079706e0b620aa95bafe86daad96d6ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mik77&#39;s gravatar image" />
<p><span>Mik77</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mik77 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Nov '16, 14:19</strong> </span></p>
</div>
</div>
<div id="comments-container-53000" class="comments-container">
<span id="53001"></span>
<div id="comment-53001" class="comment">
<div id="post-53001-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What is the "new" and "old" street name in this context?</p>
</div>
<div id="comment-53001-info" class="comment-info">
<span class="comment-age">(17 Nov '16, 14:14)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="53003"></span>
<div id="comment-53003" class="comment">
<div id="post-53003-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>old name is names of street in comunist period new name of street is name that street get when USSR crash.</p>
</div>
<div id="comment-53003-info" class="comment-info">
<span class="comment-age">(17 Nov '16, 14:20)</span> <span class="comment-user userinfo">Mik77</span>
</div>
</div>
<span id="53360"></span>
<div id="comment-53360" class="comment">
<div id="post-53360-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You want to add the old name, or what do you want to do?</p>
</div>
<div id="comment-53360-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 09:59)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
<span id="53361"></span>
<div id="comment-53361" class="comment">
<div id="post-53361-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/12994/mik77">@Mik77</a> The 2nd comment means something like "Stalingrad" &amp; "Volgograd"?</p>
</div>
<div id="comment-53361-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 10:01)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
</div>
<div id="comment-tools-53000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53000-form-container" class="comment-form-container">
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

<span id="53387"></span>

<div id="answer-container-53387" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53387-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I doubt that you will find a lot of information in OSM about old street names. But OSM has 3 different fields for what you need : name, old_name, name:XX where XX is the language code. As for old_name, there is no guarantee it is the name during the period you want.</p>
<p>I am not very familiar with the database scheme, but all info about a street is stored in 1 row using hstore. In case you need 3 different rows, you will need 3 queries (one for each "name") and make the union of their results to get the table you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Dec '16, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-53387" class="comments-container">
&#10;</div>
<div id="comment-tools-53387" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53387-form-container" class="comment-form-container">
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

