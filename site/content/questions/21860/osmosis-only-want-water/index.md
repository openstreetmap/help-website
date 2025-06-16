+++
type = "question"
title = "Osmosis - Only want water..."
description = '''Greetings, I&#x27;m digging into planet files and creating extracts for the first time, and I&#x27;d like to create a regional extract which contains only water elements - lakes, ponds, rivers, streams, and coastlines... etc.  I&#x27;ve created an Osmosis filter which has a bounding box which works well, as well a...'''
date = "2013-04-25T21:13:00Z"
lastmod = "2013-04-29T21:46:00Z"
weight = 21860
keywords = [ "osmosis" ]
aliases = [ "/questions/21860" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis - Only want water...](/questions/21860/osmosis-only-want-water)

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
<span id="post-21860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21860-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Greetings,</p>
<p>I'm digging into planet files and creating extracts for the first time, and I'd like to create a regional extract which contains <em>only</em> water elements - lakes, ponds, rivers, streams, and coastlines... etc.</p>
<p>I've created an Osmosis filter which has a bounding box which works well, as well as...</p>
<p>--way-key-value keyValueList=natural.water,natural.wetland,natural.coastline,waterway</p>
<p>There are no other filters present... I was <em>expecting</em> to get output which had ONLY those elements above in them. I do get my water data, but in addition I'm getting lots and lots of extraneous nodes. Many match up with roads and intersections, others are power transmission poles, etc.</p>
<p>How can I filter OUT these extra nodes, while keeping in that which is associated with the water items I'm searching for?</p>
<p>Any help is appreciated! -Greg</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '13, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/e795e6d25ba5d6b1f651ba091399c6f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="greggerm&#39;s gravatar image" />
<p><span>greggerm</span><br />
<span class="score" title="45 reputation points">45</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="greggerm has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Apr '13, 21:14</strong> </span></p>
</div>
</div>
<div id="comments-container-21860" class="comments-container">
&#10;</div>
<div id="comment-tools-21860" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21860-form-container" class="comment-form-container">
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

<span id="21911"></span>

<div id="answer-container-21911" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21911-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-21911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Though you seem to have found the solution for your problem I'd like to mention <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfiler</a>. It should do for your problem and as C-program is several times faster than osmosis.</p>
<p>Probably you also want to retrieve just waterways (or what you need) from the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a>. So you'd get only the data you want - no filtering for areas and tags afterwards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '13, 11:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-21911" class="comments-container">
<span id="21977"></span>
<div id="comment-21977" class="comment">
<div id="post-21977-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Malenki - great tips. I've been able to use Overpass to export information directly to JOSM which contains the data I need.</p>
<p>(Ultimately, I'm trying to download all water data into JOSM so I can see what's MISSING, and then draw it in based on a Bing overlay)</p>
<p>Thanks once again - your solution with Overpass is precisely what I needed.</p>
</div>
<div id="comment-21977-info" class="comment-info">
<span class="comment-age">(29 Apr '13, 15:48)</span> <span class="comment-user userinfo">greggerm</span>
</div>
</div>
<span id="21979"></span>
<div id="comment-21979" class="comment">
<div id="post-21979-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Glad I could help. :) It would be nice if you'd mark this question as solved.</p>
</div>
<div id="comment-21979-info" class="comment-info">
<span class="comment-age">(29 Apr '13, 21:46)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
</div>
<div id="comment-tools-21911" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21911-form-container" class="comment-form-container">
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

