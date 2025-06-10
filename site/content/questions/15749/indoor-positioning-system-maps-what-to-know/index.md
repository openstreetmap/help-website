+++
type = "question"
title = "Indoor positioning system maps , what to know ?"
description = '''Hi everyone , I&#x27;m developing an indoor positioning system for my college as an Android app without using GPS or wifi (just accelerometer &amp;amp; compass) , I&#x27;m really new to this but I started by trying to figure out how to generate a map for the building. I began by understanding the concepts of OSM ...'''
date = "2012-09-02T13:19:00Z"
lastmod = "2020-04-28T10:36:00Z"
weight = 15749
keywords = [ "josm", "android", "indoor" ]
aliases = [ "/questions/15749" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Indoor positioning system maps , what to know ?](/questions/15749/indoor-positioning-system-maps-what-to-know)

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
<span id="post-15749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15749-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone , I'm developing an indoor positioning system for my college as an Android app without using GPS or wifi (just accelerometer &amp; compass) , I'm really new to this but I started by trying to figure out how to generate a map for the building. I began by understanding the concepts of OSM (nodes, routes , closed ways , ect ,ect ..). Having finished the basic concepts of OSM , mapping is still kind of vague. I heard words like "tiles", "slippy tiles" , "rendering" , "vector data map" , so I'm little confused. So , what should be done after generating the .xml file using JOSM representing my map and how to use it ? If someone could give me some advise or some steps/terms that I should know , then I would be greatful.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '12, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/fc2d98d9a9bd0bd68e5fc9f2804d558b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aur&#39;s gravatar image" />
<p><span>aur</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aur has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15749" class="comments-container">
&#10;</div>
<div id="comment-tools-15749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15749-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="15755"></span>

<div id="answer-container-15755" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15755-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aur has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming that you are able to determine accurate position within the building based on accelerometer and compass:</p>
<p>What you have in josm is map data (vector). By rendering it becomes raster map (picture). For practical reasons the big map is split in multiple smaller pictures (tiles). Slippy tiles would mean that you can move the map without reloading all the tiles. (easier, way more storage space, no routing) Alternatively you could do the rendering on the fly directly from vector data (not that xml, some transformation needed). This would be vector map. (more CPU intensive, less storage, more flexible).</p>
<p>There are two options you can choose:<br />
1. map and actual position are displayed, user is expected to find his way based on this. 2. nr.1 + user is given directions to reach the destination</p>
<p>For option 1 you would just display correctly aligned raster tiles and some mark for current position. If it is only limited to your college, you could use Maperitive to do the rendering and only concentrate on determining the position and displaying correct pieces of map around it.</p>
<p>Option 2 is not so easy to be described here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Sep '12, 00:43</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-15755" class="comments-container">
<span id="15757"></span>
<div id="comment-15757" class="comment">
<div id="post-15757-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>pretty nice explanation .. also I found a related article : <a href="http://goo.gl/a4WnY">http://goo.gl/a4WnY</a> . we're trying to achieve sth like FootPath project : <a href="http://goo.gl/li2Fh">http://goo.gl/li2Fh</a> so I think we would choose option 2 , just to make sure that I understood right : we should convert the generated .osm file into a vector map (for less storage) , and process that map according to the project ? any correction or additional info would be great</p>
</div>
<div id="comment-15757-info" class="comment-info">
<span class="comment-age">(03 Sep '12, 06:03)</span> <span class="comment-user userinfo">aur</span>
</div>
</div>
<span id="15759"></span>
<div id="comment-15759" class="comment">
<div id="post-15759-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the building as a lot on steel or high current cables the compass in the smart phone or will be affected.</p>
</div>
<div id="comment-15759-info" class="comment-info">
<span class="comment-age">(03 Sep '12, 12:16)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="15762"></span>
<div id="comment-15762" class="comment">
<div id="post-15762-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@andy mackey</span> this is a considerable issue :) but right now we're trying to figure out how could we do the mapping right</p>
</div>
<div id="comment-15762-info" class="comment-info">
<span class="comment-age">(03 Sep '12, 13:25)</span> <span class="comment-user userinfo">aur</span>
</div>
</div>
</div>
<div id="comment-tools-15755" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15755-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74440"></span>

<div id="answer-container-74440" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74440-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-74440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes sure, OSM is the best way to learn to make a map for indoor positioning projects.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '20, 10:36</strong></p>
<img src="https://secure.gravatar.com/avatar/d65bf3b998394330195797de81ff2de4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smith%20Hennry&#39;s gravatar image" />
<p><span>Smith Hennry</span><br />
<span class="score" title="-20 reputation points">-20</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smith Hennry has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74440" class="comments-container">
&#10;</div>
<div id="comment-tools-74440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74440-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74033"></span>

<div id="answer-container-74033" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74033-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-74033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The very appreciating project, best of luck for your project.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '20, 06:06</strong></p>
<img src="https://secure.gravatar.com/avatar/d65bf3b998394330195797de81ff2de4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smith%20Hennry&#39;s gravatar image" />
<p><span>Smith Hennry</span><br />
<span class="score" title="-20 reputation points">-20</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smith Hennry has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74033" class="comments-container">
&#10;</div>
<div id="comment-tools-74033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74033-form-container" class="comment-form-container">
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

