+++
type = "question"
title = "Can a way contain the same node more than just at the beginning and end?"
description = '''Can a way contain the same node more than once and not be a simple loop? I know the following is possible: 1-2-3-4-5-1 But can you do this? (The following could, for example, produce a P-shaped way) 1-2-3-1-4-5 Thankyou Gary'''
date = "2010-07-12T13:01:00Z"
lastmod = "2010-07-16T10:47:00Z"
weight = 119
keywords = [ "ways", "mapping" ]
aliases = [ "/questions/119" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Can a way contain the same node more than just at the beginning and end?](/questions/119/can-a-way-contain-the-same-node-more-than-just-at-the-beginning-and-end)

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
<span id="post-119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-119-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can a way contain the same node more than once and not be a simple loop?</p>
<p>I know the following is possible: 1-2-3-4-5-1</p>
<p>But can you do this? (The following could, for example, produce a P-shaped way) 1-2-3-1-4-5</p>
<p>Thankyou Gary</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '10, 13:01</strong></p>
<img src="https://secure.gravatar.com/avatar/1071b6092ed439c03bc5678d2ce1c249?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gsteinert&#39;s gravatar image" />
<p><span>gsteinert</span><br />
<span class="score" title="74 reputation points">74</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gsteinert has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-119" class="comments-container">
&#10;</div>
<div id="comment-tools-119" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-119-form-container" class="comment-form-container">
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

<span id="124"></span>

<div id="answer-container-124" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-124-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, that is possible in the OSM API.</p>
<p>Nodes can appear as many times as you like within the same way. You can even do figure of 8 ways that join in the middle.</p>
<p>These are most useful for lines like roads, rather than areas, as for areas what's inside and outside can become confusing.</p>
<p>Of course there's no guarantee that all tools out there will support every configuration of way you create, and just because you can doesn't mean that you should :-) So keep it simple. I've used P-shaped ways before but nothing more complicated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '10, 13:23</strong></p>
<img src="https://secure.gravatar.com/avatar/3b5143f79efbb5d8c7d52325f41e0e3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="randomjunk&#39;s gravatar image" />
<p><span>randomjunk</span><br />
<span class="score" title="1545 reputation points"><span>1.5k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="randomjunk has 3 accepted answers">75%</span></p>
</div>
</div>
<div id="comments-container-124" class="comments-container">
<span id="251"></span>
<div id="comment-251" class="comment">
<div id="post-251-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think we should distinguish between "crossing" and "touching". "Touching", like in the "P" case is ok and there are good uses for that, for instance a road ending in a turning circle. But I haven't come across any case where it actually makes sense for a way to cross itself. A closed way (for instance a roundabout or an area) is just a form of a way touching itself.</p>
</div>
<div id="comment-251-info" class="comment-info">
<span class="comment-age">(16 Jul '10, 09:33)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="252"></span>
<div id="comment-252" class="comment">
<div id="post-252-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Indeed. The question was specifically about using the same node more than once in a way.</p>
</div>
<div id="comment-252-info" class="comment-info">
<span class="comment-age">(16 Jul '10, 10:35)</span> <span class="comment-user userinfo">randomjunk</span>
</div>
</div>
<span id="254"></span>
<div id="comment-254" class="comment">
<div id="post-254-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>Here's</span> a case where it would make sense for a trunk_link to cross itself. It doesn't because I had to break it to add a turn restriction.</p>
</div>
<div id="comment-254-info" class="comment-info">
<span class="comment-age">(16 Jul '10, 10:47)</span> <span class="comment-user userinfo">NE2</span>
</div>
</div>
</div>
<div id="comment-tools-124" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-124-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="122"></span>

<div id="answer-container-122" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-122-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes thats possible but in my Opinion there are very few cases where this makes sense. in my opinion it is better to split the way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '10, 13:11</strong></p>
<img src="https://secure.gravatar.com/avatar/fa6455b91461452a50ec757caf9d42d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Islanit&#39;s gravatar image" />
<p><span>Islanit</span><br />
<span class="score" title="44 reputation points">44</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Islanit has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jul '10, 13:11</strong> </span></p>
</div>
</div>
<div id="comments-container-122" class="comments-container">
&#10;</div>
<div id="comment-tools-122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-122-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="147"></span>

<div id="answer-container-147" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-147-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As already stated it's technically possible to create a way in OSM that contains a node more than once.</p>
<p>It's usually considered faulty and tools like JOSM validator or the numerous quality check tools will report such self-intersecting ways.</p>
<p>That relates to constructions like a 'P' or '8'. It does not apply to closed ways creating areas. That is a way where the first and last node are the same. You will use the later to map buildings or lakes.</p>
<p>Some quality checks that list self-intersections are:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Self_intersecting_way_reports"></a><a href="http://wiki.openstreetmap.org/wiki/Self_intersecting_way_reports"></a><a href="http://wiki.openstreetmap.org/wiki/Self_intersecting_way_reports">http://wiki.openstreetmap.org/wiki/Self_intersecting_way_reports</a></p>
<p><a href="http://wiki.openstreetmap.org/wiki/OSM_Inspector/Views/Geometry#Fix_self-intersecting_ways"></a><a href="http://wiki.openstreetmap.org/wiki/OSM_Inspector/Views/Geometry#Fix_self-intersecting_ways"></a><a href="http://wiki.openstreetmap.org/wiki/OSM_Inspector/Views/Geometry#Fix_self-intersecting_ways">http://wiki.openstreetmap.org/wiki/OSM_Inspector/Views/Geometry#Fix_self-intersecting_ways</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '10, 20:14</strong></p>
<img src="https://secure.gravatar.com/avatar/09b2b8d17e144e0bf320379096429046?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stephan%20Knauss&#39;s gravatar image" />
<p><span>Stephan Knauss</span><br />
<span class="score" title="450 reputation points">450</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stephan Knauss has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jul '10, 20:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/3b5143f79efbb5d8c7d52325f41e0e3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="randomjunk&#39;s gravatar image" />
<p><span>randomjunk</span><br />
<span class="score" title="1545 reputation points"><span>1.5k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span></p>
</div>
</div>
<div id="comments-container-147" class="comments-container">
&#10;</div>
<div id="comment-tools-147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-147-form-container" class="comment-form-container">
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

