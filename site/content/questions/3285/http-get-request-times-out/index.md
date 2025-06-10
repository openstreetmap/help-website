+++
type = "question"
title = "HTTP GET Request Times Out"
description = '''I have a program running in Smallworld GIS that makes OpenStreetMap.org maps available as a backdrop. The program works for the vendor but not at my site. I can access OpenStreetMap.org maps from Internet Explorer just fine. I&#x27;ve dug down into the Smallworld api calls and found the method that makes...'''
date = "2011-02-22T19:41:00Z"
lastmod = "2011-02-24T17:01:00Z"
weight = 3285
keywords = [ "tiles", "http", "get" ]
aliases = [ "/questions/3285" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP GET Request Times Out](/questions/3285/http-get-request-times-out)

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
<span id="post-3285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3285-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a program running in Smallworld GIS that makes <a href="http://OpenStreetMap.org">OpenStreetMap.org</a> maps available as a backdrop. The program works for the vendor but not at my site. I can access <a href="http://OpenStreetMap.org">OpenStreetMap.org</a> maps from Internet Explorer just fine. I've dug down into the Smallworld api calls and found the method that makes the HTTP request. When I manually invoke the method to get data from other places, it works, but with <a href="http://OpenStreetMap.org">OpenStreetMap.org</a> it times out. I changed the HTTP GET request to HEAD, it works fine. Below is printed return information from a HEAD request:</p>
<pre><code>HTTP Port # 80
Setting up TCPIP Connection...
Local address: 131.191.187.166. port 1203
Remote address: 129.132.168.206. port 80
TCP Connection Result: HTTP/1.1 200 OK
Date: Tue, 22 Feb 2011 20:21:24 GMT
Server: Apache/2.2.3 (CentOS)
Cache-Control: max-age=10800
Last-Modified: Mon, 15 Nov 2010 08:56:07 GMT
Content-Length: 21013
Connection: close
Content-Type: image/png</code></pre>
<p>I've tried accessing <a href="http://OpenStreetMap.org">OpenStreetMap.org</a> maps from telnet and it times out as well:</p>
<pre><code>jfarmer@smtp001:~$ telnet 129.132.168.206 80
Trying 129.132.168.206...
Connected to 129.132.168.206.
Escape character is &#39;^]&#39;.
GET / HTTP/1.0</code></pre>
<p>And there it will sit for about 5 minutes, until the connection is closed by the remote host.</p>
<p>I suspect that this problem is very unique but hope someone may have an idea of what is going on.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-get" rel="tag" title="see questions tagged &#39;get&#39;">get</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '11, 19:41</strong></p>
<img src="https://secure.gravatar.com/avatar/fdc3e843c8c0e6ed7934cdc8cf9250d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tom%20Arer&#39;s gravatar image" />
<p><span>Tom Arer</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tom Arer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Feb '11, 08:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-3285" class="comments-container">
<span id="3288"></span>
<div id="comment-3288" class="comment">
<div id="post-3288-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>may be its your fire wall see my question... beginner-in-josm-stuck-at-download</p>
</div>
<div id="comment-3288-info" class="comment-info">
<span class="comment-age">(22 Feb '11, 21:09)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="3299"></span>
<div id="comment-3299" class="comment">
<div id="post-3299-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note1: 129.132.168.206 is <a href="http://wiki.openstreetmap.org/wiki/Servers/karosm">karosm</a> not www not tile Note2: do you press enter twice?</p>
</div>
<div id="comment-3299-info" class="comment-info">
<span class="comment-age">(23 Feb '11, 09:11)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="3356"></span>
<div id="comment-3356" class="comment">
<div id="post-3356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I looked at your response to beginner-in-josm-stuck-at-download.</p>
<p>I replaced the code in my api call with the URL you provided. I then did a HEAD request and here is part of the response:</p>
<p>Remote address: 128.40.168.105. port 80 TCP Connection Result: HTTP/1.1 405 Method Not Allowed Date: Thu, 24 Feb 2011 16:15:54 GMT</p>
<p>I did the GET request and it timed out.</p>
<p>My firewall guy doesn't believe that the GET request is being blocked. I need some specific information for him to do anything more. Any help is appreciated. BTW is there a way to do longer comments?</p>
</div>
<div id="comment-3356-info" class="comment-info">
<span class="comment-age">(24 Feb '11, 16:53)</span> <span class="comment-user userinfo">Tom Arer</span>
</div>
</div>
<span id="3357"></span>
<div id="comment-3357" class="comment">
<div id="post-3357-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Use the mailing lists.</p>
</div>
<div id="comment-3357-info" class="comment-info">
<span class="comment-age">(24 Feb '11, 17:01)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-3285" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3285-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

