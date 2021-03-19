+++
type = "question"
title = "Telnet messages are being dropped"
description = '''Hello.  I am using a Python3.3 script that uses a telnet connection from telnetlib library. Now, I am using the write(command) and read() functions of this connection. So, after wiresharking this simple code: import telnetlib import sys def func1(IP,user,passw):  t=telnetlib.Telnet(IP)  t.write(user...'''
date = "2013-10-30T04:30:00Z"
lastmod = "2013-10-30T06:02:00Z"
weight = 26533
keywords = [ "python", "telnet" ]
aliases = [ "/questions/26533" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Telnet messages are being dropped](/questions/26533/telnet-messages-are-being-dropped)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26533-score" class="post-score" title="current number of votes">0</div><span id="post-26533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I am using a Python3.3 script that uses a telnet connection from telnetlib library.</p><p>Now, I am using the <code>write(command)</code> and <code>read()</code> functions of this connection.</p><p>So, after wiresharking this simple code:</p><pre><code>import telnetlib
import sys
def func1(IP,user,passw):
    t=telnetlib.Telnet(IP)
    t.write(user.encode(&#39;ascii&#39;)+b&#39;\n&#39;)
    t.write(passw.encode(&#39;ascii&#39;)+b&#39;\n&#39;)
    return t

def func2(t,command):
    t.write(command.encode(&#39;ascii&#39;)+b&#39;\n&#39;)
    print(command)

user=sys.argv[1]
passw=sys.argv[2]
IP=sys.argv[3]
t=func1(IP,user,passw)
for i in range(6):
   func2(t, &quot;message &quot;+str(i))</code></pre><p>I saw a weird behavior on Wireshark. After submitting the username and password, it send to the server a packet which contains only 2 messages out of six (within the 'for loop'), and the next packet is also from my computer, resetting the telnet conection!</p><p>By adding a line to <code>func2</code>:</p><pre><code>def func2(t,command):
    t.write(command.encode(&#39;ascii&#39;)+b&#39;\n&#39;)
    t.read_eager()   #The new line
    print(command)</code></pre><p>Somehow it works fine.</p><p>Now, it should not be like that. If I am using the <code>write(command)</code> 10 times one after each other, not the way I used here, It works fine without any need of <code>read()</code>.</p><p>Any idea?</p><p>The last two packets:</p><pre><code>  no.    time       source  destination  protocol  info

1501    11.754366   A.B.C.A *.*.*.113   TELNET  Telnet Data ...

1502    11.760757   A.B.C.A *.*.*.113   TCP esimport &gt; telnet [RST, ACK] Seq=40 Ack=7 Win=0 Len=0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-telnet" rel="tag" title="see questions tagged &#39;telnet&#39;">telnet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '13, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/f74689baa9af8a44163fa395c457212f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itay_user&#39;s gravatar image" /><p><span>itay_user</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itay_user has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Oct '13, 04:58</strong> </span></p></div></div><div id="comments-container-26533" class="comments-container"></div><div id="comment-tools-26533" class="comment-tools"></div><div class="clear"></div><div id="comment-26533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26536"></span>

<div id="answer-container-26536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26536-score" class="post-score" title="current number of votes">0</div><span id="post-26536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>this sounds more like a question for the developer of telnetlib (and/or a Python network programming forum) than for the Wireshark community, especially as did not provide a capture file !?!</p><p>Anyway: Can you post a capture file somewhere (google docs, dropbox, cloudshark.org). Maybe we can see something that helps you to debug your code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '13, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span></p></div></div><div id="comments-container-26536" class="comments-container"></div><div id="comment-tools-26536" class="comment-tools"></div><div class="clear"></div><div id="comment-26536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

