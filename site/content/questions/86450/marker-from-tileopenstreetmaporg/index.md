+++
type = "question"
title = "marker from tile.openstreetmap.org"
description = '''I&#x27;m using the Kartographer add-on for MediaWiki. It does not display markers. The address to the marker is: https://tile.openstreetmap.org/v4/marker/pin-s+7e7e7e.png Anyone know why this isn&#x27;t working?'''
date = "2023-01-07T18:04:00Z"
lastmod = "2023-04-09T10:01:00Z"
weight = 86450
keywords = [ "marker", "tiles" ]
aliases = [ "/questions/86450" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [marker from tile.openstreetmap.org](/questions/86450/marker-from-tileopenstreetmaporg)

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
<span id="post-86450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86450-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using the Kartographer add-on for MediaWiki. It does not display markers. The address to the marker is: <a href="https://tile.openstreetmap.org/v4/marker/pin-s+7e7e7e.png">https://tile.openstreetmap.org/v4/marker/pin-s+7e7e7e.png</a></p>
<p>Anyone know why this isn't working?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jan '23, 18:04</strong></p>
<img src="https://secure.gravatar.com/avatar/f4bb43f992c61a4ac04605dabcf9fd37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danielgolub&#39;s gravatar image" />
<p><span>danielgolub</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danielgolub has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86450" class="comments-container">
<span id="87086"></span>
<div id="comment-87086" class="comment">
<div id="post-87086-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello, I have the same problem. I'm using Kartographer in version 1.39. On the map i only see a border but without marker. <a href="https://help.openstreetmap.org/users/22556/danielgolub">@danielgolub</a>: Have you already fixed this problem? Maybe you or anybody else can help me fixing this problem...</p>
</div>
<div id="comment-87086-info" class="comment-info">
<span class="comment-age">(09 Apr '23, 00:23)</span> <span class="comment-user userinfo">uli_h</span>
</div>
</div>
</div>
<div id="comment-tools-86450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86450-form-container" class="comment-form-container">
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

<span id="87089"></span>

<div id="answer-container-87089" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87089-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These marker urls are wrong. It does seem as if Kartographer is using the tile host and adds the path /v4/marker/....png. But those markers only exist on maps.wikimedia.org. So if you use maps.wikimedia.org, those marker urls should work but not with a different tile host.</p>
<p>This is nothing for OpenStreetMap to do but a problem with the code of Kartographer (or your usage of Kartographer).</p>
<p>At the Kartographer help sections it says:</p>
<pre><code>$wgKartographerSimpleStyleMarkers   true
&#10;    Use an api to generate markers using the simplestyle-spec for features. Should be set to false for most applications outside WMF. Otherwise images of markers are assumed to be hosted on the map server.</code></pre>
<p>You should set this to false if you use Kartographer outside of Wikipedia.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '23, 10:01</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-87089" class="comments-container">
&#10;</div>
<div id="comment-tools-87089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87089-form-container" class="comment-form-container">
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

