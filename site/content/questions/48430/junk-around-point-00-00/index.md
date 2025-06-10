+++
type = "question"
title = "Junk around point 0.0 0.0"
description = '''There is some random stuff/junk around point 0.0 0.0 (see here). It&#x27;s not visible in all maps, but it is in the Transport map. I can&#x27;t query it though, and when starting to edit with ID it disappears when I zoom in far enough to be able to edit at all.'''
date = "2016-03-01T14:27:00Z"
lastmod = "2016-03-01T14:50:00Z"
weight = 48430
keywords = [ "junk", "null" ]
aliases = [ "/questions/48430" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Junk around point 0.0 0.0](/questions/48430/junk-around-point-00-00)

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
<span id="post-48430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48430-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is some random stuff/junk around point 0.0 0.0 (see <a href="https://www.openstreetmap.org/query?lat=0.0060&amp;lon=0.0185#map=15/0.0000/0.0000&amp;layers=T">here</a>). It's not visible in all maps, but it is in the Transport map. I can't query it though, and when starting to edit with ID it disappears when I zoom in far enough to be able to edit at all.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-junk" rel="tag" title="see questions tagged &#39;junk&#39;">junk</span> <span class="post-tag tag-link-null" rel="tag" title="see questions tagged &#39;null&#39;">null</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Mar '16, 14:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e9667ab36399d3f198751e097a2c1b50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mennoowh&#39;s gravatar image" />
<p><span>mennoowh</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mennoowh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48430" class="comments-container">
<span id="48432"></span>
<div id="comment-48432" class="comment">
<div id="post-48432-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Btw: a good tool to check for some types of the <code>null</code> junk (long ways etc.) is the OSMi Geometry view: <a href="http://tools.geofabrik.de/osmi/?view=geometry&amp;lon=-2.99121&amp;lat=-1.47859&amp;zoom=5">http://tools.geofabrik.de/osmi/?view=geometry&amp;lon=-2.99121&amp;lat=-1.47859&amp;zoom=5</a></p>
</div>
<div id="comment-48432-info" class="comment-info">
<span class="comment-age">(01 Mar '16, 14:50)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
</div>
<div id="comment-tools-48430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48430-form-container" class="comment-form-container">
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

<span id="48431"></span>

<div id="answer-container-48431" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48431-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The fact that it shows in the Transport Map probably means that this tiles just hadn't updated at the time that you looked at them. They now have, and the "junk" has mostly gone.</p>
<p>The remaining items there are <a href="https://www.openstreetmap.org/node/3815077900">a buoy</a> (which apparently does exist and even has its own <a href="http://www.ndbc.noaa.gov/station_page.php?station=13010">website</a>), and a <a href="https://www.openstreetmap.org/way/400450050">line for the equator</a> which is of questionable value. I asked about another of that user's "odd lines" <a href="https://www.openstreetmap.org/changeset/37484390">a day ago</a>, but haven't had a reply yet.</p>
<p>Stuff gets added accidentally at "null island" (latitude 0, longitude 0) quite regularly - usually JOSM users getting their maths wrong with imports. Several people (including me) do regularly clean it up - if you look at history in that area you'll see <a href="https://www.openstreetmap.org/changeset/36994453">this changeset</a>, which does exactly that. There's other questionable stuff around the place - I asked about <a href="https://www.openstreetmap.org/way/388953305#map=3/-11.18/-20.57">this well</a> a few days ago. If you try exploring with JOSM and Overpass I'm sure there's more to find!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '16, 14:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-48431" class="comments-container">
&#10;</div>
<div id="comment-tools-48431" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48431-form-container" class="comment-form-container">
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

