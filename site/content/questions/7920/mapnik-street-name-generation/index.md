+++
type = "question"
title = "Mapnik Street Name Generation"
description = '''Hi all, I need generate tiles for my country(Armenia) and all names comes out in native Armenian language. Is there a way to translit it to English? I want to make offline map app for foreigners and thus need latin char names in map.... Can you hint how to setup the osm.xml or other config file to g...'''
date = "2011-09-16T09:10:00Z"
lastmod = "2018-10-05T23:19:00Z"
weight = 7920
keywords = [ "generate_tiles", "mapnik" ]
aliases = [ "/questions/7920" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Mapnik Street Name Generation](/questions/7920/mapnik-street-name-generation)

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
<span id="post-7920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7920-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I need generate tiles for my country(Armenia) and all names comes out in native Armenian language. Is there a way to translit it to English? I want to make offline map app for foreigners and thus need latin char names in map.... Can you hint how to setup the osm.xml or other config file to get all street names in english</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '11, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/d5392fe7a68088f8c8e3bdc43a16f156?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gevork&#39;s gravatar image" />
<p><span>Gevork</span><br />
<span class="score" title="234 reputation points">234</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gevork has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7920" class="comments-container">
&#10;</div>
<div id="comment-tools-7920" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7920-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="7922"></span>

<div id="answer-container-7922" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7922-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-7922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gevork has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not familiar with the Armenian language and whether or not there is a potential automatic transliteration into English. If there is, then that transliteration could be implemented as a PostgreSQL stored procedure, and in the Mapnik style file you could then write</p>
<pre><code>select my_transliteration_procedure(name), ... other fields ...</code></pre>
<p>wherever it now says</p>
<pre><code>select name, ... other fields ...</code></pre>
<p>If, on the other hand, you are not looking for an automatic transliteration but only want the English names displayed where they have been explicitly entered as <code>name:en</code> tags in OpenStreetMap, then you need to modify the osm2pgsql style file (usually called <code>default.style</code>) and add a column for the name:en tag so that it ends up in your database; and after that you can modify the Mapnik style file to use something like</p>
<pre><code>select case when &quot;name:en&quot; is not null then &quot;name:en&quot; else &quot;name&quot;, ... other fields ...</code></pre>
<p>Of course if all you want is a one-off set of tiles then you can also leave the Mapnik style unchanged and run something like</p>
<pre><code>update planet_osm_xxx set name=&quot;name:en&quot; where &quot;name:en&quot; is not null;</code></pre>
<p>on the tables generated by osm2pgsql.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '11, 09:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-7922" class="comments-container">
<span id="7925"></span>
<div id="comment-7925" class="comment">
<div id="post-7925-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Frederik Ramm</span> you are my star :)))) Thanks a lot</p>
</div>
<div id="comment-7925-info" class="comment-info">
<span class="comment-age">(16 Sep '11, 10:06)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
<span id="7926"></span>
<div id="comment-7926" class="comment">
<div id="post-7926-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Be carefull when transliterating (and translating words like "street"). You probably want to do a manual check of the result before contributing the "name:en" tag to the main OSM db. At least working inside postgres might be handyer than working via the api, depending on what you're used to.</p>
<p>Once you have the tag in the db of course, just change the mapnik style and you're good to go.</p>
</div>
<div id="comment-7926-info" class="comment-info">
<span class="comment-age">(16 Sep '11, 10:54)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="8137"></span>
<div id="comment-8137" class="comment">
<div id="post-8137-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@vincent de phily</span> <span></span><span>@Frederik Ramm</span> I have managed to change default.style and now name:en is going to db. BUT! I couldn't find Mapnik style file and didn't fully understood how exactly change it... Could you help out???</p>
</div>
<div id="comment-8137-info" class="comment-info">
<span class="comment-age">(25 Sep '11, 17:26)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
<span id="66183"></span>
<div id="comment-66183" class="comment">
<div id="post-66183-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/104/frederik-ramm"></a><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik Ramm</a> I was able to get English names to come up for high zoom level objects like roads and buildings using your steps above but it seems like city and country names are using their native alphabet still. Do you have any idea on what might be the issue?</p>
<p>I am using Thailand as a test. I thought perhaps the country and city objects didn't have a "name:en" tag, however it seemed unlikely to me that streets in Bangkok, Thailand would have english names added, but the country and city itself would not.</p>
<p>For updating the tables, I listed all tables in my postgis database and then ran your update command for all tables that matched the pattern planet_osm_xxx.</p>
<p>Thanks in advance for any help.</p>
</div>
<div id="comment-66183-info" class="comment-info">
<span class="comment-age">(05 Oct '18, 20:22)</span> <span class="comment-user userinfo">coderunner</span>
</div>
</div>
<span id="66187"></span>
<div id="comment-66187" class="comment">
<div id="post-66187-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is it possible that you simply have the low-zoom tiles cached, so that you are still seeing tiles from before you made the style change? You could clear your cache with something like <code>rm -rf /var/lib/mod_tile/*</code> or you could use the /dirty suffix on a tile.png request to have that tile re-rendered.</p>
</div>
<div id="comment-66187-info" class="comment-info">
<span class="comment-age">(05 Oct '18, 20:34)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="66189"></span>
<div id="comment-66189" class="comment not_top_scorer">
<div id="post-66189-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik Ramm</a> Ah! Yes you are right. I am using a custom piece of software for rendering and forgot I am caching zoom 0 to 12 and not re-rendering them. That fixed it. Thanks for your help!</p>
<p>Also, I noticed you also commented on my question here:</p>
<p><a href="https://help.openstreetmap.org/questions/66165/openstreetmap-carto-english-names">https://help.openstreetmap.org/questions/66165/openstreetmap-carto-english-names</a></p>
<p>mentioning that the German fork of osm-carto is the best solution. Are there any major shortcomings to doing it the way I have here versus using the fork?</p>
</div>
<div id="comment-66189-info" class="comment-info">
<span class="comment-age">(05 Oct '18, 23:19)</span> <span class="comment-user userinfo">coderunner</span>
</div>
</div>
</div>
<div id="comment-tools-7922" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-7922-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32326"></span>

<div id="answer-container-32326" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32326-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have edited the default.style and have made following sql statements</p>
<p>update planet_osm_line set name="name:en" where "name:en" is not null; update planet_osm_point set name="name:en" where "name:en" is not null; update planet_osm_polygon set name="name:en" where "name:en" is not null; update planet_osm_roads set name="name:en" where "name:en" is not null;</p>
<p>thanks to <span>@Fredrik</span> Ramm</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '14, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/d5392fe7a68088f8c8e3bdc43a16f156?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gevork&#39;s gravatar image" />
<p><span>Gevork</span><br />
<span class="score" title="234 reputation points">234</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gevork has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32326" class="comments-container">
&#10;</div>
<div id="comment-tools-32326" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32326-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66186"></span>

<div id="answer-container-66186" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66186-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://help.openstreetmap.org/questions/66165/openstreetmap-carto-english-names">https://help.openstreetmap.org/questions/66165/openstreetmap-carto-english-names</a> is a similar question with more up-to-date answers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '18, 20:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-66186" class="comments-container">
&#10;</div>
<div id="comment-tools-66186" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66186-form-container" class="comment-form-container">
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

