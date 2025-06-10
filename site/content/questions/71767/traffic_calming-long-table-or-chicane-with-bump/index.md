+++
type = "question"
title = "[traffic_calming] long table or chicane with bump"
description = '''Hi, In my area I have a lot of weird traffic bump table chicane... and sometimes there are very long and combine multiple solutions like chicane with bump and crossing for pedestrians. What&#x27;s the best way to draw them ? For now I add 2 points (set to &quot;speed bump&quot; on the object type) on the road line...'''
date = "2019-11-21T23:25:00Z"
lastmod = "2019-11-23T10:05:00Z"
weight = 71767
keywords = [ "table", "traffic_calming", "long-path" ]
aliases = [ "/questions/71767" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[traffic_calming\] long table or chicane with bump](/questions/71767/traffic_calming-long-table-or-chicane-with-bump)

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
<span id="post-71767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71767-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>In my area I have a lot of weird traffic bump table chicane... and sometimes there are very long and combine multiple solutions like chicane with bump and crossing for pedestrians. What's the best way to draw them ?</p>
<p>For now I add 2 points (set to "speed bump" on the object type) on the road line and set this section to "speed bump/speed reducer" and modify the speed to 30km/h. But I saw that some already existed with just a point in the middle set with "speed bump". I have the feeling that this is not very precise :/</p>
<p>Same type of question; when you specify chicane on a road, do you add attributes or change the object type to chicane ?</p>
<p>So what's your opinion guy ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-table" rel="tag" title="see questions tagged &#39;table&#39;">table</span> <span class="post-tag tag-link-traffic_calming" rel="tag" title="see questions tagged &#39;traffic_calming&#39;">traffic_calming</span> <span class="post-tag tag-link-long-path" rel="tag" title="see questions tagged &#39;long-path&#39;">long-path</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '19, 23:25</strong></p>
<img src="https://secure.gravatar.com/avatar/8ddbdd9e0573ad084e34ada81c6a793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Winultimate&#39;s gravatar image" />
<p><span>Winultimate</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Winultimate has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '19, 23:37</strong> </span></p>
</div>
</div>
<div id="comments-container-71767" class="comments-container">
&#10;</div>
<div id="comment-tools-71767" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71767-form-container" class="comment-form-container">
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

<span id="71772"></span>

<div id="answer-container-71772" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71772-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-71772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well in principle these are traffic_calming table see <a href="https://wiki.openstreetmap.org/wiki/Key:traffic_calming">https://wiki.openstreetmap.org/wiki/Key:traffic_calming</a></p>
<p>If you don't want to simply add a point on the road (part of the actual OSM way) then you could split the way at the start and end of the table and simply add traffic_calming=table to the segment (no guarantees that there are currently routers that would use it though).</p>
<p>Please don't add non-existing speed limits to the objects though.</p>
<p>As to a chicane, except if very long, as a tendency I would add it as a point on the road.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '19, 11:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Nov '19, 12:37</strong> </span></p>
</div>
</div>
<div id="comments-container-71772" class="comments-container">
<span id="71774"></span>
<div id="comment-71774" class="comment">
<div id="post-71774-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok so both is alright :)</p>
<p>Don't worry, in France all traffic calming come with speed reduction (30km/h) so in theory all maps should indicate a section at 30km/h around it. Unless OSM calculs this automaticaly ?</p>
<p>Ok got it for the chicanes.</p>
</div>
<div id="comment-71774-info" class="comment-info">
<span class="comment-age">(22 Nov '19, 17:40)</span> <span class="comment-user userinfo">Winultimate</span>
</div>
</div>
<span id="71781"></span>
<div id="comment-71781" class="comment">
<div id="post-71781-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In general, OSM doesn't map traffic law. There are wiki pages to record the "defaults" per jurisdiction. A note should probably be added to the relevant page about speed limits through traffic calming (if there isn't one already).</p>
</div>
<div id="comment-71781-info" class="comment-info">
<span class="comment-age">(23 Nov '19, 10:05)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-71772" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71772-form-container" class="comment-form-container">
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

