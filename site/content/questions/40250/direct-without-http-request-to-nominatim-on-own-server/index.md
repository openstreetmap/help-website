+++
type = "question"
title = "Direct (without HTTP) request to Nominatim on own server"
description = '''I have server with installed Nominatim. I would like to use it without setting up a website. Is it possible to make direct (without using HTTP) request to Nominatim on own server? What I need to do it? Thank you.'''
date = "2015-01-12T14:09:00Z"
lastmod = "2015-01-12T16:53:00Z"
weight = 40250
keywords = [ "nominatim", "request", "direct" ]
aliases = [ "/questions/40250" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Direct (without HTTP) request to Nominatim on own server](/questions/40250/direct-without-http-request-to-nominatim-on-own-server)

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
<span id="post-40250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40250-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have server with installed Nominatim. I would like to use it without setting up a website. Is it possible to make direct (without using HTTP) request to Nominatim on own server? What I need to do it? Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-direct" rel="tag" title="see questions tagged &#39;direct&#39;">direct</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jan '15, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/aeafd4156483ce12e60c02d426635abe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yaahor&#39;s gravatar image" />
<p><span>yaahor</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yaahor has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jan '15, 14:36</strong> </span></p>
</div>
</div>
<div id="comments-container-40250" class="comments-container">
&#10;</div>
<div id="comment-tools-40250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40250-form-container" class="comment-form-container">
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

<span id="40257"></span>

<div id="answer-container-40257" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40257-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yaahor has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a small command line tool <code>./utils/query.php</code> which you can use to search without using the web interface. It has been written for testing the database, so it is not as powerful as the web API in terms of configuration parameters. It only supports JSON output and no reverse geocoding. But it should provide a good starting point and is easily extendible for your own needs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '15, 16:53</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-40257" class="comments-container">
&#10;</div>
<div id="comment-tools-40257" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40257-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40256"></span>

<div id="answer-container-40256" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40256-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://github.com/twain47/Nominatim/blob/master/lib/Geocode.php">Geocoder that extracts information from Nominatim's database</a> is written in PHP, so you could use that library in your code. Alternatively, you could extract the SQL statements the library uses to use in your own library if you want to reimplement it in another language. In either case you would import the OSM data using <code>osm2pgsql</code> in the same way as a <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Installation">full Nominatim installation</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '15, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-40256" class="comments-container">
&#10;</div>
<div id="comment-tools-40256" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40256-form-container" class="comment-form-container">
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

