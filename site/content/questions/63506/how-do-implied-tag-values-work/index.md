+++
type = "question"
title = "How do implied tag values work?"
description = '''I&#x27;m trying to understand how implied tags work. I&#x27;ve been doing some Googling and searching around on the OSM wiki, but haven&#x27;t clearly understood them.   If I tag a way highway=footway, then (by this list), a routing engine will assume that this path cannot be used for motor vehicles (as if the way...'''
date = "2018-05-16T14:27:00Z"
lastmod = "2018-05-16T16:21:00Z"
weight = 63506
keywords = [ "access", "tagging" ]
aliases = [ "/questions/63506" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do implied tag values work?](/questions/63506/how-do-implied-tag-values-work)

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
<span id="post-63506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63506-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to understand how implied tags work. I've been doing some Googling and searching around on the OSM wiki, but haven't clearly understood them.</p>
<ul>
<li>If I tag a way <code>highway=footway</code>, then (by <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">this list</a>), a routing engine will assume that this path cannot be used for motor vehicles (as if the way was tagged <code>motor_vehicle=no</code>) - depending on the country. Is this correct? Is this implied tagging implemented in each routing engine separately, or is it a built-in feature of the OSM database (i.e. is there a "master" list)?</li>
<li>The implied access tags for highway tags seems to be <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">reasonably well documented</a>, but other tags (notably barriers) seem to have implied tags as well. For example, <code>barrier=bollard</code> (according to <a href="https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dbollard">the wiki</a>) implies <code>foot=yes</code> and <code>bicycle=yes</code>. This documented on the wiki page for that specific tag - is there a central list of these implied tags? And, like above, I take it these are implemented at the behest of every routing engine programmer?</li>
<li>Can I "override" an implied tag, or is this a bad idea? For example, explicitly tagging <code>foot=no</code> on a <code>highway=path</code> if (by sign) pedestrians are not allowed on that path (even though, by default, <code>highway=path</code> implies <code>foot=yes</code>)?</li>
<li>Are there other kinds of implied tags, other than access tags?</li>
</ul>
<p>The reason I stumbled across this is that I do a lot of bicycle-related tagging, and I'm perenially checking the wiki to make sure that the features I'm tagging (based on what I see on the ground) don't by accident imply access tags that would cause routers to route i.A. bicycle traffic a different way.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 May '18, 14:27</strong></p>
<img src="https://secure.gravatar.com/avatar/390c3a1e9ea7b1f10deea61828ad66eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lightsider&#39;s gravatar image" />
<p><span>Lightsider</span><br />
<span class="score" title="1540 reputation points"><span>1.5k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lightsider has 9 accepted answers">42%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 May '18, 14:31</strong> </span></p>
</div>
</div>
<div id="comments-container-63506" class="comments-container">
&#10;</div>
<div id="comment-tools-63506" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63506-form-container" class="comment-form-container">
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

<span id="63514"></span>

<div id="answer-container-63514" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63514-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Lightsider has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ul>
<li>Routing engine developers are responsible for making sure their routing engine assumes sensible defaults, which is done separately for every application consuming OSM data. This is not built into the OSM database at all. It's just a set of conventions that mappers and developers (hopefully) agree on, and it's documented on the wiki in the hopes of achieving this agreement and avoiding misunderstandings. Unfortunately, this does not always work, and you sometimes end up with routing engines making mutually incompatible assumptions as a result.</li>
<li>There's no central list of default values and implied tags that I know of. The "implies" field from the wiki infobox template is, in theory, machine readable. In practice, I believe these tend to be implemented manually by data consumers in their respective projects.</li>
<li>Yes, you can override defaults. It's not unusual and it is often necessary to do so.</li>
<li>There are a couple examples that are unrelated to access restrictions, such as <code>amenity=drinking_water</code> implying <code>drinking_water=yes</code>, but these aren't very common.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '18, 16:21</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-63514" class="comments-container">
&#10;</div>
<div id="comment-tools-63514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63514-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63507"></span>

<div id="answer-container-63507" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63507-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63507-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-63507-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's no master list. Even if there was, a given routing engine could ignore it. The various wiki pages are probably the closest thing to a "central" list, but you can also look for rules <a href="https://github.com/Project-OSRM/osrm-backend/blob/master/profiles/bicycle.lua">implemented by a given engine</a>.</p>
<p>It's okay to override an access tag. But consider using some other <code>highway</code> tag than <code>highway=path</code> if foot access isn't allowed, like if it is a for bicycles, <code>highway=cycleway</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '18, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-63507" class="comments-container">
&#10;</div>
<div id="comment-tools-63507" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63507-form-container" class="comment-form-container">
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

