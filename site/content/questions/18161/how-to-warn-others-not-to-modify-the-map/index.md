+++
type = "question"
title = "How to warn others not to modify the map"
description = '''In the city that I live, there is a very important newly built road junction. The bing&#x27;s satellite photo represents the old structure of the junction which is completely different from its current state. Based on my knowledge and GPS data I corrected the junction in the OSM. However, I fear that any...'''
date = "2012-12-03T07:51:00Z"
lastmod = "2023-01-16T12:12:00Z"
weight = 18161
keywords = [ "map", "satellite-images" ]
aliases = [ "/questions/18161" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to warn others not to modify the map](/questions/18161/how-to-warn-others-not-to-modify-the-map)

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
<span id="post-18161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18161-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the city that I live, there is a very important newly built road junction. The bing's satellite photo represents the old structure of the junction which is completely different from its current state.</p>
<p>Based on my knowledge and GPS data I corrected the junction in the OSM. However, I fear that anyone can remodify it to its previous form based on the bing's old satellite image.</p>
<p>Is there any way to warn users who blindly try to modify the corresponding part of the map based on satellite image?</p>
<p>Similarly, is there anyway to indicate regions for which the satellite photos do not represents the current structure?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-satellite-images" rel="tag" title="see questions tagged &#39;satellite-images&#39;">satellite-images</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '12, 07:51</strong></p>
<img src="https://secure.gravatar.com/avatar/b357be198f4d267d029942e5135da35b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yigiter&#39;s gravatar image" />
<p><span>yigiter</span><br />
<span class="score" title="96 reputation points">96</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yigiter has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Dec '12, 07:52</strong> </span></p>
</div>
</div>
<div id="comments-container-18161" class="comments-container">
&#10;</div>
<div id="comment-tools-18161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18161-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="18163"></span>

<div id="answer-container-18163" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18163-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-18163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yigiter has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's not widely accepted way to achieve this. I would recommend placing a <a href="http://wiki.openstreetmap.org/wiki/Key:note">"note"</a> tag on the junction and putting a message in there.</p>
<p>It would be possible to invent a system whereby editors would display a pop-up warning when edits are made inside an area tagged with certain warning tags, or when an object that carries such tags is modified, but we don't have that yet.</p>
<p>The same applies to aerial imagery offsets - in some areas, some imagery sources might be 10 metres off or more, and it would be great if it were possible to automatically alert users to this situation, rather than having them mindlessly trace from misaligned imagery. Some work has been done towards this (see <a href="http://wiki.openstreetmap.org/wiki/True_Offset_Process)">http://wiki.openstreetmap.org/wiki/True_Offset_Process)</a> and both problems - aerial imagery being out of date, or out of kilter - are really quite similar, but we haven't yet got a universally working solution.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '12, 08:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Dec '12, 08:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span></p>
</div>
</div>
<div id="comments-container-18163" class="comments-container">
<span id="18164"></span>
<div id="comment-18164" class="comment">
<div id="post-18164-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You could perhaps also draw ways where the roads used to be and tag those with a note to make them easier to spot. I think I did something where a building was demolished but it was still visible (of course) in Bing.</p>
</div>
<div id="comment-18164-info" class="comment-info">
<span class="comment-age">(03 Dec '12, 10:02)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-18163" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18163-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18175"></span>

<div id="answer-container-18175" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18175-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps we should ask all users not to modify the map based on aerial imagery alone, since any single source of information can be wrong. Aerial imagery can be either out of date or a few metres adrift in its positioning, and a single GPS trace can be wrong if the GPS receiver was trying to make the best of poor reception. An error of a few metres may seem fairly insignificant, but we can usually do better than that, and anyway it makes for difficulties if another contributor tries to add features using accurate GPS traces, which then fail to line up with the existing mapping.</p>
<p>We should normally try to find at least two separate sources of information before we change the map. Possibly an exception to that principle can be made if the mapping of an area is either blank or very obviously wrong, and there is little information available. In that case even approximate mapping could be seen as an improvement.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '12, 18:54</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Dec '12, 21:01</strong> </span></p>
</div>
</div>
<div id="comments-container-18175" class="comments-container">
<span id="18177"></span>
<div id="comment-18177" class="comment">
<div id="post-18177-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>There's some good stuff there but I'd disagree that "we should normally require at least two separate sources of information before we update the map". OSM is iterative: it gets better and better the more people use it.</p>
<p>If someone mistakenly notes down a street name as "Market Road" when it's actually "Market Street", that's no big deal - a subsequent visitor will come along and correct it. We don't want completely bogus information, of course, but "the perfect is the enemy of the good" as the old phrase goes.</p>
</div>
<div id="comment-18177-info" class="comment-info">
<span class="comment-age">(03 Dec '12, 22:04)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="18204"></span>
<div id="comment-18204" class="comment">
<div id="post-18204-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's a difficult balance to strike. As Madryn says, using a single source can be problematic, but in a blank area something may be better than nothing. However, when something is totally misleading (like a bogus road running along the peaks of the High Atlas Mountains) it could cause harm or at least confusion. In general, if I've entered data on the basis of a single source, I add a "fixme" code asking that the precise location/name/road surface be confirmed. It's relatively easy to find all the "fixme"s in a locality using JOSM, then you head out with a GPS and notepad and check it out!</p>
</div>
<div id="comment-18204-info" class="comment-info">
<span class="comment-age">(05 Dec '12, 12:37)</span> <span class="comment-user userinfo">Dave W Farthing</span>
</div>
</div>
</div>
<div id="comment-tools-18175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18175-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86496"></span>

<div id="answer-container-86496" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86496-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is an old but valid question. We can now add map notes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '23, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-86496" class="comments-container">
<span id="86519"></span>
<div id="comment-86519" class="comment">
<div id="post-86519-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's what I've done for example with a junction near me which has been remodelled. In addition to the Note, I also explained in the Changeset that the aerial photos were out of date and that the revised layout was based on up to date knowledge. So far so good, as nobody has gone in a year later and reversed my changes!</p>
</div>
<div id="comment-86519-info" class="comment-info">
<span class="comment-age">(16 Jan '23, 12:12)</span> <span class="comment-user userinfo">Mikey Co</span>
</div>
</div>
</div>
<div id="comment-tools-86496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86496-form-container" class="comment-form-container">
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

