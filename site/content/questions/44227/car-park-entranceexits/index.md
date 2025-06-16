+++
type = "question"
title = "Car park entrance/exits"
description = '''Is there a way to tag car park entrances and exits, if the route of vehicles within the car park is not known? In the past I have just tagged the entrance/exit roads with the appropriate oneway tag, but it seems oneways that do not create a loop seem to be viewed as errors. Recently there has been a...'''
date = "2015-07-17T00:49:00Z"
lastmod = "2016-02-20T17:47:00Z"
weight = 44227
keywords = [ "parking_entrance", "exit", "oneway" ]
aliases = [ "/questions/44227" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Car park entrance/exits](/questions/44227/car-park-entranceexits)

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
<span id="post-44227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44227-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-44227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to tag car park entrances and exits, if the route of vehicles within the car park is not known?</p>
<p>In the past I have just tagged the entrance/exit roads with the appropriate oneway tag, but it seems oneways that do not create a loop seem to be viewed as errors. Recently there has been a flurry of people playing the <a href="http://osmlab.github.io/to-fix/#/task/deadendoneway">http://osmlab.github.io/to-fix/#/task/deadendoneway</a> game going around stripping entrance/exit roads of their oneway tag</p>
<p>eg <a href="https://www.openstreetmap.org/way/228323772">https://www.openstreetmap.org/way/228323772</a> is the exit from an underground car park below the visible upper one</p>
<p>If I can't tag them as oneway, is there a way to tag them as entrance/exit roads and the traffic direction to be interpolated from that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-parking_entrance" rel="tag" title="see questions tagged &#39;parking_entrance&#39;">parking_entrance</span> <span class="post-tag tag-link-exit" rel="tag" title="see questions tagged &#39;exit&#39;">exit</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jul '15, 00:49</strong></p>
<img src="https://secure.gravatar.com/avatar/7c24812608179f09b4374b3231cfb750?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YoP&#39;s gravatar image" />
<p><span>YoP</span><br />
<span class="score" title="506 reputation points">506</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YoP has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jul '15, 00:55</strong> </span></p>
</div>
</div>
<div id="comments-container-44227" class="comments-container">
&#10;</div>
<div id="comment-tools-44227" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44227-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="44236"></span>

<div id="answer-container-44236" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44236-score" class="post-score" title="current number of votes">
12
</div>
<span id="post-44236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a massive difference on OpenStreetMap between inaccurate and accurate, but incomplete, data.</p>
<p>Stub ways showing the direction of service roads entering &amp; leaving car parks clearly fall into the latter category. They have useful information, and are not wrong.</p>
<p>I would politely ask the people removing this information to desist: they clearly have a less clear picture of the situation than the original mapper. I'm afraid it's a case of blindly following a false positive from a QA tool. They should also be requested to revert edits which have removed valid information from OSM.</p>
<p>It may help to add other tags, but I would suggest following a couple of fairly widely used conventions by adding a <a href="https://wiki.openstreetmap.org/wiki/Key:fixme">fixme</a> tag:</p>
<ul>
<li>Add <code>fixme=continue</code> on the last unattached node of the way.</li>
<li>Add a <code>fixme=stub for further survey</code> to the way itself.</li>
</ul>
<p>A much less used convention would be to add a further way connecting entrance &amp; exit purely to illustrate the correct connectivity. This could be tagged <code>artificial_path=yes</code>, which has been used for rivers/streams passing through lakes and reservoirs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '15, 11:03</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jul '15, 10:03</strong> </span></p>
</div>
</div>
<div id="comments-container-44236" class="comments-container">
<span id="44284"></span>
<div id="comment-44284" class="comment">
<div id="post-44284-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good advice. Note that it's "fixme=continue" (not "continues"), according to both wiki and current usage. I corrected that part.</p>
</div>
<div id="comment-44284-info" class="comment-info">
<span class="comment-age">(20 Jul '15, 08:20)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="44291"></span>
<div id="comment-44291" class="comment">
<div id="post-44291-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I happen to use fixme=continues, which seems more natural to me. More to the point it really doesnt matter which is used: it is there to help people avoid blunders of removing reasonable data.</p>
</div>
<div id="comment-44291-info" class="comment-info">
<span class="comment-age">(20 Jul '15, 10:02)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44236" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44236-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44231"></span>

<div id="answer-container-44231" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44231-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking_entrance">amenity=parking_entrance</a>, but I don't know whether all QA-tools and validators take it into account.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '15, 06:45</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-44231" class="comments-container">
&#10;</div>
<div id="comment-tools-44231" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44231-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44283"></span>

<div id="answer-container-44283" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44283-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could resolve this by adding the missing parking area, even if only approximately.</p>
<p>Add an area to indicate the underground car park. It need not be absolutely precise, but you can probably roughly guess the area (e.g. from the various entries). Tag it as "amenity=parking", "parking=underground", "level=-1", and possibly "fixme=resurvey" to indicate the area is only estimated.</p>
<p>SK53's answer still stands: It is incorrect to blindly correct this, but by mapping it like this you avoid any ambiguity, and provide valuable information (namely that there is an underground car park, which for example routers may offer to people looking for parking).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jul '15, 08:17</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-44283" class="comments-container">
&#10;</div>
<div id="comment-tools-44283" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44283-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48242"></span>

<div id="answer-container-48242" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48242-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<blockquote>
<p>Is there a way to tag car park <strong>entrances</strong> and <strong>exits</strong>, if the route of vehicles within the car park is not known?</p>
</blockquote>
</blockquote>
<p>I agree. IMHO... Just as streets are usually tagged as unidirectional or bidirectional, All entry/exit points to those roads should be as well. This should help navigation to proper point to the amenity to avoid future glitches that could result in vehicular collisions.</p>
<blockquote>
<blockquote>
<p>eg <a href="https://www.openstreetmap.org/way/228323772">https://www.openstreetmap.org/way/228323772</a> is the exit from an underground car park below the visible upper one</p>
</blockquote>
</blockquote>
<p><a href="https://www.openstreetmap.org/?mlat=47.61599&amp;mlon=-122.34063#map=19/47.61599/-122.34063">This exit only point</a> will become an unidirectional exit only linked underground to <a href="https://www.openstreetmap.org/?mlat=47.61584&amp;mlon=-122.34058#map=19/47.61584/-122.34058">this entry/exit bidirectional parking entry/exit point</a>.</p>
<blockquote>
<blockquote>
<p>If I can't tag them as one-way, is there a way to tag them as entrance/exit roads and the traffic direction to be interpolated from that?</p>
</blockquote>
</blockquote>
<p>So my question is similar to the original post.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '16, 17:47</strong></p>
<img src="https://secure.gravatar.com/avatar/45200d6c589a6bb79222db45c233025d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EugeneWII&#39;s gravatar image" />
<p><span>EugeneWII</span><br />
<span class="score" title="44 reputation points">44</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EugeneWII has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48242" class="comments-container">
&#10;</div>
<div id="comment-tools-48242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48242-form-container" class="comment-form-container">
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

