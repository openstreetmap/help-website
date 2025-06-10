+++
type = "question"
title = "What&#x27;s the best way of searching for misplaced semicolons in OSM data?"
description = '''Normally the answer is &quot;taginfo&quot;, but (as you&#x27;d expect) that does explicit processing of semicolons. If I search for http://taginfo.openstreetmap.org.uk/search?q=bar%3Bcafe%3Btoilets#values I get the one expected value back, but I&#x27;m not aware of a way of searching for any values (or keys for that ma...'''
date = "2016-01-21T14:32:00Z"
lastmod = "2016-01-22T07:09:00Z"
weight = 47614
keywords = [ "overpass", "taginfo", "postgresql" ]
aliases = [ "/questions/47614" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [What's the best way of searching for misplaced semicolons in OSM data?](/questions/47614/whats-the-best-way-of-searching-for-misplaced-semicolons-in-osm-data)

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
<span id="post-47614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47614-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Normally the answer is "taginfo", but (as you'd expect) that does explicit processing of semicolons. If I search for <a href="http://taginfo.openstreetmap.org.uk/search?q=bar%3Bcafe%3Btoilets#values">http://taginfo.openstreetmap.org.uk/search?q=bar%3Bcafe%3Btoilets#values</a> I get the <a href="http://www.openstreetmap.org/way/234822100/history">one expected value</a> back, but I'm not aware of a way of searching for any values (or keys for that matter) containing multiple semicolons.</p>
<p>In postgres (with a "normal" rendering database) I can do:</p>
<pre><code>gis=# SELECT amenity FROM planet_osm_polygon WHERE (amenity LIKE &#39;%;%;%&#39;);
                  amenity
-------------------------------------------
 bar;cafe;toilets
 private_hire_cars;coach_hire;minibus_hire
(2 rows)</code></pre>
<p>but obviously that requires a local database and doesn't search for semicolons in keys - presumably there's a way to search the "<code>tags</code>" array in "<code>planet_osm_ways</code>"? Obviously for "<code>planet_osm_polygon</code>" I'd also need to look at "<code>planet_osm_point</code>" and "<code>planet_osm_line</code>", and for "<code>planet_osm_ways</code>" I'd need to look at "<code>planet_osm_nodes</code>" too (ignoring relations for now).</p>
<p>Maybe there's a way of doing it with Overpass?</p>
<p>EDIT: This was prompted by this <a href="https://lists.openstreetmap.org/pipermail/tagging/2016-January/028057.html">taginfo</a> discussion, as well as the related <a href="https://github.com/openstreetmap/iD/issues/2896">iD issue</a> and someone "correcting" name_X tags in Ireland (the link to which I've lost).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-taginfo" rel="tag" title="see questions tagged &#39;taginfo&#39;">taginfo</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '16, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '16, 14:38</strong> </span></p>
</div>
</div>
<div id="comments-container-47614" class="comments-container">
<span id="47616"></span>
<div id="comment-47616" class="comment">
<div id="post-47616-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://www.openstreetmap.org/changeset/36573638">This</a> is probably the name_X correction you had in mind.</p>
</div>
<div id="comment-47616-info" class="comment-info">
<span class="comment-age">(21 Jan '16, 15:17)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47614-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="47617"></span>

<div id="answer-container-47617" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47617-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have an osm2pgsql/hstore database and want to operate on the keys, you have to explode the hstore into regular rows with the <code>each</code> operator before then applying a normal query, like so:</p>
<pre><code>gis=# SELECT osm_id, key
FROM
  (SELECT osm_id,(each(tags)).key as key FROM planet_osm_point) sub 
WHERE key like &#39;%;%;%&#39;;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '16, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-47617" class="comments-container">
<span id="47619"></span>
<div id="comment-47619" class="comment">
<div id="post-47619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No hstore here currently (and no "tags" column on planet_osm_point, though there is one on e.g. planet_osm_nodes) - will have to try it after reload.</p>
</div>
<div id="comment-47619-info" class="comment-info">
<span class="comment-age">(21 Jan '16, 19:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47617" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47617-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47621"></span>

<div id="answer-container-47621" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47621-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass does indeed have regex search for keys: <a href="http://overpass-turbo.eu/s/dTS">http://overpass-turbo.eu/s/dTS</a></p>
<pre><code>way[~&quot;;&quot;~&quot;.&quot;];
out geom;</code></pre>
<p>(<code>~"."</code> will match any value, some value match is required when matching a key)</p>
<p>In a similar way, you can also query for nodes or relations with at least one semicolon.</p>
<p>Edit: To check for values with at least 2 semicolons, the following regular expression might come in handy: <code>".+;(.+;)+.+"</code> - use it either for keys or values.</p>
<pre><code>[bbox:{{bbox}}];
way[~&quot;.&quot;~&quot;.+;(.+;)+.+&quot;];
out geom;</code></pre>
<p>In any case it is recommended to also specify a suitable key like e.g. amenity, otherwise tags like opening_hours will produce quite a lot of hits.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '16, 21:33</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '16, 08:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span></p>
</div>
</div>
<div id="comments-container-47621" class="comments-container">
&#10;</div>
<div id="comment-tools-47621" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47621-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47623"></span>

<div id="answer-container-47623" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47623-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Taginfo doesn't have a way to do searches like that (mostly for performance reasons), but you can <a href="https://taginfo.openstreetmap.org/download">download</a> the taginfo database and do the query yourself. The database is in Sqlite format and quite big, but once you have it, usage is simple and reasonably fast if you know SQL:</p>
<pre><code>sqlite&gt; select count(*) from tags where value like &#39;%;%;%&#39;;
205966</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '16, 07:09</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-47623" class="comments-container">
&#10;</div>
<div id="comment-tools-47623" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47623-form-container" class="comment-form-container">
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

