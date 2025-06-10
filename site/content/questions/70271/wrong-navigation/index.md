+++
type = "question"
title = "Wrong Navigation"
description = '''We have lived on a new road for 1 year and was immediately able to add it to Google Maps. However over the last year many deliveries do not navigate correctly. The address is 2061 Mistyoak Ln, Cincinnati Ohio 45237. The incorrect navigation ends up at the end of Warren Ave (you will see on the map. ...'''
date = "2019-08-01T05:50:00Z"
lastmod = "2019-08-09T16:20:00Z"
weight = 70271
keywords = [ "navigation", "newstreet" ]
aliases = [ "/questions/70271" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wrong Navigation](/questions/70271/wrong-navigation)

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
<span id="post-70271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70271-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have lived on a new road for 1 year and was immediately able to add it to Google Maps. However over the last year many deliveries do not navigate correctly. The address is 2061 Mistyoak Ln, Cincinnati Ohio 45237. The incorrect navigation ends up at the end of Warren Ave (you will see on the map. It is 50 ft away but does not connect and it is over a fence).</p>
<p>I found that many companies use this program vs Google Maps so I edited the street to change it to paved and residential and corrected the shape. I even added an "area" as a building (house) with my street number. However it still routes to the end of Warren Avenue instead of taking the obvious turn off the main street onto Mistyoak.</p>
<p>Can someone look at this and tell me what needs to be done (or correct it). Thanks!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-navigation" rel="tag" title="see questions tagged &#39;navigation&#39;">navigation</span> <span class="post-tag tag-link-newstreet" rel="tag" title="see questions tagged &#39;newstreet&#39;">newstreet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '19, 05:50</strong></p>
<img src="https://secure.gravatar.com/avatar/78ad155cdb266a2c4761d69a55128544?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bballgt00&#39;s gravatar image" />
<p><span>bballgt00</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bballgt00 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70271" class="comments-container">
<span id="70338"></span>
<div id="comment-70338" class="comment">
<div id="post-70338-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It has now been 6 days and still routes incorrectly. Interesting if I go out of Openstreet maps (following the link to OSRM) the routing engine has it correct. Also within Openstreet, OSRM BICYCLE is correct just not car. Again, I have made it a residential street so I can not figure out why!!</p>
<p>I just added a chain link fence that exist. It goes between Warren Ave (the route it takes) and Mistyoak ln, my street.</p>
<p>Please, I'm sure someone in this forum understands why a bike can get there but a car can not. Thanks</p>
</div>
<div id="comment-70338-info" class="comment-info">
<span class="comment-age">(07 Aug '19, 19:26)</span> <span class="comment-user userinfo">bballgt00</span>
</div>
</div>
<span id="70340"></span>
<div id="comment-70340" class="comment">
<div id="post-70340-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There appears to have been an old "proposed road" tag on the road. It's possible that the routing engines were interpreting this to mean "the road is proposed and hasn't been built yet". I've deleted this, so let's see what happens on the next routing update.</p>
</div>
<div id="comment-70340-info" class="comment-info">
<span class="comment-age">(07 Aug '19, 20:49)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="70350"></span>
<div id="comment-70350" class="comment">
<div id="post-70350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OSRM / car routes now. see <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=39.17891%2C-84.45867%3B39.17833%2C-84.45789">https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=39.17891%2C-84.45867%3B39.17833%2C-84.45789</a></p>
</div>
<div id="comment-70350-info" class="comment-info">
<span class="comment-age">(09 Aug '19, 01:02)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="70357"></span>
<div id="comment-70357" class="comment">
<div id="post-70357-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great Removing "the proposed road" tag appears to have fixed OSRM navigation, But GraphHopper is still incorrect. I've waited an extra day on it but it still maybe server syncing. Other thoughts?</p>
<p>Still had a Grocery Deliver go to the wrong street yesterday - starting to frustrate my wife lol. Thanks for the help</p>
</div>
<div id="comment-70357-info" class="comment-info">
<span class="comment-age">(09 Aug '19, 16:20)</span> <span class="comment-user userinfo">bballgt00</span>
</div>
</div>
</div>
<div id="comment-tools-70271" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70271-form-container" class="comment-form-container">
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

<span id="70275"></span>

<div id="answer-container-70275" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70275-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-70275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have <a href="https://www.openstreetmap.org/changeset/72875411">added</a> the road only three hours ago. While it displays quite quickly on www.openstreetmap.org the routers to be updated takes somewhat longer. The routing engines on the same site update their routing data once a day I believe. Apps on your smartphone might take much longer, update cycles of one or two months are normal I would say.</p>
<p>I suggest to wait a day and then see if the routers on www.openstreetmap.org work correctly. Eventually other routers will then follow suit.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '19, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-70275" class="comments-container">
<span id="70339"></span>
<div id="comment-70339" class="comment">
<div id="post-70339-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It has now been 6 days and still routes incorrectly. Interesting if I go out of Openstreet maps (following the link to OSRM) the routing engine has it correct. Also within Openstreet, OSRM BICYCLE is correct just not car. Again, I have made it a residential street so I can not figure out why!! I just added a chain link fence that exist. It goes between Warren Ave (the route it takes) and Mistyoak ln, my street. Please, I'm sure someone in this forum understands why a bike can get there but a car can not. Thanks</p>
</div>
<div id="comment-70339-info" class="comment-info">
<span class="comment-age">(07 Aug '19, 19:26)</span> <span class="comment-user userinfo">bballgt00</span>
</div>
</div>
</div>
<div id="comment-tools-70275" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70275-form-container" class="comment-form-container">
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

