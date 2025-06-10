+++
type = "question"
title = "Unusual routing decision"
description = '''Can anyone explain this rather exotic routing decision? https://www.openstreetmap.org/#map=14/50.8579/-1.1657 I have checked for ways that are not correctly joined, but I cannot find any. The route that I am trying to create is from 50.8507, -1.1538, to 50.8515, -1.1882 by car. Eventually I will red...'''
date = "2017-12-14T18:15:00Z"
lastmod = "2018-01-02T08:22:00Z"
weight = 61189
keywords = [ "osrm", "routingerror" ]
aliases = [ "/questions/61189" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Unusual routing decision](/questions/61189/unusual-routing-decision)

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
<span id="post-61189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61189-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can anyone explain this rather exotic routing decision? <a href="https://www.openstreetmap.org/#map=14/50.8579/-1.1657">https://www.openstreetmap.org/#map=14/50.8579/-1.1657</a> I have checked for ways that are not correctly joined, but I cannot find any.</p>
<p>The route that I am trying to create is from 50.8507, -1.1538, to 50.8515, -1.1882 by car. Eventually I will rediscover how to attach an image to this question, and I will be able to show everyone what route the computer chose.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-routingerror" rel="tag" title="see questions tagged &#39;routingerror&#39;">routingerror</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '17, 18:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Dec '17, 08:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-61189" class="comments-container">
<span id="61191"></span>
<div id="comment-61191" class="comment">
<div id="post-61191-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>... which I think is:</p>
<p><a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=50.8507%2C-1.1535%3B50.8521%2C-1.1884#map=14/50.8579/-1.1506">https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=50.8507%2C-1.1535%3B50.8521%2C-1.1884#map=14/50.8579/-1.1506</a></p>
</div>
<div id="comment-61191-info" class="comment-info">
<span class="comment-age">(14 Dec '17, 18:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61192"></span>
<div id="comment-61192" class="comment not_top_scorer">
<div id="post-61192-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you, Someone Else. That certainly illustrates the behaviour, although I had intended the journey to stop somewhere around the railway station.</p>
</div>
<div id="comment-61192-info" class="comment-info">
<span class="comment-age">(14 Dec '17, 18:31)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
<span id="61197"></span>
<div id="comment-61197" class="comment not_top_scorer">
<div id="post-61197-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Madryn it seems mapzen and graph hopper seem to work as you would expect. Only osrm takes the longer distance route, perhaps osrm's timings for the junctions cause the odd route. I assume from SomeoneElse's comment you now know that you can just cut and paste the url of the map with the route on it. <a href="https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=50.8510%2C-1.1554%3B50.8520%2C-1.1910#map=14/50.8510/-1.1673">https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=50.8510%2C-1.1554%3B50.8520%2C-1.1910#map=14/50.8510/-1.1673</a></p>
</div>
<div id="comment-61197-info" class="comment-info">
<span class="comment-age">(14 Dec '17, 23:49)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="61198"></span>
<div id="comment-61198" class="comment">
<div id="post-61198-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Just an idea: To test an odd routing result i usually just push red and green flags along in short sections until it reveals the problem, it also gives the distance and the time, that may give a clue why osrm does what it does. no need to open an editor until the "error" has been located, maybe?</p>
</div>
<div id="comment-61198-info" class="comment-info">
<span class="comment-age">(14 Dec '17, 23:57)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="61200"></span>
<div id="comment-61200" class="comment not_top_scorer">
<div id="post-61200-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the suggestion, andy mackey, but I tried that before I asked the question. The routing system behaved as though the Eastern Way sliproad leading south west from the Delme Roundabout was not connected to the main dual carriageway. However, when I looked, there seemed to be nothing wrong with that junction. It seems that the router really wants to avoid the roundabout, but will use it if left with no alternative.</p>
</div>
<div id="comment-61200-info" class="comment-info">
<span class="comment-age">(15 Dec '17, 07:53)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
<span id="61204"></span>
<div id="comment-61204" class="comment">
<div id="post-61204-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>At the risk of stating the obvious, it's perhaps worth mentioning that some routers use older data (sometimes quite a lot older). A problem with one router doesn't mean a problem with OSM data.</p>
</div>
<div id="comment-61204-info" class="comment-info">
<span class="comment-age">(15 Dec '17, 12:03)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61207"></span>
<div id="comment-61207" class="comment not_top_scorer">
<div id="post-61207-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you check the surface=* tag on the roads? Sometimes it might effect routing.</p>
</div>
<div id="comment-61207-info" class="comment-info">
<span class="comment-age">(15 Dec '17, 17:52)</span> <span class="comment-user userinfo">Mxdanger</span>
</div>
</div>
<span id="61208"></span>
<div id="comment-61208" class="comment">
<div id="post-61208-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>, I checked the history of the Cams Hill, it's from 2013, one of the traffic signals causing the problem from 2014. I think it's unlikely that data is the reason. I think it's a glitch in their algorithm.</p>
</div>
<div id="comment-61208-info" class="comment-info">
<span class="comment-age">(15 Dec '17, 19:06)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="61322"></span>
<div id="comment-61322" class="comment">
<div id="post-61322-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You can report potential OSRM bugs at <a href="https://github.com/Project-OSRM/osrm-backend/issues.">https://github.com/Project-OSRM/osrm-backend/issues.</a> I've created a report for you: <a href="https://github.com/Project-OSRM/osrm-backend/issues/4754">https://github.com/Project-OSRM/osrm-backend/issues/4754</a></p>
</div>
<div id="comment-61322-info" class="comment-info">
<span class="comment-age">(22 Dec '17, 08:59)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-61189" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-61189-form-container" class="comment-form-container">
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

<span id="61202"></span>

<div id="answer-container-61202" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61202-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-61202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Madryn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>when I move the start marker, I notice that for OSRM the problem is located at the traffic signal on Cams Hill (near the bus stop 'Delme Arms Ph') . Exclude that from the route, and it goes over the roundabout. Include it, and it makes a u-turn at the traffic signal. After moving the end marker, it seems the OSRM does not "like' the 2 traffic signals: <a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=50.85216%2C-1.16498%3B50.85311%2C-1.16852#map=18/50.85266/-1.16673">https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=50.85216%2C-1.16498%3B50.85311%2C-1.16852#map=18/50.85266/-1.16673</a> include both and it goes wrong, include only 1 and the route is OK.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '17, 11:26</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-61202" class="comments-container">
&#10;</div>
<div id="comment-tools-61202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61202-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61448"></span>

<div id="answer-container-61448" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61448-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-61448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to <a href="https://github.com/Project-OSRM/osrm-backend/issues/4754">https://github.com/Project-OSRM/osrm-backend/issues/4754</a> this is an upstream bug caused by an invalidly applied U-Turn penalty. It will be fixed in the next OSRM release.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '18, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-61448" class="comments-container">
&#10;</div>
<div id="comment-tools-61448" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61448-form-container" class="comment-form-container">
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

