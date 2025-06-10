+++
type = "question"
title = "How to use Geofabrik internal download server to use non-anonymized change files (.osc.gz) w/osmosis/osm2pgsql ?"
description = '''Hi, When using osmosis/osm2pgsql to keep an openstreetmap database up-to-date, we commonly use Osmosis with options --read-replication-interval --simplify-change --write-xml-change to get changes from a directory containing change files. This directory could be defined within Osmosis configuration.t...'''
date = "2023-11-22T13:54:00Z"
lastmod = "2023-11-22T14:37:00Z"
weight = 88015
keywords = [ "geofabrik", "osmosis", "osm2pgsql" ]
aliases = [ "/questions/88015" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to use Geofabrik internal download server to use non-anonymized change files (.osc.gz) w/osmosis/osm2pgsql ?](/questions/88015/how-to-use-geofabrik-internal-download-server-to-use-non-anonymized-change-files-oscgz-wosmosisosm2pgsql)

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
<span id="post-88015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88015-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>When using osmosis/osm2pgsql to keep an openstreetmap database up-to-date, we commonly use Osmosis with options <code>--read-replication-interval --simplify-change --write-xml-change</code> to get changes from a directory containing change files. This directory could be defined within Osmosis <code>configuration.txt</code> file thanks to the variable <code>baseUrl</code>.</p>
<p>Currently I use <code>baseUrl=</code><a href="https://download.geofabrik.de/europe/france-updates/"><code>https://download.geofabrik.de/europe/france-updates/</code></a> but since some years, Geofabrik has removed user names, user IDs and changeset IDs of the OSM objects (which are "subject to data protection regulations in the European Union").</p>
<p>Geofabrik also have an "internal download server" available for OpenStreetMap authentified users. Here is the url for France updates : <a href="https://osm-internal.download.geofabrik.de/europe/france-updates/">https://osm-internal.download.geofabrik.de/europe/france-updates/</a></p>
<p>My question is : <strong>how to use Geofabrik "internal download server" with Osmosis</strong>, that means how to manage OSM authentication in a classic Osmosis/Osm2pgsql stack to keep an OSM database up-to-date using <a href="https://osm-internal.download.geofabrik.de/europe/france-updates/">https://osm-internal.download.geofabrik.de/europe/france-updates/</a> as Osmosis <code>baseUrl</code></p>
<p>Thanks in advance for your help.</p>
<p>Augustin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Nov '23, 13:54</strong></p>
<img src="https://secure.gravatar.com/avatar/e8872726c57a506c351071fc1b7b3aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustind&#39;s gravatar image" />
<p><span>augustind</span><br />
<span class="score" title="166 reputation points">166</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustind has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-88015" class="comments-container">
&#10;</div>
<div id="comment-tools-88015" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88015-form-container" class="comment-form-container">
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

<span id="88016"></span>

<div id="answer-container-88016" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88016-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-88016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="augustind has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you really want to use Osmosis, you have to check out our pull request we submitted in 2018 when started the "internal download server". Unfortunately, Osmosis is in "light-maintenance mode". To be honest, I do not expect that the pull request will be accepted within the next years.</p>
<p>Please consider switching to <a href="https://docs.osmcode.org/pyosmium/latest/tools_get_changes.html">Pyosmium</a>. Pyosmium has cookie support.</p>
<p>The documentation about how to get a cookie for Pyosmium can be found <a href="https://github.com/geofabrik/sendfile_osm_oauth_protector/blob/master/doc/client.md">on GitHub</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '23, 14:16</strong></p>
<img src="https://secure.gravatar.com/avatar/d2a3b905e2632430b47dd9b8de3d8ba0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nakaner&#39;s gravatar image" />
<p><span>Nakaner</span><br />
<span class="score" title="610 reputation points">610</span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nakaner has 3 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-88016" class="comments-container">
<span id="88017"></span>
<div id="comment-88017" class="comment">
<div id="post-88017-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for your quick answer ! I'm going to try migrate our stack to use <code>Pyosmium</code> and <code>sendfile_osm_oauth_protector</code> instead of Osmosis, I did not know these tools.</p>
</div>
<div id="comment-88017-info" class="comment-info">
<span class="comment-age">(22 Nov '23, 14:37)</span> <span class="comment-user userinfo">augustind</span>
</div>
</div>
</div>
<div id="comment-tools-88016" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88016-form-container" class="comment-form-container">
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

