+++
type = "question"
title = "How to create place=island out of natural=coastline in iD?"
description = '''While trying to perform an extract of Caribbean islands in Quick OSM (Overpass API), I discovered that some major islands were left out of my extract. I supposed that the problem was inconsistent tagging.  I&#x27;m a newbie iD editor, but I dove in to try to figure out what&#x27;s going on. I found that islan...'''
date = "2017-04-16T06:15:00Z"
lastmod = "2017-04-16T14:10:00Z"
weight = 55622
keywords = [ "ideditor", "islands", "relations", "multipolygons" ]
aliases = [ "/questions/55622" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to create place=island out of natural=coastline in iD?](/questions/55622/how-to-create-placeisland-out-of-naturalcoastline-in-id)

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
<span id="post-55622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55622-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><img src="https://help.openstreetmap.org/upfiles/Screen_Shot_2017-04-16_at_8.21.48_AM_2YZIzWn.png" alt="alt text" />While trying to perform an extract of Caribbean islands in Quick OSM (Overpass API), I discovered that some major islands were left out of my extract. I supposed that the problem was inconsistent tagging.</p>
<p>I'm a newbie iD editor, but I dove in to try to figure out what's going on. I found that islands that extracted properly have a relation defined between their coastline (line) feature and their island feature, in which the coastline is defined as the "outer" of the island. On the other hand, islands that <em>didn't</em> extract properly had a coastline tag, but no island tag.</p>
<p>My question is how to define the area of an island as an island feature, and how to create the required relation between that and the coastline feature, for the islands that need this. Does a guide or tutorial exist for doing this task in iD? I have looked and haven't been able to find one.</p>
<p>EDIT: I added two images to show what I'm finding. The first shows tags for the coastline of Long Island in The Bahamas, where the coastline is tagged as having a relation with the island. The second is for the coastline of the island of Eleuthera in The Bahamas, where no island tag exists.</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screen_Shot_2017-04-16_at_8.23.57_AM.png" alt="tags for Long Island in The Bahamas, including the island relation" /> Many thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-islands" rel="tag" title="see questions tagged &#39;islands&#39;">islands</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-multipolygons" rel="tag" title="see questions tagged &#39;multipolygons&#39;">multipolygons</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '17, 06:15</strong></p>
<img src="https://secure.gravatar.com/avatar/bdb6a3533bdced106f8edd2c1dcb5495?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abijah&#39;s gravatar image" />
<p><span>abijah</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abijah has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '17, 13:29</strong> </span></p>
</div>
</div>
<div id="comments-container-55622" class="comments-container">
&#10;</div>
<div id="comment-tools-55622" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55622-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="55623"></span>

<div id="answer-container-55623" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55623-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would think that a relation in the sense that osm uses would not be required unless you want to group a number of islands under the same name or the island is very large.<br />
It is likely that many of the Caribbean islands are large enough to need the outer way split into multiple parts and therefore need to be mapped as a multipolygon. e.g. <a href="http://www.openstreetmap.org/relation/4092586">Kerera</a> is a multipolygon with the outer way split into 4 segments and each of the segments (members) are tagged natural=coastline<br />
There is a difference between mapping islands in the sea and islands in lakes and rivers.<br />
Have a look at the <a href="http://wiki.openstreetmap.org/wiki/Tag:place%3Disland">place=island tags</a></p>
<p>Can't help with iD but JOSM seems well suited for multipolygon mapping.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '17, 06:41</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '17, 07:07</strong> </span></p>
</div>
</div>
<div id="comments-container-55623" class="comments-container">
<span id="55625"></span>
<div id="comment-55625" class="comment">
<div id="post-55625-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I added some images to the original post to explain what I'm seeing. How can I use the coastline features to create island features?</p>
</div>
<div id="comment-55625-info" class="comment-info">
<span class="comment-age">(16 Apr '17, 13:31)</span> <span class="comment-user userinfo">abijah</span>
</div>
</div>
</div>
<div id="comment-tools-55623" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55623-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55629"></span>

<div id="answer-container-55629" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55629-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The solution is to create a relation and give it these tags:<br />
- type=multipolygon<br />
- <a href="https://wiki.openstreetmap.org/wiki/Tag:place%3Disland">place=island</a> (or perhaps place=islet)</p>
<p>Then add all the parts of coastline that makes up the coastline for the island.</p>
<p>I found that to do this in ID was not so easy so the easiest way to do this and my advice to you is to <a href="https://josm.openstreetmap.de/">install JOSM</a>, have a quick view at this <a href="https://www.youtube.com/watch?v=8gH_fu2vICk">instructional movie</a> for how to do this. It's in Russian and quite dated, but he presses the same buttons and they still look the same.</p>
<p>Or, a quick fix, if you don't want to figure it out. Put a note on the map explaining what's wrong and someone will/might fix it.</p>
<p>Edit: Some examples of <a href="http://www.openstreetmap.org/relation/5847770">a medium island</a> and <a href="http://www.openstreetmap.org/relation/6361027">a large island</a> with lots of ways that form the outer way that makes the coastline of the island.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '17, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '17, 14:16</strong> </span></p>
</div>
</div>
<div id="comments-container-55629" class="comments-container">
&#10;</div>
<div id="comment-tools-55629" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55629-form-container" class="comment-form-container">
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

