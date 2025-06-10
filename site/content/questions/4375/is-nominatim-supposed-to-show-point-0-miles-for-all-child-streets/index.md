+++
type = "question"
title = "Is Nominatim supposed to show &quot;Point, ~0 miles&quot; for all child streets?"
description = '''In a Nominatim detailed view, such as http://open.mapquestapi.com/nominatim/v1/details.php?place_id=36822949, when I scroll down to &quot;Parent of...&quot; and further to &quot;Residential&quot;, it lists polygons first (as in residential neighborhoods) and then streets. Each street has &quot;(Point, ~0 miles, way &amp;lt;osmi...'''
date = "2011-04-11T08:42:00Z"
lastmod = "2011-04-11T18:38:00Z"
weight = 4375
keywords = [ "nominatim" ]
aliases = [ "/questions/4375" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is Nominatim supposed to show "Point, ~0 miles" for all child streets?](/questions/4375/is-nominatim-supposed-to-show-point-0-miles-for-all-child-streets)

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
<span id="post-4375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4375-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In a Nominatim detailed view, such as <a href="http://open.mapquestapi.com/nominatim/v1/details.php?place_id=36822949">http://open.mapquestapi.com/nominatim/v1/details.php?place_id=36822949</a>, when I scroll down to "Parent of..." and further to "Residential", it lists polygons first (as in residential neighborhoods) and then streets. Each street has "(Point, ~0 miles, way &lt;osmid&gt;, GOTO)" next to it.</p>
<p>Shouldn't it be Way (not point) and the street's length, not zero?<br />
</p>
<p>Is it a (known) bug, a placeholder for an undeveloped feature?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '11, 08:42</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-4375" class="comments-container">
&#10;</div>
<div id="comment-tools-4375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4375-form-container" class="comment-form-container">
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

<span id="4383"></span>

<div id="answer-container-4383" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4383-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ponzu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "Nominatim detailed view" is more or less a dump of the internal data Nominatim uses, so much of it is probably not very understandable unless you know how Nominatim works internally.</p>
<p>That said, to address your points:</p>
<ul>
<li>The "miles" indication is the <em>distance to the object</em>, not the object's size. So "~0 miles" in your example just means that this object is 0 miles from the main object of the page you are looking at. As the main object on the page you give is a polygon, it makes sense for streets that lie inside that polygon to have a distance of 0. If you look for example at the details for Düsseldorf, Germany, you see that most entries have a "miles" indication. That's because the main object is a point, and hence you can calculate the distance to other objects: <a href="http://open.mapquestapi.com/nominatim/v1/details.php?place_id=623958">http://open.mapquestapi.com/nominatim/v1/details.php?place_id=623958</a></li>
<li>As to "Way" vs. "Point": I believe Nominatim internally does not distinguish ways and points, it just knows polygons and points. But that's a question only the Nominatim devs can answer definitively.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '11, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-4383" class="comments-container">
<span id="4397"></span>
<div id="comment-4397" class="comment">
<div id="post-4397-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that makes sense now. If this is a "dump" that's not supposed to be understandable to laymen like me (no offense taken), am I going all wrong about testing my data (outlines of suburbs and neighborhoods I'm adding within the city) using this view? I am trying to verify that after I'm done, the city will contain (be parent of) the suburbs, and each suburb will contain (be parent of) the neighborhoods. And also that any given street is found in a neighborhood, then in a suburb and then in a city. Is there a better tool to test this hierarchy?</p>
</div>
<div id="comment-4397-info" class="comment-info">
<span class="comment-age">(11 Apr '11, 18:38)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-4383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4383-form-container" class="comment-form-container">
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

