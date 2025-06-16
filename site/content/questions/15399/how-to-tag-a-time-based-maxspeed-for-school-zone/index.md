+++
type = "question"
title = "How to tag a time-based maxspeed for School Zone"
description = '''Hi, In my part of the world we have traffic zones called &quot;School Zones&quot; where all the streets in close proximity to a school are speed limited (usually to 40km/h) on School Days between hours of 0800-0930 and 1430-1600. There appears to be a proposal underway to handle such situations Extended condi...'''
date = "2012-08-22T18:57:00Z"
lastmod = "2017-09-22T12:04:00Z"
weight = 15399
keywords = [ "variable", "speedlimit", "school", "maxspeed", "times" ]
aliases = [ "/questions/15399" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag a time-based maxspeed for School Zone](/questions/15399/how-to-tag-a-time-based-maxspeed-for-school-zone)

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
<span id="post-15399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15399-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-15399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>In my part of the world we have traffic zones called "School Zones" where all the streets in close proximity to a school are speed limited (usually to 40km/h) on School Days between hours of 0800-0930 and 1430-1600.</p>
<p>There appears to be a proposal underway to handle such situations <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Extended_conditions_for_access_tags#Voting">Extended conditions for access tags</a></p>
<p>According to the proposal I would tag along the lines of: maxspeed = 60 (or whatever the "normal" speed limit is) maxspeed:(Mo-Fr 08:00-09:30, 14:30-16:00; PH off; SH off) = 40</p>
<p>When I've tried this, JOSM throws up a warning about whitespace in the key... and it makes me wonder about whether I should even be using it. I understand it's just a proposal and there seems to be some sensible objection to using values to make up a part of the key in such a way - which makes me reluctant to use it.</p>
<p>Is there a better way in which I should tag these restrictions for now?</p>
<p>Should I just tag with the default speed, and use a restriction=school_zone tag just for now, so that I might come back at some later date and retag these when there is an established syntax?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-variable" rel="tag" title="see questions tagged &#39;variable&#39;">variable</span> <span class="post-tag tag-link-speedlimit" rel="tag" title="see questions tagged &#39;speedlimit&#39;">speedlimit</span> <span class="post-tag tag-link-school" rel="tag" title="see questions tagged &#39;school&#39;">school</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-times" rel="tag" title="see questions tagged &#39;times&#39;">times</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '12, 18:57</strong></p>
<img src="https://secure.gravatar.com/avatar/4200f1aaa4fa9ccd4d02db2e8e670de1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wolftracker&#39;s gravatar image" />
<p><span>wolftracker</span><br />
<span class="score" title="475 reputation points">475</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wolftracker has 2 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-15399" class="comments-container">
&#10;</div>
<div id="comment-tools-15399" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15399-form-container" class="comment-form-container">
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

<span id="59719"></span>

<div id="answer-container-59719" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59719-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59719-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-59719-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have been using <code>maxspeed:conditional</code>=<code>40 @ (Mo-Fr 08:00-09:30, 14:30-16:00;PH off;SH off)</code> for tagging school zones in my area (QLD, Australia).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '17, 07:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7c4d5ade9c09fca7abccb79e51816879?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Dean&#39;s gravatar image" />
<p><span>David Dean</span><br />
<span class="score" title="541 reputation points">541</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Dean has 2 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-59719" class="comments-container">
<span id="59720"></span>
<div id="comment-59720" class="comment">
<div id="post-59720-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, this is currently the best solution. <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">Conditional restrictions</a> are more and more common.</p>
</div>
<div id="comment-59720-info" class="comment-info">
<span class="comment-age">(20 Sep '17, 07:56)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-59719" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59719-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15424"></span>

<div id="answer-container-15424" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15424-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-15424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Updated answer:</p>
<p>Meanwhile <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">conditional restrictions</a> are widely in use. They are very flexible and allow to specify various access restrictions based on time (based on the <a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours">opening_hours</a> syntax), transportation mode, purpose of access and many more.</p>
<p>See David Dean's answer for a good example.</p>
<p>Old, outdated answer:</p>
<p><del>First, JOSM and other editors never know all tags in use and especially not every proposal because you can use <a href="https://wiki.openstreetmap.org/wiki/Any_tags_you_like">any tags you like</a>. Whitespaces are unusual for most keys but they can still be valid.</del></p>
<del></del>
<p>And you are right, these extended access conditions are just a proposal. Yet it seems that there is no better way of specifying such conditions at the moment. The <a href="https://wiki.openstreetmap.org/wiki/Key:access">access wiki page</a> also lists <a href="https://wiki.openstreetmap.org/wiki/Key:access#Access_time_restrictions">date_on, date_off etc.</a> which aren't much easier to use and which can't handle such complex conditions at all, especially when having multiple time ranges.</p>
<p>Furthermore, most current tools won't be able to parse any of those tags as they aren't widely in use and require a rather complex parser. Also most end devices like sat navs don't support such complex conditions anyway.</p>
<p>Still there is a valid reason to include them in OSM as they probably will become more important in the future. Even if the syntax changes, conditions like <em>Mo-Fr 08:00-09:30, 14:30-16:00</em> can be converted to other formats with only little work. They are also easy to read for humans so that a simple tool can at least just display them without parsing.</p>
</strike>
<p><del>So if you like, use this proposal to tag these conditions. Even if no current tool can handle them or even if some tools complain, it isn't wrong to enter them into the database as long as they provide useful information.</del></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '12, 07:40</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '17, 10:12</strong> </span></p>
</div>
</div>
<div id="comments-container-15424" class="comments-container">
<span id="15461"></span>
<div id="comment-15461" class="comment">
<div id="post-15461-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you very much. Your answer raises many good points. Given the uncertainty of the proposal, and the likely need to tweak the syntax, I'm now thinking the best interim solution is to use restriction=school_zone, and place the extra information about days and times either as a note= or a description=</p>
</div>
<div id="comment-15461-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 18:24)</span> <span class="comment-user userinfo">wolftracker</span>
</div>
</div>
<span id="59729"></span>
<div id="comment-59729" class="comment">
<div id="post-59729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The "Extended conditions for access tags" proposal is now obsolete and has been replaced with <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">Conditional restrictions</a>. Perhaps the accepted answer can be updated a bit?</p>
</div>
<div id="comment-59729-info" class="comment-info">
<span class="comment-age">(20 Sep '17, 15:17)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="59762"></span>
<div id="comment-59762" class="comment">
<div id="post-59762-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14/tordanik">@Tordanik</a> I updated the answer, thanks for the hint.</p>
</div>
<div id="comment-59762-info" class="comment-info">
<span class="comment-age">(22 Sep '17, 10:13)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="59769"></span>
<div id="comment-59769" class="comment">
<div id="post-59769-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've taken the liberty of changing the accepted answer to the other one since everyone's now agreed on it - hope this is OK!</p>
</div>
<div id="comment-59769-info" class="comment-info">
<span class="comment-age">(22 Sep '17, 12:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15424" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15424-form-container" class="comment-form-container">
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

