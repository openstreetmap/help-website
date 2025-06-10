+++
type = "question"
title = "osm2pgsql problem with projection"
description = '''I would like to import an .osm file into the postgresql database. I used this code to start import: osm2pgsql -M -d postgres -S &quot;/usr/share/osm2pgsql/default.style&quot; -U &quot;postgres&quot; -W -H &quot;localhost&quot; -P 5432 &quot;/home/szg_osm_db.osm&quot;  I have no errors or cleaning ups, but when I open it in QuantumGis from...'''
date = "2013-09-29T11:14:00Z"
lastmod = "2013-09-30T17:58:00Z"
weight = 26840
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/26840" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql problem with projection](/questions/26840/osm2pgsql-problem-with-projection)

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
<span id="post-26840-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26840-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26840-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to import an .osm file into the postgresql database. I used this code to start import:</p>
<pre><code>osm2pgsql -M -d postgres -S &quot;/usr/share/osm2pgsql/default.style&quot; -U &quot;postgres&quot; -W -H &quot;localhost&quot; -P 5432 &quot;/home/szg_osm_db.osm&quot;</code></pre>
<p>I have no errors or cleaning ups, but when I open it in QuantumGis from postgresql database the geometry has faults. I dont know why. roads locate in wrong place, polygons are on each others. Is it projection problem? QuantumGis shows WGS84 Mercator EPGS:3395 projection. (I saved a test area from JOSM. It doesnt contain too much value. Its 2MB file.)</p>
<p>faults: <img src="http://abload.de/img/faultsjrsyb.jpg" alt="quantumgis printsceen" /></p>
<p>I could not recognize this coordinates which QGIS shows.Thanks</p>
<p>PS: sorry for my bad english</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Sep '13, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/9261163ee10e32bb91ceac5147b149a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lockdown90&#39;s gravatar image" />
<p><span>lockdown90</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lockdown90 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Sep '13, 11:36</strong> </span></p>
</div>
</div>
<div id="comments-container-26840" class="comments-container">
&#10;</div>
<div id="comment-tools-26840" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26840-form-container" class="comment-form-container">
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

<span id="26852"></span>

<div id="answer-container-26852" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26852-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I remember seeing something similar when using an old version of osm2pgsql that didn't support 64 bit ids. Can you run</p>
<pre><code>osm2pgsql --version</code></pre>
<p>and verify that it reports "64bit id space"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '13, 03:22</strong></p>
<img src="https://secure.gravatar.com/avatar/b9a8b8a3b1418b4b0bb41041555b18a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dymo12&#39;s gravatar image" />
<p><span>Dymo12</span><br />
<span class="score" title="796 reputation points">796</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dymo12 has 2 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-26852" class="comments-container">
<span id="26855"></span>
<div id="comment-26855" class="comment">
<div id="post-26855-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Wasn't there a 64-bit issue with QGIS itself, as described here:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/QGIS_OSM_Plugin">http://wiki.openstreetmap.org/wiki/QGIS_OSM_Plugin</a></p>
</div>
<div id="comment-26855-info" class="comment-info">
<span class="comment-age">(30 Sep '13, 08:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="26871"></span>
<div id="comment-26871" class="comment">
<div id="post-26871-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The 64bit issue should be fixed in the newly released QGIS 2.0</p>
<p>But I have not verified that. Is anyone able to try it and report?</p>
</div>
<div id="comment-26871-info" class="comment-info">
<span class="comment-age">(30 Sep '13, 16:35)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="26873"></span>
<div id="comment-26873" class="comment">
<div id="post-26873-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Like Dymo12 I think this is an osm2pgsql 64-bit problem, rather than anything to do with QGIS.</p>
</div>
<div id="comment-26873-info" class="comment-info">
<span class="comment-age">(30 Sep '13, 17:58)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26852" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26852-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26841"></span>

<div id="answer-container-26841" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26841-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The coordinates that QGis shows are Mercator meters, just like you requested by adding "-M" to the osm2pgsql command line. Use "-l" (small letter L) instead if you want latitude/longitude values.</p>
<p>The reason why some geometries are broken is likely that you saved your file from JOSM and some relations will be incomplete. This can break polygons (but not usually lines). A more thorough analysis might be possible if you placed your .osm file somewhere for us to inspect!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '13, 12:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-26841" class="comments-container">
<span id="26846"></span>
<div id="comment-26846" class="comment">
<div id="post-26846-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I downloaded the map of Malta from the official site: <a href="http://download.geofabrik.de/europe/malta-latest.osm.bz2">geofabrik</a></p>
<p>I used this command that you suggested:</p>
<pre><code>osm2pgsql -l -d GIStest -S &quot;/usr/share/osm2pgsql/default.style&quot; -U &quot;postgres&quot; -W -H &quot;localhost&quot; -P 5432 &quot;/home/malta.osm&quot;</code></pre>
<p>and the result is also same like above. BUT the coordinates changed. <img src="http://abload.de/img/faults21nsmh.jpg" alt="screenshot" /></p>
<p>osm_roads and osm_line originated from one point.</p>
</div>
<div id="comment-26846-info" class="comment-info">
<span class="comment-age">(29 Sep '13, 16:44)</span> <span class="comment-user userinfo">lockdown90</span>
</div>
</div>
</div>
<div id="comment-tools-26841" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26841-form-container" class="comment-form-container">
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

