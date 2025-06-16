+++
type = "question"
title = "How to Map Intersections with Turns"
description = '''How do I map this kind of intersection in terms of adding lane numbers, turning lanes and width? For example, what I have so far for the bottom road leading up to the intersection is: lanes = 3 lanes:forward = 1 lanes:backward = 1 turn:lanes:backward = 1 And I don&#x27;t have width added yet, but I was t...'''
date = "2020-09-17T16:38:00Z"
lastmod = "2020-09-17T19:11:00Z"
weight = 76678
keywords = [ "intersections", "lanes", "highway", "turnlanes" ]
aliases = [ "/questions/76678" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to Map Intersections with Turns](/questions/76678/how-to-map-intersections-with-turns)

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
<span id="post-76678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76678-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I map this kind of intersection in terms of adding lane numbers, turning lanes and width?</p>
<p>For example, what I have so far for the bottom road leading up to the intersection is:</p>
<p>lanes = 3</p>
<p>lanes:forward = 1</p>
<p>lanes:backward = 1</p>
<p>turn:lanes:backward = 1</p>
<p>And I don't have width added yet, but I was thinking of adding it as:</p>
<p>width = 15'</p>
<p>Or should I specify which lane has which width? In general, for roads and streets with lane tags on the way, does width specify for the entire width of the way? And what else should I add/edit to make the bottom road leading up to the intersection complete?</p>
<p>Thank you!</p>
<p><img src="/upfiles/MappingIntersections2.JPG" alt="Aerial of an intersection without overlaying OSM data" /></p>
<p><img src="/upfiles/Mappingintersections_cEZHVHN.JPG" alt="Aerial of intersection with overlaying OSM data" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersections" rel="tag" title="see questions tagged &#39;intersections&#39;">intersections</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-turnlanes" rel="tag" title="see questions tagged &#39;turnlanes&#39;">turnlanes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '20, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/56308f2719f8c02190a91d44d9a5836c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IanVG&#39;s gravatar image" />
<p><span>IanVG</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IanVG has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-76678" class="comments-container">
&#10;</div>
<div id="comment-tools-76678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76678-form-container" class="comment-form-container">
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

<span id="76680"></span>

<div id="answer-container-76680" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76680-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to split the highways at the intersection and at the position where the lanes start or stop. Let's take the road north of the intersection. Assuming the way runs north to south the tags would be:</p>
<p><code>lanes=3</code><br />
<code>lanes:forward=2</code><br />
<code>lanes:backward=1</code><br />
<code>turn:lanes:forward=left|through;right</code></p>
<p>If the way runs south to north forward and backward would have to be swapped, but the order in the turn:lanes is always left to right in driving direction (not way direction).</p>
<p>If there are no markings on the right lane you could also tag<br />
<code>turn:lanes:forward=left|</code><br />
instead. It's not so clear from the picture.</p>
<p>There are some <a href="https://wiki.openstreetmap.org/wiki/Key:turn">examples on the Wiki</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '20, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '20, 18:53</strong> </span></p>
</div>
</div>
<div id="comments-container-76680" class="comments-container">
&#10;</div>
<div id="comment-tools-76680" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76680-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76679"></span>

<div id="answer-container-76679" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76679-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the correct tagging would be (speaking of North Milledge Avenue and assuming it goes S&gt;N):<br />
<code>lanes = 3</code><br />
<code>lanes:forward = 1</code><br />
<code>lanes:backward = 2</code><br />
<code>turn:lanes:backward = left|</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '20, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/e3dbac44db8deb4b09af6e6df914de1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mannivu&#39;s gravatar image" />
<p><span>Mannivu</span><br />
<span class="score" title="1084 reputation points"><span>1.1k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mannivu has 3 accepted answers">6%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> reverted <strong>17 Sep '20, 18:56</strong> </span></p>
</div>
</div>
<div id="comments-container-76679" class="comments-container">
<span id="76681"></span>
<div id="comment-76681" class="comment">
<div id="post-76681-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><code>lanes:forward</code> and <code>lanes:backward</code> should add up to <code>lanes</code> (except if there is a lane open to both directions.</p>
</div>
<div id="comment-76681-info" class="comment-info">
<span class="comment-age">(17 Sep '20, 18:56)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="76682"></span>
<div id="comment-76682" class="comment">
<div id="post-76682-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, you're right. I've edited my answer just before your comment 😅</p>
</div>
<div id="comment-76682-info" class="comment-info">
<span class="comment-age">(17 Sep '20, 18:56)</span> <span class="comment-user userinfo">Mannivu</span>
</div>
</div>
</div>
<div id="comment-tools-76679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76679-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76683"></span>

<div id="answer-container-76683" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76683-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I agree with the previous answers that turn:lanes:forward= <em>and/or turn:lanes:backward=</em> are the tags to be use.</p>
<p>I personally like to use 'none' instead of nothing between the "|" lane delimiters as I find it easier to read especially on wide streets with lots of lanes. (Software tools shouldn't care one way or the other.)</p>
<p>You can tag all this by hand, but the turn lanes plug-in for JOSM makes it really, really easy and assures that you have the proper match up between the number of lanes specified in the turn:lanes:*, lanes:forward, lanes:backward tagging and the total lane count.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '20, 19:11</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span> </br></br></p>
</div>
</div>
<div id="comments-container-76683" class="comments-container">
&#10;</div>
<div id="comment-tools-76683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76683-form-container" class="comment-form-container">
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

