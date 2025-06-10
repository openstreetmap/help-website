+++
type = "question"
title = "An editor puts their name in the source tag"
description = '''When editing some map data in Romania, I found paths marked with source=Lazar C., which is most probably the name of the user who created it. I&#x27;ve already sent them a personal message asking them to tag their new edits correctly. However it turns out there&#x27;s a lot of data tagged this way and it&#x27;s pr...'''
date = "2018-08-19T17:05:00Z"
lastmod = "2018-08-20T13:46:00Z"
weight = 65445
keywords = [ "mass_tagging", "source", "mistake" ]
aliases = [ "/questions/65445" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [An editor puts their name in the source tag](/questions/65445/an-editor-puts-their-name-in-the-source-tag)

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
<span id="post-65445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65445-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When editing some map data in Romania, I found paths marked with <code>source=Lazar C.</code>, which is most probably the name of the user who created it. I've already sent them a personal message asking them to tag their new edits correctly. However it turns out there's <a href="http://overpass-turbo.eu/s/Bdt"><strong>a lot</strong></a> of data tagged this way and it's probably impossible to correct it by hand.</p>
<p>What is the preferred way of dealing with this? Is automatic replacing of <code>source=Lazar C.</code> with <code>source=survey</code> a good idea? Or would it be better to leave the tag unchanged or even mass-remove it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mass_tagging" rel="tag" title="see questions tagged &#39;mass_tagging&#39;">mass_tagging</span> <span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-mistake" rel="tag" title="see questions tagged &#39;mistake&#39;">mistake</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '18, 17:05</strong></p>
<img src="https://secure.gravatar.com/avatar/9b2a13764b560b46cc04e2e0e29940a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m93a&#39;s gravatar image" />
<p><span>m93a</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m93a has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '18, 20:40</strong> </span></p>
</div>
</div>
<div id="comments-container-65445" class="comments-container">
<span id="65452"></span>
<div id="comment-65452" class="comment">
<div id="post-65452-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>It should be noted that source tags on the objects themselves, as opposed to changesets, have fallen out of favour a bit. If that also applies to your local community, it might be better to just remove the tags in question instead of replacing them with a different source tag.</p>
</div>
<div id="comment-65452-info" class="comment-info">
<span class="comment-age">(19 Aug '18, 18:44)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-65445" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65445-form-container" class="comment-form-container">
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

<span id="65454"></span>

<div id="answer-container-65454" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65454-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-65454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's absolutely no need to change this, unless there is a privacy issue. Changing it to survey may well be adding erroneous information.</p>
<p>The source tag is used in many different ways, often particular to a given mapper, or mappers in a given area. The idea that there is a <strong>correct</strong> way to use the tag is an error: there are merely values which because they are more frequent are more recognisable and familiar. Often source tags are left solely on the changeset, or a tag indicating use of aerial imagery has long been superseded by numerous ground truth edits, but the tag remains.</p>
<p>By all means leave a message for the user, or comment on one of their changesets, suggesting use of the more widely used tags. However, if they don't want to follow your suggestion then that's fine too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '18, 18:57</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-65454" class="comments-container">
<span id="65459"></span>
<div id="comment-65459" class="comment">
<div id="post-65459-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>There's no reason to get all relativist about this. There may not be a single correct choice for the source value, but that doesn't mean there aren't clearly wrong values. And using it to store the name of the mapper who added a feature? That's definitely not what the source tag is for.</p>
</div>
<div id="comment-65459-info" class="comment-info">
<span class="comment-age">(20 Aug '18, 07:26)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="65465"></span>
<div id="comment-65465" class="comment">
<div id="post-65465-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I'm not actually being relativist, but I'm certainly opposed to prescriptivist attitudes with respect to tags, much preferring a descriptivist approach. Putting one's own name may be unconventional, but could clearly be parsed as "personal knowledge". Meta tags such as source are much less likely to have clearly wrong values, whereas tags representing real world features it's relatively easy to instantiate clearly incorrect values, so a descriptivist approach is not the same as anything goes. Any way a far more important point is that if we dont know what a tag means, changing it is not a good idea.</p>
</div>
<div id="comment-65465-info" class="comment-info">
<span class="comment-age">(20 Aug '18, 13:46)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65454" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65454-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65460"></span>

<div id="answer-container-65460" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65460-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-65460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First off, you're absolutely correct that this is not what the source tag is for. Using changeset discussions to contact the mapper is a good first step – hopefully this will prevent more such tags being added in the future.</p>
<p>This leaves the question what to do about the existing tags: Getting rid of them right away or removing them over time when the objects in questions are being edited for unrelated reasons?</p>
<p>The latter means that the total number of changes in the objects' edit history will be lower, which some will prefer due to the shorter (and therefore supposedly less cluttered) edit history. However, this is not purely a benefit: Instead of a single edit with a clear, easily visible and easily verified purpose, you would now have this cleanup task mixed into other, unrelated changes.</p>
<p>Doing it alongside other edits also takes a lot longer – this can easily drag on for a decade or so. During this time, new mappers in the area might mistakenly consider this usage of the source tag an example to learn from. Due to this, my suggestion would be to remove them straight away.</p>
<p>Note, however, that such a change is subject to the <a href="https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct">Automated Edits code of conduct</a> – even if you're using JOSM or other normal editing tools to perform it. Fixing your own mistakes is considered acceptable usage – so if you're doing this together with the original mapper, it's arguably ok to proceed. Otherwise, you need to ensure the support of your regional community as described in that document.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '18, 07:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-65460" class="comments-container">
&#10;</div>
<div id="comment-tools-65460" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65460-form-container" class="comment-form-container">
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

