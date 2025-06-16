+++
type = "question"
title = "Is there a way to detect very sharp angles of buildings?"
description = '''Hi everyone. I&#x27;m trying to fix several buildings having very sharp angles (see photos below), looks like they were unintentionally caused by the extrude tool in JOSM. It&#x27;s hard to find them by eyes as they need to be zoomed very close to be seen. Is there a way to detect these using JOSM or another ...'''
date = "2018-09-30T15:42:00Z"
lastmod = "2018-10-17T11:54:00Z"
weight = 66104
keywords = [ "building", "josm", "angle", "quality_assurance" ]
aliases = [ "/questions/66104" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to detect very sharp angles of buildings?](/questions/66104/is-there-a-way-to-detect-very-sharp-angles-of-buildings)

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
<span id="post-66104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66104-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-66104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone.</p>
<p>I'm trying to fix several buildings having very sharp angles (see photos below), looks like they were unintentionally caused by the extrude tool in JOSM. It's hard to find them by eyes as they need to be zoomed very close to be seen.</p>
<p>Is there a way to detect these using JOSM or another tool?</p>
<p><img src="/upfiles/17-27-08.png" alt="alt text" /></p>
<p><img src="/upfiles/17-29-09.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-angle" rel="tag" title="see questions tagged &#39;angle&#39;">angle</span> <span class="post-tag tag-link-quality_assurance" rel="tag" title="see questions tagged &#39;quality_assurance&#39;">quality_assurance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Sep '18, 15:42</strong></p>
<img src="https://secure.gravatar.com/avatar/15d45a99f101e06c9e79916af33f8336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Privatemajory&#39;s gravatar image" />
<p><span>Privatemajory</span><br />
<span class="score" title="1125 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Privatemajory has 4 accepted answers">23%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Sep '18, 15:49</strong> </span></p>
</div>
</div>
<div id="comments-container-66104" class="comments-container">
&#10;</div>
<div id="comment-tools-66104" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66104-form-container" class="comment-form-container">
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

<span id="66105"></span>

<div id="answer-container-66105" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66105-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While not the actual heuristic you are looking for, JOSM's validator would detect a "building with almost-right angle" info-level validation error for your examples.</p>
<p>JOSM <a href="https://josm.openstreetmap.de/ticket/15044">bug 15044</a> looks like wht you're looking for, but isn't implemented yet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '18, 01:01</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</img>
</div>
</div>
<div id="comments-container-66105" class="comments-container">
<span id="66106"></span>
<div id="comment-66106" class="comment">
<div id="post-66106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, if "almost-right" angles are already detected, it shouldn't be very hard for them to implement a detection of "almost-flat" angles too.</p>
</div>
<div id="comment-66106-info" class="comment-info">
<span class="comment-age">(01 Oct '18, 04:18)</span> <span class="comment-user userinfo">Privatemajory</span>
</div>
</div>
<span id="66110"></span>
<div id="comment-66110" class="comment">
<div id="post-66110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I believe MapBox did run such an algorithm on OSM data, but I'm not sure if all such bugs were surfaced publicly. I cant see anything in the most widely used debug/lint tools: Osmose &amp; KeepRight. At least some of these features are known as kickbacks &amp; spikes in GIS circles. It may be possible to find a suitable spatial validation tool which works with opensource software such as QGIS.</p>
</div>
<div id="comment-66110-info" class="comment-info">
<span class="comment-age">(01 Oct '18, 14:08)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66105-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66366"></span>

<div id="answer-container-66366" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66366-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not sure how others are handling the issue but in most of the OSM maps the sharp angles (the spikes) are present. Besides the buildings the spiky configurations are present an other geometries like roads, roundabouts and so on. In almost all cases, spiky configurations are errors. Because of the maps' start scale, antialias rendering and object overlaps spikes are hardly visible and consequently they remain in the source indefinitely. At the same time, vector based GIS and map-makers should (and they do) have a tool to detect and remove spiky configurations. Actually, spikes are just special cases of tiny outgrowths created bay data generalisation while creating the scale/zoom levels (on fiords, peninsulas, tributaries and so on) and should be programmatically detected and removed. Therefor robust map-makers never see spikes in their maps.<br />
The algorithms for the outgrowths is too complex and complicated to apply if only the spiky buildings are in focus. For this simple issue I have made a special algorithm presented in a meta language so anyone can make a program to detect and remove spikes on buildings in any languages. Besides, I have made a test and demo using OSM buildings for the UK. The algorithm, the demonstration, many examples and a visual analyses is presented/described with details here<br />
<a href="https://drive.google.com/open?id=1MaLdnSnc454xKjn3eL95vDQKeoIW8zGU">https://drive.google.com/open?id=1MaLdnSnc454xKjn3eL95vDQKeoIW8zGU</a><br />
The result and the analyses show that out of about 5625K buildings 2834 are with spiky configurations. These are detected and corrected. So, if interested, enjoy the paper in the link.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '18, 07:07</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-66366" class="comments-container">
<span id="66370"></span>
<div id="comment-66370" class="comment">
<div id="post-66370-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/3194/sanser">@sanser</a> for this! I'm no programmer, but perhaps your algorithm could be implemented in a JavaScript/Python script and be used on JOSM through the scripting plugin? If yes, I guess we're close to a solution.</p>
</div>
<div id="comment-66370-info" class="comment-info">
<span class="comment-age">(17 Oct '18, 11:54)</span> <span class="comment-user userinfo">Privatemajory</span>
</div>
</div>
</div>
<div id="comment-tools-66366" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66366-form-container" class="comment-form-container">
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

