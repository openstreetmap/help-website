+++
type = "question"
title = "Add POI with PHP"
description = '''I have a web site developed in PHP, and would like to create new POIs in OpenStreetMap from that web site, much like an editor does. Is there any library or class PHP to do this?'''
date = "2012-06-25T10:36:00Z"
lastmod = "2012-06-26T07:44:00Z"
weight = 13758
keywords = [ "api", "php" ]
aliases = [ "/questions/13758" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Add POI with PHP](/questions/13758/add-poi-with-php)

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
<span id="post-13758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13758-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a web site developed in PHP, and would like to create new POIs in OpenStreetMap from that web site, much like an editor does. Is there any library or class PHP to do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '12, 10:36</strong></p>
<img src="https://secure.gravatar.com/avatar/b11e5d0a19be06c51068e63791f7a63d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Independent%20L&#39;s gravatar image" />
<p><span>Independent L</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Independent L has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '12, 19:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-13758" class="comments-container">
&#10;</div>
<div id="comment-tools-13758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13758-form-container" class="comment-form-container">
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

<span id="13774"></span>

<div id="answer-container-13774" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13774-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Check out the (outdated) <a href="http://wiki.openstreetmap.org/wiki/Develop/Frameworks#Single_Purpose_Client_Libraries_for_API0.6_.28the_RESTful_API.29">list of clients</a> on the wiki, and have a look at Ken Guest's <a href="https://github.com/kenguest/Services_Openstreetmap">Services_Openstreetmap</a> code.</p>
<p>If you build something that can be used to edit OSM, please make use of the OAuth scheme, so that users of your web interface have to register with OSM first and their edits are later submitted under their own account. Web services where edits from all users are submitted under the same account can be a problem because OSM has no means to identify or contact the individual user.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '12, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-13774" class="comments-container">
<span id="13780"></span>
<div id="comment-13780" class="comment">
<div id="post-13780-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many Thanks</p>
</div>
<div id="comment-13780-info" class="comment-info">
<span class="comment-age">(26 Jun '12, 07:44)</span> <span class="comment-user userinfo">Independent L</span>
</div>
</div>
</div>
<div id="comment-tools-13774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13774-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13767"></span>

<div id="answer-container-13767" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13767-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When I am not wrong, the framework around <a href="http://yapis.eu/">Yapis</a> is written in PHP ... ask the maintainer Moenk for help if that fits for you.</p>
<p>Maybe <a href="http://wheelmap.org/">Wheelmap.org</a> is similat to your aims?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '12, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-13767" class="comments-container">
&#10;</div>
<div id="comment-tools-13767" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13767-form-container" class="comment-form-container">
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

