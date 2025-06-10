+++
type = "question"
title = "Merge towerblocks to one building with n housenumbers"
description = '''Hi there, I noticed that users have splittet a lot of towerblocks / Plattenbau buildings into small buildings for each part / stairwell. After discussion, I would like to merge the building shape into a single building way, that contains indipendend nodes per housenumber.   But I know only a manual ...'''
date = "2019-07-12T18:17:00Z"
lastmod = "2019-07-12T20:34:00Z"
weight = 70008
keywords = [ "josm", "buildings", "quality_assurance", "housenumbers" ]
aliases = [ "/questions/70008" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Merge towerblocks to one building with n housenumbers](/questions/70008/merge-towerblocks-to-one-building-with-n-housenumbers)

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
<span id="post-70008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70008-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there, I noticed that users have splittet a lot of towerblocks / Plattenbau buildings into small buildings for each part / stairwell. After discussion, I would like to merge the building shape into a single building way, that contains indipendend nodes per housenumber.</p>
<p><img src="https://help.openstreetmap.org/upfiles/josm_wohnblock_gesplittet_Z3jaKHk.jpg" alt="Small separated buildings form a building block, which is just wrong" /></p>
<p><img src="https://help.openstreetmap.org/upfiles/josm_wohnblock.jpg" alt="Improved version, a merged building (block) that contains multiple housenumbers per entrance" /></p>
<p>But I know only a manual way using JOSM to extract and cleanup the infos (add nodes, copy &amp; paste content of each building part, remove remaining tags, merge parts to main building). Anybody an idea to speedup this process? building-tools addon just offer another splitup, but not a reunion :-(</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-quality_assurance" rel="tag" title="see questions tagged &#39;quality_assurance&#39;">quality_assurance</span> <span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '19, 18:17</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</img>
</div>
</div>
<div id="comments-container-70008" class="comments-container">
&#10;</div>
<div id="comment-tools-70008" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70008-form-container" class="comment-form-container">
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

<span id="70009"></span>

<div id="answer-container-70009" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70009-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While I'm not convinced this is a good idea (are you sure these don't outline separate residences?), I do have a method that should work:</p>
<ol>
<li>Select a all of the nodes along one side of the building except the last, and copy-paste them offset so that you have nodes roughly where you want them (or create them another way).</li>
<li>Use the <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Conflation">conflate plugin</a> with the "replace geometry" box un-ticked to copy all tags from the surrounding ways to the destination nodes (full instructions in wiki)</li>
<li>Select the destination nodes and delete the irrelevant tags</li>
<li>Select the outline ways and <em>Join Overlapping Areas</em> (SHIFT+J), selecting "<strong>none</strong>" for the conflict resolution on the address tags.</li>
<li>Use the <em>Simplify Way</em> (SHIFT+Y) command to delete midpoint nodes (you may need to tighten the sensitivity)</li>
<li>Remove the irrelevant tags from the outline way. (For those not done as a part of step 4).</li>
<li>Modify the building tags on the outline way to reflect the fact that they are <a href="https://wiki.openstreetmap.org/wiki/Tag:building%3Dterrace">building=terrace</a> or <a href="https://wiki.openstreetmap.org/wiki/Tag:building%3Dapartments">apartments</a> as appropriate.</li>
<li>Unless specifically against local practice it may be useful to place the new address nodes joined to the new way and tag them as <a href="https://wiki.openstreetmap.org/wiki/Key:entrance">entrances</a> if you know where the doors are.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '19, 20:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jul '19, 20:37</strong> </span></p>
</div>
</div>
<div id="comments-container-70009" class="comments-container">
<span id="70010"></span>
<div id="comment-70010" class="comment">
<div id="post-70010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that in an area / development where you think several streets worth of addresses are misrepresented, the conflate plugin and join overlapping areas tool can both operate over several terraces at once so this isn't necessarily as long as it seems.</p>
<p>For a one off, it might be quicker to use the auto increment function of the address preset as on the new address nodes.</p>
</div>
<div id="comment-70010-info" class="comment-info">
<span class="comment-age">(12 Jul '19, 20:34)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-70009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70009-form-container" class="comment-form-container">
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

