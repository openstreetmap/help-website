+++
type = "question"
title = "Merging private data into OSM"
description = '''Hello,  I&#x27;ve just read about possibilities handling OSM data. I know I can do a layer in the javascript renderer to show private data and not mess up with OSM public data. I can also create my own server (It&#x27;s my current approach, just for testing).  But suppose that I have data collected by my user...'''
date = "2013-10-22T15:59:00Z"
lastmod = "2013-10-22T17:13:00Z"
weight = 27409
keywords = [ "merge", "private" ]
aliases = [ "/questions/27409" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Merging private data into OSM](/questions/27409/merging-private-data-into-osm)

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
<span id="post-27409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27409-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I've just read about possibilities handling OSM data. I know I can do a layer in the javascript renderer to show private data and not mess up with OSM public data. I can also create my own server (It's my current approach, just for testing).</p>
<p>But suppose that I have data collected by my users that can be used by the community. Say bar places, or other kind of public information. But this data is not ready for public use so we use it internally.</p>
<p>The best way to build it is to use OSM utils and tools to map to our own server. So it's tightly integrated.</p>
<p>But how do you know what data is edited by your users and what data is public?</p>
<p>How can you do complete separation of postgres data? If you can do this you can generate diffs like OSM planet data by hour/day/whatever and export to a xml file.</p>
<p>This way you can select what's ready and give it to the community.</p>
<p>So at the end. Is there a way to add data to OSM private server that can be separated from OSM public data? (Don't tell me JOSM and offline editing ;-))</p>
<p>Maybe setting up two servers one full of public data and one with private one. And modify OSM tools/server to take all data from public server and after merge from private server before render/answer (nominatim). That way is completly separated.</p>
<p>Is that hard?</p>
<p>Thank you in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-private" rel="tag" title="see questions tagged &#39;private&#39;">private</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '13, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ab874670390cfc1ec08b8e4433446987?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gadLinux&#39;s gravatar image" />
<p><span>gadLinux</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gadLinux has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27409" class="comments-container">
&#10;</div>
<div id="comment-tools-27409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27409-form-container" class="comment-form-container">
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

<span id="27410"></span>

<div id="answer-container-27410" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27410-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do you mean something like <a href="http://www.geofabrik.de/en/projects/separatedata/index.html">this usecase</a>?</p>
<p>Then consult the guys from geofabrik.de or maybe any other "professional" <a href="http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">provider</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '13, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-27410" class="comments-container">
<span id="27412"></span>
<div id="comment-27412" class="comment">
<div id="post-27412-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep! That can be great. This case use should be implemented by default. This way everyone with a private map server can contribute when it's ready to do it.</p>
<p>If you do it in a traditional way (editing directly over postgres) you will miss soon or later updates from public repos because id conflict or something. And you will unable to separate data.</p>
<p>So yes. That's the answer.</p>
</div>
<div id="comment-27412-info" class="comment-info">
<span class="comment-age">(22 Oct '13, 17:13)</span> <span class="comment-user userinfo">gadLinux</span>
</div>
</div>
</div>
<div id="comment-tools-27410" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27410-form-container" class="comment-form-container">
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

