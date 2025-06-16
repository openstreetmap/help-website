+++
type = "question"
title = "How do I specify County in the API call"
description = '''I asked this here on stackoverflow. Basically I have an address in New York County, which is part of New York City, which is part of New York state. There is a similar address in Staten Island. I am looking for a way to specify New York County to the geocoder and not have it return similar addresses...'''
date = "2011-06-20T20:28:00Z"
lastmod = "2011-06-21T18:27:00Z"
weight = 5911
keywords = [ "special-phrases", "nominatim", "geocoding" ]
aliases = [ "/questions/5911" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How do I specify County in the API call](/questions/5911/how-do-i-specify-county-in-the-api-call)

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
<span id="post-5911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5911-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I asked <a href="http://stackoverflow.com/questions/6364538/how-do-i-specify-the-county-in-openstreetmaps-nominatim-api">this here</a> on stackoverflow. Basically I have an address in New York County, which is part of New York City, which is part of New York state. There is a similar address in Staten Island. I am looking for a way to specify New York County to the geocoder and not have it return similar addresses in the other 4 counties in New York City.</p>
<p>I believe the solution lies in the nominatim <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases">special phrases</a>, However, <a href="/questions/5924/how-do-i-use-special-phrases-in-nominatim">I don't know how to use them</a>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-special-phrases" rel="tag" title="see questions tagged &#39;special-phrases&#39;">special-phrases</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jun '11, 20:28</strong></p>
<img src="https://secure.gravatar.com/avatar/735a05084346db68dff750870654da3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Justin%20Dearing&#39;s gravatar image" />
<p><span>Justin Dearing</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Justin Dearing has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jun '11, 13:54</strong> </span></p>
</div>
</div>
<div id="comments-container-5911" class="comments-container">
&#10;</div>
<div id="comment-tools-5911" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5911-form-container" class="comment-form-container">
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

<span id="5912"></span>

<div id="answer-container-5912" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5912-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Justin Dearing has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On the <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Wiki page for Nominatim</a>, there are descriptions for adding additional parameters to the query, including a bounding box, which will do what you're asking about geographically focusing a query.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '11, 21:53</strong></p>
<img src="https://secure.gravatar.com/avatar/5f2082b86cc50d63c05f33f55166df2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emacsen&#39;s gravatar image" />
<p><span>emacsen</span><br />
<span class="score" title="1191 reputation points"><span>1.2k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emacsen has 4 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-5912" class="comments-container">
<span id="5923"></span>
<div id="comment-5923" class="comment">
<div id="post-5923-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>While in theory a bounding box will work, I'd like to limit to a particular county. I could draw a bounding box for New York County pretty easily, but that would be hard as a general case.</p>
</div>
<div id="comment-5923-info" class="comment-info">
<span class="comment-age">(21 Jun '11, 13:44)</span> <span class="comment-user userinfo">Justin Dearing</span>
</div>
</div>
</div>
<div id="comment-tools-5912" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5912-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5926"></span>

<div id="answer-container-5926" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5926-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There doesn't seem to be a query to do what you want, so my suggestion is to do one of three things:</p>
<p>1) (Simple) If your queries are infrequent, simply do a polygon filter after the results. OSM server are not meant for large scale general purpose use anyway.</p>
<p>2) (Complex) If you run a lot of queries and need a lot of very specific data, the right answer for you is to set up your own OSM instance restricted to the polygons you care about, and run your queries on your instance.</p>
<p>3) (Complex) You can add the feature to Nominatim. It's FLOSS. Patch it you may find the feature adopted upstream.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '11, 16:42</strong></p>
<img src="https://secure.gravatar.com/avatar/5f2082b86cc50d63c05f33f55166df2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emacsen&#39;s gravatar image" />
<p><span>emacsen</span><br />
<span class="score" title="1191 reputation points"><span>1.2k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emacsen has 4 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-5926" class="comments-container">
<span id="5930"></span>
<div id="comment-5930" class="comment">
<div id="post-5930-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is their much success offering bounties for features in Nominatim? In this case I'd rather pay someone else to implement the feature.</p>
</div>
<div id="comment-5930-info" class="comment-info">
<span class="comment-age">(21 Jun '11, 17:47)</span> <span class="comment-user userinfo">Justin Dearing</span>
</div>
</div>
<span id="5931"></span>
<div id="comment-5931" class="comment">
<div id="post-5931-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can try, but generally OSM doesn't do "bounties" in that sense. Companies do hire OSM developers (MapQuest pays the Nominatim developer), but not always to work on OSM related activity. You can always get on the mailing lists and try, but I'd be surprised if people took you up on it for anything less than professional rate. The second solution of a custom instance would likely be the cheapest solution to your problem in that case.</p>
</div>
<div id="comment-5931-info" class="comment-info">
<span class="comment-age">(21 Jun '11, 18:27)</span> <span class="comment-user userinfo">emacsen</span>
</div>
</div>
</div>
<div id="comment-tools-5926" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5926-form-container" class="comment-form-container">
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

