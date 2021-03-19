+++
type = "question"
title = "tcp/ftp performance"
description = '''Trying to follow a ftp stream and figure out why transferring the same file to different machines have different finish times. the FTP-DATA bytes show 32768, but if you add the acknowledgement numbers, the byte count does not add up. I could be totaly off base so I am asking the experts I am assumin...'''
date = "2013-02-08T16:37:00Z"
lastmod = "2013-02-09T03:24:00Z"
weight = 18454
keywords = [ "ack", "ftp", "tcp", "value", "performance" ]
aliases = [ "/questions/18454" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tcp/ftp performance](/questions/18454/tcpftp-performance)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18454-score" class="post-score" title="current number of votes">0</div><span id="post-18454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to follow a ftp stream and figure out why transferring the same file to different machines have different finish times. the FTP-DATA bytes show 32768, but if you add the acknowledgement numbers, the byte count does not add up. I could be totaly off base so I am asking the experts I am assuming the value of example: packet 151 - 156, I would subtract the last ack value packet 154 from ack value of packet 151. The ftp amount of data bytes sent was 52442 in packet 152.</p><pre><code>Packet  Time    Source  Destination Protocol    Length  Info
139 10.187547   x-server    Y--client   TCP 62  ftp-data &gt; 15943 [SYN] Seq=0 Win=8192 Len=0 MSS=4034 SACK_PERM=1
140 10.187632   Y--client   x-server    TCP 62  15943 &gt; ftp-data [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=4034 SACK_PERM=1
142 10.187831   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=1 Win=64544 Len=0
143 10.203807   Y--client   x-server    FTP-DATA    8122    FTP Data: 8068 bytes
144 10.204378   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=8069 Win=64544 Len=0
145 10.204398   Y--client   x-server    FTP-DATA    16190   FTP Data: 16136 bytes
146 10.204932   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=24205 Win=64544 Len=0
147 10.204946   Y--client   x-server    FTP-DATA    8618    FTP Data: 8564 bytes
148 10.205625   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=32769 Win=64544 Len=0
149 10.228625   Y--client   x-server    FTP-DATA    32822   FTP Data: 32768 bytes
150 10.228678   Y--client   x-server    FTP-DATA    8122    FTP Data: 8068 bytes
151 10.229349   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=69571 Win=64544 Len=0
152 10.229383   Y--client   x-server    FTP-DATA    52496   FTP Data: 52442 bytes
153 10.23007    x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=85707 Win=48408 Len=0
154 10.230071   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=117979 Win=16136 Len=0
155 10.230084   Y--client   x-server    FTP-DATA    5080    FTP Data: 5026 bytes
156 10.230421   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=126047 Win=8068 Len=0
157 10.230832   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=131073 Win=3042 Len=0
159 10.321455   x-server    Y--client   TCP 60  [TCP Window Update] ftp-data &gt; 15943 [ACK] Seq=1 Ack=131073 Win=64544 Len=0
160 10.321496   Y--client   x-server    FTP-DATA    60564   FTP Data: 60510 bytes
161 10.321526   Y--client   x-server    FTP-DATA    4088    [TCP Window Full] FTP Data: 4034 bytes
162 10.321895   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=147209 Win=64544 Len=0
163 10.321906   Y--client   x-server    FTP-DATA    1046    FTP Data: 992 bytes
164 10.321964   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=155277 Win=64544 Len=0
165 10.32211    x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=171413 Win=64544 Len=0
166 10.322134   Y--client   x-server    FTP-DATA    32822   FTP Data: 32768 bytes
167 10.322281   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=187549 Win=64544 Len=0
168 10.322406   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=196609 Win=64544 Len=0
169 10.322428   Y--client   x-server    FTP-DATA    28292   FTP Data: 28238 bytes
170 10.322531   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=208711 Win=64544 Len=0
171 10.322543   Y--client   x-server    FTP-DATA    4584    FTP Data: 4530 bytes
172 10.322871   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=224847 Win=64544 Len=0
173 10.322872   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=237445 Win=64544 Len=0
174 10.322872   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=253581 Win=64544 Len=0
175 10.322894   Y--client   x-server    FTP-DATA    32822   FTP Data: 32768 bytes
176 10.32324    x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=262145 Win=64544 Len=0
177 10.32326    Y--client   x-server    FTP-DATA    28292   FTP Data: 28238 bytes
178 10.323601   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=274247 Win=64544 Len=0
179 10.323602   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=290383 Win=64544 Len=0
180 10.323603   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=294913 Win=64544 Len=0
181 10.323624   Y--client   x-server    FTP-DATA    36360   [TCP Window Full] FTP Data: 36306 bytes
182 10.323968   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=311049 Win=64544 Len=0
183 10.323969   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=319117 Win=64544 Len=0
184 10.323979   Y--client   x-server    FTP-DATA    1046    FTP Data: 992 bytes
185 10.32431    x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=335253 Win=64544 Len=0
186 10.324311   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=343321 Win=64544 Len=0
187 10.324312   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=360449 Win=64544 Len=0
188 10.324333   Y--client   x-server    FTP-DATA    32822   FTP Data: 32768 bytes
189 10.324393   Y--client   x-server    FTP-DATA    28292   FTP Data: 28238 bytes
190 10.324804   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=372551 Win=64544 Len=0
191 10.324815   Y--client   x-server    FTP-DATA    4584    FTP Data: 4530 bytes
192 10.325138   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=388687 Win=64544 Len=0
193 10.325139   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=405319 Win=64544 Len=0
194 10.32514    x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=417421 Win=64544 Len=0
195 10.325161   Y--client   x-server    FTP-DATA    32822   FTP Data: 32768 bytes
196 10.325508   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=425985 Win=64544 Len=0
197 10.325641   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=438087 Win=64544 Len=0
198 10.325642   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=454223 Win=64544 Len=0
199 10.326086   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=458753 Win=64544 Len=0
200 10.328562   Y--client   x-server    FTP-DATA    32822   FTP Data: 32768 bytes
201 10.328616   Y--client   x-server    FTP-DATA    28292   FTP Data: 28238 bytes
202 10.32924    x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=470855 Win=64544 Len=0
203 10.329244   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=482957 Win=64544 Len=0
204 10.329245   x-server    Y--client   TCP 60  ftp-data &gt; 15943 [ACK] Seq=1 Ack=495555 Win=64544 Len=0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-value" rel="tag" title="see questions tagged &#39;value&#39;">value</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '13, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/7af51537fc0a1d6b8e83eb4b12fa9671?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paul32ny&#39;s gravatar image" /><p><span>paul32ny</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paul32ny has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Feb '13, 16:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-18454" class="comments-container"></div><div id="comment-tools-18454" class="comment-tools"></div><div class="clear"></div><div id="comment-18454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18457"></span>

<div id="answer-container-18457" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18457-score" class="post-score" title="current number of votes">1</div><span id="post-18457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I assume you were capturing on the client because there are very large packets listed in Wireshark. These packets don't exist on the network, as they get split up by the NIC (see <a href="http://wiki.wireshark.org/CaptureSetup/Offloading#Segmentation_Offload">TCP Segmentation Offloading</a>). The ACKs which the NIC receives are summarized into a minimal amount of ACKs towards the TCP stack. This makes it possible that an ACK can acknowledge only part of a big packet.</p><p>You can turn off TSO to make wireshark show the real packets. But better jet, use a TAP or spanport to see the real network traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '13, 16:50</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18457" class="comments-container"><span id="18458"></span><div id="comment-18458" class="comment"><div id="post-18458-score" class="comment-score"></div><div class="comment-text"><p>That is really good to know and thanks for the rapid response. The capture is from the client PC. I am assumming that going forward it is better to capture the packets on the network and not from a tcp analyzer running on the client machine. I will also try turning off TSO.</p><p>Thank you</p></div><div id="comment-18458-info" class="comment-info"><span class="comment-age">(08 Feb '13, 17:13)</span> <span class="comment-user userinfo">paul32ny</span></div></div><span id="18466"></span><div id="comment-18466" class="comment"><div id="post-18466-score" class="comment-score"></div><div class="comment-text"><p>Please note, that TSO is an optimization that is supposed to give you better performance (so you might want to leave it on), although I have seen cases where is was actually making things worse.</p></div><div id="comment-18466-info" class="comment-info"><span class="comment-age">(09 Feb '13, 03:24)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-18457" class="comment-tools"></div><div class="clear"></div><div id="comment-18457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

