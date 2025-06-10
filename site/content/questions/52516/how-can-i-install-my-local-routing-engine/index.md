+++
type = "question"
title = "How can i install my local routing engine?"
description = '''I　want to set up a map which used in local area network. As i have installed the rails port, tile server and nominatim. I am going to build my local routing engine next step. And i find that OpenStreetMap use four online routing engine on the website, they are graphhopper, mapquest, mapzen and osrm....'''
date = "2016-10-13T07:56:00Z"
lastmod = "2016-10-25T08:39:00Z"
weight = 52516
keywords = [ "routing" ]
aliases = [ "/questions/52516" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can i install my local routing engine?](/questions/52516/how-can-i-install-my-local-routing-engine)

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
<span id="post-52516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52516-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I　want to set up a map which used in local area network. As i have installed the rails port, tile server and nominatim. I am going to build my local routing engine next step. And i find that OpenStreetMap use four online routing engine on the website, they are graphhopper, mapquest, mapzen and osrm. I have looked for many website on the wiki, but i still have no ideal what should i do to build local routing engine. Can someone tell me the overall step to build local routing engine .</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '16, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-52516" class="comments-container">
&#10;</div>
<div id="comment-tools-52516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52516-form-container" class="comment-form-container">
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

<span id="52519"></span>

<div id="answer-container-52519" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52519-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The realistic choices for running your own routing engines are likely</p>
<p>graphhopper - <a href="http://wiki.openstreetmap.org/wiki/GraphHopper">http://wiki.openstreetmap.org/wiki/GraphHopper</a></p>
<p>mapzen - <a href="https://github.com/valhalla">https://github.com/valhalla</a></p>
<p>OSRM - <a href="https://github.com/Project-OSRM">https://github.com/Project-OSRM</a></p>
<p>Which one is best suited for your needs depends really on your criteria, for example how large the area is you want to route over, if you want to be able to adjust routing parameters on the fly, what resources you have access to and so on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '16, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Oct '16, 13:29</strong> </span></p>
</div>
</div>
<div id="comments-container-52519" class="comments-container">
<span id="52521"></span>
<div id="comment-52521" class="comment">
<div id="post-52521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks to you reply, can you simply explain the difference between these three engines?</p>
</div>
<div id="comment-52521-info" class="comment-info">
<span class="comment-age">(13 Oct '16, 09:10)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
<span id="52522"></span>
<div id="comment-52522" class="comment">
<div id="post-52522-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>See <a href="https://wiki.openstreetmap.org/wiki/Routing/online_routers">https://wiki.openstreetmap.org/wiki/Routing/online_routers</a> for a comparison.</p>
</div>
<div id="comment-52522-info" class="comment-info">
<span class="comment-age">(13 Oct '16, 09:26)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="52523"></span>
<div id="comment-52523" class="comment">
<div id="post-52523-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hi yuyy, would it be better to start reading the linked pages first and ask specific questions later ?</p>
</div>
<div id="comment-52523-info" class="comment-info">
<span class="comment-age">(13 Oct '16, 09:31)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="52669"></span>
<div id="comment-52669" class="comment">
<div id="post-52669-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want try to install mapzen routing service, and i have read the mapzen turn-by-turn document in the mapzen website. Then i downloaded and installed thor on the <a href="https://github.com/valhalla/thor,">https://github.com/valhalla/thor,</a> but i don't know how to use it. Should i build a routing tile and make a web front end that provide a browser-based routing interface. If so what should i do to realize that. I don't have a clear idea, can someone tell me a feasible solution? And i am sorry that i reply so late and ask this so nasty problem.</p>
</div>
<div id="comment-52669-info" class="comment-info">
<span class="comment-age">(25 Oct '16, 08:26)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
<span id="52670"></span>
<div id="comment-52670" class="comment">
<div id="post-52670-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is a separate problem. Please open a new question for it.</p>
</div>
<div id="comment-52670-info" class="comment-info">
<span class="comment-age">(25 Oct '16, 08:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52519-form-container" class="comment-form-container">
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

