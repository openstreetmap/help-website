+++
type = "question"
title = "Duplicate Ack Count Up to 300 without retry"
description = '''I am troubleshooting periodic slowness in a streaming application running over the Internet. A trace from the client shows duplicate ack storms occasionally, which is not unusual in itself. WHat is odd is that wireshark is reporting up to 300 dup ack&#x27;s for the same sequence before a Fast Retransmit ...'''
date = "2014-09-04T11:16:00Z"
lastmod = "2014-09-05T07:51:00Z"
weight = 36009
keywords = [ "dupack" ]
aliases = [ "/questions/36009" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate Ack Count Up to 300 without retry](/questions/36009/duplicate-ack-count-up-to-300-without-retry)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36009-score" class="post-score" title="current number of votes">0</div><span id="post-36009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am troubleshooting periodic slowness in a streaming application running over the Internet. A trace from the client shows duplicate ack storms occasionally, which is not unusual in itself. WHat is odd is that wireshark is reporting up to 300 dup ack's for the same sequence before a Fast Retransmit comes through from the server. I've tested this using the same client against two different servers of the same type with the same application located on different host sites and I'm getting dup ack retries of between 15 and 300. It is my understanding that most stacks have the default maxdupack value somewhere between 1 and 3</p><p>I can't post the trace due to confidentiality, but here is the export using tcp.analysis.duplicate_ack filter from one server</p><pre><code>5634    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#280] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5422170 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5635    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#281] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5423630 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5636    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#282] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5425090 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5637    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#283] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5426550 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5638    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#284] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5428010 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5639    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#285] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5429470 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5640    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#286] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5430930 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5641    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#287] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5432390 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5642    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#288] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5433850 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5650    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#289] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5435310 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5651    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#290] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5436770 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5652    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#291] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5438230 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5653    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#292] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5439690 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5654    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#293] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5441150 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5655    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#294] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5442610 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5656    53:36.8 Client  Server  TCP 90  [TCP Dup ACK 5063#295] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5444070 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5661    53:36.9 Server  Client  TCP 66  [TCP Dup ACK 5660#1] 6100 &gt; 53048 [ACK] Seq=5449910 Ack=48939 Win=191 Len=0 SLE=48967 SRE=48981
5664    53:36.9 Server  Client  TCP 60  [TCP Dup ACK 5663#1] 6100 &gt; 53048 [ACK] Seq=5451358 Ack=48981 Win=191 Len=0
5665    53:36.9 Client  Server  TCP 90  [TCP Dup ACK 5063#296] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5445530 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5666    53:36.9 Client  Server  TCP 90  [TCP Dup ACK 5063#297] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5446990 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5667    53:36.9 Client  Server  TCP 90  [TCP Dup ACK 5063#298] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5448450 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5668    53:36.9 Client  Server  TCP 90  [TCP Dup ACK 5063#299] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5449910 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858
5669    53:36.9 Client  Server  TCP 90  [TCP Dup ACK 5063#300] 53048 &gt; 6100 [ACK] Seq=48981 Ack=5004558 Win=10738 Len=0 SLE=5035270 SRE=5451358 SLE=5032350 SRE=5033810 SLE=5013318 SRE=5030890 SLE=5008938 SRE=5011858</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dupack" rel="tag" title="see questions tagged &#39;dupack&#39;">dupack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '14, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/5bf90665156f2bd31e0e65cb77939f5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DICOM_Tracer&#39;s gravatar image" /><p><span>DICOM_Tracer</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DICOM_Tracer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Sep '14, 11:17</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-36009" class="comments-container"></div><div id="comment-tools-36009" class="comment-tools"></div><div class="clear"></div><div id="comment-36009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36010"></span>

<div id="answer-container-36010" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36010-score" class="post-score" title="current number of votes">0</div><span id="post-36010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Diagnosing things with huge ASCII dumps is really painful, so I doubt many of us will spent any amount of time on trying to figure things out with it. A trace would be much more useful, and if you're concerned about confidentiality you can use <a href="http://www.tracewrangler.com">TraceWrangler</a> to sanitize your trace. In your case you can strip all TCP payload since this is strictly a TCP layer problem (well, it shows on TCP, but you have most likely a buffer problem).</p><p>Let me guess - the trace is a conversation where the sender has a bandwith larger than the target, maybe by factor 10 (e.g. a file server on a 1G link, with a client on 100MBit, or 10G to 1G)? Your trace shows the typical result of a huge amount of packets filling up a buffer somewhere (e.g. on a router or a switch port) and packet loss occurs. The receiver sends duplicate ACKs and the sender triggers a fast retransmission, but unfortunately that retransmission has to get in line at the end of the (still completely filled) buffer - which is why it takes so long to get through, and which is also why you see so many dup acks. By the way, this is not a lot of dup acks - I had a trace where there were over 1000 of them for a 10G -&gt; 1G -&gt; 100 Mbit connection, with double buffering.</p><p>Just guessing, because there isn't much more I can do with a partial ASCII dump ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '14, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Sep '14, 11:26</strong> </span></p></div></div><div id="comments-container-36010" class="comments-container"><span id="36024"></span><div id="comment-36024" class="comment"><div id="post-36024-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the response. I understand the limited value of the ascii dump. You're reply was appreciated. We had come to a similar understanding but it is helpful to someone else's experience.</p></div><div id="comment-36024-info" class="comment-info"><span class="comment-age">(05 Sep '14, 07:51)</span> <span class="comment-user userinfo">DICOM_Tracer</span></div></div></div><div id="comment-tools-36010" class="comment-tools"></div><div class="clear"></div><div id="comment-36010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

