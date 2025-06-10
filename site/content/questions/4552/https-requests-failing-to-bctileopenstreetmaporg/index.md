+++
type = "question"
title = "https requests failing to b,c.tile.openstreetmap.org"
description = '''I am using Teleriks RadMap silverlight control (in a https site) with OpenStreetMap as the provider, I am unable to view any map data so investigated using fiddler.  I initially got: The remote server (a.tile.openstreetmap.org) presented a certificate that did not validate, due to RemoteCertificateN...'''
date = "2011-04-16T18:14:00Z"
lastmod = "2014-01-05T03:02:00Z"
weight = 4552
keywords = [ "tiles", "https" ]
aliases = [ "/questions/4552" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [https requests failing to b,c.tile.openstreetmap.org](/questions/4552/https-requests-failing-to-bctileopenstreetmaporg)

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
<span id="post-4552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4552-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using Teleriks RadMap silverlight control (in a https site) with OpenStreetMap as the provider, I am unable to view any map data so investigated using fiddler.</p>
<p>I initially got:</p>
<pre><code>The remote server (a.tile.openstreetmap.org) presented a certificate that did not validate, due to RemoteCertificateNameMismatch.
&#10;SUBJECT: CN=*.openstreetmap.org, OU=Domain Control Validated - RapidSSL(R), OU=See www.rapidssl.com/resources/cps (c)10, OU=GT33044578, O=*.openstreetmap.org, C=GB, SERIALNUMBER=Dgi7Lfgx7wbOkaryb/3olT0IlEQOS5b9
ISSUER: OU=Equifax Secure Certificate Authority, O=Equifax, C=US
EXPIRES: 14/02/2012 23:38:04
&#10;(This warning can be disabled by clicking Tools | Fiddler Options.)
&#10;HTTPS connection failed.
&#10;System.Net.Sockets.SocketException: No connection could be made because the target machine actively refused it 128.40.168.104:443
   at Fiddler.ServerChatter.CreateConnectedSocket(IPAddress[] arrDestIPs, Int32 iPort, Session _oSession)
   at Fiddler.Session._handleHTTPSConnect()</code></pre>
<p>In my browser I added a.tile.openstreetmap.org as an allowed exception and that connection now seems to be accepted, however I am still seeing no map data and for requests to b.tile.openstreetmap.org and c.tile.openstreetmap.org I see:</p>
<pre><code>HTTPS connection failed.
&#10;System.Net.Sockets.SocketException: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond 128.40.168.104:443
   at Fiddler.ServerChatter.CreateConnectedSocket(IPAddress[] arrDestIPs, Int32 iPort, Session _oSession)
   at Fiddler.Session._handleHTTPSConnect()</code></pre>
<p>I am not sure what to do to solve this so any advice appreciated.</p>
<p>Stunty.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '11, 18:14</strong></p>
<img src="https://secure.gravatar.com/avatar/451a0453d27991889a8fa70292a7a946?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stunty&#39;s gravatar image" />
<p><span>Stunty</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stunty has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jan '14, 09:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-4552" class="comments-container">
&#10;</div>
<div id="comment-tools-4552" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4552-form-container" class="comment-form-container">
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

<span id="29592"></span>

<div id="answer-container-29592" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29592-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>https is available from today (5th Jan 2014) on a,b,c.tile.openstreetmap.org. Initially only as a test.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '14, 03:02</strong></p>
<img src="https://secure.gravatar.com/avatar/e79628d44a15e95c607f8c5007d0ccd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishy&#39;s gravatar image" />
<p><span>Firefishy ♦♦</span><br />
<span class="score" title="1296 reputation points"><span>1.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishy has 14 accepted answers">29%</span></p>
</div>
</div>
<div id="comments-container-29592" class="comments-container">
&#10;</div>
<div id="comment-tools-29592" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29592-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4553"></span>

<div id="answer-container-4553" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4553-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-4553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We don't support https access to our tiles - it's just too expensive from a CPU point of view given the number of tiles that we serve.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '11, 20:37</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-4553" class="comments-container">
<span id="4585"></span>
<div id="comment-4585" class="comment">
<div id="post-4585-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thanks, I will see if I can get the control to request http only.</p>
</div>
<div id="comment-4585-info" class="comment-info">
<span class="comment-age">(18 Apr '11, 09:59)</span> <span class="comment-user userinfo">Stunty</span>
</div>
</div>
<span id="15347"></span>
<div id="comment-15347" class="comment">
<div id="post-15347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I understand the need to keep cpu load down.</p>
<p>Unfortunately, with https for the tiles, it's very difficult to embed a map in an https web page because most browsers will present the user with a scary warning about "unsecured" parts of the web page.</p>
<p>I wonder if it would be possible to offer both http and https - for people who are showing an http, they can use the http version (and reduce load). But for those displaying the map in an https page, we could choose the https page?</p>
</div>
<div id="comment-15347-info" class="comment-info">
<span class="comment-age">(21 Aug '12, 22:55)</span> <span class="comment-user userinfo">jamie</span>
</div>
</div>
<span id="15349"></span>
<div id="comment-15349" class="comment">
<div id="post-15349-score" class="comment-score">
6
</div>
<div class="comment-text">
<p>OSM is not a general-purpose, unlimited-access tileserver. If you want to embed tiles in your webpage but need more than the basic, limited-bandwidth service provided by OSM, you are encouraged to download planet.osm and render your own.</p>
</div>
<div id="comment-15349-info" class="comment-info">
<span class="comment-age">(22 Aug '12, 00:08)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-4553" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4553-form-container" class="comment-form-container">
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

