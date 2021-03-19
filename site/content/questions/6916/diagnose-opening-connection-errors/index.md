+++
type = "question"
title = "diagnose opening connection errors"
description = '''Newbie question. I&#x27;m trying to diagnose why a Java-based app runs for a while as a client making SOAP webservice calls, and then starts hitting an exception whereby it cannot open a socket. The OS is Windows 2003 server SP1. I suspect that there&#x27;s an error in the way that the client-side API is bein...'''
date = "2011-10-17T04:04:00Z"
lastmod = "2011-10-17T04:04:00Z"
weight = 6916
keywords = [ "windows", "java", "socket" ]
aliases = [ "/questions/6916" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [diagnose opening connection errors](/questions/6916/diagnose-opening-connection-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6916-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Newbie question.</p><p>I'm trying to diagnose why a Java-based app runs for a while as a client making SOAP webservice calls, and then starts hitting an exception whereby it cannot open a socket. The OS is Windows 2003 server SP1.</p><p>I suspect that there's an error in the way that the client-side API is being used (Axis2 v1.4), such that it fails to recycle some internal resource. Once we hit the condition of not being able to open a socket, we have to restart the Java app.</p><p>I'm wondering if we can use Wireshark to help diagnose the problem from an OS/network standpoint?</p><p>for information, our Java stack trace is: Caused by:</p><pre><code>java.net.ConnectException: Connection timed out: connect
at java.net.PlainSocketImpl.socketConnect(Native Method)
at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)
at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)
at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:366)
at java.net.Socket.connect(Socket.java:516)
at java.net.Socket.connect(Socket.java:466)
at java.net.Socket.&lt;init&gt;(Socket.java:366)
at java.net.Socket.&lt;init&gt;(Socket.java:239)</code></pre><p>Many thanks for any insight. Dan Haywood</p></div><div id="question-tags" class="tags-container tags">windows java socket</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '11, 04:04</strong></p><img src="https://secure.gravatar.com/avatar/104c92cb8b783d382fe406e08cbe6a6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danhaywood&#39;s gravatar image" /><p>danhaywood<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danhaywood has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '11, 23:56</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-6916" class="comments-container"></div><div id="comment-tools-6916" class="comment-tools"></div><div class="clear"></div><div id="comment-6916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

