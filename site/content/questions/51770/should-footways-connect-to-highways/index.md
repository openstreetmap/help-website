+++
type = "question"
title = "Should footways connect to highways?"
description = '''I always assumed that the different types of ways in OSM should get connected, for purposes of navigation at least. For instance, a park footway= should eventually get connected to a highway with a sidewalk= tag. But, I am noticing some other mappers leave the different types of ways disconnected, f...'''
date = "2016-08-28T17:20:00Z"
lastmod = "2020-01-26T22:07:00Z"
weight = 51770
keywords = [ "footpath", "routingerror", "footway", "highway", "routing" ]
aliases = [ "/questions/51770" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Should footways connect to highways?](/questions/51770/should-footways-connect-to-highways)

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
<span id="post-51770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51770-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I always assumed that the different types of ways in OSM should get connected, for purposes of navigation at least. For instance, a park <code>footway=</code><em></em> <em>should eventually get connected to a highway with a <code>sidewalk=</code></em> tag. But, I am noticing some other mappers leave the different types of ways disconnected, for instance, all of the park footways would be contained in the <code>leisure=park</code> polygon. Can anyone explain why this is common and how is it generally fixed? Or is this proper. I have been extending the park footways so they connect with the highway, but maybe I should not be doing it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-footpath" rel="tag" title="see questions tagged &#39;footpath&#39;">footpath</span> <span class="post-tag tag-link-routingerror" rel="tag" title="see questions tagged &#39;routingerror&#39;">routingerror</span> <span class="post-tag tag-link-footway" rel="tag" title="see questions tagged &#39;footway&#39;">footway</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '16, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/cb68523a12e3580728c6bee495ae602e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtc&#39;s gravatar image" />
<p><span>mtc</span><br />
<span class="score" title="411 reputation points">411</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtc has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Aug '16, 17:46</strong> </span></p>
</div>
</div>
<div id="comments-container-51770" class="comments-container">
&#10;</div>
<div id="comment-tools-51770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51770-form-container" class="comment-form-container">
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

<span id="51772"></span>

<div id="answer-container-51772" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51772-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-51772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mtc has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes the sidewalks should connect to the streets, or if there is a separate way for the sidewalk, to the sidewalk (which will eventually connect to the street network).</p>
<p>The people leaving them unconnected may be planning on coming back later and adding a separate way for the sidewalk, but a more likely explanation is that they don't realize that OSM based routing software tends to rely on the ways being connected.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '16, 18:16</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-51772" class="comments-container">
<span id="51859"></span>
<div id="comment-51859" class="comment">
<div id="post-51859-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>When i map a footpath that ends at a playing field or carpark i usually connect the path to either the main road or the carpark lanes. I also usually map the path around the edge of playing field, which is the usual route you would take, or the right of way, if there is one. This should allow routing to work correctley. Routing can be checked with OSRM or another routing engine, there are a few on the osm map page. Note: routing needs few days before changes are used.</p>
</div>
<div id="comment-51859-info" class="comment-info">
<span class="comment-age">(01 Sep '16, 20:48)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="51864"></span>
<div id="comment-51864" class="comment">
<div id="post-51864-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> I also notice people will draw a path/footway where it actually exists and (quite logically) not add the extra piece which connects it to the centreline of a highway. Of course this often looks fine on CartoCSS as the highways are usually depicted wider than they really are, but obviously breaks routing.</p>
</div>
<div id="comment-51864-info" class="comment-info">
<span class="comment-age">(02 Sep '16, 10:53)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51772" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51772-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72700"></span>

<div id="answer-container-72700" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72700-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is now a nice suggestion, that link from sidewalk to a road should be highway=footway + footway=link - <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Tag:footway%3Dlink">https://wiki.openstreetmap.org/wiki/Proposed_features/Tag:footway%3Dlink</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '20, 22:07</strong></p>
<img src="https://secure.gravatar.com/avatar/519892414c138fabad7b61a7a85f7fbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MiroJanosik&#39;s gravatar image" />
<p><span>MiroJanosik</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MiroJanosik has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72700" class="comments-container">
&#10;</div>
<div id="comment-tools-72700" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72700-form-container" class="comment-form-container">
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

