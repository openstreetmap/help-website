+++
type = "question"
title = "Can I add a custom layer?"
description = '''I have some data I want to add to OSM base map, but to only make that available for me and a select few people, it&#x27;s commercially sensitive so dont want to general release, is this possible?  I did a search for &quot;Private Layer&quot; and &quot;Custom layer&quot; so forgive me as a new user if I got the terminology w...'''
date = "2011-06-30T10:56:00Z"
lastmod = "2014-04-06T05:18:00Z"
weight = 6102
keywords = [ "layers" ]
aliases = [ "/questions/6102" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can I add a custom layer?](/questions/6102/can-i-add-a-custom-layer)

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
<span id="post-6102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6102-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have some data I want to add to OSM base map, but to only make that available for me and a select few people, it's commercially sensitive so dont want to general release, is this possible?</p>
<p>I did a search for "Private Layer" and "Custom layer" so forgive me as a new user if I got the terminology wrong</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jun '11, 10:56</strong></p>
<img src="https://secure.gravatar.com/avatar/265a32744bb4f6064d62772c828d21aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DominicM&#39;s gravatar image" />
<p><span>DominicM</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DominicM has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jun '11, 11:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-6102" class="comments-container">
&#10;</div>
<div id="comment-tools-6102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6102-form-container" class="comment-form-container">
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

<span id="6103"></span>

<div id="answer-container-6103" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6103-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-6103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot add things to OSM if you don't want others to see them, because OSM is a publicly available database. However what you can do is use OSM as a "base map" and display your proprietary data on top. If your proprietary data is small in volume, this could be as easy as providing a KML file on a server you control (see e.g. the <a href="http://www.bestofosm.org">Best of OSM</a> web site that uses that technology). If you have more data then you'll probably want a more elaborate solution, either one were your additional data is retrieved from a database that you operate, or where it is even rendered directly into the map (using <a href="http://www.tilemill.com">TileMill</a> or other rendering technologies).</p>
<p>So yes, you can use OpenStreetMap data, but OpenStreetMap doesn't provide free infrastructure to host your proprietary data - you'll have to do that yourself.</p>
<p>Please also read the answers to <a href="http://help.openstreetmap.org/questions/5781/">Using maps in an application with a closed user group</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jun '11, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jun '11, 11:07</strong> </span></p>
</div>
</div>
<div id="comments-container-6103" class="comments-container">
<span id="6104"></span>
<div id="comment-6104" class="comment">
<div id="post-6104-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah right, was hoping to make like a custom POI file that could be added to use on there cell phones. I will investigate further but thanx for your help</p>
</div>
<div id="comment-6104-info" class="comment-info">
<span class="comment-age">(30 Jun '11, 11:45)</span> <span class="comment-user userinfo">DominicM</span>
</div>
</div>
<span id="6106"></span>
<div id="comment-6106" class="comment">
<div id="post-6106-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm sure some of the myriad mobile map apps will have the option of loading a custom/local POI file and displaying it on top of OSM maps. Search for "iphone" or "android" on the OSM wiki to get to a list of applications.</p>
</div>
<div id="comment-6106-info" class="comment-info">
<span class="comment-age">(30 Jun '11, 12:18)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="32149"></span>
<div id="comment-32149" class="comment">
<div id="post-32149-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any link to a video tutorial on how to do this?</p>
</div>
<div id="comment-32149-info" class="comment-info">
<span class="comment-age">(06 Apr '14, 05:18)</span> <span class="comment-user userinfo">joshua robison</span>
</div>
</div>
</div>
<div id="comment-tools-6103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6103-form-container" class="comment-form-container">
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

