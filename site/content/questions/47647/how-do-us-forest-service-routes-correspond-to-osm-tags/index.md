+++
type = "question"
title = "How do US Forest Service routes correspond to OSM tags?"
description = '''According to the US Forest Service travel maps, there are six different route types in NFs. What are the OSM road tags that correspond to these US Forest Service route designations?  Paved Roads Gravel Roads Dirt Roads Unimproved Dirt Roads (4x4 recommended) Motorized Trails Non-Motorized Trails  Fo...'''
date = "2016-01-25T23:41:00Z"
lastmod = "2016-01-26T00:22:00Z"
weight = 47647
keywords = [ "tagging", "road" ]
aliases = [ "/questions/47647" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do US Forest Service routes correspond to OSM tags?](/questions/47647/how-do-us-forest-service-routes-correspond-to-osm-tags)

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
<span id="post-47647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47647-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>According to the <a href="http://apps.fs.fed.us/TravelAccess/">US Forest Service travel maps</a>, there are six different route types in NFs. What are the OSM road tags that correspond to these US Forest Service route designations?</p>
<ul>
<li>Paved Roads</li>
<li>Gravel Roads</li>
<li>Dirt Roads</li>
<li>Unimproved Dirt Roads (4x4 recommended)</li>
<li>Motorized Trails</li>
<li>Non-Motorized Trails</li>
</ul>
<p>For example, I believe "non-motorized trails" would be Paths since they are basically hiking trails.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jan '16, 23:41</strong></p>
<img src="https://secure.gravatar.com/avatar/8aea1dfc024f4fe4249da9d2ebd66387?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisMendez&#39;s gravatar image" />
<p><span>ChrisMendez</span><br />
<span class="score" title="60 reputation points">60</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisMendez has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47647" class="comments-container">
&#10;</div>
<div id="comment-tools-47647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47647-form-container" class="comment-form-container">
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

<span id="47651"></span>

<div id="answer-container-47651" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47651-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is some discussion here: <a href="http://www.openstreetmap.org/user/Richard/diary/26099">http://www.openstreetmap.org/user/Richard/diary/26099</a></p>
<p>The paved and gravel roads should mostly be highway=unclassified, with the appropriate surface tag set. Sometimes a more significant road will be a tertiary or whatever.</p>
<p>Motorized trails aren't totally settled, but some combination of access tags and/or maxwidth can accurately reflect the additional restrictions, as discussed here:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Key:access#Land-based_transportation">http://wiki.openstreetmap.org/wiki/Key:access#Land-based_transportation</a></p>
<p><a href="http://wiki.openstreetmap.org/wiki/Key:atv">http://wiki.openstreetmap.org/wiki/Key:atv</a></p>
<p>I think given that the Forest Service uses them for publishing temporary closures and that they are often the most prominent signage present, it's also useful to put the road number in the ref tag. I've seen prefixes of (at least) FS, USFS and NF used for that, it would be good to eventually standardize those some.</p>
<p>Later: Tracks that are closed to vehicles other than snowmobiles can be marked as vehicle=no, snowmobile=yes (<a href="https://help.openstreetmap.org/questions/16087/how-should-i-tag-a-snowmobile-trail">some discussion</a>). Motorcycles trails can use a similar scheme, vehicle=no, motorcycle=yes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '16, 00:22</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jan '16, 19:39</strong> </span></p>
</div>
</div>
<div id="comments-container-47651" class="comments-container">
&#10;</div>
<div id="comment-tools-47651" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47651-form-container" class="comment-form-container">
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

