+++
type = "question"
title = "Disabled Parking"
description = '''I recently gave a talk about OpenStreetMap to a non-technical group. One of the people present was a wheelchair user and he was particularly interested in locating disabled parking. In order to find out what current practice is for tagging AND whether such tags are actually consumed I naturally turn...'''
date = "2016-12-06T10:00:00Z"
lastmod = "2016-12-06T12:03:00Z"
weight = 53258
keywords = [ "disabled", "wiki", "parking" ]
aliases = [ "/questions/53258" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Disabled Parking](/questions/53258/disabled-parking)

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
<span id="post-53258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53258-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-53258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently gave a talk about OpenStreetMap to a non-technical group. One of the people present was a wheelchair user and he was particularly interested in locating disabled parking.</p>
<p>In order to find out what current practice is for tagging <strong>AND</strong> whether such tags are actually consumed I naturally turned to the wiki.</p>
<p>I found the wiki <strong>woefully lacking</strong> in a decent description of how to map disabled parking facilities.</p>
<p>What does exist seems to involve prolonged discussion of use of relations with type=site. Not something I wish to expose to people who arent already heavily committed to OSM.</p>
<p>Please could someone provide a succinct account which I can then recommend to non-OSM specialists?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-disabled" rel="tag" title="see questions tagged &#39;disabled&#39;">disabled</span> <span class="post-tag tag-link-wiki" rel="tag" title="see questions tagged &#39;wiki&#39;">wiki</span> <span class="post-tag tag-link-parking" rel="tag" title="see questions tagged &#39;parking&#39;">parking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '16, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-53258" class="comments-container">
&#10;</div>
<div id="comment-tools-53258" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53258-form-container" class="comment-form-container">
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

<span id="53260"></span>

<div id="answer-container-53260" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53260-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-53260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I agree that the wiki is currently just a mess regarding parking spaces for specific groups of people / purposes.</p>
<p>Personally I map individual parking spaces for disabled people along a road as <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking_space"><code>amenity=parking_space</code></a> + <code>parking_space=disabled</code>. According to <a href="https://taginfo.openstreetmap.org/search?q=parking_space%3Ddisabled">taginfo</a> I'm not alone. I <em>don't</em> use a site relation when mapping individual parking spaces along a road.</p>
<p>For a larger parking areas (<a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking"><code>amenity=parking</code></a>) there is <code>capacity:disabled</code> to define the number of disabled parking spaces. Individual disabled parking spaces inside this parking area can still be mapped using the previous mentioned tags I guess. Even in this case I see absolutely no reason for a site relation since the parking spaces are already located <em>inside</em> the <code>amenity=parking</code> area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '16, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '16, 10:17</strong> </span></p>
</div>
</div>
<div id="comments-container-53260" class="comments-container">
<span id="53261"></span>
<div id="comment-53261" class="comment">
<div id="post-53261-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you know anything about use of these tags by consumers?</p>
<p>And I agree with everyone who says that site relations are pointless in this case.</p>
</div>
<div id="comment-53261-info" class="comment-info">
<span class="comment-age">(06 Dec '16, 11:05)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="53263"></span>
<div id="comment-53263" class="comment">
<div id="post-53263-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>According to the wiki <a href="https://wiki.openstreetmap.org/wiki/Rollstuhlkarte.ch">rollstuhlkarte.ch</a> (a wheelchair map) supports parking_space=disabled. Unfortunately it doesn't have global coverage. The similar project <a href="https://wiki.openstreetmap.org/wiki/Wheelmap">wheelmap</a> doesn't seem to support it yet :/</p>
</div>
<div id="comment-53263-info" class="comment-info">
<span class="comment-age">(06 Dec '16, 12:03)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53260-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53259"></span>

<div id="answer-container-53259" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53259-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It used to be <code>disabled_spaces</code> but looks like <code>capacity:disabled</code> is the latest preferred tag: <a href="https://wiki.openstreetmap.org/wiki/Approved_features/Parking">https://wiki.openstreetmap.org/wiki/Approved_features/Parking</a></p>
<p>The site relation comes into play when you're mapping the individual spaces <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking_space">https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking_space</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '16, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-53259" class="comments-container">
&#10;</div>
<div id="comment-tools-53259" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53259-form-container" class="comment-form-container">
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

