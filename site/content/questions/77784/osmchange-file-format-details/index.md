+++
type = "question"
title = "OSMChange file format details"
description = '''Hi, i have just started working with OSMChange files &quot;.osc&quot; and after reading https://wiki.openstreetmap.org/wiki/OsmChange i still have some questions. In particular about the modify way and how to interpret it. For example in this case   What is this saying? That way 377346605 after the update wil...'''
date = "2020-11-29T18:27:00Z"
lastmod = "2020-11-30T08:16:00Z"
weight = 77784
keywords = [ ".osc", "osm", "fileformat", "osmchange" ]
aliases = [ "/questions/77784" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSMChange file format details](/questions/77784/osmchange-file-format-details)

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
<span id="post-77784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77784-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, i have just started working with OSMChange files ".osc" and after reading <a href="https://wiki.openstreetmap.org/wiki/OsmChange">https://wiki.openstreetmap.org/wiki/OsmChange</a> i still have some questions. In particular about the modify way and how to interpret it.</p>
<p>For example in this case <img src="https://help.openstreetmap.org/upfiles/osc_8iXO5GQ.png" alt="alt text" /></p>
<p>What is this saying? That way 377346605 after the update will have 2 nodes and 1 tag? Or could there be an incremental update? For example way 377346605 after the update will have all the previous nodes plus the two listed in the xml?</p>
<p>I guess the question is if in general in this file format a modified way is always completely described? (In the case where the update is about deleting 1 node from a way made of 20, in the osc i would get all the 19 nodes listed with their ids)</p>
<p>If you have any link to this format documentation would be great. Thanks for the help, Federico.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-.osc" rel="tag" title="see questions tagged &#39;.osc&#39;">.osc</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-fileformat" rel="tag" title="see questions tagged &#39;fileformat&#39;">fileformat</span> <span class="post-tag tag-link-osmchange" rel="tag" title="see questions tagged &#39;osmchange&#39;">osmchange</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '20, 18:27</strong></p>
<img src="https://secure.gravatar.com/avatar/dc14173998d68cfa2fb0e3619d3cb92c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Federico&#39;s gravatar image" />
<p><span>Federico</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Federico has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-77784" class="comments-container">
<span id="77785"></span>
<div id="comment-77785" class="comment">
<div id="post-77785-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not an answer to the question, but if you want to experiment with this on the development server, you can - see <a href="https://wiki.openstreetmap.org/wiki/Sandbox_for_editing">https://wiki.openstreetmap.org/wiki/Sandbox_for_editing</a> .</p>
</div>
<div id="comment-77785-info" class="comment-info">
<span class="comment-age">(29 Nov '20, 18:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="77786"></span>
<div id="comment-77786" class="comment">
<div id="post-77786-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, i'll definitely give it a try. Best.</p>
</div>
<div id="comment-77786-info" class="comment-info">
<span class="comment-age">(29 Nov '20, 18:41)</span> <span class="comment-user userinfo">Federico</span>
</div>
</div>
</div>
<div id="comment-tools-77784" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77784-form-container" class="comment-form-container">
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

<span id="77789"></span>

<div id="answer-container-77789" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77789-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The change file contains the new complete version of all objects that changed. So in the example you mentioned there was a way 377346605 version 1, which we don't get any information about whatsoever. What we get is all information about version 2 of this way. So, yes, it references two nodes and has one tag now.</p>
<p>You don't get anything about any objects that didn't change themselves, even if they are referenced by changed objects. So you will not get node 3051449243 in the change file or node X that was in version 1 of the way but isn't any more, unless those nodes themselves changed. Generally this means that change files aren't very useful without an OSM file, database, or something like it that has <em>all</em> the objects.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '20, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-77789" class="comments-container">
&#10;</div>
<div id="comment-tools-77789" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77789-form-container" class="comment-form-container">
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

