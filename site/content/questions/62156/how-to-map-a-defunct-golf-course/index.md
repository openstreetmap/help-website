+++
type = "question"
title = "How to map a defunct golf course?"
description = '''There&#x27;s an area of land in my neighborhood that was formerly a golf course, but has been defunct for years and will never be made a golf course again: Course shut down, Future use of area It is currently mapped in OSM as a golf course complete with water hazards, sand traps, etc. Seems like there is...'''
date = "2018-02-16T21:26:00Z"
lastmod = "2018-02-16T22:15:00Z"
weight = 62156
keywords = [ "defunct", "golf", "area" ]
aliases = [ "/questions/62156" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to map a defunct golf course?](/questions/62156/how-to-map-a-defunct-golf-course)

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
<span id="post-62156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62156-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There's an area of land in my neighborhood that was formerly a golf course, but has been defunct for years and will never be made a golf course again: <a href="https://www.mercurynews.com/2016/04/12/livermore-springtown-golf-course-to-shut-down/">Course shut down</a>, <a href="https://www.eastbaytimes.com/2017/02/01/livermore-springtown-golf-course-plans-for-open-space-begin/">Future use of area</a></p>
<p>It is currently mapped in OSM as a <a href="https://www.openstreetmap.org/relation/317365">golf course</a> complete with water hazards, sand traps, etc. Seems like there is an opportunity to correct this, but I wouldn't want to go in and just delete all the nodes. Is there an OSM-encouraged way to correct this area?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-defunct" rel="tag" title="see questions tagged &#39;defunct&#39;">defunct</span> <span class="post-tag tag-link-golf" rel="tag" title="see questions tagged &#39;golf&#39;">golf</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '18, 21:26</strong></p>
<img src="https://secure.gravatar.com/avatar/4975c8d2146b6c2224eb541d5c9ee46f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryandrake&#39;s gravatar image" />
<p><span>ryandrake</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryandrake has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62156" class="comments-container">
&#10;</div>
<div id="comment-tools-62156" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62156-form-container" class="comment-form-container">
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

<span id="62158"></span>

<div id="answer-container-62158" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62158-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-62158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ryandrake has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use the lifecycle prefix <a href="https://wiki.openstreetmap.org/wiki/Key:abandoned:">https://wiki.openstreetmap.org/wiki/Key:abandoned:</a> for this. E.g. at <a href="https://www.openstreetmap.org/way/293296944">https://www.openstreetmap.org/way/293296944</a> change <code>golf=bunker</code> to <code>abandoned:golf=bunker</code> and at <a href="https://www.openstreetmap.org/relation/317365">https://www.openstreetmap.org/relation/317365</a> change <code>leisure=golf_course</code> into <code>abandoned:leisure=golf_course</code> and remove the likely disfunct website tag. The <code>name</code> tag's key should be changed into <a href="https://wiki.openstreetmap.org/wiki/Key:name"><code>old_name</code></a> if this is not anymore the name.</p>
<p>In addition tag it what it is now.. Maybe now a park? Just a meadow?</p>
<p>And, of course, use a <a href="https://wiki.openstreetmap.org/wiki/Good_changeset_comments">good changeset comment</a> when saving/uploading your change.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '18, 21:41</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '18, 21:43</strong> </span></p>
</div>
</div>
<div id="comments-container-62158" class="comments-container">
<span id="62159"></span>
<div id="comment-62159" class="comment">
<div id="post-62159-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your quick help, that makes sense. Right now, it vaguely resembles a golf course, but all of the golf-like features are overgrown. The city says the land area will eventually become "open space" which could mean anything from a public park to unmaintained wilderness.</p>
</div>
<div id="comment-62159-info" class="comment-info">
<span class="comment-age">(16 Feb '18, 21:55)</span> <span class="comment-user userinfo">ryandrake</span>
</div>
</div>
<span id="62160"></span>
<div id="comment-62160" class="comment">
<div id="post-62160-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14763/ryandrake"></a><a href="https://help.openstreetmap.org/users/14763/ryandrake">@ryandrake</a>: you are welcome! If it just needs a lawn mower to be a golf course again, the prefix <a href="https://wiki.openstreetmap.org/wiki/Key:disused:"><code>disused:</code></a> might be more applicable.</p>
</div>
<div id="comment-62160-info" class="comment-info">
<span class="comment-age">(16 Feb '18, 22:15)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62158" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62158-form-container" class="comment-form-container">
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

