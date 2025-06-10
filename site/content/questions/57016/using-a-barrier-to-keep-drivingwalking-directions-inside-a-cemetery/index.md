+++
type = "question"
title = "Using a barrier to keep driving/walking directions inside a cemetery"
description = '''I am trying to render combination wall and fence barrier around a cemetery so that directions supplied to a specific lat/long combination of a grave will be directed inside the cemetery on existing paths/roads. When the grave is closer to an outside road, directions given take the user to the closes...'''
date = "2017-07-11T18:39:00Z"
lastmod = "2017-07-19T21:31:00Z"
weight = 57016
keywords = [ "directions", "routing", "barrier" ]
aliases = [ "/questions/57016" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using a barrier to keep driving/walking directions inside a cemetery](/questions/57016/using-a-barrier-to-keep-drivingwalking-directions-inside-a-cemetery)

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
<span id="post-57016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57016-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to render combination wall and fence barrier around a cemetery so that directions supplied to a specific lat/long combination of a grave will be directed inside the cemetery on existing paths/roads. When the grave is closer to an outside road, directions given take the user to the closest place on the external road and expect the person can access the location walking from the road. In many cases this is not the case - a significant wall or fence exists that cannot be "crossed". Other times, the road is very unsafe to park on (high speed or no shoulder) and the person should be directed inside the cemetery for access. I have tried creating a barrier around most of a cemetery (Cypress Lawn Memorial Park in Colma CA) and I cannot see that rendered after 3 days (<a href="http://product.itoworld.com/map/49?lon=-122.45707&amp;lat=37.67196&amp;zoom=15)">http://product.itoworld.com/map/49?lon=-122.45707&amp;lat=37.67196&amp;zoom=15)</a> while I can see a barrier not far away behind a Home Depot store (to the northwest of the cemetery). Secondly, when trying directions to other nearby places with fences, the behavior doesn't seem to do what I am trying anyway. The goal is that a person is directed to enter the cemetery main entrance and the use the internal roads to get to the closest spot to the lat/long and walk the remaining distance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-barrier" rel="tag" title="see questions tagged &#39;barrier&#39;">barrier</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '17, 18:39</strong></p>
<img src="https://secure.gravatar.com/avatar/56cab5e65d1f5909c697ed988f7d8f2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ken%20Oates&#39;s gravatar image" />
<p><span>Ken Oates</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ken Oates has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57016" class="comments-container">
<span id="57017"></span>
<div id="comment-57017" class="comment">
<div id="post-57017-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't understand the problem. If the roads inside the cemetary are properly mapped then routing engines should work as expected, e.g. in this case: <a href="http://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=37.6659%2C-122.4561%3B37.6680%2C-122.4588">http://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=37.6659%2C-122.4561%3B37.6680%2C-122.4588</a></p>
</div>
<div id="comment-57017-info" class="comment-info">
<span class="comment-age">(11 Jul '17, 18:53)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="57018"></span>
<div id="comment-57018" class="comment">
<div id="post-57018-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Presumably routes like <a href="http://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=37.66590%2C-122.45610%3B37.66701%2C-122.45955#map=17/37.66615/-122.45796">http://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=37.66590%2C-122.45610%3B37.66701%2C-122.45955#map=17/37.66615/-122.45796</a> are the issue.</p>
<p>The general purpose routing engines on OSM.org won't account for a barrier or wall that isn't connected to a highway that is a possible route. They tend to be car focused on don't focus on pedestrian convenience at the end of the route.</p>
<p>Such questions also come up when routing to a school or something like that where there is no established way to hint where in the school grounds would be the best place to stop a vehicle.</p>
</div>
<div id="comment-57018-info" class="comment-info">
<span class="comment-age">(11 Jul '17, 19:01)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="57019"></span>
<div id="comment-57019" class="comment">
<div id="post-57019-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, maxerickson has the problem nailed. Here is more clarification, but probably isn't necessary at this point.</p>
<p>The first image is the type of routing I am looking for. The user is at the entrance of the cemetery and the red point is where the grave is. It routes correctly through the cemetery because the destination lat/long is closer to the internal road than the external one (Collins Avenue) <a href="https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=37.67329%2C-122.45447%3B37.67321%2C-122.45735#map=17/37.67294/-122.45423">https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=37.67329%2C-122.45447%3B37.67321%2C-122.45735#map=17/37.67294/-122.45423</a></p>
<p>If the grave location is moved just slightly closer to the edge of the cemetery, the person is routed outside to Collins Drive. There are businesses on Collins between the road and the cemetery as well as a high concrete wall separating the back of the businesses from the cemetery. There is no way to get from Collins to the cemetery. <a href="https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=37.67329%2C-122.45447%3B37.67332%2C-122.45734#map=18/37.67399/-122.45613">https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=37.67329%2C-122.45447%3B37.67332%2C-122.45734#map=18/37.67399/-122.45613</a></p>
<p>So, does anyone have a some solution suggestions? Thanks!</p>
</div>
<div id="comment-57019-info" class="comment-info">
<span class="comment-age">(11 Jul '17, 19:17)</span> <span class="comment-user userinfo">Ken Oates</span>
</div>
</div>
<span id="57020"></span>
<div id="comment-57020" class="comment">
<div id="post-57020-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>perhaps you could add the path ? It seems to me that there is a path in that corner of the cemetery. A general purpose router will bring you as close as possible over the existing paths, it does not know about walls around the area.</p>
</div>
<div id="comment-57020-info" class="comment-info">
<span class="comment-age">(11 Jul '17, 20:05)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-57016" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57016-form-container" class="comment-form-container">
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

<span id="57022"></span>

<div id="answer-container-57022" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57022-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-57022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "sane" solution is to implement routing on areas (which could then take barriers etc in to account), this is not the highest priority with the routing engine developers, but it is an known issue. The stop gap measure is to add fake paths, but that is not particularly satisfactory.</p>
<p>PS: this is a largish issue for indoor routing too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '17, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-57022" class="comments-container">
<span id="57188"></span>
<div id="comment-57188" class="comment">
<div id="post-57188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you everyone for the suggestions. Agreed the best solution would be to have the routing engine take info consideration barriers, etc. that exist between the closest road/path and the destination lat/long. I put in my vote to put this on the priority list.</p>
<p>The not so great practical solution of building "false" paths to cause the routing engine to produce the desired result is what I have chosen to do. The goal would be that when barriers are taken into consideration, these false paths will be removed.</p>
</div>
<div id="comment-57188-info" class="comment-info">
<span class="comment-age">(19 Jul '17, 21:31)</span> <span class="comment-user userinfo">Ken Oates</span>
</div>
</div>
</div>
<div id="comment-tools-57022" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57022-form-container" class="comment-form-container">
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

