+++
type = "question"
title = "Adding new node (Shift-D) wipes map on JOSM"
description = '''Hello, When I try to add a new node using coordinates (Shift-D command), the rest of the data on the map disappears. The data doesn&#x27;t seem to be deleted because the file still has the same amount of nodes and ways.  This seems to be an interface or display thing? I haven&#x27;t been able to find any post...'''
date = "2019-04-10T19:09:00Z"
lastmod = "2019-04-11T19:16:00Z"
weight = 68751
keywords = [ "node", "josm", "shift-d", "wipe", "map" ]
aliases = [ "/questions/68751" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adding new node (Shift-D) wipes map on JOSM](/questions/68751/adding-new-node-shift-d-wipes-map-on-josm)

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
<span id="post-68751-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68751-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68751-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, When I try to add a new node using coordinates (Shift-D command), the rest of the data on the map disappears.</p>
<p>The data doesn't seem to be deleted because the file still has the same amount of nodes and ways.</p>
<p>This seems to be an interface or display thing? I haven't been able to find any post about it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-shift-d" rel="tag" title="see questions tagged &#39;shift-d&#39;">shift-d</span> <span class="post-tag tag-link-wipe" rel="tag" title="see questions tagged &#39;wipe&#39;">wipe</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '19, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/8386ef7c51e0af20ceed80c7af0a9a31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ymtopcu&#39;s gravatar image" />
<p><span>ymtopcu</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ymtopcu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68751" class="comments-container">
<span id="68755"></span>
<div id="comment-68755" class="comment">
<div id="post-68755-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which JOSM version? I don't experience this issue with the latest josm-tested (14945). Maybe Shift-D toggles your layer visibility?</p>
</div>
<div id="comment-68755-info" class="comment-info">
<span class="comment-age">(11 Apr '19, 08:54)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="68758"></span>
<div id="comment-68758" class="comment">
<div id="post-68758-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>To rule out the obvious: Are you sure you are adding the point at the correct coordinate and it is not just JOSM recentering the view on the new point's location away from the previously downloaded data? If you scroll out, does the other data re-appear somewhere?</p>
</div>
<div id="comment-68758-info" class="comment-info">
<span class="comment-age">(11 Apr '19, 09:36)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="68762"></span>
<div id="comment-68762" class="comment">
<div id="post-68762-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for your replies.</p>
<p>I've been playing around with different layers to see if adding a node on a new layer would make it so the rest of the map is still visible. Unfortunately no: the rest of the map still disappears, even if the new node I am adding is on a layer entirely by itself.</p>
<p>Its interesting you ask if other data is visible. When I zoom out, oddly enough, just one random node is visible but the rest of the map is not (so I end up seeing this one random node from the old map, along with the new one I am trying to add)</p>
<p>This one random node was one I added some time ago: its position is accurate to where the new node I am trying to add would be.</p>
<p>The camera does recenter when I add a node of course, but when I zoom out, I only see this one particular node remaining from the map. The rest of it is missing.</p>
<p>I am using version 14824</p>
</div>
<div id="comment-68762-info" class="comment-info">
<span class="comment-age">(11 Apr '19, 17:27)</span> <span class="comment-user userinfo">ymtopcu</span>
</div>
</div>
<span id="68764"></span>
<div id="comment-68764" class="comment">
<div id="post-68764-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16524/ymtopcu">@ymtopcu</a>: Please try zooming in on that random old node. When you're zoomed out far enough, even several square kilometers' worth of map data will shrink into a single point and look exactly like a single node.</p>
<p>If that doesn't help, press Ctrl+A to select all elements no matter where they are. (Only works in the current layer though!) What is the result of that?</p>
</div>
<div id="comment-68764-info" class="comment-info">
<span class="comment-age">(11 Apr '19, 19:16)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-68751" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68751-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

