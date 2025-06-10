+++
type = "question"
title = "[Not] tagging for the rendering - Suggestions?"
description = '''I am updating a large medical complex. The complex combines a hospital and a medical faculty, each of them consisting of several buildings and/or wings. The entire complex (land) is currently tagged as amenity=hospital. I associated the buildings of the medical faculty to a multipolygon (amenity=uni...'''
date = "2021-01-22T22:03:00Z"
lastmod = "2021-01-23T17:58:00Z"
weight = 78449
keywords = [ "suggestion", "rendering", "bestpractice", "tagging" ]
aliases = [ "/questions/78449" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[Not\] tagging for the rendering - Suggestions?](/questions/78449/not-tagging-for-the-rendering-suggestions)

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
<span id="post-78449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78449-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am updating a large medical complex. The complex combines a hospital and a medical faculty, each of them consisting of several buildings and/or wings. The entire complex (land) is currently tagged as amenity=hospital. I associated the buildings of the medical faculty to a multipolygon (amenity=university; name=Campus Santé) and tagged them as inner rings of the hospital multipolygon. See …</p>
<p>[<a href="https://www.openstreetmap.org/#map=17/45.44780/-71.86699%5D">https://www.openstreetmap.org/#map=17/45.44780/-71.86699]</a></p>
<p>What I would like, while respecting good practices, is to obtain the following two results on the map (if possisble).</p>
<ul>
<li><p>a) Distinguish the hospital sector from the medical faculty sector by name. The name of the medical faculty is visible, but the name of the hospital complex does not appear anymore.</p></li>
<li><p>b) Display 2-3 meaningful accesses for patients (by their door number). It would be a big improvement for the locals as the location of the doors is almost impossible to find in the maze of the hospital website!</p></li>
</ul>
<p>Any suggestion that could help is welcome for one or both cases :-)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-suggestion" rel="tag" title="see questions tagged &#39;suggestion&#39;">suggestion</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-bestpractice" rel="tag" title="see questions tagged &#39;bestpractice&#39;">bestpractice</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '21, 22:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78449" class="comments-container">
&#10;</div>
<div id="comment-tools-78449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78449-form-container" class="comment-form-container">
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

<span id="78450"></span>

<div id="answer-container-78450" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78450-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfd553 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Building entrances can be tagged with <code>entrance=</code> (and then named and so on). There's also some tags for interiors of buildings: <a href="https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging">https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging</a></p>
<p>The campus label isn't rendering because the labeling system can't find a place to put it. This happens with automatic labeling.</p>
<p>I think I wouldn't cut the buildings out of the hospital campus (but this can be a metaphysical discussion). My thinking is that it's really part of the hospital campus, even if there is relatively separate administration and operation and so forth. Even if there is clearly separated ownership, we might still say that it is located on the grounds of the hospital. It can be within the hospital and have a name and so on.</p>
<p>The campus doesn't need/shouldn't have a layer tag (this tag is about vertical ordering of physical features, the campus doesn't really have such an attribute).</p>
<p>I'd encourage you not to map the emergency room as an additional hospital (There is no other well established way to do it though). If you are going to map it as a hospital, it should probably have <code>emergency=yes</code> rather than the ambulance station tag (the ambulance station can be mapped separately).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '21, 01:44</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-78450" class="comments-container">
<span id="78454"></span>
<div id="comment-78454" class="comment">
<div id="post-78454-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Here's an example where the Medical School is mapped as an area within the hospital building (in practice it's a discrete wing of the hospital): <a href="https://www.openstreetmap.org/way/16878374.">https://www.openstreetmap.org/way/16878374.</a></p>
<p>Unfortunately at present we have not really developed a sophisticated way of mapping the reality of large hospital sites. There is recent discussion on tagging about some particular aspects, but they are better looked at in toto.</p>
</div>
<div id="comment-78454-info" class="comment-info">
<span class="comment-age">(23 Jan '21, 16:32)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="78456"></span>
<div id="comment-78456" class="comment">
<div id="post-78456-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a>: About Hospital's labeling, I thought it was related to automated name location and priorities. About doors number, it does not show up on the map (and may be it is even expecte). I used the above tags to identify one of the door ( door #2)...</p>
<p>access=yes emergency=emergency_ward_entrance emergency_ward_entrance=walk-in entrance=yes door=folding ref=2 wheelchair=yes</p>
</div>
<div id="comment-78456-info" class="comment-info">
<span class="comment-age">(23 Jan '21, 17:58)</span> <span class="comment-user userinfo">jfd553</span>
</div>
</div>
</div>
<div id="comment-tools-78450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78450-form-container" class="comment-form-container">
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

