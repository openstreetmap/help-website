+++
type = "question"
title = "How to start using my own mounted Tile Server?"
description = '''So, I have succesfully installed my own map tile server using this guide: https://switch2osm.org/manually-building-a-tile-server-18-04-lts/ Everything went perfect, but now, I dont know how to start consuming my service in my WEB page using leaflet: L.tileLayer(&#x27;http://{s}.tile.osm.org/{z}/{x}/{y}.p...'''
date = "2019-02-01T13:58:00Z"
lastmod = "2019-04-15T16:47:00Z"
weight = 67834
keywords = [ "leaflet", "tileserver" ]
aliases = [ "/questions/67834" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to start using my own mounted Tile Server?](/questions/67834/how-to-start-using-my-own-mounted-tile-server)

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
<span id="post-67834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67834-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So, I have succesfully installed my own map tile server using this guide: <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a></p>
<p>Everything went perfect, but now, I dont know how to start consuming my service in my WEB page using leaflet:</p>
<p>L.tileLayer(<strong>'http://{s}.tile.osm.org/{z}/{x}/{y}.png'</strong>, { attribution: '© <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' }).addTo(map);</p>
<p>I have a ddns and I want to catch my service. What kind of routing should I do in my router to point to my Tile Server? What number of internal port should I use to point to the server machine and consume the service from the outside? And then, how should the link look like? Im assuming it should be something like: <strong>'http://MyDdns:OuterPort/Mod_tiles/{z}/{x}/{y}.png'</strong> Am I wrong? Is there a way to protect the acces to the service to be restrictive, via a key or of the sorts?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '19, 13:58</strong></p>
<img src="https://secure.gravatar.com/avatar/9ae0c5f5d68d1969f28ebdc5a89d18a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leo_1991&#39;s gravatar image" />
<p><span>Leo_1991</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leo_1991 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Feb '19, 21:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-67834" class="comments-container">
<span id="68799"></span>
<div id="comment-68799" class="comment">
<div id="post-68799-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've moved the new question that was "asked" as an answer here to <a href="https://help.openstreetmap.org/questions/68798/how-to-make-a-tile-server-on-my-lan-externally-accessible">https://help.openstreetmap.org/questions/68798/how-to-make-a-tile-server-on-my-lan-externally-accessible</a> .</p>
</div>
<div id="comment-68799-info" class="comment-info">
<span class="comment-age">(15 Apr '19, 16:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67834" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67834-form-container" class="comment-form-container">
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

<span id="67835"></span>

<div id="answer-container-67835" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67835-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Leo_1991 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>What kind of routing should I do in my router to point to my Tile Server?</p>
</blockquote>
<p>Set up your router to forward whatever port you want to forward to your internal server to that server on the same or another port.</p>
<blockquote>
<p>Im assuming it should be something like: 'http://MyDdns:OuterPort/Mod_tiles/{z}/{x}/{y}.png'</p>
</blockquote>
<p>The config file for “renderd” is “/usr/local/etc/renderd.conf”. Your version of that probably refers to a map style called "ajt" so the full path to a file would be something like <a href="https://yourdns">https://yourdns</a>:yourport/hot/0/0/0.png .</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '19, 14:21</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-67835" class="comments-container">
<span id="67836"></span>
<div id="comment-67836" class="comment">
<div id="post-67836-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer!</p>
<p>But now it throws an "ERR_CONNECTION_REFUSED", I have all ports closed by default.Must I have any other opened?</p>
</div>
<div id="comment-67836-info" class="comment-info">
<span class="comment-age">(01 Feb '19, 15:51)</span> <span class="comment-user userinfo">Leo_1991</span>
</div>
</div>
<span id="67837"></span>
<div id="comment-67837" class="comment">
<div id="post-67837-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried an nmap on the domain, and the port 5000, the one I configured on router pointing to tile server throws the following:</p>
<p>PORT STATE SERVICE REASON 5000/tcp closed upnp conn-refused</p>
<p>Other ports wich I have open and running other services clearly specifies the service being run...</p>
</div>
<div id="comment-67837-info" class="comment-info">
<span class="comment-age">(01 Feb '19, 16:21)</span> <span class="comment-user userinfo">Leo_1991</span>
</div>
</div>
<span id="67838"></span>
<div id="comment-67838" class="comment">
<div id="post-67838-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Oh oh oh oh, I see where is my error now. The internal port should be an specific one. Now everything is fine and up running. Thank you!</p>
</div>
<div id="comment-67838-info" class="comment-info">
<span class="comment-age">(01 Feb '19, 16:35)</span> <span class="comment-user userinfo">Leo_1991</span>
</div>
</div>
</div>
<div id="comment-tools-67835" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67835-form-container" class="comment-form-container">
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

