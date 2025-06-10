+++
type = "question"
title = "Lake Michigan disappeared from OpenStreetMap...how long until this is corrected?"
description = '''On several zoom levels (but not all zoom levels), Lake Michigan (of the Great Lakes in USA and Canada) is painted with the typical color of land rather than water. Perhaps it has not &quot;disappeared&quot;, but incorrect colors are being applied on tile servers. I checked from two different computers, so I&#x27;m...'''
date = "2019-03-30T19:13:00Z"
lastmod = "2019-04-01T16:08:00Z"
weight = 68553
keywords = [ "incorrect", "tileserver" ]
aliases = [ "/questions/68553" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Lake Michigan disappeared from OpenStreetMap...how long until this is corrected?](/questions/68553/lake-michigan-disappeared-from-openstreetmaphow-long-until-this-is-corrected)

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
<span id="post-68553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68553-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>On several zoom levels (but not all zoom levels), Lake Michigan (of the Great Lakes in USA and Canada) is painted with the typical color of land rather than water. Perhaps it has not "disappeared", but incorrect colors are being applied on tile servers. I checked from two different computers, so I'm fairly sure the problem is coming from tile servers. I suppose something has gone wrong with the tile data generation, maintenance or bounding. How much time does it typically take for a very apparent error like this to be corrected? Is it possible for me or any regular OpenStreetMap user to make such a correction? Does everyone see this same problem and what might be the cause? I was thinking perhaps the polygon that defines the lake's boundary is broken somehow.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-incorrect" rel="tag" title="see questions tagged &#39;incorrect&#39;">incorrect</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Mar '19, 19:13</strong></p>
<img src="https://secure.gravatar.com/avatar/ce059a30f2c246deb88c872350584d50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tim%20D&#39;s gravatar image" />
<p><span>Tim D</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tim D has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68553" class="comments-container">
<span id="68561"></span>
<div id="comment-68561" class="comment">
<div id="post-68561-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, something went wrong in this map layer <a href="https://osm.org/go/cArvf?layers=H">https://osm.org/go/cArvf?layers=H</a> while in the others the lakes are rendered properly. The link indicates that probably the vector tiling of some zoom levels failed. You know, the vector tiling is much, much more complex than the raster tiling and it is easier to fail than to make it correct. Anyway, the source data is correct as you can see here <a href="https://drive.google.com/file/d/1eoogr4vKpvytX63qSRPdww6B0A-YaZm2/view?usp=sharing.">https://drive.google.com/file/d/1eoogr4vKpvytX63qSRPdww6B0A-YaZm2/view?usp=sharing.</a> My suggestion is, do not worry. The autors of this layer certainly see the problem and will correct it shortly.</p>
</div>
<div id="comment-68561-info" class="comment-info">
<span class="comment-age">(31 Mar '19, 07:54)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
</div>
<div id="comment-tools-68553" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68553-form-container" class="comment-form-container">
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

<span id="68556"></span>

<div id="answer-container-68556" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68556-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tim D has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The reason for the problem you are describing is almost always, as you say, a problem in the polygon that describes the lake, here: <a href="https://www.openstreetmap.org/relation/1205149">https://www.openstreetmap.org/relation/1205149</a></p>
<p>The polygon currently looks all right. Among the tools you can use to check is the "OSM inspector" (<a href="http://tools.geofabrik.de/osmi/?view=areas&amp;lon=-86.83492&amp;lat=43.58693&amp;zoom=8)">http://tools.geofabrik.de/osmi/?view=areas&amp;lon=-86.83492&amp;lat=43.58693&amp;zoom=8)</a> which would likely show red markers along the lake boundary if something was amiss. Another option is loading the relation in the JOSM editor and running the validator on it. Repairing such problems can be daunting for less-experienced mappers as it is not always obvious where a problem lies.</p>
<p>From where I'm accessing the map, all tiles show Lake Michigan correctly. But different viewers are served by different caches so it is possible that the tile cache you are being served from still has a broken version. It'll straight itself out eventually!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '19, 21:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68556" class="comments-container">
<span id="68582"></span>
<div id="comment-68582" class="comment">
<div id="post-68582-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It looks like someone changed it from a lake to a school back in February, but it only got fixed a few days ago <a href="https://osmlab.github.io/osm-deep-history/#/relation/1205149.">https://osmlab.github.io/osm-deep-history/#/relation/1205149.</a> The Great Lakes shorelines have always been a bit complicated in terms of rendering processing, and I'm not sure that every map shown on the main OSM page uses the same techniques.</p>
</div>
<div id="comment-68582-info" class="comment-info">
<span class="comment-age">(01 Apr '19, 16:08)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68556" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68556-form-container" class="comment-form-container">
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

