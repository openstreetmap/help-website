+++
type = "question"
title = "Apache server shows multiple POST requests, Wireshark shows none. Why?"
description = '''I have an Apache access log showing that multiple POST requests were sent to it and they all succeeded with a return code of 200. When I look at the Wireshark trace, I don&#x27;t see anything except the certificate authentications. What am I missing here? Why don&#x27;t I see the POST activity? The Wireshark ...'''
date = "2012-07-16T11:55:00Z"
lastmod = "2012-07-16T12:28:00Z"
weight = 12776
keywords = [ "post" ]
aliases = [ "/questions/12776" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Apache server shows multiple POST requests, Wireshark shows none. Why?](/questions/12776/apache-server-shows-multiple-post-requests-wireshark-shows-none-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12776-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an Apache access log showing that multiple POST requests were sent to it and they all succeeded with a return code of 200. When I look at the Wireshark trace, I don't see anything except the certificate authentications. What am I missing here? Why don't I see the POST activity?</p><p>The Wireshark trace is at: <a href="http://cloudshark.org/captures/b97dc3a7b311?filter=ip.addr%20%3D%3D%20192.168.5.103">http://cloudshark.org/captures/b97dc3a7b311?filter=ip.addr%20%3D%3D%20192.168.5.103</a></p><p>The Apache access log entries are:</p><pre><code>192.168.5.103 - - [16/Jul/2012:11:07:31 -0700] &quot;POST /support/electronic/itssdr/IESproxy.wss HTTP/1.0&quot; 200 11290    
192.168.5.103 - - [16/Jul/2012:11:07:50 -0700] &quot;POST /support/electronic/itssdr/IESproxy.wss HTTP/1.0&quot; 200 11290    
192.168.5.103 - - [16/Jul/2012:11:07:55 -0700] &quot;POST /support/electronic/itssdr/IESproxy.wss HTTP/1.0&quot; 200 11290    
192.168.5.103 - - [16/Jul/2012:11:08:20 -0700] &quot;POST /support/electronic/itssdr/IESproxy.wss HTTP/1.0&quot; 200 11290    
192.168.5.103 - - [16/Jul/2012:11:08:25 -0700] &quot;POST /support/electronic/itssdr/IESproxy.wss HTTP/1.0&quot; 200 11290
192.168.5.103 - - [16/Jul/2012:11:08:51 -0700] &quot;POST /support/electronic/itssdr/IESproxy.wss HTTP/1.0&quot; 200 11290    
192.168.5.103 - - [16/Jul/2012:11:08:56 -0700] &quot;POST /support/electronic/itssdr/IESproxy.wss HTTP/1.0&quot; 200 11290    
192.168.5.103 - - [16/Jul/2012:11:09:21 -0700] &quot;POST /support/electronic/itssdr/IESproxy.wss HTTP/1.0&quot; 200 11290    
192.168.5.103 - - [16/Jul/2012:11:09:26 -0700] &quot;POST /support/electronic/itssdr/IESproxy.wss HTTP/1.0&quot; 200 11290</code></pre></div><div id="question-tags" class="tags-container tags">post</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '12, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/90ace4ca58ca53e9c64e6713d5950cf2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tcoder&#39;s gravatar image" /><p>tcoder<br />
<span class="score" title="0 reputation points">0</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tcoder has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jul '12, 11:59</p></div></div><div id="comments-container-12776" class="comments-container"></div><div id="comment-tools-12776" class="comment-tools"></div><div class="clear"></div><div id="comment-12776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12778"></span>

<div id="answer-container-12778" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12778-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The timestamps in the capture file do not match those in the apache log.</p><blockquote><p>minutes in the capture xx:<strong>23</strong>:xx<br />
minutes in the logs xx:<strong>07</strong>:xx - xx:<strong>09</strong>:xx</p></blockquote><p>So, either there is a time difference between the apache server and the capturing machine, or you are analyzing the wrong capture file.</p><p>I assume the later, as you can't see the POST requests (no TLS Application Data in the capture file).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '12, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jul '12, 12:29</p></div></div><div id="comments-container-12778" class="comments-container"></div><div id="comment-tools-12778" class="comment-tools"></div><div class="clear"></div><div id="comment-12778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

