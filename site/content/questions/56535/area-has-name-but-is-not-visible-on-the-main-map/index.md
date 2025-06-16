+++
type = "question"
title = "Area has name, but is not visible on the main map"
description = '''I am trying to name an area but the name only shows in my &quot;edit&quot; mode. It been a week now and other names I added is showed in the map. It is the area named Poppeludden, way #497816343, which I added on 2017-06-03. I must have done something wrong but no idea what it is and how I can fix it. Is ther...'''
date = "2017-06-08T15:45:00Z"
lastmod = "2017-06-09T18:14:00Z"
weight = 56535
keywords = [ "tagging", "area" ]
aliases = [ "/questions/56535" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Area has name, but is not visible on the main map](/questions/56535/area-has-name-but-is-not-visible-on-the-main-map)

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
<span id="post-56535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56535-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to name an area but the name only shows in my "edit" mode. It been a week now and other names I added is showed in the map. It is the area named Poppeludden, <a href="https://www.openstreetmap.org/way/497816343">way #497816343</a>, which I added on 2017-06-03.</p>
<p>I must have done something wrong but no idea what it is and how I can fix it. Is there any videoguide that shows it, how to do it step my by step?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '17, 15:45</strong></p>
<img src="https://secure.gravatar.com/avatar/d63f90c86920552fa8a5c9b0d9402bcc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ironwalkers&#39;s gravatar image" />
<p><span>Ironwalkers</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ironwalkers has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jun '17, 13:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span></p>
</div>
</div>
<div id="comments-container-56535" class="comments-container">
&#10;</div>
<div id="comment-tools-56535" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56535-form-container" class="comment-form-container">
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

<span id="56538"></span>

<div id="answer-container-56538" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56538-score" class="post-score" title="current number of votes">
11
</div>
<span id="post-56538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tagging a polygon with area=yes and a name does not supply enough information for rendering software to make an intelligent choice about how to make it visible.</p>
<p>If there is a corresponding landuse for the area in question, for example, landuse=industrial, or if the area is a park, tagged with leisure=park, then it would become visible on most maps. By the way, once you choose some other scheme to tag your area, in most cases the area=yes tag becomes redundant and should be deleted. (Exceptions to this rule that I'm aware of are highway=pedestrian and running tracks where one may tag the track with area=no.)</p>
<p>Even were you to determine that some other tags describe your area better, there are many objects that will not be rendered. This can happen for many reasons but often it's because there are too few of the objects in existence to justify the effort to render it or so many that the map would become cluttered (example: power lines and poles).</p>
<p>The question you need to ask yourself is; what is this area and how should I tag it? Leave the whole question of rendering out of your decision making process.</p>
<p>Best,</p>
<p>Dave</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '17, 18:57</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-56538" class="comments-container">
<span id="56544"></span>
<div id="comment-56544" class="comment">
<div id="post-56544-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>This is a little part in a park.</p>
</div>
<div id="comment-56544-info" class="comment-info">
<span class="comment-age">(09 Jun '17, 07:22)</span> <span class="comment-user userinfo">Ironwalkers</span>
</div>
</div>
<span id="56555"></span>
<div id="comment-56555" class="comment">
<div id="post-56555-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/13810/ironwalkers">@Ironwalkers</a>: That's not enough information. <em>What</em> part of the park is it? What makes it different from the park around it? Is it a sports pitch? A garden with a specific theme? Or is it just an area that happens to have a name of its own for whatever reason?</p>
</div>
<div id="comment-56555-info" class="comment-info">
<span class="comment-age">(09 Jun '17, 13:51)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="56556"></span>
<div id="comment-56556" class="comment">
<div id="post-56556-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it is the last thing</p>
<p>just an area that happens to have a name</p>
</div>
<div id="comment-56556-info" class="comment-info">
<span class="comment-age">(09 Jun '17, 13:54)</span> <span class="comment-user userinfo">Ironwalkers</span>
</div>
</div>
<span id="56563"></span>
<div id="comment-56563" class="comment">
<div id="post-56563-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If it's just a place with a name you could tag it with place=locality. The Wiki says, "The place=locality tag can be used to name an unpopulated place which is not associated with any existing feature to which such a tag could be associated."</p>
<p>In other words, if it's not a park or some sort of landuse (industrial, forest, etc.), not a settlement or village of some sort, then the locality tag is the one to use.</p>
</div>
<div id="comment-56563-info" class="comment-info">
<span class="comment-age">(09 Jun '17, 18:14)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-56538" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56538-form-container" class="comment-form-container">
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

