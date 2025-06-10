+++
type = "question"
title = "Which possibilities do I have to check relations for errors?"
description = '''Which possibilities do I have to check relations for errors?'''
date = "2010-08-14T11:09:00Z"
lastmod = "2010-08-15T08:03:00Z"
weight = 665
keywords = [ "relation", "analyse", "check", "error" ]
aliases = [ "/questions/665" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Which possibilities do I have to check relations for errors?](/questions/665/which-possibilities-do-i-have-to-check-relations-for-errors)

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
<span id="post-665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-665-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Which possibilities do I have to check <a href="http://wiki.openstreetmap.org/wiki/Relations" title="relations">relations</a> for errors?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-analyse" rel="tag" title="see questions tagged &#39;analyse&#39;">analyse</span> <span class="post-tag tag-link-check" rel="tag" title="see questions tagged &#39;check&#39;">check</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '10, 11:09</strong></p>
<img src="https://secure.gravatar.com/avatar/bc6d0b055d631830f7891d3f89edb66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="katpatuka&#39;s gravatar image" />
<p><span>katpatuka</span><br />
<span class="score" title="1041 reputation points"><span>1.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="katpatuka has 2 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Aug '10, 11:12</strong> </span></p>
</div>
</div>
<div id="comments-container-665" class="comments-container">
&#10;</div>
<div id="comment-tools-665" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-665-form-container" class="comment-form-container">
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

<span id="669"></span>

<div id="answer-container-669" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-669-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Depends what the relation is.</p>
<hr />
<p>If it's a multipolygon, the JOSM validator will handle it. Difficult geometry problems can be sorted out with te <a href="http://tools.geofabrik.de/osmi/debug.html?view=multipolygon&amp;lon=-12.00000&amp;lat=25.00000&amp;zoom=3&amp;overlays=invalid_geometry_hull,duplicate_ways,intersections,intersection_lines,ring_not_closed_hull,ring_not_closed,unconnected_end_nodes,touching_inner_rings_hull,touching_inner_rings,role_mismatch_hull,role_mismatch,duplicate_tags_hull,duplicate_tags,multipolygons_type_is_boundary,type_is_boundary,ways,role_markers,way_end_nodes,way_nodes">OSM Inspector's multipolygon view</a>.</p>
<hr />
<p>If it's a route relation, you can order the elements in JOSM's relation editor and see if they connect, but this only works if the route is the same in both directions. The <span>Relation Analyzer</span> automates this process for a saved relation.</p>
<p>If your route relation uses directional roles (north for ways that carry only northbound traffic, etc.; common in the US but probably not elsewhere), you can use <span>Nakor's tool</span>. I know of no tool that will handle the more common forward/backward roles.</p>
<hr />
<p>If it's a turn restriction, JOSM (with the restriction plugin) will check it. You can also use the <span>Restriction Analyser</span>, which may find errors that JOSM doesn't (and vice versa).</p>
<hr />
<p>There's also <span>Relation Check</span>, which I haven't used.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '10, 14:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0c334b9f230e39c1e73a2b0322a23fb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NE2&#39;s gravatar image" />
<p><span>NE2</span><br />
<span class="score" title="1359 reputation points"><span>1.4k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NE2 has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Aug '10, 18:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-669" class="comments-container">
&#10;</div>
<div id="comment-tools-669" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-669-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="674"></span>

<div id="answer-container-674" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-674-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is also the <strong>Analyseur de Relation</strong> which analyzes relations for gaps and intersections - see <a href="http://analyser.openstreetmap.fr/cgi-bin/index.py">http://analyser.openstreetmap.fr/cgi-bin/index.py</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '10, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/bc6d0b055d631830f7891d3f89edb66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="katpatuka&#39;s gravatar image" />
<p><span>katpatuka</span><br />
<span class="score" title="1041 reputation points"><span>1.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="katpatuka has 2 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-674" class="comments-container">
&#10;</div>
<div id="comment-tools-674" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-674-form-container" class="comment-form-container">
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

