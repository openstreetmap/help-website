+++
type = "question"
title = "Tagging a youth club"
description = '''The title says it all. I feel like in some categories the tags are insanely detailed but anything considering youth is nonexistent, unless i wasn&#x27;t able to find it. Is there a way to add tags in that area? Don&#x27;t want to use &#x27;Pub&#x27; which comes closest but gives off a weird vibe, considering it&#x27;s for y...'''
date = "2020-04-22T09:23:00Z"
lastmod = "2020-04-22T12:24:00Z"
weight = 74325
keywords = [ "youth", "tagging" ]
aliases = [ "/questions/74325" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging a youth club](/questions/74325/tagging-a-youth-club)

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
<span id="post-74325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74325-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The title says it all. I feel like in some categories the tags are insanely detailed but anything considering youth is nonexistent, unless i wasn't able to find it. Is there a way to add tags in that area? Don't want to use 'Pub' which comes closest but gives off a weird vibe, considering it's for youth...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-youth" rel="tag" title="see questions tagged &#39;youth&#39;">youth</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '20, 09:23</strong></p>
<img src="https://secure.gravatar.com/avatar/d61aebfa6ad5f53e2d41ab5efc008d60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="The%20Wololo&#39;s gravatar image" />
<p><span>The Wololo</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="The Wololo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74325" class="comments-container">
&#10;</div>
<div id="comment-tools-74325" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74325-form-container" class="comment-form-container">
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

<span id="74326"></span>

<div id="answer-container-74326" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74326-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-74326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are basically a range of (rather similar) options:</p>
<ul>
<li>amenity=<code>community_centre</code> with '<code>community_centre</code>='<code>youth_centre</code>'</li>
<li>amenity=<code>'youth_club'</code></li>
<li>amenity=<code>'youth_centre'</code></li>
<li>club=youth</li>
<li>Surprisingly amenity=<code>'social_facility'</code> with <code>'social_facility'</code>=<code>'youth_club'</code> does not appear to be used, although in my view this would be appropriate for many run in deprived areas with outreach workers. Various other '<code>social_facility'</code>:* tags allows greater precision.</li>
</ul>
<p>The former is more widely used, but it's popularity is hard to assess as some of these values are as a result of a remote edit by a single contributor. Personally, I've always been a bit wary of reducing really widespread things like community halls, youth clubs etc to subtags of another tag. My general view is that if something is common it is best supported by a single 'top-level tag. Of course it may be that <code>community_centre</code>, <code>social_facility</code> etc are themselves itself on its way to being a top-level tag in its own right, which would remove my reservations.</p>
<p>I do very much like using amenity=<code>social_facility</code> with the range of other tags for places which are difficult to categorise (secure facilities for difficult children for instance), and this approach still requires use of the amenity key.</p>
<p>No doubt there are some clubs for young people which are more of the nature of pure clubs, and for these the club key will be appropriate. This key can also be used together with the above recommendations.</p>
<p>A note about usage in Britain. Youth clubs are of a wide range of forms: anything from Army Cadets, Young Farmers, through Boys Clubs to modern youth clubs led by trained social workers in deprived areas usually based in a community centre. A single tagging scheme for this range of usage is probably not very sensible. Army Cadets is a bit more than a club for young people, the ones run by professional workers are much more social facilities whereas Young Farmers is clearly a type of club. Classically what is meant by a youth club stems from the Boys &amp; Lads Club movement. When I was a teenager there were many of these around Nottingham, usually with a sports hall, snooker tables, a dry bar and areas for informal socialising. They were run by charities with a membership fee. In many ways they were analogous to working mens clubs but for people under the legal age for drinking. Some still exist, but not being in the target age range I have no idea how popular they are.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '20, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-74326" class="comments-container">
<span id="74328"></span>
<div id="comment-74328" class="comment">
<div id="post-74328-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately, as SK53 hints at, this is an area that has suffered from a bit of "tagfiddling" in the past. As an example, see <a href="https://www.openstreetmap.org/changeset/35253388">here</a> (that changeset was unhelpfully labelled "UK: landuse refinements") which changed the tags <a href="https://www.openstreetmap.org/node/568630560/history">here</a> into <a href="https://www.openstreetmap.org/way/379857288/history">these</a>.</p>
<p>For the typical youth club in my mind's eye I'd use "amenity=youth_club" of the options above, but of course an individual example may lean toward other tagging, dependent on context.</p>
</div>
<div id="comment-74328-info" class="comment-info">
<span class="comment-age">(22 Apr '20, 12:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74326" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74326-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74327"></span>

<div id="answer-container-74327" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74327-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's one as an example. <a href="https://www.openstreetmap.org/#map=18/52.33998/-0.18341">https://www.openstreetmap.org/#map=18/52.33998/-0.18341</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '20, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-74327" class="comments-container">
<span id="74329"></span>
<div id="comment-74329" class="comment">
<div id="post-74329-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If <a href="https://www.openstreetmap.org/way/107609397/history">https://www.openstreetmap.org/way/107609397/history</a> has a name rather than simply "youth club" I'd suggest using that. It may not have one of course - it might be known to all and sundry as simply "The Youth Club".</p>
</div>
<div id="comment-74329-info" class="comment-info">
<span class="comment-age">(22 Apr '20, 12:24)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74327" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74327-form-container" class="comment-form-container">
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

