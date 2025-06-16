+++
type = "question"
title = "What is the reason to assign way to relation many times?"
description = '''Sometimes I see relations have the same way assigned many times. From my point of view such ways are redundant, but maybe they have some hidden goal :)  Can they be simply ignored in such case or have to be taken into account because of something? Samples: Relation 6172257 has way 385987825 assigned...'''
date = "2016-07-21T21:46:00Z"
lastmod = "2016-07-22T10:12:00Z"
weight = 51049
keywords = [ "import", "shape" ]
aliases = [ "/questions/51049" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What is the reason to assign way to relation many times?](/questions/51049/what-is-the-reason-to-assign-way-to-relation-many-times)

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
<span id="post-51049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51049-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Sometimes I see relations have the same way assigned many times.<br />
From my point of view such ways are redundant, but maybe they have some hidden goal :)</p>
<p>Can they be simply ignored in such case or have to be taken into account because of something?</p>
<p>Samples:<br />
Relation <a href="https://www.openstreetmap.org/relation/6172257">6172257</a> has way <a href="https://www.openstreetmap.org/way/385987825">385987825</a> assigned 10 times and way <a href="https://www.openstreetmap.org/way/385594983">385594983</a> assigned 9 times.<br />
Relation <a href="https://www.openstreetmap.org/relation/6025059">6025059</a> has way <a href="https://www.openstreetmap.org/way/401613413">401613413</a> assigned 2 times.</p>
<p>Top 20 :-)</p>
<p><img src="/upfiles/Top20Ways.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-shape" rel="tag" title="see questions tagged &#39;shape&#39;">shape</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '16, 21:46</strong></p>
<img src="https://secure.gravatar.com/avatar/9d6cd718cdeb41535fa4aa16477eeeb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stalek&#39;s gravatar image" />
<p><span>stalek</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stalek has no accepted answers">0%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jul '16, 21:46</strong> </span></p>
</div>
</div>
<div id="comments-container-51049" class="comments-container">
<span id="51054"></span>
<div id="comment-51054" class="comment">
<div id="post-51054-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As far as I can tell, these are just plain bad taggings of multipolygons. Actually, it would be highly desirable if editor Apps prevented this kind of duplication, or at the very least presented users with a big warning if they try to upload this type of mess. I would just clean this up without asking the original editor who created it, it is not worth contacting, better spend the time on the clean up.</p>
</div>
<div id="comment-51054-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 23:12)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
<span id="51061"></span>
<div id="comment-51061" class="comment">
<div id="post-51061-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OK, I decided to fix these issues myself. In case of the relation 6172257, I have also decided to drop all buildings from the multipolygon. It is a bit a disputed point, but generally speaking, above surface man made structures like building do not belong as part of a landuse multipolygon.</p>
</div>
<div id="comment-51061-info" class="comment-info">
<span class="comment-age">(22 Jul '16, 10:12)</span> <span class="comment-user userinfo">mboeringa</span>
</div>
</div>
</div>
<div id="comment-tools-51049" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51049-form-container" class="comment-form-container">
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

<span id="51053"></span>

<div id="answer-container-51053" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51053-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My guess in the case of <a href="http://osm.mapki.com/history/relation.php?id=6172257">6172257</a> it's not deliberate. That is a landuse=grass, and was created in one go by iD, which hides much relation processing from the user. Maybe ask the person who added it about it?</p>
<p>With some relations (e.g. bus routes) it might make more sense.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '16, 22:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-51053" class="comments-container">
&#10;</div>
<div id="comment-tools-51053" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51053-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51051"></span>

<div id="answer-container-51051" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51051-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-51051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, look at this one 385987825 then you’ll notice it’s a large collection of multypoligones and every inner has a relation with the outer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '16, 21:54</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-51051" class="comments-container">
<span id="51052"></span>
<div id="comment-51052" class="comment">
<div id="post-51052-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Hendrik, 385987825 is a way with a collection of nodes (points). We see on the definition of this way also that it has been mapped many times to relation 6172257. I'm not sure I understand your answer :-) ...</p>
</div>
<div id="comment-51052-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 22:24)</span> <span class="comment-user userinfo">stalek</span>
</div>
</div>
<span id="51055"></span>
<div id="comment-51055" class="comment">
<div id="post-51055-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Follow mboerings advice and dont think over it.</p>
</div>
<div id="comment-51055-info" class="comment-info">
<span class="comment-age">(21 Jul '16, 23:18)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-51051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51051-form-container" class="comment-form-container">
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

