+++
type = "question"
title = "Shortest route"
description = '''Our administrators install OSRM v5. I try build the shortest route. uri: /route/v1/driving/50.792940,61.659061;50.798636,61.665437;50.811901,61.669517;50.768080,61.730977 server return faster route (about 11,5 km) and i can`t find how build shortest route (aboute 10 km). Can i do this by options in ...'''
date = "2017-04-26T13:31:00Z"
lastmod = "2017-04-27T14:18:00Z"
weight = 55887
keywords = [ "osrm", "shortest" ]
aliases = [ "/questions/55887" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Shortest route](/questions/55887/shortest-route)

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
<span id="post-55887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55887-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Our administrators install OSRM v5. I try build the shortest route. uri: /route/v1/driving/50.792940,61.659061;50.798636,61.665437;50.811901,61.669517;50.768080,61.730977 server return faster route (about 11,5 km) and i can`t find how build shortest route (aboute 10 km).</p>
<p>Can i do this by options in request string or need change config on server. Or it is not possible.</p>
<p>thank you in advance<img src="/upfiles/1_8XGezPK.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-shortest" rel="tag" title="see questions tagged &#39;shortest&#39;">shortest</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '17, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/deaffec0d34d8055de6b275d94bb3aa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex%20taxi21&#39;s gravatar image" />
<p><span>Alex taxi21</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex taxi21 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '17, 15:02</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span></p>
</div>
</div>
<div id="comments-container-55887" class="comments-container">
<span id="55915"></span>
<div id="comment-55915" class="comment">
<div id="post-55915-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your responses )</p>
<p>It is a pity that can not just ask the OSRM option in the query to build the shortest route (</p>
</div>
<div id="comment-55915-info" class="comment-info">
<span class="comment-age">(27 Apr '17, 14:18)</span> <span class="comment-user userinfo">Alex taxi21</span>
</div>
</div>
</div>
<div id="comment-tools-55887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55887-form-container" class="comment-form-container">
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

<span id="55908"></span>

<div id="answer-container-55908" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55908-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To get the shortest route, you will need to create a custom profile (a .lua file) where all roads are weighted at the same speed. The routing algorithm will then choose a 5-mile unclassified road (at 60mph) in preference to a 6-mile trunk road (at 60mph), whereas the standard car.lua will choose a 6-mile trunk road at 60mph in preference to a 5-mile unclassified road at 40mph.</p>
<p>You will need to specify the path to your profile in the command line when calling osrm-extract. I would recommend starting with car.lua and modifying it rather than creating a new profile from scratch.</p>
<p>As Andy has mentioned, I gave a brief overview of OSRM's profiles at <a href="/questions/30272/how-the-routing-osrm-algorithm-works">https://help.openstreetmap.org/questions/30272/how-the-routing-osrm-algorithm-works</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '17, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-55908" class="comments-container">
&#10;</div>
<div id="comment-tools-55908" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55908-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55899"></span>

<div id="answer-container-55899" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55899-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Note: this is not from first hand experience.</p>
<p>OSRM always only has one profile per instance, at least when it is run in normal CH mode. And, as far as I know, the standard setup optimizes drive time, not distance. In other words you would have to set up an instance that uses the travelled distance as the metric (which I assume is possible, bat may be not easy).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '17, 21:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-55899" class="comments-container">
<span id="55905"></span>
<div id="comment-55905" class="comment">
<div id="post-55905-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you tell more about travelled distance as the metric? I tried build alternative routes by options, but OSRM always build only that route for points like in picture</p>
</div>
<div id="comment-55905-info" class="comment-info">
<span class="comment-age">(27 Apr '17, 07:51)</span> <span class="comment-user userinfo">Alex taxi21</span>
</div>
</div>
</div>
<div id="comment-tools-55899" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55899-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55906"></span>

<div id="answer-container-55906" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55906-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This works <a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=61.7141%2C50.7956%3B61.6808%2C50.8076#map=12/61.6972/50.8332">https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=61.7141%2C50.7956%3B61.6808%2C50.8076#map=12/61.6972/50.8332</a></p>
<p>but if i extend the route south a small amount <a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=61.7141%2C50.7956%3B61.6759%2C50.8092#map=12/61.6951/50.8095">https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=61.7141%2C50.7956%3B61.6759%2C50.8092#map=12/61.6951/50.8095</a> the route takes the detour you have found. The obvious route your dotted one as a 60kph speed limit mapped the used alternative as no limit set. Maybe osrm calculates that as slower because of the 60kph</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '17, 08:26</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Apr '17, 08:29</strong> </span></p>
</div>
</div>
<div id="comments-container-55906" class="comments-container">
<span id="55907"></span>
<div id="comment-55907" class="comment">
<div id="post-55907-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Richard's answer here may help you <a href="/questions/30272/how-the-routing-osrm-algorithm-works">https://help.openstreetmap.org/questions/30272/how-the-routing-osrm-algorithm-works</a></p>
</div>
<div id="comment-55907-info" class="comment-info">
<span class="comment-age">(27 Apr '17, 08:49)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-55906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55906-form-container" class="comment-form-container">
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

