+++
type = "question"
title = "I see some nodes on the map, but I can&#x27;t find them in Planet.osm. Why?"
description = '''I want to get some node (for example, schools, kindergartens) from Planet.osm (http://wiki.openstreetmap.org/wiki/Planet.osm).  I can see necessary objects on the map http://www.openstreetmap.org/?lat=59.87326&amp;amp;lon=30.3124&amp;amp;zoom=17&amp;amp;layers=M (school #509, kindergarten #108 and kindergarten ...'''
date = "2011-01-28T09:58:00Z"
lastmod = "2011-01-28T10:45:00Z"
weight = 2505
keywords = [ "openstreetmap", "xml", "parsing" ]
aliases = [ "/questions/2505" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [I see some nodes on the map, but I can't find them in Planet.osm. Why?](/questions/2505/i-see-some-nodes-on-the-map-but-i-cant-find-them-in-planetosm-why)

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
<span id="post-2505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2505-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get some node (for example, schools, kindergartens) from Planet.osm (<a href="http://wiki.openstreetmap.org/wiki/Planet.osm">http://wiki.openstreetmap.org/wiki/Planet.osm</a>). I can see necessary objects on the map <a href="http://www.openstreetmap.org/?lat=59.87326&amp;lon=30.3124&amp;zoom=17&amp;layers=M">http://www.openstreetmap.org/?lat=59.87326&amp;lon=30.3124&amp;zoom=17&amp;layers=M</a> (school #509, kindergarten #108 and kindergarten #390). But I can't find them in the XML file! I got all nodes, which have Latitude &gt; 59.86 and Latitude &lt; 59.88 and Longitude &gt; 30.31 and Longitude &lt; 30.32 (this part of map). I've got 42 objects with any tags, but I couldn't find school #509, kindergarten #108 and kindergartens #390. Why?</p>
<p>Are the information on the map and in the XML file quite different? Why I can't find map's object in the XML file?</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '11, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/0a4b8ed0e85849e6ab3d37ca51c94374?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yan%20Fisher&#39;s gravatar image" />
<p><span>Yan Fisher</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yan Fisher has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2505" class="comments-container">
&#10;</div>
<div id="comment-tools-2505" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2505-form-container" class="comment-form-container">
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

<span id="2508"></span>

<div id="answer-container-2508" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2508-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2508-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2508-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Yan Fisher has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Yan,</p>
<p>I think the problem is that you are searching for nodes, when what you are looking for are drawn as ways (e.g. <a href="http://www.openstreetmap.org/browse/way/47661121"></a><a href="http://www.openstreetmap.org/browse/way/47661121"></a><a href="http://www.openstreetmap.org/browse/way/47661121">http://www.openstreetmap.org/browse/way/47661121</a>)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '11, 10:38</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-2508" class="comments-container">
<span id="2510"></span>
<div id="comment-2510" class="comment">
<div id="post-2510-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! I must look for both, the nodes and the ways.</p>
</div>
<div id="comment-2510-info" class="comment-info">
<span class="comment-age">(28 Jan '11, 10:45)</span> <span class="comment-user userinfo">Yan Fisher</span>
</div>
</div>
</div>
<div id="comment-tools-2508" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2508-form-container" class="comment-form-container">
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

