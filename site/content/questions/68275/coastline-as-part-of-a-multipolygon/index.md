+++
type = "question"
title = "Coastline as part of a multipolygon?"
description = '''Can a coastline defined object be part of other objects like here https://osm.org/go/e5qjytbLk-?layers=C&amp;amp;way=503623451 .  As I understand a coastline defined object is either a land or a water object. Eventually, it is an error object. '''
date = "2019-03-05T17:01:00Z"
lastmod = "2019-03-05T19:08:00Z"
weight = 68275
keywords = [ "coasline", "multipolygons" ]
aliases = [ "/questions/68275" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Coastline as part of a multipolygon?](/questions/68275/coastline-as-part-of-a-multipolygon)

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
<span id="post-68275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68275-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can a coastline defined object be part of other objects like here <a href="https://osm.org/go/e5qjytbLk-?layers=C&amp;way=503623451">https://osm.org/go/e5qjytbLk-?layers=C&amp;way=503623451</a> .<br />
As I understand a coastline defined object is either a land or a water object. Eventually, it is an error object.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-coasline" rel="tag" title="see questions tagged &#39;coasline&#39;">coasline</span> <span class="post-tag tag-link-multipolygons" rel="tag" title="see questions tagged &#39;multipolygons&#39;">multipolygons</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '19, 17:01</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Mar '19, 18:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span></p>
</div>
</div>
<div id="comments-container-68275" class="comments-container">
&#10;</div>
<div id="comment-tools-68275" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68275-form-container" class="comment-form-container">
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

<span id="68280"></span>

<div id="answer-container-68280" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68280-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This particular case is an error. A closed natural=coastline way has been mapped inside of another closed natural=coastline way and with the same direction, which doesn't make any semantic sense. As tagged currently, it represents an island (not in a body of water) on an island in an ocean. It was likely intended to be tagged as natural=water.</p>
<p>In addition, the exclusion of this small area from the <a href="https://www.openstreetmap.org/relation/1959008">"Western Isles" relation</a> is likely also an error.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '19, 19:08</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-68280" class="comments-container">
&#10;</div>
<div id="comment-tools-68280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68280-form-container" class="comment-form-container">
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

