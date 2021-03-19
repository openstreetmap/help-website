+++
type = "question"
title = "Why can&#x27;t Wireshark catch packets?"
description = '''Hi guys: My OS is windowsxp.When I use Wireshark to catch the packets between server and client who are both running on my comuputer,I can&#x27;t catch any packets between them. But on the other hand,I use command &#x27;netstat&#x27; to show connection between them and still find the establishment between them. Ma...'''
date = "2012-06-14T01:11:00Z"
lastmod = "2012-06-14T01:38:00Z"
weight = 11895
keywords = [ "netstat", "socket", "tcp" ]
aliases = [ "/questions/11895" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why can't Wireshark catch packets?](/questions/11895/why-cant-wireshark-catch-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11895-score" class="post-score" title="current number of votes">0</div><span id="post-11895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys:</p><p>My OS is windowsxp.When I use Wireshark to catch the packets between server and client who are both running on my comuputer,I can't catch any packets between them. But on the other hand,I use command 'netstat' to show connection between them and still find the establishment between them.</p><p>Maybe I can figure out the reason why Wireshark catch no data.(Because of their correspondence relys on LoopBack and datas aren't sent by interface.) Strongly I have no idea about the result that 'netstat' shows.In my opinion, netstat is connected with TCP/IP protocol and no three-way handshaking means no establishment,so how can netstat show this kind of result? It's a very confusing and contradictory result.</p><p>The result just look like belows:</p><p>Proto Local Address Foreign Address State PID</p><p>TCP 0.0.0.0:60000 0.0.0.0:0 LISTENING 2924</p><p>TCP 172.16.80.65:60000 172.16.80.65:1827 ESTABLISHED 2924</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-netstat" rel="tag" title="see questions tagged &#39;netstat&#39;">netstat</span> <span class="post-tag tag-link-socket" rel="tag" title="see questions tagged &#39;socket&#39;">socket</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '12, 01:11</strong></p><img src="https://secure.gravatar.com/avatar/eb9828f2ae3d482ad932d4192f555a4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="waterjacky&#39;s gravatar image" /><p><span>waterjacky</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="waterjacky has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '12, 01:22</strong> </span></p></div></div><div id="comments-container-11895" class="comments-container"></div><div id="comment-tools-11895" class="comment-tools"></div><div class="clear"></div><div id="comment-11895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11896"></span>

<div id="answer-container-11896" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11896-score" class="post-score" title="current number of votes">0</div><span id="post-11896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately you cannot sniff the loopback interface on Windows with Wireshark (WinPCAP).</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Loopback</code><br />
</p></blockquote><p>Regarding the netstat output (IP address not beeing the loopback address). What you see, depends on the IP address used by the client to connect to the server.</p><p>telnet 127.0.0.1 445</p><blockquote><p><code>TCP    127.0.0.1:1058         127.0.0.1:445          ESTABLISHED</code></p></blockquote><p>telnet 192.168.30.142 445</p><blockquote><p><code>TCP    192.168.30.142:1059    192.168.30.142:445     ESTABLISHED</code><br />
</p></blockquote><p>BOTH connections won't show up in Wireshark, as both are handled internally in the IP stack.</p><p>Finally here is an explanation for the last line of your netstat output:</p><blockquote><p><code>TCP 0.0.0.0:60000 0.0.0.0:0 LISTENING 2924</code><br />
<strong><code>TCP 172.16.80.65:60000 172.16.80.65:1827 ESTABLISHED 2924</code></strong><br />
</p></blockquote><p>Windows shows ESTABLISHED connections in this format</p><blockquote><p><code>LOCAL_ADDR:LOCAL_PORT REMOTE_ADDR:REMOTE_PORT.</code><br />
</p></blockquote><p>If the connection was established from the same machine, you will see <strong>two entries</strong>:</p><blockquote><p><code>TCP 172.16.80.65:60000 172.16.80.65:1827 ESTABLISHED 2924</code><br />
<code>TCP 172.16.80.65:1827 172.16.80.65:60000 ESTABLISHED xxxx</code><br />
</p></blockquote><p>2924 is the PID of your server process and <strong>xxxx</strong> is the PID of your client process.</p><p>Please run this command <code>netstat -nabo -p tcp</code> (be patient, it can take some time) and review the result.</p><p>Example, after <code>telnet localhost 445</code><br />
</p><blockquote><p><code>TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4</code><br />
<code>TCP    127.0.0.1:445          127.0.0.1:1073         ESTABLISHED     4</code><br />
<code>TCP    127.0.0.1:1073         127.0.0.1:445          ESTABLISHED     2884</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '12, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '12, 03:38</strong> </span></p></div></div><div id="comments-container-11896" class="comments-container"></div><div id="comment-tools-11896" class="comment-tools"></div><div class="clear"></div><div id="comment-11896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

