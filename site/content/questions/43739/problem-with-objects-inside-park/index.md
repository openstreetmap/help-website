+++
type = "question"
title = "Problem with Objects Inside Park"
description = '''Fremont Central Park is a park located in Fremont, CA. There are several objects in it. None of these objects are shown to be part of the park when searched up on the map. For example, a lake in the park, Lake Elizabeth, is not shown to be part of the park when searched up. Oddly, it is shown to be ...'''
date = "2015-06-24T04:30:00Z"
lastmod = "2015-06-25T01:01:00Z"
weight = 43739
keywords = [ "objects", "park", "relations", "multipolygon" ]
aliases = [ "/questions/43739" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problem with Objects Inside Park](/questions/43739/problem-with-objects-inside-park)

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
<span id="post-43739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43739-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Fremont Central Park is a park located in Fremont, CA. There are several objects in it. None of these objects are shown to be part of the park when searched up on the map. For example, a lake in the park, Lake Elizabeth, is not shown to be part of the park when searched up. Oddly, it is shown to be part of a small nearby bridge. My question is: How am I supposed to have these objects shown as part of the park? I've tried using relations and multipolygons, but I am out of luck.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-objects" rel="tag" title="see questions tagged &#39;objects&#39;">objects</span> <span class="post-tag tag-link-park" rel="tag" title="see questions tagged &#39;park&#39;">park</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '15, 04:30</strong></p>
<img src="https://secure.gravatar.com/avatar/33df889d3ba6bd2d758bfabb60692b4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Suprav&#39;s gravatar image" />
<p><span>Suprav</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Suprav has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43739" class="comments-container">
<span id="43764"></span>
<div id="comment-43764" class="comment">
<div id="post-43764-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When you say "searched up", you mean the search on openstreetmap.org?</p>
<p>Those results are the output of one particular system for indexing the data:</p>
<p><a href="http://nominatim.openstreetmap.org/details.php?place_id=90306622">http://nominatim.openstreetmap.org/details.php?place_id=90306622</a></p>
<p>That system generally doesn't take note of whether things are inside a park or not. As scai says, the geometry should be enough for systems that do index such things.</p>
<p>I guess the lake probably doesn't really have an address (before you added one, the result you were seeing was from just matching it somehow to a nearby road).</p>
</div>
<div id="comment-43764-info" class="comment-info">
<span class="comment-age">(25 Jun '15, 01:01)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-43739" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43739-form-container" class="comment-form-container">
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

<span id="43742"></span>

<div id="answer-container-43742" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43742-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Suprav has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure, but expect that this problem is still <a href="https://wiki.openstreetmap.org/wiki/Good_practice">not finally discussed</a> at the community. AFAIK there are different opinions:</p>
<ul>
<li>Yes, all such objects should be part of a multipolygone <a href="https://wiki.openstreetmap.org/wiki/Relation:site">(site) relation</a> to group them together.</li>
<li>No, Its not up to the mappers to tag objects for geocoder search. Instead it's up to the applications to do the boundary processing and create the hierachies dynamically.</li>
</ul>
<p>I guess both statements have their pros and cons (maintainability, performance, ...). Usually I don't see relations beside multipolygones on landuse, but that can be an local phenomena.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '15, 06:05</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-43742" class="comments-container">
<span id="43744"></span>
<div id="comment-43744" class="comment">
<div id="post-43744-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Usually the latter should be preferred. That is, do not create any unnecessary site relations as long as the information can be automatically deduced from the existing geometry information. If an object is inside another object then it is, well, inside this other object. There is no relation required to represent this. Site relations are only necessary if two or more objects belong together but are geographically separated.</p>
</div>
<div id="comment-43744-info" class="comment-info">
<span class="comment-age">(24 Jun '15, 08:08)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="43763"></span>
<div id="comment-43763" class="comment">
<div id="post-43763-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks both of you. It has made relations a lot more clear to me.</p>
</div>
<div id="comment-43763-info" class="comment-info">
<span class="comment-age">(25 Jun '15, 00:48)</span> <span class="comment-user userinfo">Suprav</span>
</div>
</div>
</div>
<div id="comment-tools-43742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43742-form-container" class="comment-form-container">
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

