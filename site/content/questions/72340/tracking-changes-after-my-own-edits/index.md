+++
type = "question"
title = "Tracking changes after my own edits"
description = '''I&#x27;m new to OSM but really enjoying it, so I asked myself: Is it possible to have a comprehensive list/map to see when changes are made after I made some edits? I know there is an overpass turbo which displays objects which were last changed a certain user, but what about objects changed 2, 3 or more...'''
date = "2020-01-02T19:45:00Z"
lastmod = "2020-01-03T16:54:00Z"
weight = 72340
keywords = [ "changeset", "tracking", "user", "objects", "history" ]
aliases = [ "/questions/72340" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tracking changes after my own edits](/questions/72340/tracking-changes-after-my-own-edits)

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
<span id="post-72340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72340-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSM but really enjoying it, so I asked myself: Is it possible to have a comprehensive list/map to see when changes are made after I made some edits? I know there is an overpass turbo which displays objects which were last changed a certain user, but what about objects changed 2, 3 or more changesets before by a certain user?</p>
<p>I sometimes put a bit of effort into my changes, i. e. making detours from my travels, so I already know what the object looks like, where and how it is located, so it would be good to see what other users think about it, i. e. how they map and change these objects.</p>
<p>The following topic <a href="https://help.openstreetmap.org/questions/33838/monitor-changes-to-specific-feature">https://help.openstreetmap.org/questions/33838/monitor-changes-to-specific-feature</a> goes in that direction. It would mean I need to somehow get a list of all the objects I changed and then load it into this API request - which would result in a rather long query.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-tracking" rel="tag" title="see questions tagged &#39;tracking&#39;">tracking</span> <span class="post-tag tag-link-user" rel="tag" title="see questions tagged &#39;user&#39;">user</span> <span class="post-tag tag-link-objects" rel="tag" title="see questions tagged &#39;objects&#39;">objects</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jan '20, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/748e67664207ccf32cd4871e550b9b0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peppone84&#39;s gravatar image" />
<p><span>peppone84</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peppone84 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72340" class="comments-container">
&#10;</div>
<div id="comment-tools-72340" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72340-form-container" class="comment-form-container">
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

<span id="72343"></span>

<div id="answer-container-72343" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72343-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-72343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To add to the complexity that has already been pointed out in the answers to your linked question: OSM objects can not only be modified in position and tagging but also be split and merged. Say you created a road. After you someone splits the road into two sections. Only one of those sections will retain the history and information that you created it with. The other section will be created as a new object, only by comparing the nodes is it possible to link that new object to your original one.</p>
<p>Thus it is easier to monitor a certain area with tools like <a href="https://simon04.dev.openstreetmap.org/whodidit/">whodidit</a> than individual objects. But there are also limitations as that service only registers changes to nodes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '20, 23:34</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '20, 13:12</strong> </span></p>
</div>
</div>
<div id="comments-container-72343" class="comments-container">
<span id="72348"></span>
<div id="comment-72348" class="comment">
<div id="post-72348-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Tzorn, thank you for your answer, although I won't give up on it yet. :)</p>
<p>Yes whodidit I was not using because of the limitations, especially area-wise.</p>
<p>Isn't there a method to search "last editor/user unequal previous specific editor/user xyz"?</p>
</div>
<div id="comment-72348-info" class="comment-info">
<span class="comment-age">(03 Jan '20, 10:20)</span> <span class="comment-user userinfo">peppone84</span>
</div>
</div>
<span id="72350"></span>
<div id="comment-72350" class="comment">
<div id="post-72350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Whodidit is pretty reliable. In my experience it picks up &gt;90% of all changesets. Only changesets which did not modify any node are missed. That's a problem with the underlying data model (only nodes carry location information) and the desire to keep the programming/resources simple. I have to pass on your last question. Surely, there is a method and you could implement it with your own database. But to my knowledge there is no public implementation of such method out there.</p>
</div>
<div id="comment-72350-info" class="comment-info">
<span class="comment-age">(03 Jan '20, 13:11)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="72352"></span>
<div id="comment-72352" class="comment">
<div id="post-72352-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've been using OSMCha for a while, and it works great. You can monitor a specified area and it will show any changesets with a bbox that intersects that area. You sometimes get global changesets showing up, but there aren't too many of those and you can just ignore them.</p>
</div>
<div id="comment-72352-info" class="comment-info">
<span class="comment-age">(03 Jan '20, 16:54)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-72343" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72343-form-container" class="comment-form-container">
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

