+++
type = "question"
title = "Download amenities"
description = '''How to download only the amenities from OSM data? Thanks'''
date = "2012-06-27T09:50:00Z"
lastmod = "2015-03-06T13:47:00Z"
weight = 13827
keywords = [ "download", "amenity" ]
aliases = [ "/questions/13827" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Download amenities](/questions/13827/download-amenities)

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
<span id="post-13827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13827-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How to download only the amenities from OSM data? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '12, 09:50</strong></p>
<img src="https://secure.gravatar.com/avatar/b11e5d0a19be06c51068e63791f7a63d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Independent%20L&#39;s gravatar image" />
<p><span>Independent L</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Independent L has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13827" class="comments-container">
<span id="13829"></span>
<div id="comment-13829" class="comment">
<div id="post-13829-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you specify which type of "amenities" you are looking for ? Did you check how they are tagged in OSM ? With the 'amenity' key or 'leisure' or 'tourism' ? Do u want them for the whole planet or just a country or a municipality ? Depending of that, you might have to use different methods to get them.</p>
</div>
<div id="comment-13829-info" class="comment-info">
<span class="comment-age">(27 Jun '12, 10:13)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="13830"></span>
<div id="comment-13830" class="comment">
<div id="post-13830-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For the whole planet the key to 'amenity'. If it were possible to all: 'amenity' key and 'leisure' and 'tourism'. Thanks</p>
</div>
<div id="comment-13830-info" class="comment-info">
<span class="comment-age">(27 Jun '12, 10:23)</span> <span class="comment-user userinfo">Independent L</span>
</div>
</div>
<span id="13838"></span>
<div id="comment-13838" class="comment">
<div id="post-13838-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Given the amount of data involved (see Pieren's answer below) perhaps it's worth asking what problem you're trying to solve? I'm sure that you don't just have a burning desire to have a very large list of amenities locally - you're doing that to solve a problem. It might help us to help you if you explain a bit about what that problem is.</p>
</div>
<div id="comment-13838-info" class="comment-info">
<span class="comment-age">(27 Jun '12, 11:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-13827" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13827-form-container" class="comment-form-container">
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

<span id="13831"></span>

<div id="answer-container-13831" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13831-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-13831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Currently, we have about <a href="http://taginfo.openstreetmap.org/keys/amenity">4.6 millions objects tagged as 'amenity'</a>, <a href="http://taginfo.openstreetmap.org/keys/leisure">1.2m as 'leisure'</a> and <a href="http://taginfo.openstreetmap.org/keys/tourism">0.5m as 'tourism</a>'. Fur such amount of data, you cannot use one of the servers delivering extracts (<a href="https://wiki.openstreetmap.org/wiki/Xapi">like XAPI or compatibles</a>). For you, I would recommend to download a <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">full planet dump</a> and use one tool extracting the data from the file like <a href="https://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a>, <a href="https://wiki.openstreetmap.org/wiki/Osmium">Osmium</a> or <a href="https://wiki.openstreetmap.org/wiki/Osmium">OSMFilter</a>. Probably the easiest to use is Osmosis (but maybe not the fastest).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '12, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-13831" class="comments-container">
&#10;</div>
<div id="comment-tools-13831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13831-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41541"></span>

<div id="answer-container-41541" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41541-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you do mean the possible amenity values that can hold then you can get them from <a href="http://taginfo.openstreetmap.org/keys/amenity#values">http://taginfo.openstreetmap.org/keys/amenity#values</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '15, 13:27</strong></p>
<img src="https://secure.gravatar.com/avatar/920070b90f09d42fec1560d80441afa8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rami%20Al-Salman&#39;s gravatar image" />
<p><span>Rami Al-Salman</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rami Al-Salman has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '15, 13:48</strong> </span></p>
</div>
</div>
<div id="comments-container-41541" class="comments-container">
<span id="41543"></span>
<div id="comment-41543" class="comment">
<div id="post-41543-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you want a list of the actual values that people have used, you need to look at taginfo:</p>
<p><a href="http://taginfo.openstreetmap.org/keys/amenity#values">http://taginfo.openstreetmap.org/keys/amenity#values</a></p>
<p>Unfortunately a number wiki pages are updated by people who "like to tell people how to tag things" rather than "document how people have tagged things", which makes the wiki less valuable as documentation than it might be.</p>
</div>
<div id="comment-41543-info" class="comment-info">
<span class="comment-age">(06 Mar '15, 13:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="41544"></span>
<div id="comment-41544" class="comment">
<div id="post-41544-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah thanks a lot for the info.</p>
</div>
<div id="comment-41544-info" class="comment-info">
<span class="comment-age">(06 Mar '15, 13:47)</span> <span class="comment-user userinfo">Rami Al-Salman</span>
</div>
</div>
</div>
<div id="comment-tools-41541" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41541-form-container" class="comment-form-container">
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

