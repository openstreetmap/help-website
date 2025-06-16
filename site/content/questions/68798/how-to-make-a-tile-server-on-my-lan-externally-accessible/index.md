+++
type = "question"
title = "How to make a tile server on my LAN externally accessible?"
description = '''I have successfully installed my own map tile server using the same guide as here on an Ubuntu desktop. I have reserved the IP of my server using its MAC address via DHCP in my router so now my server has always the same IP in the home network. I can serve tiles to any device (laptop, cell phone) th...'''
date = "2019-04-15T15:49:00Z"
lastmod = "2019-04-19T00:57:00Z"
weight = 68798
keywords = [ "forwarding", "port" ]
aliases = [ "/questions/68798" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to make a tile server on my LAN externally accessible?](/questions/68798/how-to-make-a-tile-server-on-my-lan-externally-accessible)

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
<span id="post-68798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68798-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have successfully installed my own map tile server using the same guide as <a href="/questions/67834/how-to-start-using-my-own-mounted-tile-server?page=1&amp;focusedAnswerId=68798#68798">here</a> on an Ubuntu desktop.</p>
<p>I have reserved the IP of my server using its MAC address via DHCP in my router so now my server has always the same IP in the home network. I can serve tiles to any device (laptop, cell phone) that is connected to the home network using this IP, but I need some help regarding accessing the service from outside. I have followed some instructions and created a hostname on DDNS provider No-IP. After that, I have opened a port in my router (port forwarding) that “shows” at the stable internal IP (192.168.X.X) of my server. Is this correct? Then, I installed and configured ddclient on the desktop to use my account at No-IP and redirect the hits of the hostname at my server. When I change the first argument of L.tileLayer to “hostname:port” in leaflet files the map does not appear and finally times out.</p>
<p>I used nmap for both hostname and 192.168.X.X and I received “Host is up”, “not shown: xxx closed ports”. I received the same for nmap localhost but with an additional open port shown for postgresql. Is there something wrong with the installation? Finally, when I nslookup the hostname from my Windows laptop I get as an address the gateway (router’s IP).</p>
<p>Finally, is there a way to make the access to the service restrictive? Apologies for mentioning too many details but I am a beginner and just want to be surel. I searched for a guide on network configuration for own osm tile server but did not find any. Please for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-forwarding" rel="tag" title="see questions tagged &#39;forwarding&#39;">forwarding</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '19, 15:49</strong></p>
<img src="https://secure.gravatar.com/avatar/e8163e2e2f7e46a3f8f153657008a6d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yol_89&#39;s gravatar image" />
<p><span>yol_89</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yol_89 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> converted to question <strong>15 Apr '19, 16:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-68798" class="comments-container">
&#10;</div>
<div id="comment-tools-68798" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68798-form-container" class="comment-form-container">
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

<span id="68800"></span>

<div id="answer-container-68800" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68800-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It sounds like you've already set up port forwarding on your router between your external IP address and the internal machine where Apache is running. To check that this is working</p>
<ul>
<li><p>Use a "show my ip address" service such as <a href="https://whatismyipaddress.com/">this one</a> (others are available) to show your current IPV4 address.</p></li>
<li><p>Turn off wifi access on your phone and browse using mobile data to that address - just type the numbers into the address bar and tap return to try and make an http:// connection to that address.</p></li>
</ul>
<p>If it gives "unable to connect" then either your haven't done the port forwarding properly or your ISP is blocking access to port 80 on your connection. We know you can serve tiles to other devices on your home LAN so it's unlikely (although not impossible) that a local firewall is blocking access on the tile server itself. If it can (i.e. you can an Apache "it worked" page), then we'd need to understand exactly how you are referencing the tile layer.</p>
<p>What to do next depends on the answer to the previous paragraph...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '19, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '19, 17:01</strong> </span></p>
</div>
</div>
<div id="comments-container-68800" class="comments-container">
<span id="68819"></span>
<div id="comment-68819" class="comment">
<div id="post-68819-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I checked the port (24) I had declared at NO-IP and at my router for port forwarding at several online tools for open port checking and it always seemed close. I tried different ports and adjusted some settings on the router with my ISP but the result was the same for all. I finally tried to port forward the port 80 which appeared open in every tool only when my desktop was open. At this time I got the Apache "It works" when I browse to my public IP from my phone using mobile data. I then tried to use my hostname in leaflet file (I removed the ":24" from my IP at NO-IP site) but it did not load. Finally when I "ip a" command on desktop I get inet 192.168.X.X:24.</p>
</div>
<div id="comment-68819-info" class="comment-info">
<span class="comment-age">(16 Apr '19, 20:26)</span> <span class="comment-user userinfo">yol_89</span>
</div>
</div>
<span id="68843"></span>
<div id="comment-68843" class="comment">
<div id="post-68843-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>First things first - don't worry about dynamic DNS or your account at NO-IP - just try and get internet routing working first.</p>
<p>What you'd normally do is:</p>
<ul>
<li>Run a web server on port 80 on your LAN</li>
<li>Forward port 80 on your router to port 80 on the web server o your LAN</li>
<li>Have users access port 80 on the external address of your router, which gets forwarded to port 80 on your web server</li>
</ul>
<p>It sounds like you've got port forwarding working on port 80 (you got the Apache "It works" when you browsed to your public IP from your phone using mobile data).</p>
<p>The next bit is name resolution. Let's imagine that the name you've reserved with NO-IP is "example123.hopto.org". From a command line on a PC do "nslookup example123.hopto.org". If that returns your current IP address then you should be able to use "example123.hopto.org" in place of your current IP address, and the client that you can download from them is supposed to keep it updated when your IP address changes. I'm not sure why you'd declare a port with NO-IP (but I've never used their update client - maybe it is something to do with that?).</p>
</div>
<div id="comment-68843-info" class="comment-info">
<span class="comment-age">(19 Apr '19, 00:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68800" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68800-form-container" class="comment-form-container">
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

