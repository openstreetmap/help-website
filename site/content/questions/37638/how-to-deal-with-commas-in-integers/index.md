+++
type = "question"
title = "How to deal with commas in integers?"
description = '''Attempting to follow steps 7 and 8 here, currently: https://github.com/mapserver/mapserver/wiki/RenderingOsmDataWindows A recently-updated osm file I&#x27;m working with (british-isles-latest.osm.bz2, from http://download.geofabrik.de/europe/british-isles.html) seems to have a number of &#x27;integer&#x27; values ...'''
date = "2014-10-16T09:39:00Z"
lastmod = "2014-10-16T13:45:00Z"
weight = 37638
keywords = [ "mapserver", "postgresql", "osm2pgsql" ]
aliases = [ "/questions/37638" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to deal with commas in integers?](/questions/37638/how-to-deal-with-commas-in-integers)

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
<span id="post-37638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37638-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Attempting to follow steps 7 and 8 here, currently: <a href="https://github.com/mapserver/mapserver/wiki/RenderingOsmDataWindows">https://github.com/mapserver/mapserver/wiki/RenderingOsmDataWindows</a></p>
<p>A recently-updated osm file I'm working with (british-isles-latest.osm.bz2, from <a href="http://download.geofabrik.de/europe/british-isles.html)">http://download.geofabrik.de/europe/british-isles.html)</a> seems to have a number of 'integer' values that contain commas - two, both population so far.</p>
<p>I've loaded the data to a postgres database using osm2pgsql, and am currently attempting to run osm2pgsql-to-imposm-schema.sql, but keep running into the error 'invalid input syntax for integer: "[some number with comma separators]"'. A little investigation shows that thus far these are population values, and whilst I can manually edit the commas out of the osm, postgres will only complain about one at a time and loading the data takes half a day or so, so this doesn't seem like the best solution.</p>
<p>I've loaded a slightly older (few weeks older?) version of this osm file to a local copy of postgres using the same steps previously, without issue.</p>
<p>Is this a recent change to how population values are stored in osms, or is this something that will be corrected in the data, and in either case how can I solve this without manually fixing all population values as postgres reports errors?</p>
<p>Pieren: osm2pgsql version is osm2pgsql SVN version 0.83.0 (64bit id space). According to default.style it is being treated as text: 'node,way population text linear'</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapserver" rel="tag" title="see questions tagged &#39;mapserver&#39;">mapserver</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '14, 09:39</strong></p>
<img src="https://secure.gravatar.com/avatar/1293b1c7c8f44cd7a4320534a7ce2832?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RPaliwoda&#39;s gravatar image" />
<p><span>RPaliwoda</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RPaliwoda has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Oct '14, 13:11</strong> </span></p>
</div>
</div>
<div id="comments-container-37638" class="comments-container">
<span id="37639"></span>
<div id="comment-37639" class="comment">
<div id="post-37639-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I can't tell you how to fix this issue but there is one important fact: OSM data will always contain errors because the API does perform (almost) no validation. Population numbers might even contain letters. The only valid solution is that each parsing tool must be able to handle unexpected contents of tags and values.</p>
</div>
<div id="comment-37639-info" class="comment-info">
<span class="comment-age">(16 Oct '14, 09:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="37640"></span>
<div id="comment-37640" class="comment">
<div id="post-37640-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is actually the only sensible answer, tag values are strings, therefore you need a filter, validation &amp; conversion routine.</p>
</div>
<div id="comment-37640-info" class="comment-info">
<span class="comment-age">(16 Oct '14, 10:11)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="37649"></span>
<div id="comment-37649" class="comment">
<div id="post-37649-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Normally, "population" tag is treated as text datatyp. Please report your osm2pgsql version.</p>
</div>
<div id="comment-37649-info" class="comment-info">
<span class="comment-age">(16 Oct '14, 13:00)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-37638" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37638-form-container" class="comment-form-container">
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

<span id="37652"></span>

<div id="answer-container-37652" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37652-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-37652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RPaliwoda has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Having a quick look into the sql script <a href="https://github.com/mapserver/basemaps/blob/master/contrib/osm2pgsql-to-imposm-schema.sql">osm2pgsql-to-imposm-schema.sql</a>, it seems that the script is transforming the original population column into an integer type:</p>
<pre><code>-- cast population column as an integer
ALTER TABLE osm_new_places ADD COLUMN population2 integer;
UPDATE osm_new_places SET population2 = cast(population as integer) WHERE population IS NOT NULL;
ALTER TABLE osm_new_places DROP COLUMN population;
ALTER TABLE osm_new_places RENAME COLUMN population2 TO population;</code></pre>
<p>Which means that if you want to reuse osm2pgsql, you should drop either everything and recreate all tables or just drop this column and recreate it with its original datatyp (text I guess). Something like :</p>
<pre><code>ALTER TABLE osm_new_places DROP COLUMN population;
ALTER TABLE osm_new_places ADD COLUMN population text;</code></pre>
<p>or try</p>
<pre><code>ALTER TABLE osm_new_places ALTER COLUMN population type text using population::text;</code></pre>
<p>if it works</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '14, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Oct '14, 15:52</strong> </span></p>
</div>
</div>
<div id="comments-container-37652" class="comments-container">
&#10;</div>
<div id="comment-tools-37652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37652-form-container" class="comment-form-container">
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

