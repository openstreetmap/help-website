+++
type = "question"
title = "Overpass Server:  Dispatcher Error Please help!"
description = '''Hi, I am trying to run an overpass instance on my own server but I&#x27;m stuck.  I can successfully run static queries on the server and they work as expected.  Now i&#x27;m trying to get the Web service API working but Im having trouble.  If I run the command  http://195.53.128.67/api/interpreter?data=way(5...'''
date = "2014-05-26T18:47:00Z"
lastmod = "2014-07-03T21:08:00Z"
weight = 33487
keywords = [ "overpass", "api", "dispatcher", "install", "error" ]
aliases = [ "/questions/33487" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass Server: Dispatcher Error Please help!](/questions/33487/overpass-server-dispatcher-error-please-help)

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
<span id="post-33487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33487-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am trying to run an overpass instance on my own server but I'm stuck.</p>
<p>I can successfully run static queries on the server and they work as expected. Now i'm trying to get the Web service API working but Im having trouble.</p>
<p>If I run the command</p>
<p><a href="http://195.53.128.67/api/interpreter?data=way(50.838400,%20-0.124373,50.839240,%20-0.122571);">http://195.53.128.67/api/interpreter?data=way(50.838400,%20-0.124373,50.839240,%20-0.122571);</a></p>
<p>I get the message</p>
<pre><code>Error: runtime error: open64: 2 No such file or directory /osm3s_v0.7.4_osm_base Dispatcher_Client::1</code></pre>
<p>Now, if I try to start the dispatcher server:</p>
<pre><code>sudo nohup /root/osm-3s_v0.7.4/build/bin/dispatcher --osm-base --db-dir=/root/osm-3s_v0.7.4/db --meta &amp;
tail -f nohup.out</code></pre>
<p>It tells me:</p>
<pre><code>File_Error Address already in use 98 /root/osm-3s_v0.7.4/db//osm3s_v0.7.4_osm_base Dispatcher_Server::4</code></pre>
<p>Does anyone know anything I can try to get it working please? Ive been battling with this all weekend This is driving me crazy!</p>
<p>Thanks in advance :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-dispatcher" rel="tag" title="see questions tagged &#39;dispatcher&#39;">dispatcher</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 May '14, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/5abb2932327bb97ee8a2abc3c14caa8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmeister4&#39;s gravatar image" />
<p><span>gmeister4</span><br />
<span class="score" title="60 reputation points">60</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmeister4 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33487" class="comments-container">
<span id="33493"></span>
<div id="comment-33493" class="comment">
<div id="post-33493-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Address already in use seems to indicate that there's another process which is already bound to the same TCP/IP socket. What does netstat -t tell you?</p>
<p>The wiki page I originally quoted here was talking about some issues with stale lock files in /dev/shm. But your error message seems to point to another issue.</p>
</div>
<div id="comment-33493-info" class="comment-info">
<span class="comment-age">(26 May '14, 19:15)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="33494"></span>
<div id="comment-33494" class="comment">
<div id="post-33494-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi mmd thanks for getting back to me,</p>
<p>I did know about the lock and had deleted it.</p>
<p>Here is the output of netstat -t</p>
<p>tcp 0 64 StreetServer:ssh cpc1-brig15-2-0-c:61674 ESTABLISHED tcp 0 0 StreetServer:ssh cpc1-brig15-2-0-c:61626 ESTABLISHED tcp 0 0 StreetServer:ssh pa1-160.wireless.:44703 ESTABLISHED tcp 0 0 StreetServer:ssh pa1-160.wireless.:39404 ESTABLISHED tcp 0 0 StreetServer:http cpc1-brig15-2-0-c:61676 TIME_WAIT</p>
<p>I am new to ubuntu :/</p>
</div>
<div id="comment-33494-info" class="comment-info">
<span class="comment-age">(26 May '14, 19:44)</span> <span class="comment-user userinfo">gmeister4</span>
</div>
</div>
<span id="33498"></span>
<div id="comment-33498" class="comment">
<div id="post-33498-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, I put in the wrong parameter for netstat (didn't have a system available). I was looking for active processes listening on tcp/ip ports. The following command should print those along with the respective program name.</p>
<p>sudo netstat -ltp</p>
<p>Sample output:</p>
<p>Proto Recv-Q Send-Q Local Address Foreign Address State PID/Program name tcp 0 0 localhost:ipp <em>:</em> LISTEN 993/cupsd<br />
tcp 0 0 <em>:postgresql</em> :* LISTEN 1280/postgres<br />
[...]</p>
</div>
<div id="comment-33498-info" class="comment-info">
<span class="comment-age">(26 May '14, 22:03)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="33507"></span>
<div id="comment-33507" class="comment">
<div id="post-33507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here it is:</p>
<p>root@GeoNet:~# sudo netstat -ltp</p>
<p>Proto Recv-Q Send-Q Local Address Foreign Address State PID/Program name tcp 0 0 <em>:smtp</em> : <em>LISTEN 597/master tcp 0 0</em> :http <em>:</em> LISTEN 15767/apache2 tcp 0 0 <em>:ssh</em> : <em>LISTEN 1661/sshd tcp6 0 0 [::]:smtp [::]:</em> LISTEN 597/master tcp6 0 0 [::]:ssh [::]:* LISTEN 1661/sshd</p>
</div>
<div id="comment-33507-info" class="comment-info">
<span class="comment-age">(27 May '14, 13:47)</span> <span class="comment-user userinfo">gmeister4</span>
</div>
</div>
<span id="33508"></span>
<div id="comment-33508" class="comment">
<div id="post-33508-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Now im getting a new problem, if I try to make a request I get a 403 forbidden error.</p>
<p>"You don't have permission to access /api/interpreter on this server."</p>
<p>I have run all the permission commands suggested here though: <a href="http://overpass-api.de/full_installation.html">http://overpass-api.de/full_installation.html</a></p>
<p>Any ideas? Thanks</p>
</div>
<div id="comment-33508-info" class="comment-info">
<span class="comment-age">(27 May '14, 13:49)</span> <span class="comment-user userinfo">gmeister4</span>
</div>
</div>
</div>
<div id="comment-tools-33487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33487-form-container" class="comment-form-container">
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

<span id="34610"></span>

<div id="answer-container-34610" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34610-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>FYI: Someone else reported the same issue on <a href="http://stackoverflow.com/questions/24525795/overpass-api-dispatcher-fails-with-address-already-in-use-98">stackoverflow</a> just yesterday. It seemed to be caused by some stale lock files. Added this to the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/install#Troubleshooting">Overpass API troubleshooting section</a> on the OSM wiki now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '14, 21:08</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span> </br></br></p>
</div>
</div>
<div id="comments-container-34610" class="comments-container">
&#10;</div>
<div id="comment-tools-34610" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34610-form-container" class="comment-form-container">
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

