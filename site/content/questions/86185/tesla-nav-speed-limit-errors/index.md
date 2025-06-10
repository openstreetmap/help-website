+++
type = "question"
title = "Tesla NAV Speed Limit errors"
description = '''Brand new user, so please excuse me off this isn’t the correct location to ask, or if this has been discussed previously.  I drive a Tesla with Full Service Drive (FSD), which navigates automatically. I’ve heard they get mapping data from this organization.  In many locations, before the car sees a ...'''
date = "2022-11-18T20:38:00Z"
lastmod = "2023-08-27T12:51:00Z"
weight = 86185
keywords = [ "speedlimit", "tesla" ]
aliases = [ "/questions/86185" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Tesla NAV Speed Limit errors](/questions/86185/tesla-nav-speed-limit-errors)

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
<span id="post-86185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86185-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Brand new user, so please excuse me off this isn’t the correct location to ask, or if this has been discussed previously. I drive a Tesla with Full Service Drive (FSD), which navigates automatically. I’ve heard they get mapping data from this organization. In many locations, before the car sees a speed limit sign (in narrow, windy local neighborhood streets, etc.), the car erroneously defaults to 35 MPH, when the safe speed limit is 25 MPH. In fact, as soon as I put my car in drive, it shows 35 MPH (while I’m still in my garage and driveway). This continues until the car sees a sign. Other times, the car defaults to 25 MPH before it sees a sign on a busy four lane road with a 45 speed limit. The problem is, the car will drive the speed limit (plus or minus an offset) as soon as FSD is engaged, so if I were to use it in my neighborhood, the car would dangerously race to 35 MPH. Obviously, I can't use it on these roads. This issue has been present for a few updates, and it's nearly impossible to communicate to Tesla to fix, so I was wondering if it can be adjusted here? Is the speed limit data supplied by this organization? If so, can it be corrected? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-speedlimit" rel="tag" title="see questions tagged &#39;speedlimit&#39;">speedlimit</span> <span class="post-tag tag-link-tesla" rel="tag" title="see questions tagged &#39;tesla&#39;">tesla</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Nov '22, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/3b5e8940618cbe55772622cd28dbe520?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Larryd517&#39;s gravatar image" />
<p><span>Larryd517</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Larryd517 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Nov '22, 20:44</strong> </span></p>
</div>
</div>
<div id="comments-container-86185" class="comments-container">
&#10;</div>
<div id="comment-tools-86185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86185-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="86186"></span>

<div id="answer-container-86186" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86186-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-86186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I do not know if Tesla uses OpenStreetData or not.</p>
<p>But to answer your questions: Yes, OpenStreetMap has "tagging" allowing a mapper to indicate what the speed limit is on every road. However, many, many roads are not tagged with speed. So any navigation app (or car) that uses OpenStreetMap data will make default assumptions to use for roads that do not have the speed limit tagged.</p>
<p>You don't say where you are, but if you open the map at <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> and go to your location you can either:</p>
<ul>
<li><p>Open the data in an editor using the "Edit" pull down on the top left. You will need to be logged into a free account to be able to edit.</p></li>
<li><p>Or if you only want to verify that the road(s) in your area specify the "maxspeed" then on the right side of the map is a icon with several stacked layers. Click on that to expand a side bar. On the side bar click on the check box by "Map Data". All of the actual data will be outlined in blue. Click on the blue line on the road(s) of interest to see how they are tagged. When you click on the "object" a side bar will pop up on the left side showing all of the characteristics (tags) for that road.</p></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '22, 23:15</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-86186" class="comments-container">
&#10;</div>
<div id="comment-tools-86186" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86186-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86187"></span>

<div id="answer-container-86187" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86187-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-86187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks. I played around and made edits to my local roads, requesting someone to review. They were not any speed limits on the roads, as opposed to the wrong limit showing. I set them to 25. Not sure if the car will get the information, and if so, how long the changes take to get there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '22, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/3b5e8940618cbe55772622cd28dbe520?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Larryd517&#39;s gravatar image" />
<p><span>Larryd517</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Larryd517 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Nov '22, 12:24</strong> </span></p>
</div>
</div>
<div id="comments-container-86187" class="comments-container">
<span id="87390"></span>
<div id="comment-87390" class="comment">
<div id="post-87390-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Follow up. Despite updating the map, car still thinks the speed limit on local streets is 35. I guess Tesla doesn’t pull data from this service</p>
<p>On a positive note, the speed limit showing on car’s screen for my driveway and garage (yes the car shows a speed limit in my garage) was recently reduced from 35 to 25, so there’s progress!</p>
</div>
<div id="comment-87390-info" class="comment-info">
<span class="comment-age">(24 Jun '23, 08:45)</span> <span class="comment-user userinfo">Larryd517</span>
</div>
</div>
<span id="87727"></span>
<div id="comment-87727" class="comment">
<div id="post-87727-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm here for the same reason! I'm hoping when the maps update (not sure how often they do that) it gets changed. I have issues where the speed limit is 45 but in one tiny 100yard stretch it thinks it's 35 and the car slows down for it. The first time it took me by surprise but now I just do a bug report every time. Hopefully our edits help!</p>
</div>
<div id="comment-87727-info" class="comment-info">
<span class="comment-age">(21 Aug '23, 23:26)</span> <span class="comment-user userinfo">352Guy</span>
</div>
</div>
<span id="87768"></span>
<div id="comment-87768" class="comment">
<div id="post-87768-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/23278/352guy"></a><a href="https://help.openstreetmap.org/users/23278/352guy">@352Guy</a> " The first time it took me by surprise but now I just do a bug report every time"</p>
<p>That's not how Bug Report works. It’s not a bug reporting system (as the name would imply) that most of us are familiar with where engineers read comments, for example apple.com/feedback,.</p>
<p>When you create a bug report in Tesla, you’re just adding a “sticky note” to your car’s computer log. It’s only read by Tesla personnel if you create a service ticket, and then a technician analyzes your log. The report can help them isolate the specific set of events that were occurring in your car at, or around, the time of your complaint.</p>
<p>No one will see your bug report comment unless they’re told to investigate an issue.</p>
</div>
<div id="comment-87768-info" class="comment-info">
<span class="comment-age">(27 Aug '23, 12:51)</span> <span class="comment-user userinfo">Larryd517</span>
</div>
</div>
</div>
<div id="comment-tools-86187" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86187-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87391"></span>

<div id="answer-container-87391" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87391-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-87391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Many organizations that use OpenStreetMap data only pull fresh data at periodic intervals. If Tesla is using OSM data, they may only get a fresh copy every month or every six months.</p>
<p>I have a different brand of car that also has an automatic speed limit setup. It is also wrong about the speed often enough that I have disabled that feature. It the case of my car, they do not use OSM data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '23, 15:39</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-87391" class="comments-container">
&#10;</div>
<div id="comment-tools-87391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87391-form-container" class="comment-form-container">
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

