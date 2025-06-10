+++
type = "question"
title = "Two synonymous tag systems - apply both?"
description = '''I want to map a sanitary disposal station for boats to empty their chemical toilets. Using https://taginfo.openstreetmap.org I have found a number of tags for this and they are not applied consistently at all: amenity=sanitary_dump_station - 3 109 instances sanitary_dump_station=yes - 2 579 instance...'''
date = "2019-07-04T19:29:00Z"
lastmod = "2019-07-05T10:09:00Z"
weight = 69884
keywords = [ "retagging", "tagging" ]
aliases = [ "/questions/69884" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Two synonymous tag systems - apply both?](/questions/69884/two-synonymous-tag-systems-apply-both)

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
<span id="post-69884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69884-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to map a sanitary disposal station for boats to empty their chemical toilets.</p>
<p>Using <a href="https://taginfo.openstreetmap.org">https://taginfo.openstreetmap.org</a> I have found a number of tags for this and they are not applied consistently at all:</p>
<pre><code>amenity=sanitary_dump_station - 3 109 instances
sanitary_dump_station=yes - 2 579 instances
waterway=sanitary_dump_station - 470 instances
waste=excrements = 92 instances
waste=solid_waste = 92 instances
waste=toilet = 68 instances
waste=excrement = 17 instances
waste=chemical_toilet = 11 instances
waste=Solid␣Waste = 6 instances
waste=toilets = 6 instances
waste=human_excrement = 3 instances</code></pre>
<p>All of these are interchangable. I'm inclined to use waterway=sanitary_dump_station as these are specific to boaters. However I feel like many of these other tags could be useful when searching for these facilities - is it acceptable to tag more than one synonymous tag? For example, the following three:</p>
<pre><code>amenity=sanitary_dump_station
sanitary_dump_station=yes
waterway=sanitary_dump_station</code></pre>
<p>Or if I choose one of these tags, would it be acceptable to standardise the tags across the country (or the whole map)?</p>
<p>There are also some extra fields in the sanitary_dump_station namespace that are a bit more specific:</p>
<pre><code>sanitary_dump_station:pump-out = 384 instances
sanitary_dump_station:chemical_toilet = 308 instances
sanitary_dump_station:basin = 207 instances
sanitary_dump_station:gravity = 195 instances
sanitary_dump_station:suction = 98 instances
sanitary_waste_station:chemical_toilet = 1 instance</code></pre>
<p>I'd like to apply these where applicable, too. These aren't synonymous.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-retagging" rel="tag" title="see questions tagged &#39;retagging&#39;">retagging</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '19, 19:29</strong></p>
<img src="https://secure.gravatar.com/avatar/9f678904f8d9e865e21514a2140742bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivansams&#39;s gravatar image" />
<p><span>ivansams</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivansams has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69884" class="comments-container">
&#10;</div>
<div id="comment-tools-69884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69884-form-container" class="comment-form-container">
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

<span id="69888"></span>

<div id="answer-container-69888" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69888-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-69888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ivansams has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would only tag it the way most people tagged it, thus as amenity=sanitary_dump_station. It also has a <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity=sanitary_dump_station">wiki page</a> and an <a href="https://wiki.openstreetmap.org/wiki/Toilet_Holding_Tank_Disposal">accompanying page</a> giving an overview. It seems like all the other tags were proposals, but only this one got approved.</p>
<p>If you really do not agree with a certain tagging scheme (because it lacks details, is just plain wrong or another good reason), you could use an alternative tagging schema, otherwise, stick with the approved or most popular one. There is, in general, no reason to use tags from 2 schemas when one is approved.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '19, 04:24</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-69888" class="comments-container">
&#10;</div>
<div id="comment-tools-69888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69888-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69891"></span>

<div id="answer-container-69891" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69891-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Agreed to escada's answer.</p>
<p>Adding to that: amenity= <em>and waterway=</em> are primary tags. Either could be used for the feature in general but you should only use one. I'd go with amenity=sanitary_dump_station as there is no principal difference between a dump station for boats or road vehicles. So why let the former stand out by using waterway?</p>
<p>sanitary_dump_station=yes on the other hand should only be used as a secondary tag. If you for example map a marina as one big feature and only want to indicate that is possesses a dump station without mapping it individually you would add sanitary_dump_station=yes to the marina object.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '19, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-69891" class="comments-container">
&#10;</div>
<div id="comment-tools-69891" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69891-form-container" class="comment-form-container">
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

