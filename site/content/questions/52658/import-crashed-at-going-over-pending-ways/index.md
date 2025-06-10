+++
type = "question"
title = "Import crashed at &quot;going over pending ways&quot;"
description = '''I ran an import of the full planet file in slim mode. It seems to have successfully imported the data, but then it crashed when going over pending ways. The log before the crash looks like this: Node stats: total(3545099707), max(4418326239) in 4387s Way stats: total(369751285), max(444345685) in 19...'''
date = "2016-10-24T09:48:00Z"
lastmod = "2016-10-24T11:36:00Z"
weight = 52658
keywords = [ "planet", "import", "ways" ]
aliases = [ "/questions/52658" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Import crashed at "going over pending ways"](/questions/52658/import-crashed-at-going-over-pending-ways)

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
<span id="post-52658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52658-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I ran an import of the full planet file in slim mode. It seems to have successfully imported the data, but then it crashed when going over pending ways. The log before the crash looks like this:</p>
<pre><code>Node stats: total(3545099707), max(4418326239) in 4387s
Way stats: total(369751285), max(444345685) in 192701s
Relation stats: total(4509999), max(6610383) in 264005s
Committing transaction for planet_osm_point
Committing transaction for planet_osm_line
Committing transaction for planet_osm_polygon
Committing transaction for planet_osm_roads
&#10;Going over pending ways...
Maximum node in persistent node cache: 4418699263</code></pre>
<p>Is it possible to resume the import for the remaining steps?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '16, 09:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0ba845809eb8c74c664ed9409636b3ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnNM&#39;s gravatar image" />
<p><span>johnNM</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnNM has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '16, 09:49</strong> </span></p>
</div>
</div>
<div id="comments-container-52658" class="comments-container">
<span id="52659"></span>
<div id="comment-52659" class="comment">
<div id="post-52659-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What platform and version?</p>
<p><a href="https://www.google.co.uk/search?q=">https://www.google.co.uk/search?q="Maximum+node+in+persistent+node+cache"</a></p>
<p>suggests that you might be using an old non-64-bit-aware version, and you may need to upgrade.</p>
</div>
<div id="comment-52659-info" class="comment-info">
<span class="comment-age">(24 Oct '16, 09:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52661"></span>
<div id="comment-52661" class="comment">
<div id="post-52661-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you <a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>. Apologies for not including additional info. My specs are as follows:</p>
<p>Ubuntu 14.04 LTS 700GB disk 30GB RAM</p>
<p>I used the following command:</p>
<p>sudo -u offlineuser osm2pgsql --create-d gis --slim --flat-nodes ~/osm/flat_nodes.bin -C 14000 --number-processes 4 --style ~/osm/openstreetmap-carto/openstreetmap-carto.style --multi-geometry /home/offlineserver/planet-latest.osm.pbf</p>
</div>
<div id="comment-52661-info" class="comment-info">
<span class="comment-age">(24 Oct '16, 10:24)</span> <span class="comment-user userinfo">johnNM</span>
</div>
</div>
<span id="52662"></span>
<div id="comment-52662" class="comment">
<div id="post-52662-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What does "osm2pgsql -h -v | grep -i version" say?</p>
</div>
<div id="comment-52662-info" class="comment-info">
<span class="comment-age">(24 Oct '16, 10:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="52663"></span>
<div id="comment-52663" class="comment">
<div id="post-52663-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>osm2pgsql SVN version 0.85.0 (64bit id space)</p>
</div>
<div id="comment-52663-info" class="comment-info">
<span class="comment-age">(24 Oct '16, 11:36)</span> <span class="comment-user userinfo">johnNM</span>
</div>
</div>
</div>
<div id="comment-tools-52658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52658-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

