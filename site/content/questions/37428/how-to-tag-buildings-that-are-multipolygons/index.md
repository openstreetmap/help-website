+++
type = "question"
title = "How to tag buildings that are multipolygons?"
description = '''The multipolygon wiki page talks about using ways and tagging the relation instead of the members. As I read it, this would mean that a building with internal spaces would be composed of multiples ways (inner and outer) and then the whole relation would be tagged as a building.  Is that right? If so...'''
date = "2014-10-08T18:06:00Z"
lastmod = "2014-10-08T19:57:00Z"
weight = 37428
keywords = [ "building", "relations", "multipolygon" ]
aliases = [ "/questions/37428" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag buildings that are multipolygons?](/questions/37428/how-to-tag-buildings-that-are-multipolygons)

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
<span id="post-37428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37428-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The <a href="http://wiki.openstreetmap.org/wiki/Relation:multipolygon">multipolygon wiki page</a> talks about using ways and tagging the relation instead of the members. As I read it, this would mean that a building with internal spaces would be composed of multiples ways (inner and outer) and then the whole relation would be tagged as a building.</p>
<ol>
<li>Is that right?</li>
<li>If so, I don't understand how to tag the relation a building.</li>
<li>In contrast, what I actually find are cases of a building that is given the role of outer in a relation that makes up a MP, along with ways that play the inner role. These things seem to render correctly.</li>
</ol>
<p>Here's an example of a relation I just did:</p>
<p><a href="https://www.openstreetmap.org/relation/4096469">https://www.openstreetmap.org/relation/4096469</a></p>
<p>Here's how it's rendered:</p>
<p><a href="https://www.openstreetmap.org/#map=19/41.89464/12.49875">https://www.openstreetmap.org/#map=19/41.89464/12.49875</a></p>
<p>That looks right, even though it's not done according to the wiki page (again if I read it correctly).</p>
<p>Thanks for any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '14, 18:06</strong></p>
<img src="https://secure.gravatar.com/avatar/1b061a7fc6f2d4aaa77d6e607ac75ae2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eponymous&#39;s gravatar image" />
<p><span>Eponymous</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eponymous has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37428" class="comments-container">
&#10;</div>
<div id="comment-tools-37428" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37428-form-container" class="comment-form-container">
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

<span id="37430"></span>

<div id="answer-container-37430" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37430-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tags should be on the OSM object representing the building as a whole, which would be the multipolygon relation in your example. If you didn't do that, you'd have a multipolygon relation describing some unknown object. Data users can't necessarily use the tags of the members to determine what the relation represents.</p>
<p>Also, keep in mind that something can appear to render correctly even if the underlying data is incorrect. Getting the underlying data correct is the most important, because OSM data is used for more things than just image rendering.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '14, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-37430" class="comments-container">
<span id="37431"></span>
<div id="comment-37431" class="comment">
<div id="post-37431-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OK, so here's what I did (which wasn't clear to me before):</p>
<ol>
<li>Made the three lines.</li>
<li>Created a multipolygon relation.</li>
<li>Added the tag "building=yes" to the relation.</li>
</ol>
<p>Previously I was trying to change the type of the MP.</p>
</div>
<div id="comment-37431-info" class="comment-info">
<span class="comment-age">(08 Oct '14, 19:05)</span> <span class="comment-user userinfo">Eponymous</span>
</div>
</div>
<span id="37432"></span>
<div id="comment-37432" class="comment">
<div id="post-37432-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, it looks correct now.</p>
</div>
<div id="comment-37432-info" class="comment-info">
<span class="comment-age">(08 Oct '14, 19:57)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-37430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37430-form-container" class="comment-form-container">
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

