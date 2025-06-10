+++
type = "question"
title = "OpenStreetMap statistics"
description = '''What is the number of users, nodes, ways and relations in OSM till November 2017 for India region?'''
date = "2017-11-07T05:05:00Z"
lastmod = "2021-01-21T10:39:00Z"
weight = 60494
keywords = [ "stats" ]
aliases = [ "/questions/60494" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OpenStreetMap statistics](/questions/60494/openstreetmap-statistics)

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
<span id="post-60494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60494-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the number of users, nodes, ways and relations in OSM till November 2017 for India region?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-stats" rel="tag" title="see questions tagged &#39;stats&#39;">stats</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Nov '17, 05:05</strong></p>
<img src="https://secure.gravatar.com/avatar/357d59e7559dc9809641c15f88c37ad5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jasmeet_kaur&#39;s gravatar image" />
<p><span>jasmeet_kaur</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jasmeet_kaur has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60494" class="comments-container">
&#10;</div>
<div id="comment-tools-60494" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60494-form-container" class="comment-form-container">
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

<span id="60497"></span>

<div id="answer-container-60497" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60497-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-60497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nodes, ways, and relations are relatively easy to count, you can simply use the India file from here <a href="http://download.geofabrik.de/asia/india.html">http://download.geofabrik.de/asia/india.html</a> and count the elements. Either use a sophisticated, osmium-based statistics program or simply</p>
<pre><code>bzcat india-latest.osm.bz2 |
grep -E &quot;&lt;(node|way|relation)&quot; |
cut -d\  -f1 | sort | uniq -c</code></pre>
<p>Users are more difficult to count because the current data file does not list all users who are in India or whose centre of activity is India - it lists all users who are the last person to have edited an object in India, which likely includes tons of "drive-by mappers" and bots, and excludes those whose contributions have meanwhile been modified by others. Hence you will want to look at the history file for India for a more thorough analysis. It also depends on whether you only want to count active users or all users, and what your definition of an active user is!</p>
<p>Here are some ready-made pages with information about India:</p>
<ul>
<li><a href="http://mapbox.github.io/osm-analysis-collab/users-by-country?yearIdx=11&amp;minActiveDays=10&amp;maxActiveDays=365&amp;#2/22.0/28.0">http://mapbox.github.io/osm-analysis-collab/users-by-country?yearIdx=11&amp;minActiveDays=10&amp;maxActiveDays=365&amp;#2/22.0/28.0</a></li>
<li><a href="https://osmstats.neis-one.org/?item=countries&amp;country=India">https://osmstats.neis-one.org/?item=countries&amp;country=India</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '17, 07:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-60497" class="comments-container">
<span id="78430"></span>
<div id="comment-78430" class="comment">
<div id="post-78430-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately the Mapbox site doesn't have new data after 2016.</p>
</div>
<div id="comment-78430-info" class="comment-info">
<span class="comment-age">(21 Jan '21, 10:13)</span> <span class="comment-user userinfo">Richlv</span>
</div>
</div>
</div>
<div id="comment-tools-60497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60497-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78431"></span>

<div id="answer-container-78431" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78431-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since the above was written, a new command-line tool has made OSM data wrangling a bit easier for non-programmers. The <code>osmium</code> command-line program can convert an OSM PBF data file into an ASCII data format called "OPL" (short for object-per-line, meaning it has one line per OSM object). Once converted into this OPL format, standard command line tools can be used to process the data. For example, for a top-20 list of all users editing India, get the India history file from <a href="https://osm-internal.download.geofabrik.de/asia/india-internal.osh.pbf">https://osm-internal.download.geofabrik.de/asia/india-internal.osh.pbf</a> and then (all on one line):</p>
<pre><code>osmium cat india-internal.osh.pbf -fopl | 
   cut -d\  -f7 | cut -c2- | sort | uniq -c |
   sort -rn | head -20</code></pre>
<p>Insert "grep" commands at liberty to count just edits in certain years, and so on.</p>
<p>If you are comfortable with Python or C++, you can also use the <code>pyosmium</code> bindings to read the original .osm.pbf with Python, or <code>libosmium</code> to do so in C++.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '21, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78431" class="comments-container">
&#10;</div>
<div id="comment-tools-78431" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78431-form-container" class="comment-form-container">
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

