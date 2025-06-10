+++
type = "question"
title = "Geofabrik diff files by country"
description = '''Hi all, I&#x27;m testing how to use osm2pgsql to keep an up-to-date Postgres base with OSM data on France (all tables). I take my extracts from Geofabrik for the country, but I can&#x27;t find if there is any link for diffs on countries ? Is there just the diff files for the whole world ? What would be the be...'''
date = "2017-08-18T15:03:00Z"
lastmod = "2017-08-18T15:53:00Z"
weight = 58385
keywords = [ "diff", "geofabrik", "osm2pgsql", "update" ]
aliases = [ "/questions/58385" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Geofabrik diff files by country](/questions/58385/geofabrik-diff-files-by-country)

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
<span id="post-58385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58385-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I'm testing how to use osm2pgsql to keep an up-to-date Postgres base with OSM data on France (all tables). I take my extracts from Geofabrik for the country, but I can't find if there is any link for diffs on countries ? Is there just the diff files for the whole world ? What would be the best strategy to update a country base ?</p>
<p>Thanks a lot !!</p>
<p>Gabriel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '17, 15:03</strong></p>
<img src="https://secure.gravatar.com/avatar/208cd7e1271d4e4f19105949e0f39692?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GabrielV&#39;s gravatar image" />
<p><span>GabrielV</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GabrielV has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58385" class="comments-container">
&#10;</div>
<div id="comment-tools-58385" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58385-form-container" class="comment-form-container">
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

<span id="58386"></span>

<div id="answer-container-58386" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58386-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-58386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes there are diff files per country. It's only daily (no minutely or hourly diffs), and you'll have to use the custom status number from the file.</p>
<p>For france the url is here <a href="http://download.geofabrik.de/europe/france-updates/">http://download.geofabrik.de/europe/france-updates/</a></p>
<p>It's probably not as clear as it could be, but if you click on <code>raw directory index</code>, you can see the <code>france-updates</code> directory.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '17, 15:53</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-58386" class="comments-container">
&#10;</div>
<div id="comment-tools-58386" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58386-form-container" class="comment-form-container">
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

