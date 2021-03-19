+++
type = "question"
title = "SSL MySQL Need help to construe wireshark"
description = '''Hello  I use wireshark the first time to make sure that my MS Access connection to the MYSQL Database (Webserver) is SSL secured.  Now I got foue lines (protocols?) first and third line (PC to Server): Login Request User= And the second line (Server to PC): Server greeting proto=10 version=5.5.37-0+...'''
date = "2014-06-01T08:24:00Z"
lastmod = "2014-06-01T13:31:00Z"
weight = 33240
keywords = [ "ssl", "fixme", "incomplete", "mysql" ]
aliases = [ "/questions/33240" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL MySQL Need help to construe wireshark](/questions/33240/ssl-mysql-need-help-to-construe-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33240-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I use wireshark the first time to make sure that my MS Access connection to the MYSQL Database (Webserver) is SSL secured.</p>Now I got foue lines (protocols?) first and third line (PC to Server): <code>Login Request User=</code>And the second line (Server to PC): <code>Server greeting proto=10 version=5.5.37-0+wheezy1</code>In this three lines the MYSQL Protocol tells me: <code>Switch to SSL after handshake: Set</code>'That sound great!But the last line and the second line (Server to PC) tells me: <code>Switch to SSL after handshake: Not Set</code>Furthermore in the last line and the: the Payload protocol has a yellow background an tells me:<pre><code>[Expert Info (warn/ undecoded): FIXME - dissector is incomplete]
[Message: FIXME - dissector is incomplete]
[Severity level: Warn]
[Group: Undecoded]</code></pre>Now my question: Is my connection save or not?I don't dare to post the protocols because I don't know which of the lines have relevant security informations.Thanks Sebastian</div><div id="question-tags" class="tags-container tags">ssl fixme incomplete mysql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '14, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/42d0919d3b7a46da793f6228e29529a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sebastian12345&#39;s gravatar image" /><p>Sebastian12345<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sebastian12345 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jun '14, 08:31</p></div></div><div id="comments-container-33240" class="comments-container"></div><div id="comment-tools-33240" class="comment-tools"></div><div class="clear"></div><div id="comment-33240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33244"></span>

<div id="answer-container-33244" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33244-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Select one frame, right click it and select 'Follow TCP Stream'. If you can read ASCII Text in the popup window, like SQL commands (SELECT etc.) the connection is <strong>not encrypted</strong>.</p><p>You can test that procedure and compare the results with the following MySQL capture file</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=mysql_complete.pcap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=mysql_complete.pcap</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '14, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jun '14, 15:18</p></div></div><div id="comments-container-33244" class="comments-container"><span id="33263"></span><div id="comment-33263" class="comment"><div id="post-33263-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt,</p><p>thanks, Danke!</p><p>It looks like my connection is encrypted. Although the first lines which I can read shows the following clear text ("vQp^hui!.mysql_native_passwort as well as the official Adress of my hoster. But thats nothing I have to worry about, right?</p><pre><code>T...
5.5.37-0+wheezy1..J..,&lt;&#39;P;vdq...................-)&amp;&quot;vQp^hui!.mysql_native_password. 
.....&gt;[email protected]!...........................Y...U..G...to.....`..H.U&lt;...L.
[..S.p.2.....9.8.5.3.2./.~.}.|.y.x.w.t.s.r....</code></pre><p>In your example file it is not encrypted, right?</p><p>Regards Sebastian</p></div><div id="comment-33263-info" class="comment-info"><span class="comment-age">(02 Jun '14, 03:25)</span> Sebastian12345</div></div><span id="33283"></span><div id="comment-33283" class="comment"><div id="post-33283-score" class="comment-score"></div><div class="comment-text"><blockquote><p>It looks like my connection is encrypted.</p></blockquote><p>well, without the file I cannot say anything about that. The small snippet you posted gives no clear indication.</p><p><strong>But</strong>, if you are not seeing any cleartext in the whole file (after you retrieved some data), chances are good, that the connection is encrypted.</p><p>Unfortunately I don't have access to a capture file with SSL encrypted MySQL traffic, so I cannot check if there is a better criteria.</p><p>You could try to "Decode As" the connections as SSL and check if Wireshark detects a SSL handshake.</p><ul><li>select one frame</li><li>right click it</li><li>select "Decode As"</li><li>select "Transport [tab]"</li><li>select "SSL" (in the list of protocols on the right side)</li></ul><p>Then use the following display filter: <strong>ssl</strong>. If you see any frames, especially a CLIENT HELO and a SERVER HELO, the connection is (most certainly) encrypted!</p><blockquote><p>In your example file it is not encrypted, right?</p></blockquote><p>right.</p></div><div id="comment-33283-info" class="comment-info"><span class="comment-age">(02 Jun '14, 07:51)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-33244" class="comment-tools"></div><div class="clear"></div><div id="comment-33244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

