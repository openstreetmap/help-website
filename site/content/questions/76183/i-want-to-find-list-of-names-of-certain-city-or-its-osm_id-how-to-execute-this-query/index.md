+++
type = "question"
title = "I want to find list of names of certain city or its OSM_ID - how to execute this query?"
description = '''I want to find the old name of the city. So, using Nominatim API I just execute  https://nominatim.openstreetmap.org/search?#?city=Kyiv&amp;amp;state=Kyiv&amp;amp;country=Ukraine&amp;amp;format=json&amp;amp;namedetails=1 And have a list of city&#x27;s names. But I can&#x27;t figure out how to execute this query from the data...'''
date = "2020-08-18T14:30:00Z"
lastmod = "2020-08-20T08:23:00Z"
weight = 76183
keywords = [ "osm_id", "query", "nominatim", "osm", "database" ]
aliases = [ "/questions/76183" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I want to find list of names of certain city or its OSM_ID - how to execute this query?](/questions/76183/i-want-to-find-list-of-names-of-certain-city-or-its-osm_id-how-to-execute-this-query)

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
<span id="post-76183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76183-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to find the old name of the city. So, using Nominatim API I just execute <a href="https://nominatim.openstreetmap.org/search?#?city=Kyiv&amp;state=Kyiv&amp;country=Ukraine&amp;format=json&amp;namedetails=1">https://nominatim.openstreetmap.org/search?#?city=Kyiv&amp;state=Kyiv&amp;country=Ukraine&amp;format=json&amp;namedetails=1</a></p>
<p>And have a list of city's names.</p>
<p>But I can't figure out how to execute this query from the database.</p>
<p>I can write something like: SELECT name FROM placex WHERE OSM_ID='XXXXX'</p>
<p>But to do it I need to know the OSM_id of the city.</p>
<p>So, my question is How to find old names (or at least osm_id) of the city if I have city_name, state and country?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm_id" rel="tag" title="see questions tagged &#39;osm_id&#39;">osm_id</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '20, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/15f1f94010a3f646d648f1ed2e60e16e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MariiaZav&#39;s gravatar image" />
<p><span>MariiaZav</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MariiaZav has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76183" class="comments-container">
&#10;</div>
<div id="comment-tools-76183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76183-form-container" class="comment-form-container">
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

<span id="76197"></span>

<div id="answer-container-76197" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76197-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Searching for city use the API documented in <a href="https://nominatim.org/release-docs/latest/api/Search/">https://nominatim.org/release-docs/latest/api/Search/</a></p>
<p>saint petersburg, russia</p>
<p><a href="https://nominatim.openstreetmap.org/search.php?q=saint%20petersburg%2C%20russia&amp;format=jsonv2">https://nominatim.openstreetmap.org/search.php?q=saint%20petersburg%2C%20russia&amp;format=jsonv2</a></p>
<p>or structured, though many big cities are also states which makes it harder for a computer to differentiate</p>
<p><a href="https://nominatim.openstreetmap.org/search.php?city=saint%20petersburg&amp;country=russia&amp;format=jsonv2">https://nominatim.openstreetmap.org/search.php?city=saint%20petersburg&amp;country=russia&amp;format=jsonv2</a></p>
<p>If you have your own server replace the domain the IP address of your server or 'localhost'.</p>
<p>Alternatively in your installation in the 'build' directory there's a script <code>utils/query.php</code>.</p>
<p>Add <code>&amp;namedetails=1</code> and you get a list of all names. <a href="https://nominatim.openstreetmap.org/search.php?q=saint%20petersburg%2C%20russia&amp;format=jsonv2&amp;namedetails=1&amp;pretty=1">https://nominatim.openstreetmap.org/search.php?q=saint%20petersburg%2C%20russia&amp;format=jsonv2&amp;namedetails=1&amp;pretty=1</a></p>
<p><code>"name:tzl": "Sant Pairbuerg", "short_name": "СПб", "alt_name:mk": "Петроград", "alt_name:pl": "Sankt Petersburg", "alt_name:vi": "Sankt-Peterburg", "old_name:ar": "لينينغراد;بيتروغراد", "old_name:ca": "Petrograd;Leningrad",</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '20, 23:07</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-76197" class="comments-container">
<span id="76220"></span>
<div id="comment-76220" class="comment">
<div id="post-76220-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. I have no problem to execute query from Nominatim API. The main problem is to run this query from the database. It has 784 tables and no descriptions of it.</p>
<p>I can't figure out how to get osm_id of the city without using Nominatim API and just using database.</p>
</div>
<div id="comment-76220-info" class="comment-info">
<span class="comment-age">(19 Aug '20, 19:01)</span> <span class="comment-user userinfo">MariiaZav</span>
</div>
</div>
<span id="76221"></span>
<div id="comment-76221" class="comment">
<div id="post-76221-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Adding &amp;debug=1 to the URL <a href="https://nominatim.openstreetmap.org/search.php?city=saint%20petersburg&amp;country=russia&amp;format=jsonv2&amp;debug=1">https://nominatim.openstreetmap.org/search.php?city=saint%20petersburg&amp;country=russia&amp;format=jsonv2&amp;debug=1</a> gives some output of the SQL that is run. In the background Nominatim uses several thousand lines of code to create and manage the SQL, finding places in a world-wide database is complex, especially finding the most relevant/important city when many have the same name. There's no single or few SQL queries one can run manually to get the same result.</p>
</div>
<div id="comment-76221-info" class="comment-info">
<span class="comment-age">(19 Aug '20, 20:49)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="76231"></span>
<div id="comment-76231" class="comment">
<div id="post-76231-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much! I didn't know about the debug mode. It helps me a lot!</p>
</div>
<div id="comment-76231-info" class="comment-info">
<span class="comment-age">(20 Aug '20, 08:23)</span> <span class="comment-user userinfo">MariiaZav</span>
</div>
</div>
</div>
<div id="comment-tools-76197" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76197-form-container" class="comment-form-container">
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

