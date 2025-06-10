+++
type = "question"
title = "unable to download tiles (403 forbidden)"
description = '''Hello, As a developper, I now have to work on an existing application with a setup of leaflet using OSM that is already in place. The application is displaying a map on a page (client side application using Angular). If I deploy the code somewhere, the map is working fine. But during the development...'''
date = "2022-03-16T15:39:00Z"
lastmod = "2022-03-17T14:52:00Z"
weight = 83887
keywords = [ "tiles", "network" ]
aliases = [ "/questions/83887" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [unable to download tiles (403 forbidden)](/questions/83887/unable-to-download-tiles-403-forbidden)

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
<span id="post-83887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83887-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>As a developper, I now have to work on an existing application with a setup of leaflet using OSM that is already in place. The application is displaying a map on a page (client side application using Angular). If I deploy the code somewhere, the map is working fine. But during the development phase, the project runs in local (served on localhost:4200). But in local the map does not load and I can see many calls failing in the network tab of the debugger. I can see that the app can't load tiles because it gets an HTTP 403 forbidden as a reponse.</p>
<p>Below you can find a example of a call done for a tile that is failing:</p>
<p>curl 'https://a.tile.openstreetmap.org/18/134243/87922.png' \<br />
-H 'authority: a.tile.openstreetmap.org' \<br />
-H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36' \<br />
-H 'accept: image/avif,image/webp,image/apng,image/svg+xml,image/<em>,</em>/*;q=0.8' \ -H 'sec-fetch-site: cross-site' \<br />
-H 'sec-fetch-mode: no-cors' \<br />
-H 'sec-fetch-dest: image' \<br />
-H 'referer: <a href="http://localhost:4200/&#39;">http://localhost:4200/'</a> \<br />
-H 'accept-language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7' \<br />
--compressed</p>
<p>After some more investigation I found that in local it works on Safari but not on Chrome. So the problem seems to come from headers added by the browser.</p>
<p><em>UPDATE 1</em>:<br />
On chrome I can retrieve a tile if the referer if different than localhost.<br />
On Safari it works even with referer is equal to localhost.<br />
It seems to be related to user-agent and/or referer.<br />
</p>
<p>I have the impression that OSM is validating those 2 headers: referer and user-agent<br />
If this statement is correct:</p>
<ul>
<li>Chrome user agent is not accepted</li>
<li>localhost referer is not accepted</li>
</ul>
<p><strong>Chrome</strong><br />
version used: Version 99.0.4844.74 (Build officiel) (x86_64)<br />
user-agent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"</p>
<p><strong>Safari</strong><br />
version used: Version 15.3 (17612.4.9.1.8)<br />
user-agent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15"</p>
<p>Do you think this is a normal behavior ? If OSM need one of those 2 headers to be validated on the server side, I'm not getting why it does not reconize Chrome user-agent as a valid one. Am I missing something ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '22, 15:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ac7dd92a1c18b822d8f79a7a4566e415?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="X4V1PXS&#39;s gravatar image" />
<p><span>X4V1PXS</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="X4V1PXS has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Mar '22, 16:51</strong> </span></p>
</div>
</div>
<div id="comments-container-83887" class="comments-container">
<span id="83892"></span>
<div id="comment-83892" class="comment">
<div id="post-83892-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It's unclear exactly what you are trying to do and where localhost fits in?</p>
<p>Normally a leaflet map would use localhost if there are tiles being served locally. Do you believe that you are doing that?</p>
</div>
<div id="comment-83892-info" class="comment-info">
<span class="comment-age">(16 Mar '22, 16:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="83893"></span>
<div id="comment-83893" class="comment">
<div id="post-83893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm working on a projet as a developper. During the development phase, the project runs in local (served on localhost:4200). Leaflet is set up to have a map on a page. It works everywhere but not in local. After some investigation I saw that it's due to 2 headers: user-agent and/or referer. I added more details as an update in the original post. If something is not clear, please tell me and I'll add all the needed informations.</p>
</div>
<div id="comment-83893-info" class="comment-info">
<span class="comment-age">(16 Mar '22, 16:44)</span> <span class="comment-user userinfo">X4V1PXS</span>
</div>
</div>
<span id="83894"></span>
<div id="comment-83894" class="comment">
<div id="post-83894-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Now just look at the other side. The OWG has to try to block users that are not following the Tile Usage Policy and overusing the systems. The problem is: some of them just fake user-agent and referrer, therefore they'll have to block those combinations (right now it's maybe localhost as referrer + Chrome as User-Agent) that are used by bad actors, which might result in false positives while blocking, so this may happen anytime. Works today, stops tomorrow (the same would happen if e.g. Fastly would stop sponsoring their CDN resources for OSM). But please remember: the OWG is working on this voluntarily in their free time for the OSM project. So if the application is a project for work, it's best to find a reliable tile provider (when you pay someone money, you have someone to complain to if sth. is not working). If the project is just for fun, you may think about setting up your own tileserver (see <a href="https://www.switch2osm.org">https://www.switch2osm.org</a> for a guide), which will cost time (and server resources=money) as well.</p>
</div>
<div id="comment-83894-info" class="comment-info">
<span class="comment-age">(16 Mar '22, 16:59)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83895"></span>
<div id="comment-83895" class="comment">
<div id="post-83895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So is there a way to get localhost working or no? If so, what are the steps?</p>
<p>Thanks.</p>
</div>
<div id="comment-83895-info" class="comment-info">
<span class="comment-age">(17 Mar '22, 12:46)</span> <span class="comment-user userinfo">Pintosack</span>
</div>
</div>
<span id="83896"></span>
<div id="comment-83896" class="comment not_top_scorer">
<div id="post-83896-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the OWG blocks localhost right now, you can't do anything about but either not use localhost or use a different tile provider or host tiles yourself. The problem with localhost is that the OWG won't be able to distinguish your application. So be creative in making UA and Referrer unique and best include a way to contact you. See <a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a> for more information.</p>
</div>
<div id="comment-83896-info" class="comment-info">
<span class="comment-age">(17 Mar '22, 12:51)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="83899"></span>
<div id="comment-83899" class="comment">
<div id="post-83899-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Maybe this will help someone else, for those using leaflet, we fixed it by changing http to https on the tileLayer png. Seems to work on localhost in Chrome &amp; Edge.</p>
</div>
<div id="comment-83899-info" class="comment-info">
<span class="comment-age">(17 Mar '22, 14:05)</span> <span class="comment-user userinfo">Pintosack</span>
</div>
</div>
</div>
<div id="comment-tools-83887" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-83887-form-container" class="comment-form-container">
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

<span id="83900"></span>

<div id="answer-container-83900" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83900-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer from Pintosack works for me. Thanks!</p>
<p><strong>Maybe this will help someone else, for those using leaflet, we fixed it by changing http to https on the tileLayer png. Seems to work on localhost in Chrome &amp; Edge.</strong></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '22, 14:52</strong></p>
<img src="https://secure.gravatar.com/avatar/1e4209b8b09a21c4b2b96450fe686ded?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Captainfreedom&#39;s gravatar image" />
<p><span>Captainfreedom</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Captainfreedom has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-83900" class="comments-container">
&#10;</div>
<div id="comment-tools-83900" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83900-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83897"></span>

<div id="answer-container-83897" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83897-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Set up your own tile server (see <a href="https://switch2osm.org/serving-tiles/">here</a>) or use a third-party supplier (see <a href="https://switch2osm.org/providers/">here</a>).</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '22, 12:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Mar '22, 12:54</strong> </span></p>
</div>
</div>
<div id="comments-container-83897" class="comments-container">
&#10;</div>
<div id="comment-tools-83897" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83897-form-container" class="comment-form-container">
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

