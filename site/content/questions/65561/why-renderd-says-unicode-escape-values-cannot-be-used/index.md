+++
type = "question"
title = "Why renderd says Unicode escape values cannot be used?"
description = '''Trying my first OSM install to generate map of Indonesia. Following https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/ Got through problems with package name changes and nodejs version issues. Thought I was unstoppable until I failed check when running: $ renderd -f -c /usr/local/et...'''
date = "2018-08-26T05:41:00Z"
lastmod = "2018-08-27T03:30:00Z"
weight = 65561
keywords = [ "renderd", "unicode", "error" ]
aliases = [ "/questions/65561" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why renderd says Unicode escape values cannot be used?](/questions/65561/why-renderd-says-unicode-escape-values-cannot-be-used)

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
<span id="post-65561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65561-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Trying my first OSM install to generate map of Indonesia. Following <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> Got through problems with package name changes and nodejs version issues. Thought I was unstoppable until I failed check when running: $ renderd -f -c /usr/local/etc/renderd.conf</p>
<p>renderd[11486]: An error occurred while loading the map layer 'ajt': Postgis Plugin: ERROR: Unicode escape values cannot be used for code point values above 007F when the server encoding is not UTF8 at or near "\2212'"</p>
<p>LINE 58: ...LACE(ROUND((tags-&gt;'ele')::NUMERIC)::TEXT, '-', U&amp;'\2212'), U... ^ in executeQuery Full sql was: 'SELECT * FROM (SELECT</p>
<p>&lt;snip obscenely="" long="" sql="" query=""&gt;</p>
<p>) AS text_poly LIMIT 0' encountered during parsing of layer 'text-poly' in Layer at line 44438 of '/home/osm/src/openstreetmap-carto/mapnik.xml'</p>
<p>The referenced line in mapnik.xml looks harmless: &lt;layer maximum-scale-denominator="750000" name="text-poly" srs="+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=<a href="https://help.openstreetmap.org/users/2957/nullpointer">@null</a> +wktext +no_defs +over"&gt;</p>
<p>But the reference to "when the server is not UTF8" has me thinking the "server" is renderd. But there's nothing in the renderd.conf that jumps out at me. I really want to display local names, so UTF-8/Unicode support is going to be needed.</p>
<p>Ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-unicode" rel="tag" title="see questions tagged &#39;unicode&#39;">unicode</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Aug '18, 05:41</strong></p>
<img src="https://secure.gravatar.com/avatar/df91ae002e65d6837e48925720ba323a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eric%20Phelps%20exz5z5&#39;s gravatar image" />
<p><span>Eric Phelps ...</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eric Phelps exz5z5 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65561" class="comments-container">
&#10;</div>
<div id="comment-tools-65561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65561-form-container" class="comment-form-container">
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

<span id="65562"></span>

<div id="answer-container-65562" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65562-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-65562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Eric Phelps exz5z5 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The server this refers to is the PostgeSQL server. On the page linked to you can see the line</p>
<pre><code>createdb -E UTF8 -O renderaccount gis</code></pre>
<p>which should make sure that your database is UTF8. Please refer to the PostgreSQL manual for details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '18, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-65562" class="comments-container">
<span id="65572"></span>
<div id="comment-65572" class="comment">
<div id="post-65572-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And so it was! Apparently there's a change in Postgres where you have to specify the -T option on createdb in order to get UTF-8. And no way to fix an existing database :( so I had to delete and re-create it. And then renderd complained it was missing "/usr/local/etc/renderd.conf" (which was, in fact, missing). And this is where I've decided to slick the whole thing and start over. And pay a lot more attention to things.</p>
<p>Seriously though, thanks for the quick help!</p>
</div>
<div id="comment-65572-info" class="comment-info">
<span class="comment-age">(27 Aug '18, 03:30)</span> <span class="comment-user userinfo">Eric Phelps ...</span>
</div>
</div>
</div>
<div id="comment-tools-65562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65562-form-container" class="comment-form-container">
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

