+++
type = "question"
title = "What should be done about a temporary relocation of an amenity for rebuilding?"
description = '''For example, an elementary school is being rebuilt, and has moved into a new building for the 2010-11 school year. After that, it will move back to its original location and the temporary location will become a new school with a new name. Both the old and temporary locations currently have the same ...'''
date = "2010-07-23T10:39:00Z"
lastmod = "2010-07-26T09:45:00Z"
weight = 455
keywords = [ "temporary", "tagging" ]
aliases = [ "/questions/455" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What should be done about a temporary relocation of an amenity for rebuilding?](/questions/455/what-should-be-done-about-a-temporary-relocation-of-an-amenity-for-rebuilding)

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
<span id="post-455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-455-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For example, an elementary school is being rebuilt, and has moved into a new building for the 2010-11 school year. After that, it will move back to its original location and the temporary location will become a new school with a new name.</p>
<p>Both the old and temporary locations currently have the same name. So how do I ensure that someone searching for the school can tell which one is currently in use?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-temporary" rel="tag" title="see questions tagged &#39;temporary&#39;">temporary</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '10, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/0c334b9f230e39c1e73a2b0322a23fb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NE2&#39;s gravatar image" />
<p><span>NE2</span><br />
<span class="score" title="1359 reputation points"><span>1.4k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NE2 has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-455" class="comments-container">
&#10;</div>
<div id="comment-tools-455" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-455-form-container" class="comment-form-container">
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

<span id="458"></span>

<div id="answer-container-458" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-458-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The golden rule is to tag what's currently on the ground. So retag the temporary location as <strong>amenity=school</strong> and the site under redevelopment as a construction site (perhaps: see below!). Name both the same while the work is being performed if they have the same name on the ground. It might be wise to record a bug with <a href="http://openstreetbugs.schokokeks.org/">OpenStreetBugs</a> reminding yourself or others to undo this change later on, when work is complete.</p>
<p>If the site under redevelopment is currently just school offices with work being carried out on them while school staff go about their everyday office work, but classes have been moved for safety reasons, tag the old site as <strong>landuse=commercial</strong> (i.e. offices) and still name both sites the same.</p>
<p>Couple of other observations:</p>
<ul>
<li><p>This sort of situation and others like it is a suitable use for the <a href="https://wiki.openstreetmap.org/wiki/Description"><strong>description=*</strong> tag</a>, which can be used for additional information which may be visible when the map is rendered. Keep such notes brief and descriptive of the current situation. Other mappers will appreciate <strong>FIXME=*</strong> or <strong>note=*</strong> tags, which are used for internal notes and can be a bit more long-winded. The name tag is for names only, not descriptions.</p></li>
<li><p>Temporary works are always tricky to represent - how long must a temporary situation be in effect before you decide to alter the map? - but as noted in <a href="/questions/259/temporary-road-works-and-traffic-situations/265">Jochen's excellent answer here</a>, it's certainly OK to do this when the "temporary" alteration will be actually a feature in the landscape for several months. A school year is such a period.</p></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '10, 11:50</strong></p>
<img src="https://secure.gravatar.com/avatar/b4a99bb74962d3cedff3e6d591847852?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew%20Chadwick&#39;s gravatar image" />
<p><span>Andrew Chadwick</span><br />
<span class="score" title="1129 reputation points"><span>1.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew Chadwick has 3 accepted answers">25%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '10, 11:51</strong> </span></p>
</div>
</div>
<div id="comments-container-458" class="comments-container">
<span id="465"></span>
<div id="comment-465" class="comment">
<div id="post-465-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>WHat do I do if the old site is a node? Landuse, I believe, only applies to areas.</p>
</div>
<div id="comment-465-info" class="comment-info">
<span class="comment-age">(23 Jul '10, 23:03)</span> <span class="comment-user userinfo">NE2</span>
</div>
</div>
<span id="481"></span>
<div id="comment-481" class="comment">
<div id="post-481-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@NE2 fudge it for the duration of temporary work and use a node anyway. However sometimes this sort of thing forms the impetus I need to go out and map an area properly.</p>
</div>
<div id="comment-481-info" class="comment-info">
<span class="comment-age">(26 Jul '10, 09:45)</span> <span class="comment-user userinfo">Andrew Chadwick</span>
</div>
</div>
</div>
<div id="comment-tools-458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-458-form-container" class="comment-form-container">
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

