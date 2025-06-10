+++
type = "question"
title = "How to estimate building height"
description = '''I&#x27;m programming an interface which allow to draw path fo drones. But I need to know if there are buildings(and infos like height) on the drone&#x27;s path. Even an estimation would be fine for me. I&#x27;m wondering how this website estimate the building height without infos like building:levels  https://osmb...'''
date = "2017-08-17T18:50:00Z"
lastmod = "2017-08-18T10:48:00Z"
weight = 58360
keywords = [ "building", "height" ]
aliases = [ "/questions/58360" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to estimate building height](/questions/58360/how-to-estimate-building-height)

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
<span id="post-58360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58360-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm programming an interface which allow to draw path fo drones. But I need to know if there are buildings(and infos like height) on the drone's path. Even an estimation would be fine for me.</p>
<p>I'm wondering how this website estimate the building height without infos like building:levels <a href="https://osmbuildings.org/?lat=48.13475&amp;lon=-1.63061&amp;zoom=19&amp;rotation=0&amp;tilt=30">https://osmbuildings.org/?lat=48.13475&amp;lon=-1.63061&amp;zoom=19&amp;rotation=0&amp;tilt=30</a></p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-height" rel="tag" title="see questions tagged &#39;height&#39;">height</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '17, 18:50</strong></p>
<img src="https://secure.gravatar.com/avatar/3b023bbb92dfc8bb4e406206b1c83ec6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naxos222&#39;s gravatar image" />
<p><span>naxos222</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naxos222 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '17, 19:47</strong> </span></p>
</div>
</div>
<div id="comments-container-58360" class="comments-container">
&#10;</div>
<div id="comment-tools-58360" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58360-form-container" class="comment-form-container">
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

<span id="58362"></span>

<div id="answer-container-58362" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58362-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58362-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-58362-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="naxos222 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps someone with more knowledge about OSM Buildings' implementation can add some information here, but 3D renderers often use the same default height for all buildings without <code>height</code> or <code>building:levels</code> tags (perhaps with some random variation thrown in). And from the looks of it, OSM Buildings is no different in that regard.</p>
<p>If you want to go down that road, one resource that you could use to guess heights is the value of the building key. While <a href="https://taginfo.openstreetmap.org/keys/building#values">most buildings use <code>yes</code> as the building value</a>, quite a few have more detailed tagging. When estimating heights, an <code>apartments</code> building is probably taller than a <code>shed</code> or <code>garages</code> building. There are other tags that might be found on buildings, such as <a href="https://wiki.openstreetmap.org/wiki/Key:shop">shop</a>, <a href="https://wiki.openstreetmap.org/wiki/Key:amenity">amenity</a> or even <a href="https://wiki.openstreetmap.org/wiki/Tag:man_made%3Dtower">man_made=tower</a> – all of which allow some refining of your initial estimates.</p>
<p>Ultimately, though, I doubt that you can produce sufficiently reliable estimates on that basis. Keep in mind that, even though these tags are a lot more common than level counts or height measurements, they are still only available for a minority of buildings. And even where they exist, there are exceptions for all assumptions one might make about "normal" heights for a particular building category.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '17, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-58362" class="comments-container">
<span id="58363"></span>
<div id="comment-58363" class="comment">
<div id="post-58363-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not to mention that we may not "even" have the building outlines at all (while OSM probably has the best building coverage of all map data providers on a global scale, it is still very patchy).</p>
</div>
<div id="comment-58363-info" class="comment-info">
<span class="comment-age">(17 Aug '17, 20:46)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-58362" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58362-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="58364"></span>

<div id="answer-container-58364" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58364-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Naxos222, please remember to use the old boy-scouts trick, measure the building with a pencil at the length of your arm on its base and the height. And use that to determine the height of the building. There's one problem you’ll have to make a local survey. Or choose to count the levels and estimate the height of a level as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '17, 22:37</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-58364" class="comments-container">
<span id="58366"></span>
<div id="comment-58366" class="comment">
<div id="post-58366-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Unless I'm mistaken, naxos222 is asking about extracting and/or extrapolating height information from the existing data, not measuring the height to add to the data.</p>
</div>
<div id="comment-58366-info" class="comment-info">
<span class="comment-age">(17 Aug '17, 23:58)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="58367"></span>
<div id="comment-58367" class="comment">
<div id="post-58367-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>alester yes, its possible using programmes to build up the elevation, but its special and priceless. Needless to say, that I don’t expect any mapper to have that that kind of tools or even the right valuable views to use with the program, images up to 5 cm in detail. A mapper should use what’s legal possible and available during a survey, is n't it ? Although this is not a platform for reply’s I recon you should get one anyway.</p>
</div>
<div id="comment-58367-info" class="comment-info">
<span class="comment-age">(18 Aug '17, 00:30)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="58368"></span>
<div id="comment-58368" class="comment">
<div id="post-58368-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hendrikklaas, the OP is asking as a data consumer, not as a mapper. He is not asking for tools nor methods to use during survey. Actually, he is asking to make up data that is not there. Data that current 3D engines seems to make up randomly, so completely useless for his purposes.</p>
</div>
<div id="comment-58368-info" class="comment-info">
<span class="comment-age">(18 Aug '17, 04:10)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="58378"></span>
<div id="comment-58378" class="comment">
<div id="post-58378-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hendrikklass, Alester and Escada are right but thank you for reply anyway</p>
</div>
<div id="comment-58378-info" class="comment-info">
<span class="comment-age">(18 Aug '17, 10:48)</span> <span class="comment-user userinfo">naxos222</span>
</div>
</div>
</div>
<div id="comment-tools-58364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58364-form-container" class="comment-form-container">
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

