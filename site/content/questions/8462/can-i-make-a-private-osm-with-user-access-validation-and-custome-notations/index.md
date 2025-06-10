+++
type = "question"
title = "Can i make a private osm, with user access validation and custome notations?"
description = '''How could that be implemented? Should i make a private server? Would i be able to make modifications to the map? Please help me with this,i&#x27;m just making my first steps.'''
date = "2011-10-15T20:50:00Z"
lastmod = "2013-05-31T03:42:00Z"
weight = 8462
keywords = [ "modification", "markers", "private", "custom" ]
aliases = [ "/questions/8462" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can i make a private osm, with user access validation and custome notations?](/questions/8462/can-i-make-a-private-osm-with-user-access-validation-and-custome-notations)

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
<span id="post-8462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8462-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How could that be implemented? Should i make a private server? Would i be able to make modifications to the map? Please help me with this,i'm just making my first steps.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-modification" rel="tag" title="see questions tagged &#39;modification&#39;">modification</span> <span class="post-tag tag-link-markers" rel="tag" title="see questions tagged &#39;markers&#39;">markers</span> <span class="post-tag tag-link-private" rel="tag" title="see questions tagged &#39;private&#39;">private</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '11, 20:50</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 May '13, 02:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-8462" class="comments-container">
&#10;</div>
<div id="comment-tools-8462" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8462-form-container" class="comment-form-container">
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

<span id="8463"></span>

<div id="answer-container-8463" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8463-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-8463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="alexz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>All the code in the OpenStreeMap project is open source and you can create your own OSM server by installing the <a href="http://wiki.openstreetmap.org/wiki/Rails_port">rails port</a>. This contains the front end, the api and potlatch. It does not include the tile generator (<a href="http://wiki.openstreetmap.org/wiki/Mapnik">mapnik</a>), the searching (<a href="http://wiki.openstreetmap.org/wiki/Nominatim">nominatim</a>) or the extended API.</p>
<p>I am currently running this on my laptop, without the whole planet imported.</p>
<p>Note that this will be your own seperate private map based on OSM software. You can import OSM data to your database or part of it, even continuasly. But you may get problems with colliding id if you commit to your own database and then import updates from the central database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '11, 21:43</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Oct '11, 21:49</strong> </span></p>
</div>
</div>
<div id="comments-container-8463" class="comments-container">
<span id="8464"></span>
<div id="comment-8464" class="comment">
<div id="post-8464-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What won't i be able to do without mapnik? But most important: would i be able to make custom notations? because i want to make a map of a wired network. I haven't seen such notations in <a href="http://osm.org">osm.org</a>.</p>
</div>
<div id="comment-8464-info" class="comment-info">
<span class="comment-age">(15 Oct '11, 22:21)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8465"></span>
<div id="comment-8465" class="comment">
<div id="post-8465-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Mapnik is a map renderer that renders the vector data that is in OSM to pritty map tiles.</p>
<p>If you just want to use OSM on your web site you may look at <a href="http://OpenLayers.org">OpenLayers.org</a> . It is an open source javascript slippy map that can display map tiles created by mapnik or any other map renderer, and even custom markers that can be updated by javascript.</p>
</div>
<div id="comment-8465-info" class="comment-info">
<span class="comment-age">(15 Oct '11, 23:34)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
<span id="8471"></span>
<div id="comment-8471" class="comment">
<div id="post-8471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Gnonthgol</span>, No, i don't want to use osm on a website. But i want to create custom markers. SO, is that possible with osm?</p>
</div>
<div id="comment-8471-info" class="comment-info">
<span class="comment-age">(16 Oct '11, 11:11)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="22902"></span>
<div id="comment-22902" class="comment">
<div id="post-22902-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you <em>just</em> want to make custom markers? No roads, buildings, history, etc? If so, installing OpenStreetMap will be massive overkill, and you'd be better off with a 100-line PHP/MySQL application with Leaflet.</p>
</div>
<div id="comment-22902-info" class="comment-info">
<span class="comment-age">(31 May '13, 03:42)</span> <span class="comment-user userinfo">mcw</span>
</div>
</div>
</div>
<div id="comment-tools-8463" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8463-form-container" class="comment-form-container">
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

