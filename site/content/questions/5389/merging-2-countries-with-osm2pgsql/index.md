+++
type = "question"
title = "Merging 2 countries with osm2pgsql"
description = '''I have some issues while i try to append new country (Ukraine) to already imported one (US). First I created db with US OSM data: osm2pgsql -l --create --database gis --username gis --prefix planet --slim --cache 2048 united_states.osm.bz2  Then I tried to append ukraine.osm.bz2: osm2pgsql -l --appe...'''
date = "2011-05-26T12:57:00Z"
lastmod = "2017-02-20T10:18:00Z"
weight = 5389
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/5389" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Merging 2 countries with osm2pgsql](/questions/5389/merging-2-countries-with-osm2pgsql)

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
<span id="post-5389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5389-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have some issues while i try to append new country (Ukraine) to already imported one (US).</p>
<p>First I created db with US OSM data:</p>
<pre><code>osm2pgsql -l --create --database gis --username gis --prefix planet --slim --cache 2048 united_states.osm.bz2</code></pre>
<p>Then I tried to append ukraine.osm.bz2:</p>
<pre><code>osm2pgsql -l --append --database gis --username gis --prefix planet --slim --cache 2048 ukraine.osm.bz2</code></pre>
<p>And received:</p>
<pre><code>Going over pending relations
COPY_END for COPY planet_rels FROM STDIN;
 failed: ERROR:  duplicate key value violates unique constraint &quot;planet_rels_pkey&quot;
CONTEXT:  COPY planet_rels, line 61: &quot;60189     1       481     {27503927,96165454,96165453,62055667,43761343,100453556,43764881,62055669,44097114,77755...&quot;</code></pre>
<p>Files with countries were taken from <a href="http://download.cloudmade.com">download.cloudmade.com</a></p>
<p>What is wrong in my actions and is there any way to import 2 countries information into DB?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '11, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/d74db3d2cab53a21a0d231a84d55d174?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bestic2&#39;s gravatar image" />
<p><span>bestic2</span><br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bestic2 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5389" class="comments-container">
&#10;</div>
<div id="comment-tools-5389" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5389-form-container" class="comment-form-container">
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

<span id="5390"></span>

<div id="answer-container-5390" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5390-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-5390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bestic2 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The relation in your error message is the border of the Russian Federation:</p>
<p><a href="http://www.openstreetmap.org/browse/relation/60189">http://www.openstreetmap.org/browse/relation/60189</a></p>
<p>which shares ways such as</p>
<p><a href="http://www.openstreetmap.org/browse/way/50752242">http://www.openstreetmap.org/browse/way/50752242</a></p>
<p>with the border of the USA.</p>
<p>I am not an expert, but suspect you might need to use Osmosis to merge the two files first and then import using osm2pgsql in one go.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '11, 13:49</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-5390" class="comments-container">
<span id="5391"></span>
<div id="comment-5391" class="comment">
<div id="post-5391-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks! It's really 1 common relation between 2 countries - 60189 id in planet_rels. I temporary dropped constraint before appending and all goes well</p>
</div>
<div id="comment-5391-info" class="comment-info">
<span class="comment-age">(26 May '11, 15:43)</span> <span class="comment-user userinfo">bestic2</span>
</div>
</div>
<span id="40581"></span>
<div id="comment-40581" class="comment">
<div id="post-40581-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can both of you please share ways how to do this (<a href="http://help.openstreetmap.org/users/339/edloach">@EdLoach</a> how to use Osmosis for that, bestic2 how to temporarily drop the constraints)? I’ve got <a href="https://help.openstreetmap.org/questions/40580/how-much-disc-space-do-the-exports-use">similar issues</a>…</p>
</div>
<div id="comment-40581-info" class="comment-info">
<span class="comment-age">(24 Jan '15, 21:23)</span> <span class="comment-user userinfo">mirabilos</span>
</div>
</div>
</div>
<div id="comment-tools-5390" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5390-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54745"></span>

<div id="answer-container-54745" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54745-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-54745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use <a href="https://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a>.</p>
<p>You have 2 choices:</p>
<p>1) Merge new region file with existing map file:</p>
<p><code>osmconvert new_region.pbf --out-o5m | osmconvert.exe - already_loaded_map.pbf -o=map_with_new_region.pbf</code></p>
<p>and then load merged file to postgreSQL with cleaning database:</p>
<p><code>osm2pgsql --create ... map_with_new_region.pbf</code></p>
<p>2) Or separate already existing data from new region file using:</p>
<p><code>osmconvert new_region.pbf -o=new_region.o5m</code></p>
<p><code>osmconvert already_loaded_map.pbf -o=already_loaded_map.o5m</code></p>
<p><code>osmconvert new_region.o5m --subtract already_loaded_map.o5m -o=new_region_cleaned.o5m</code></p>
<p><code>osmconvert new_region_cleaned.o5m -o=new_region_cleaned.pbf</code></p>
<p>And then you can just append new file to PostgreSQL using:</p>
<p><code>osm2pgsql --append ... new_region_cleaned.pbf</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '17, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/36e2f34616e97c8a7f49b03c7915eb60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ReckyXXX&#39;s gravatar image" />
<p><span>ReckyXXX</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ReckyXXX has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54745" class="comments-container">
&#10;</div>
<div id="comment-tools-54745" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54745-form-container" class="comment-form-container">
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

