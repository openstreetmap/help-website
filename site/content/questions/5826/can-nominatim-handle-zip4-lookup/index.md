+++
type = "question"
title = "Can Nominatim handle Zip+4 lookup?"
description = '''Opened Trac Ticket # 3838 about this. Please vote follow if you have the same issue. It would seem that Nominatim has no support for zip+4 codes in US addresses. While its understandable that it cannot return a zip+4 zip code, adding a zip+4 to an address will cause the geocoder to not match an addr...'''
date = "2011-06-16T22:38:00Z"
lastmod = "2011-06-18T23:18:00Z"
weight = 5826
keywords = [ "zip-code", "nominatim" ]
aliases = [ "/questions/5826" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can Nominatim handle Zip+4 lookup?](/questions/5826/can-nominatim-handle-zip4-lookup)

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
<span id="post-5826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5826-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Opened <a href="http://trac.openstreetmap.org/ticket/3838">Trac Ticket # 3838</a> about this. Please vote follow if you have the same issue.</p>
<p>It would seem that Nominatim has no support for zip+4 codes in US addresses. While its understandable that it cannot return a zip+4 zip code, adding a zip+4 to an address will cause the geocoder to not match an address that it would otherwise match.</p>
<ul>
<li><a href="http://nominatim.openstreetmap.org/search?q=19%20Elizabeth%20Street%2C%20New%20York%2C%20NY%2C%2010013-4803&amp;format=xml&amp;polygon=1&amp;addressdetails=1&amp;limit=50">19 Elizabeth Street, New York, NY, 10013-4803</a></li>
<li><a href="http://nominatim.openstreetmap.org/search?q=19%20Elizabeth%20Street%2C%20New%20York%2C%20NY%2C%2010013&amp;format=xml&amp;polygon=1&amp;addressdetails=1&amp;limit=50">19 Elizabeth Street, New York, NY, 10013</a></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zip-code" rel="tag" title="see questions tagged &#39;zip-code&#39;">zip-code</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jun '11, 22:38</strong></p>
<img src="https://secure.gravatar.com/avatar/735a05084346db68dff750870654da3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Justin%20Dearing&#39;s gravatar image" />
<p><span>Justin Dearing</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Justin Dearing has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '11, 12:58</strong> </span></p>
</div>
</div>
<div id="comments-container-5826" class="comments-container">
<span id="5832"></span>
<div id="comment-5832" class="comment">
<div id="post-5832-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>seen this? <a href="/questions/5819/added-street-doesnt-show-up-on-search">https://help.openstreetmap.org/questions/5819/added-street-doesnt-show-up-on-search</a></p>
</div>
<div id="comment-5832-info" class="comment-info">
<span class="comment-age">(16 Jun '11, 23:22)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="5834"></span>
<div id="comment-5834" class="comment">
<div id="post-5834-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's good to know. However, I don't see how its relevant in this case, except of course if this database migration would take up resources that would be used to change the address parsing algorithm, if that is indeed the resolution to my request.</p>
</div>
<div id="comment-5834-info" class="comment-info">
<span class="comment-age">(17 Jun '11, 02:55)</span> <span class="comment-user userinfo">Justin Dearing</span>
</div>
</div>
</div>
<div id="comment-tools-5826" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5826-form-container" class="comment-form-container">
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

<span id="5874"></span>

<div id="answer-container-5874" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5874-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Justin Dearing has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Short answer:</p>
<p>Yes this is appears to be a bug in Nominatim, and should be submitted as a bug to: <a href="http://trac.openstreetmap.org/query?status=new&amp;status=assigned&amp;status=reopened&amp;component=nominatim&amp;order=id&amp;desc=1">trac</a>.</p>
<p>Please be aware that Nominatim itself is down currently due to unforeseen scaling issues (there's too much stuff in OSM!).</p>
<p>And what you see may in fact be an artifact of that fact.</p>
<p>Longer answer:</p>
<p>Zip codes are complex things, they have to be placed on every POI, especially the +4 zip codes, and it's well known that (sadly) throwing more data at Nominatim can make a good search fail. That is given more data, Nominatim can sometimes return no result, rather than the expected behavior.</p>
<p>That's unfortunately a long standing problem, and unlikely to be solved in the short term, but I'm sure the Nominatim developers would love more help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '11, 23:18</strong></p>
<img src="https://secure.gravatar.com/avatar/5f2082b86cc50d63c05f33f55166df2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emacsen&#39;s gravatar image" />
<p><span>emacsen</span><br />
<span class="score" title="1191 reputation points"><span>1.2k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emacsen has 4 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-5874" class="comments-container">
&#10;</div>
<div id="comment-tools-5874" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5874-form-container" class="comment-form-container">
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

