+++
type = "question"
title = "Adding data to (runnning) postgresql with osm2pgsql"
description = '''Hello, after following this https://switch2osm.org/manually-building-a-tile-server-18-04-lts/ tutorial I wonder, if it is possible to add additional files to a postgresql, even if it is running.  osm2pgsql -d gis --create --slim -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreet...'''
date = "2019-01-24T14:49:00Z"
lastmod = "2019-01-24T19:07:00Z"
weight = 67712
keywords = [ "postgresql", "osm2pgsql", "tileserver" ]
aliases = [ "/questions/67712" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Adding data to (runnning) postgresql with osm2pgsql](/questions/67712/adding-data-to-runnning-postgresql-with-osm2pgsql)

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
<span id="post-67712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67712-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>after following this <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> tutorial I wonder, if it is possible to add additional files to a postgresql, even if it is running.</p>
<pre><code> osm2pgsql -d gis --create --slim  -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 2500 --number-processes 1 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/azerbaijan-latest.osm.pbf</code></pre>
<p>Will executing this command again, only with a different osm.pbf, result in an error or will it merge the new data into the existing one? What if I add data which the existing data is a subset of (Germany already imported and I execute osm2pgsql with the Europe osm.pbf)? Will it overwrite the existing data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jan '19, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/5eabcf32b6244f650e286d308d9341e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Erik1988osm&#39;s gravatar image" />
<p><span>Erik1988osm</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Erik1988osm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67712" class="comments-container">
&#10;</div>
<div id="comment-tools-67712" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67712-form-container" class="comment-form-container">
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

<span id="67723"></span>

<div id="answer-container-67723" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67723-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Erik1988osm has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a more that frequent FAQ.</p>
<ul>
<li>In general datasets need to be merged before import, if they are very far apart they might not have common objects, but as soon as they have you will run in to constraint violations.</li>
<li>the --create flag will remove any existing data, so you definitely don't want to use that on trying a second import.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '19, 19:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-67723" class="comments-container">
&#10;</div>
<div id="comment-tools-67723" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67723-form-container" class="comment-form-container">
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

