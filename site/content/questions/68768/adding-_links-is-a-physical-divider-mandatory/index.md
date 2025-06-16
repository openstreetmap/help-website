+++
type = "question"
title = "Adding *_links. Is a physical divider mandatory?"
description = '''Hi OSM people!  I&#x27;ve been editing roads in Europe and noticed that there a lot of *_link cases mapped as separate ways even though there is no physical separation between the lanes - only painted lanes on the ground.  I understand that this can be mapped as a singleway with turn:lane information but...'''
date = "2019-04-12T11:19:00Z"
lastmod = "2019-04-13T11:48:00Z"
weight = 68768
keywords = [ "roads", "divider", "highway", "links", "bestpractice" ]
aliases = [ "/questions/68768" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Adding \*\_links. Is a physical divider mandatory?](/questions/68768/adding-_links-is-a-physical-divider-mandatory)

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
<span id="post-68768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68768-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi OSM people!</p>
<p>I've been editing roads in Europe and noticed that there a lot of *_link cases mapped as separate ways even though there is no physical separation between the lanes - only painted lanes on the ground.</p>
<p>I understand that this can be mapped as a singleway with turn:lane information but there are a lot of link cases where that are only paint divided, and I don't want to modify them without making sure that physical separation is mandatory for links (can't seem to find that information on OSM wiki)</p>
<p>Example this intersection in Romania:</p>
<p>OSM geometry: <img src="/upfiles/Capture_vX77v0X.PNG" alt="alt text" /> Street level imagery from Mapilary: <img src="/upfiles/Capture2_Uj5BqXi.PNG" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-divider" rel="tag" title="see questions tagged &#39;divider&#39;">divider</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-links" rel="tag" title="see questions tagged &#39;links&#39;">links</span> <span class="post-tag tag-link-bestpractice" rel="tag" title="see questions tagged &#39;bestpractice&#39;">bestpractice</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '19, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/3ee439f69ed018e731f5a46d4fae4f24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Armin%20Gheorghina&#39;s gravatar image" />
<p><span>Armin Gheorg...</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Armin Gheorghina has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '19, 11:26</strong> </span></p>
</div>
</div>
<div id="comments-container-68768" class="comments-container">
&#10;</div>
<div id="comment-tools-68768" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68768-form-container" class="comment-form-container">
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

<span id="68770"></span>

<div id="answer-container-68770" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68770-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-68770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Armin Gheorghina has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, nothing is really mandatory in OSM. But there are certain conventions and reasons for those. You are right, if there are no physical dividers one should not map different ways, let alone using *_link. Routers and turn-by-turn navigation will not be able to give correct directions on this intersection. They are likely to say something like "take the exit to the right" instead of "turn right".</p>
<p>On the other had it is good practice and conduct to get in touch with the local community before changing things like this, especially if you are doing it remotely. You can contact the original mapper via changeset comment and ask for their reasons to map the intersection like this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '19, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</img>
</div>
</div>
<div id="comments-container-68770" class="comments-container">
<span id="68771"></span>
<div id="comment-68771" class="comment">
<div id="post-68771-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I fully aggree. I see no reasons for this separation. It increases data complexity, possibly introduces additional errors (forbidden u-turns), leads to wrong navigation instructions and makes correct lane tagging hard/impossible.</p>
</div>
<div id="comment-68771-info" class="comment-info">
<span class="comment-age">(12 Apr '19, 13:15)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68770-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68779"></span>

<div id="answer-container-68779" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68779-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In some cases, communities do not add physical dividers that others would. Removing an extra way would result in routers issuing bad directions, such as the southbound from Reid School Road to Edwards Mill Road in <a href="https://www.openstreetmap.org/changeset/59180915">this example</a>.</p>
<p>So it can be acceptable to create a separate way without a physical divider.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '19, 11:48</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Apr '19, 21:22</strong> </span></p>
</div>
</div>
<div id="comments-container-68779" class="comments-container">
&#10;</div>
<div id="comment-tools-68779" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68779-form-container" class="comment-form-container">
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

