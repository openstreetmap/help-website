+++
type = "question"
title = "Visualize differences between two osm files (.osc files)"
description = '''Is there a way to visualize (say QGIS) the difference between two versions of OSM data? I did a couple test edits in JOSM by removing/adding turn restrictions and deleting roads for a dummy training dataset. Thru Osmosis, I created an osc file which is the diff between original osm and the version t...'''
date = "2018-09-20T00:14:00Z"
lastmod = "2018-09-20T08:19:00Z"
weight = 65984
keywords = [ "diff", ".osc", "osmosis", "visualization" ]
aliases = [ "/questions/65984" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Visualize differences between two osm files (.osc files)](/questions/65984/visualize-differences-between-two-osm-files-osc-files)

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
<span id="post-65984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65984-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to visualize (say QGIS) the difference between two versions of OSM data? I did a couple test edits in JOSM by removing/adding turn restrictions and deleting roads for a dummy training dataset. Thru Osmosis, I created an osc file which is the diff between original osm and the version that I manipulated. I can see the xml info for this file but how do I "see" the data (roads, relationships, nodes, etc)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-.osc" rel="tag" title="see questions tagged &#39;.osc&#39;">.osc</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-visualization" rel="tag" title="see questions tagged &#39;visualization&#39;">visualization</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Sep '18, 00:14</strong></p>
<img src="https://secure.gravatar.com/avatar/146f9c2b954b5bbe3c30ae5f4be407e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markzawi&#39;s gravatar image" />
<p><span>markzawi</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markzawi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65984" class="comments-container">
&#10;</div>
<div id="comment-tools-65984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65984-form-container" class="comment-form-container">
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

<span id="65987"></span>

<div id="answer-container-65987" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65987-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-65987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This will not work with .osc fiels as they only contain the changes to the data, not the objects that have been affected by the changes (which for example means if you move a way node you will only see a position change in the node, and no change to the way it is a member of).</p>
<p>What you probably should be looking at are <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Augmented_Diffs">overpass augmented diffs</a> and <a href="https://wiki.openstreetmap.org/wiki/Achavi">Achavi</a> (a viewer for them).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '18, 08:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Sep '18, 08:21</strong> </span></p>
</div>
</div>
<div id="comments-container-65987" class="comments-container">
&#10;</div>
<div id="comment-tools-65987" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65987-form-container" class="comment-form-container">
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

