+++
type = "question"
title = "Cannot pan/scroll using FireFox"
description = '''Since updating to the new FireFox (maybe five months ago) OpenStreetMap will not pan/scroll with the mouse. The mouse cursor is always a hand as if it had already grabbed the map. If I double click it will zoom and I can use the cursor keys. This is currently with FireFox 63 on Windows 10. There don...'''
date = "2018-11-05T11:21:00Z"
lastmod = "2019-01-30T00:09:00Z"
weight = 66671
keywords = [ "firefox" ]
aliases = [ "/questions/66671" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot pan/scroll using FireFox](/questions/66671/cannot-panscroll-using-firefox)

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
<span id="post-66671-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66671-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66671-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Since updating to the new FireFox (maybe five months ago) OpenStreetMap will not pan/scroll with the mouse. The mouse cursor is always a hand as if it had already grabbed the map. If I double click it will zoom and I can use the cursor keys. This is currently with FireFox 63 on Windows 10. There don't seem to be any posts like this in the help so I am guessing it is something specific to my system - does anyone know what it could be?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-firefox" rel="tag" title="see questions tagged &#39;firefox&#39;">firefox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Nov '18, 11:21</strong></p>
<img src="https://secure.gravatar.com/avatar/f975d12117093ce5b3b4748dc4927400?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobChafer&#39;s gravatar image" />
<p><span>RobChafer</span><br />
<span class="score" title="220 reputation points">220</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobChafer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66671" class="comments-container">
<span id="66673"></span>
<div id="comment-66673" class="comment">
<div id="post-66673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've not noticed it with Firefox (whatever is the current version - it updates itself regularly) on Windows 10. Do you have any add-ins installed? Presumably you're getting the problem when just browsing the map, not while editing?</p>
</div>
<div id="comment-66673-info" class="comment-info">
<span class="comment-age">(05 Nov '18, 14:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="66674"></span>
<div id="comment-66674" class="comment">
<div id="post-66674-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I disabled all the addins and the problem still remains. If I click edit I can pan/scroll and it immediately stops working when I exit edit mode.</p>
</div>
<div id="comment-66674-info" class="comment-info">
<span class="comment-age">(05 Nov '18, 15:03)</span> <span class="comment-user userinfo">RobChafer</span>
</div>
</div>
<span id="66679"></span>
<div id="comment-66679" class="comment">
<div id="post-66679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you pan on e.g. <a href="https://www.gpsies.com/createTrack.do">https://www.gpsies.com/createTrack.do</a> and on <a href="https://www.openstreetmap.de/karte.html">https://www.openstreetmap.de/karte.html</a> ?</p>
</div>
<div id="comment-66679-info" class="comment-info">
<span class="comment-age">(05 Nov '18, 19:30)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="66680"></span>
<div id="comment-66680" class="comment not_top_scorer">
<div id="post-66680-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Works on both those.</p>
</div>
<div id="comment-66680-info" class="comment-info">
<span class="comment-age">(05 Nov '18, 21:24)</span> <span class="comment-user userinfo">RobChafer</span>
</div>
</div>
<span id="66681"></span>
<div id="comment-66681" class="comment not_top_scorer">
<div id="post-66681-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm, GPSies uses the same library (Leaflet) like on osm.org.</p>
<p>I think you should try with a fresh firefox profile. E.g. try with another useraccount in your Windows.</p>
<p>By the way: does osm.org work with Internet Exporer or Edge?</p>
<p>What may give a hint: open the firefox console (hit ctrl+shift+K) and then open <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> . Any errors shown ("[HTTP/2.0 200 OK XXms]" is fine)?</p>
</div>
<div id="comment-66681-info" class="comment-info">
<span class="comment-age">(05 Nov '18, 21:31)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67796"></span>
<div id="comment-67796" class="comment">
<div id="post-67796-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have the exact same problem. I even uninstalled Firefox altogether and installed it again, without change.</p>
</div>
<div id="comment-67796-info" class="comment-info">
<span class="comment-age">(29 Jan '19, 19:16)</span> <span class="comment-user userinfo">Spades</span>
</div>
</div>
<span id="67797"></span>
<div id="comment-67797" class="comment not_top_scorer">
<div id="post-67797-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16223/spades">@Spades</a>: please could you provide version details of your firefox and system? With other browsers on the same system it works? What about other computers in the same network?</p>
</div>
<div id="comment-67797-info" class="comment-info">
<span class="comment-age">(29 Jan '19, 19:23)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67802"></span>
<div id="comment-67802" class="comment">
<div id="post-67802-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's Firefox 65.0 on Windows 10, version 1803. The problem affects Firefox on my desktop only, Edge on the same computer or Firefox on another one work just fine. Tried turning off the firefox add-ons too.</p>
</div>
<div id="comment-67802-info" class="comment-info">
<span class="comment-age">(30 Jan '19, 00:09)</span> <span class="comment-user userinfo">Spades</span>
</div>
</div>
</div>
<div id="comment-tools-66671" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-66671-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

