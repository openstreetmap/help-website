+++
type = "question"
title = "Is it possible to apply a bounding polygon to a changeset before applying it?"
description = '''I&#x27;ve got a copy of planet.osm.pbf and a subsection op_area.osm (bounded by bounds.poly) which covers several US states. I&#x27;ve also set up a way to get the planet.osm diffs each week (rssdownloader + rtorrent + http://osm-torrent.torres.voyager.hr/files/rss.xml, for the curious), and it&#x27;s trivial to a...'''
date = "2014-04-22T15:19:00Z"
lastmod = "2014-04-25T23:50:00Z"
weight = 32514
keywords = [ "planet", "changeset", "bounding-polygon", "osmosis" ]
aliases = [ "/questions/32514" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is it possible to apply a bounding polygon to a changeset before applying it?](/questions/32514/is-it-possible-to-apply-a-bounding-polygon-to-a-changeset-before-applying-it)

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
<span id="post-32514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32514-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've got a copy of planet.osm.pbf and a subsection op_area.osm (bounded by bounds.poly) which covers several US states.</p>
<p>I've also set up a way to get the planet.osm diffs each week (rssdownloader + rtorrent + <a href="http://osm-torrent.torres.voyager.hr/files/rss.xml,">http://osm-torrent.torres.voyager.hr/files/rss.xml,</a> for the curious), and it's trivial to automatically apply the diff to planet.osm.pbf and write out an updated version. Then I can clip the planet whichever way I want, and write a new op_area.osm.</p>
<p>The problem is, clipping the planet after applying a changeset takes ~6 hours with my current hardware. Is it possible to apply the planet-based diffs to op_area.osm using osmosis (or some other tool) without needing that intermediate step? I couldn't find any pipeline items that can take a change stream and apply bounds.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-bounding-polygon" rel="tag" title="see questions tagged &#39;bounding-polygon&#39;">bounding-polygon</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '14, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/3199e242d0eeb4a0be104026c3a34c75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BarqsDew&#39;s gravatar image" />
<p><span>BarqsDew</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BarqsDew has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Apr '14, 15:23</strong> </span></p>
</div>
</div>
<div id="comments-container-32514" class="comments-container">
&#10;</div>
<div id="comment-tools-32514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32514-form-container" class="comment-form-container">
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

<span id="32645"></span>

<div id="answer-container-32645" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32645-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="BarqsDew has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do not clip the planet <em>after</em> applying diff; clip it <em>while</em> doing so. Most of the time spent doing this is very likely the reading and writing of the data. Your toolchain seems esoteric to me; what people would usually do to solve your problem is (all on one line, written here on multiple lines for clarity)</p>
<pre><code>osmosis
   --read-replication-interval
   --read-pbf mylocalregion.osm.pbf
   --apply-diff
   --bp file=bounds.poly
   --write-pbf mylocalregion-new.osm.pbf</code></pre>
<p>This is extremely unlikely to take six hours even on small hardware! Working with .osm.pbf files (and not with .osm.bz2 files or plain .osm files) is essential here for speed; if your CPU is particularly weak then adding "compress=none" to the <code>write-pbf</code> task could also improve things.</p>
<p>Before you can run Osmosis in the above fashion you will have to initialize the replication loading (<code>--rrii</code>, and modify configuration.txt if you want hourly or daily updates). You can of course download the diffs your way too and then replace the <code>--read-replication-interval</code> with a <code>--read-xml-change myfile.osc</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '14, 23:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-32645" class="comments-container">
&#10;</div>
<div id="comment-tools-32645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32645-form-container" class="comment-form-container">
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

