+++
type = "question"
title = "Download OpenStreetMap till Zoom Level"
description = '''Hello guys! I am trying to download the OpenStreetMap until zoom level x, but I could only find how to download the .osm archive for the full zoom level, compressed. Even compressed it has over 100gigs of memory. Where can I download it until zoom level 10/11/12 or something along these lines. I`ve ...'''
date = "2023-04-06T11:44:00Z"
lastmod = "2023-04-06T12:19:00Z"
weight = 87068
keywords = [ "download", "zoomlevel", "zoom" ]
aliases = [ "/questions/87068" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Download OpenStreetMap till Zoom Level](/questions/87068/download-openstreetmap-till-zoom-level)

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
<span id="post-87068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87068-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello guys!</p>
<p>I am trying to download the OpenStreetMap until zoom level x, but I could only find how to download the .osm archive for the full zoom level, compressed. Even compressed it has over 100gigs of memory. Where can I download it until zoom level 10/11/12 or something along these lines.</p>
<p>I`ve tried various tools such as Osmium and Osmosis, but they all require to decompress the file, which is a no-go as it has over 1TB of memory.</p>
<p>I need the map downloaded as I am using it in an offline environment.</p>
<p>Can you guys give me a suggestion?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Apr '23, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/30e34f2456d0c417d6c6f231103afa14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vlad-Marin&#39;s gravatar image" />
<p><span>Vlad-Marin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vlad-Marin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87068" class="comments-container">
&#10;</div>
<div id="comment-tools-87068" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87068-form-container" class="comment-form-container">
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

<span id="87069"></span>

<div id="answer-container-87069" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87069-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>I need the map downloaded as I am using it in an offline environment.</p>
</blockquote>
<p>One way to do this is to <a href="https://switch2osm.org/serving-tiles/">render your own tiles</a> on the fly offline. That way you don't need massive amounts of disk space for tiles containing only sea.</p>
<p>If you want to download tiles from OSM servers you'll need to follow <a href="https://operations.osmfoundation.org/policies/tiles/">this policy</a>. It's possible that you may be able to set up a one-off download process of low-zoom tiles that abides by that.</p>
<p>For the avoidance of doubt, OpenStreetMap IS the data, not one particular rendering of it. You may have only seen one of the six layers at openstreetmap.org, but it's not the only one and is extremely uunlikely to be the best one for your needs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Apr '23, 12:19</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-87069" class="comments-container">
&#10;</div>
<div id="comment-tools-87069" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87069-form-container" class="comment-form-container">
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

