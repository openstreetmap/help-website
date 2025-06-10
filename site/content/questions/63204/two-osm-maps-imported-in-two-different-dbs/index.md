+++
type = "question"
title = "Two OSM maps imported in two different dbs"
description = '''We already filtered amenities and shops from a o5m file and then converted that into a osm file. The next step is importing that to a new db. After that is it possible to have an entry on renderd.conf to look at the new tiles without amenities and shops in other path? Like so /hot/0/0/0.png &amp;lt; til...'''
date = "2018-04-28T17:27:00Z"
lastmod = "2018-05-21T01:06:00Z"
weight = 63204
keywords = [ "postgresql", "renderd", "osm" ]
aliases = [ "/questions/63204" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Two OSM maps imported in two different dbs](/questions/63204/two-osm-maps-imported-in-two-different-dbs)

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
<span id="post-63204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63204-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We already filtered amenities and shops from a o5m file and then converted that into a osm file. The next step is importing that to a new db.</p>
<p>After that is it possible to have an entry on renderd.conf to look at the new tiles without amenities and shops in other path? Like so</p>
<p>/hot/0/0/0.png &lt; tiles with shops and amenities</p>
<p>/custom/0/0/0.png &lt; tiles without shops and amenities</p>
<p>Do we have to make a copy of mapnik.xml pointing to the new db as well?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '18, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/7dc2ca85ad0fdecfb5c66a390b83180a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gfitz&#39;s gravatar image" />
<p><span>gfitz</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gfitz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63204" class="comments-container">
&#10;</div>
<div id="comment-tools-63204" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63204-form-container" class="comment-form-container">
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

<span id="63589"></span>

<div id="answer-container-63589" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63589-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes and yes.</p>
<p>The "ajt" section in <a href="https://github.com/SomeoneElseOSM/mod_tile/blob/switch2osm/renderd.conf">this example</a> is a map style. Just create another section pointing at the other mapnik.xml to create another map style. It would have "URI=/custom/" in your example.</p>
<p>As you've mentioned, you'll need to manually edit either the second mapnik.xml to point at the alternative database, or edit a second map style before creating mapnik.xml from it. I tend to do the former.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '18, 01:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-63589" class="comments-container">
&#10;</div>
<div id="comment-tools-63589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63589-form-container" class="comment-form-container">
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

