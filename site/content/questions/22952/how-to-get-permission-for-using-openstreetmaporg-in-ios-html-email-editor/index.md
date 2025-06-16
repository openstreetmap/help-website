+++
type = "question"
title = "How to get Permission for Using Openstreetmap.org in iOS Html Email Editor?"
description = '''I am currently developing a rich text email editor for iPads (and other platforms) which will soon appear on Indiegogo.com . One of the email templates I want to add is called &quot;This is my Current Position&quot;. It uses staticmap.openstreetmap.de and openstreetmap.org to display a map inside an email. Ac...'''
date = "2013-06-02T10:30:00Z"
lastmod = "2013-06-02T16:38:00Z"
weight = 22952
keywords = [ "tile", "use", "commercial", "licence", "server" ]
aliases = [ "/questions/22952" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get Permission for Using Openstreetmap.org in iOS Html Email Editor?](/questions/22952/how-to-get-permission-for-using-openstreetmaporg-in-ios-html-email-editor)

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
<span id="post-22952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22952-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently developing a rich text email editor for iPads (and other platforms) which will soon appear on Indiegogo.com . One of the email templates I want to add is called "This is my Current Position". It uses staticmap.openstreetmap.de and openstreetmap.org to display a map inside an email.</p>
<p>According to <a href="https://wiki.openstreetmap.org/wiki/Tile_Usage_Policy,">https://wiki.openstreetmap.org/wiki/Tile_Usage_Policy,</a> I need a permission from the system administrators for "distributing an app that uses tiles from openstreetmap.org". How can I get that permission? I can not find email addresses of the system administrators. Is staticmap.openstreetmap.de using the tile server at all?</p>
<p>Marvin iNimated.com</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-use" rel="tag" title="see questions tagged &#39;use&#39;">use</span> <span class="post-tag tag-link-commercial" rel="tag" title="see questions tagged &#39;commercial&#39;">commercial</span> <span class="post-tag tag-link-licence" rel="tag" title="see questions tagged &#39;licence&#39;">licence</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '13, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/1e13135c8e537fade6659516d4366371?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marvin&#39;s gravatar image" />
<p><span>Marvin</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marvin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22952" class="comments-container">
&#10;</div>
<div id="comment-tools-22952" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22952-form-container" class="comment-form-container">
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

<span id="22953"></span>

<div id="answer-container-22953" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22953-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-22953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Marvin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>staticmap.openstreetmap.de uses tiles from the OSM tile server, therefore integrating this into your application would use two types of project resources - the OSM tile server and the openstreetmap.de server on which the static map script is running.</p>
<p>staticmap.openstreetmap.de is not intended as a "production" service for use in commercial applications. You would be expected to either</p>
<ul>
<li>set up your own "static map" service (all required software is open source but since it is based on a tile server, you will either have to set up a tile server too or find one that you are allowed to use) or</li>
<li>use a free "static map" service with terms of usage that allow commercial use - see e.g. MapQuest's offering <a href="http://open.mapquestapi.com/staticmap/">http://open.mapquestapi.com/staticmap/</a> or</li>
<li>buy a commercial "static map" service</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '13, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-22953" class="comments-container">
<span id="22954"></span>
<div id="comment-22954" class="comment">
<div id="post-22954-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks, got it working with MapQuest in 20 minutes. :-)</p>
</div>
<div id="comment-22954-info" class="comment-info">
<span class="comment-age">(02 Jun '13, 16:38)</span> <span class="comment-user userinfo">Marvin</span>
</div>
</div>
</div>
<div id="comment-tools-22953" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22953-form-container" class="comment-form-container">
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

