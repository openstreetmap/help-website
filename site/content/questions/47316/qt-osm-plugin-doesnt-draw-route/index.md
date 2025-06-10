+++
type = "question"
title = "qt osm plugin doesnt draw route"
description = '''Hey everyone, I am developing a project for my term project and in one of the modules it gets two coordinates from me, finds the shortest path and shows the route. But for about a week now, the plugin doesn&#x27;t seem to find any route. I double check with the routing server address provided on QT&#x27;s web...'''
date = "2015-12-30T00:49:00Z"
lastmod = "2016-01-01T15:04:00Z"
weight = 47316
keywords = [ "routingerror", "routing", "qt" ]
aliases = [ "/questions/47316" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [qt osm plugin doesnt draw route](/questions/47316/qt-osm-plugin-doesnt-draw-route)

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
<span id="post-47316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47316-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey everyone,</p>
<p>I am developing a project for my term project and in one of the modules it gets two coordinates from me, finds the shortest path and shows the route. But for about a week now, the plugin doesn't seem to find any route. I double check with the routing server address provided on QT's webpage and tried anything seems like a host address with no luck. I also made contact with Aaron McCarthy from QT to address the problem, still no working solution. But one of he recommended was to run a routing query on OSM website which worked just fine.</p>
<p>What I am asking, -is there any routing server host I can try or test if mine's working, -any known issues anyone experienced working with OSM and/or QT Location API lately ?</p>
<p>Thanks all in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routingerror" rel="tag" title="see questions tagged &#39;routingerror&#39;">routingerror</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-qt" rel="tag" title="see questions tagged &#39;qt&#39;">qt</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '15, 00:49</strong></p>
<img src="https://secure.gravatar.com/avatar/965611b619fb058aed5e00428671347e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aleqria&#39;s gravatar image" />
<p><span>aleqria</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aleqria has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Dec '15, 11:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-47316" class="comments-container">
<span id="47324"></span>
<div id="comment-47324" class="comment">
<div id="post-47324-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please state which routing server address you are using to make queries.</p>
</div>
<div id="comment-47324-info" class="comment-info">
<span class="comment-age">(30 Dec '15, 08:48)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="47328"></span>
<div id="comment-47328" class="comment">
<div id="post-47328-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, ok. Here it is : "http://osrm.server.address/viaroute"</p>
</div>
<div id="comment-47328-info" class="comment-info">
<span class="comment-age">(30 Dec '15, 10:16)</span> <span class="comment-user userinfo">aleqria</span>
</div>
</div>
<span id="47329"></span>
<div id="comment-47329" class="comment">
<div id="post-47329-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>osrm.server.address is not a valid domain name, so you won't get any results from there.</p>
</div>
<div id="comment-47329-info" class="comment-info">
<span class="comment-age">(30 Dec '15, 10:31)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="47331"></span>
<div id="comment-47331" class="comment">
<div id="post-47331-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it's what presented on <a href="http://doc.qt.io/qt-5/location-plugin-osm.html">http://doc.qt.io/qt-5/location-plugin-osm.html</a> . And the odd thing is this was working perfectly until a week ago. Also valid domain names are welcomed.</p>
</div>
<div id="comment-47331-info" class="comment-info">
<span class="comment-age">(30 Dec '15, 10:55)</span> <span class="comment-user userinfo">aleqria</span>
</div>
</div>
</div>
<div id="comment-tools-47316" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47316-form-container" class="comment-form-container">
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

<span id="47332"></span>

<div id="answer-container-47332" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47332-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess until a week ago you did not specify the (optional!) parameter <code>osm.routing.host</code>. Then it defaulted to <a href="http://router.project-osrm.org/viaroute"><code>http://router.project-osrm.org/viaroute</code></a> if I understand your linked Qt docu page correctly. <a href="http://osrm.server.address/viaroute"><code>http://osrm.server.address/viaroute</code></a> is just a placeholder address which is used in the example parameter listing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '15, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Dec '15, 11:40</strong> </span></p>
</div>
</div>
<div id="comments-container-47332" class="comments-container">
<span id="47335"></span>
<div id="comment-47335" class="comment">
<div id="post-47335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also note that in the description for the "osm.routing.host" parameter, the "URL" link points to the correct address: <a href="http://router.project-osrm.org/viaroute">http://router.project-osrm.org/viaroute</a></p>
</div>
<div id="comment-47335-info" class="comment-info">
<span class="comment-age">(30 Dec '15, 16:35)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="47351"></span>
<div id="comment-47351" class="comment">
<div id="post-47351-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I checked the packets being sent in and out using Wireshark and bumped into a packet named Application Data with the content of application.json file which in following struct : <a href="http://imagizer.imageshack.us/a/img633/8568/r8O6tK.jpg">http://imagizer.imageshack.us/a/img633/8568/r8O6tK.jpg</a></p>
<p>I suspect there been some adjustments in Qt side about receiving and parsing the json file.</p>
<p>Any ideas ?</p>
</div>
<div id="comment-47351-info" class="comment-info">
<span class="comment-age">(01 Jan '16, 15:04)</span> <span class="comment-user userinfo">aleqria</span>
</div>
</div>
</div>
<div id="comment-tools-47332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47332-form-container" class="comment-form-container">
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

