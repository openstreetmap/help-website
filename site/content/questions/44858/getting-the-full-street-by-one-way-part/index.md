+++
type = "question"
title = "Getting the full street by one way part"
description = '''Is it possible to obtain the whole street (through the api) by having a way id of only one part of the street? For example https://www.openstreetmap.org/way/49055428 is just a part of the &quot;Rue Mansard&quot; which also consists of https://www.openstreetmap.org/way/100012684'''
date = "2015-08-21T08:12:00Z"
lastmod = "2015-08-22T16:16:00Z"
weight = 44858
keywords = [ "api", "way" ]
aliases = [ "/questions/44858" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Getting the full street by one way part](/questions/44858/getting-the-full-street-by-one-way-part)

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
<span id="post-44858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44858-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to obtain the whole street (through the api) by having a way id of only one part of the street?</p>
<p>For example <a href="https://www.openstreetmap.org/way/49055428">https://www.openstreetmap.org/way/49055428</a> is just a part of the "Rue Mansard" which also consists of <a href="https://www.openstreetmap.org/way/100012684">https://www.openstreetmap.org/way/100012684</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Aug '15, 08:12</strong></p>
<img src="https://secure.gravatar.com/avatar/51da372f5cfba5ade32199774a0dcfca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matsli&#39;s gravatar image" />
<p><span>Matsli</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matsli has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Aug '15, 08:12</strong> </span></p>
</div>
</div>
<div id="comments-container-44858" class="comments-container">
&#10;</div>
<div id="comment-tools-44858" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44858-form-container" class="comment-form-container">
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

<span id="44860"></span>

<div id="answer-container-44860" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44860-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-44860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Matsli has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Someone requested this feature for Overpass API and there's even a <a href="https://github.com/openstreetmap/openstreetmap-website/issues/866#issuecomment-77764010">Github ticket for the main OSM site</a>.</p>
<p>As of today, a sneak preview version is already available for testing: <a href="http://overpass-turbo.eu/s/857">http://overpass-turbo.eu/s/857</a></p>
<p>Starting with a given way, it will return all ways with the same name, even if there are some small gaps in between.</p>
<p>Currently, I don't have any details, as of when this will be available on overpass-api.de as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '15, 09:39</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Aug '15, 09:52</strong> </span></p>
</div>
</div>
<div id="comments-container-44860" class="comments-container">
<span id="44874"></span>
<div id="comment-44874" class="comment">
<div id="post-44874-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>NB: Meanwhile, the sneak preview has been taken offline, as one user sent over 200`000 requests to our <em>development</em> box. For these kind of large scale activities, I strongly recommend to set up and use your own infrastructure next time.</p>
<p>Please refer to the screenshots in the mentioned Github ticket for the time being.</p>
<p>Thanks for your understanding.</p>
</div>
<div id="comment-44874-info" class="comment-info">
<span class="comment-age">(22 Aug '15, 16:16)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-44860" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44860-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44859"></span>

<div id="answer-container-44859" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44859-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-44859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, this is not possible through the API. You have to download and analyse the data yourself (i.e. check whether there's another way that shares an end node and has the same name etc.) -- Note that sometimes not even this check will work because streets can be interrupted by a small plaza, or roundabout, or something.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '15, 08:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-44859" class="comments-container">
&#10;</div>
<div id="comment-tools-44859" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44859-form-container" class="comment-form-container">
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

