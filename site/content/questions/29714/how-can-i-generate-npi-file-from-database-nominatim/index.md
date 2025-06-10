+++
type = "question"
title = "How can I generate npi file from database &quot;Nominatim&quot;?"
description = '''I want to delete some data from database &quot;Nominatim&quot;.   One way is to generate nominatim pre-indexed file from database &quot;Nominatim&quot;.  Next, remove some data from this file.  After all, create new database from this npi file.  The problem is that npi service is being deprecated http://open.mapquestap...'''
date = "2014-01-09T12:20:00Z"
lastmod = "2014-01-13T11:44:00Z"
weight = 29714
keywords = [ "nominatim", "npi" ]
aliases = [ "/questions/29714" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I generate npi file from database "Nominatim"?](/questions/29714/how-can-i-generate-npi-file-from-database-nominatim)

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
<span id="post-29714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29714-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to delete some data from database "Nominatim".</p>
<ul>
<li>One way is to generate nominatim pre-indexed file from database "Nominatim".</li>
<li>Next, remove some data from this file.</li>
<li>After all, create new database from this npi file.</li>
</ul>
<p>The problem is that npi service is being deprecated <a href="http://open.mapquestapi.com/npi/">http://open.mapquestapi.com/npi/</a></p>
<p>How can I generate npi file from database "Nominatim"?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-npi" rel="tag" title="see questions tagged &#39;npi&#39;">npi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '14, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/aea8cdb05518a630ebad09bd7c777dc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amshegar&#39;s gravatar image" />
<p><span>amshegar</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amshegar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29714" class="comments-container">
&#10;</div>
<div id="comment-tools-29714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29714-form-container" class="comment-form-container">
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

<span id="29718"></span>

<div id="answer-container-29718" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29718-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The NPI format is no longer supported. The code that still exists is not maintained and might be changed or removed at some point in the future.</p>
<p>If you want to filter data from the database you should filter your OSM file before importing it into Nominatim.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '14, 14:37</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-29718" class="comments-container">
&#10;</div>
<div id="comment-tools-29718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29718-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29716"></span>

<div id="answer-container-29716" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29716-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-29716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, did you followed III's suggestions ? 'There is currently no DB schema description of Nominatim available: <a href="http://wiki.openstreetmap.org/wiki/Category:Nominatim">http://wiki.openstreetmap.org/wiki/Category:Nominatim</a> So you might ask at the OSM-TALK or OSM-DEV mailinglist or in wiki at the Nominatim disc. A documentation at the wiki would be nice for the community :) Maybe it's easier to export your dump to preprocessed nomiatim NPI files and filter this files before reimporting to get a light DB?' And the result ? Since your asking it here again ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '14, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-29716" class="comments-container">
<span id="29742"></span>
<div id="comment-29742" class="comment">
<div id="post-29742-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>Hi, did you followed III's suggestions...</p>
</blockquote>
<p>Hello. No. This is a task from my work. Before this day I had other tasks and goals, but today all tasks were done. This is the last task: I must significantly improve the speed of geocoding (for example, ** requests per second)</p>
<p>I'm not a very good specialist in the geocoding or database design. But in our company there are no other specialists. So I ask this question on the forum.</p>
<p>So, 1) extract planet-latest.osm from planet-latest.osm.pbf or planet-latest.osm.bz2 2) write scripts for removing some data from planet-latest.osm 3) make planet-latest.osm.bz2 from planet-latest.osm using winRAR</p>
<ul>
<li><p>Is it a good idea?</p></li>
<li><p>Can I use OsmSharp for parsing data? <a href="http://www.osmsharp.com/wiki/data-processing">http://www.osmsharp.com/wiki/data-processing</a></p></li>
</ul>
</div>
<div id="comment-29742-info" class="comment-info">
<span class="comment-age">(10 Jan '14, 06:48)</span> <span class="comment-user userinfo">amshegar</span>
</div>
</div>
<span id="29747"></span>
<div id="comment-29747" class="comment">
<div id="post-29747-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>We usually use Osmosis to process .PBF or .OSM files, so it's the most reliable tool. You might also <a href="http://wiki.openstreetmap.org/wiki/OSM_file_formats#Map-data">try others</a>.<br />
AFAIK you can use osmosis without needing to extract the full planet (saves disk space and increases speed).<br />
Yes, sounds like a plan :) But I suggest to start playing with filtering with smaller extracts, so you save time and get a better feeling about the results and see possible problems fast enough. Your home area is always a good idea.</p>
</div>
<div id="comment-29747-info" class="comment-info">
<span class="comment-age">(10 Jan '14, 17:51)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="29749"></span>
<div id="comment-29749" class="comment">
<div id="post-29749-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>To be honest it sounds as if you are very much out of your depth, and anything you try will be fishing in muddy waters. Are you even sure that removing some data will speed things up? Have you tuned your PostGIS database as recommended? Is your database on an SSD, and does the machine have enough RAM? -- We have programs that can filter OSM data, like osmosis or osmfilter, there's no need to write your own. You could even run the import normally and <em>then</em> remove data from PostGIS by issuing DELETE statements for what you don't need. But as I said, it's not even sure that this will help.</p>
</div>
<div id="comment-29749-info" class="comment-info">
<span class="comment-age">(11 Jan '14, 00:15)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="29794"></span>
<div id="comment-29794" class="comment">
<div id="post-29794-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I already tuned all software (I read official documentation on each program). The database is on an SSD. The hardware is good.</p>
<p>I think I finish this task successfully if I significantly reduce the size of database "nominatim" (in this case I also save some SSD). For example, I want to delete all data, which level is less than 17. <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Development_overview#Indexing_.2F_Address_Calculation">http://wiki.openstreetmap.org/wiki/Nominatim/Development_overview#Indexing_.2F_Address_Calculation</a></p>
<p>Does such command in osmosis exist?</p>
</div>
<div id="comment-29794-info" class="comment-info">
<span class="comment-age">(13 Jan '14, 11:44)</span> <span class="comment-user userinfo">amshegar</span>
</div>
</div>
</div>
<div id="comment-tools-29716" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29716-form-container" class="comment-form-container">
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

