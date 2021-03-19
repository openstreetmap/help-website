+++
type = "question"
title = "EOF while receiving data from socket."
description = '''I found that in a TCP connection the java captured EOF exception(0 returned while reading or receiving) while receiving data from remote server and closed the connection, but from the tcpdump, the local side had been receiving data, I don&#x27;t understand why the application would receive a EOF error. T...'''
date = "2011-11-24T00:09:00Z"
lastmod = "2011-11-25T03:13:00Z"
weight = 7596
keywords = [ "socket" ]
aliases = [ "/questions/7596" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [EOF while receiving data from socket.](/questions/7596/eof-while-receiving-data-from-socket)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7596-score" class="post-score" title="current number of votes">0</div><span id="post-7596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I found that in a TCP connection the java captured EOF exception(0 returned while reading or receiving) while receiving data from remote server and closed the connection, but from the tcpdump, the local side had been receiving data, I don't understand why the application would receive a EOF error.</p><p>This often happens when the peer was receiving data at extremely slow rate, but this doesn't look like the case.</p><p>I appreciate any comments on it, Thanks.</p><pre><code>  14724 16:03:19.427810 122.11.56.106         10.198.242.132        TCP      [TCP segment of a reassembled PDU]
  14726 16:03:19.430709 122.11.56.106         10.198.242.132        TCP      [TCP segment of a reassembled PDU]
  14728 16:03:19.434005 122.11.56.106         10.198.242.132        TCP      [TCP segment of a reassembled PDU]
  14731 16:03:19.437118 122.11.56.106         10.198.242.132        TCP      [TCP segment of a reassembled PDU]
  14733 16:03:19.439956 122.11.56.106         10.198.242.132        TCP      [TCP segment of a reassembled PDU]
   Transmission Control Protocol, Src Port: 80 (80), Dst Port: 44380 (44380), Seq: 4415905, Ack: 305, Len: 1368
  14734 16:03:19.504241 10.198.242.132        122.11.56.106         TCP      44380 &gt; 80 [ACK] Seq=305 Ack=4417274 Win=279976 Len=0 TSV=24975 TSER=1978478379
  14737 16:03:19.580306 10.198.242.132        122.11.56.106         TCP      44380 &gt; 80 [FIN, ACK] Seq=305 Ack=4417274 Win=290016 Len=0 TSV=24982 TSER=1978478379
  14740 16:03:19.723586 122.11.56.106         10.198.242.132        TCP      80 &gt; 44380 [ACK] Seq=4417274 Ack=306 Win=6912 Len=0 TSV=1978478437 TSER=24982</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-socket" rel="tag" title="see questions tagged &#39;socket&#39;">socket</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '11, 00:09</strong></p><img src="https://secure.gravatar.com/avatar/6535877de270eac71c394ebbe2c5dae5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Crs&#39;s gravatar image" /><p><span>Crs</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Crs has no accepted answers">0%</span></p></div></div><div id="comments-container-7596" class="comments-container"><span id="7605"></span><div id="comment-7605" class="comment"><div id="post-7605-score" class="comment-score"></div><div class="comment-text"><p>Which host was running the program that received the EOF error? 122.11.56.106 or 10.198.242.132?</p></div><div id="comment-7605-info" class="comment-info"><span class="comment-age">(24 Nov '11, 01:27)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="7627"></span><div id="comment-7627" class="comment"><div id="post-7627-score" class="comment-score"></div><div class="comment-text"><p>Hi Harris,</p><p>10.198.242.132 was receiving data, EOS returned and then it closed the connection.</p><p>14737 16:03:19.580306 10.198.242.132 122.11.56.106 TCP 44380 &gt; 80 [FIN, ACK] Seq=305 Ack=4417274 Win=290016 Len=0 TSV=24982 TSER=1978478379</p></div><div id="comment-7627-info" class="comment-info"><span class="comment-age">(25 Nov '11, 03:13)</span> <span class="comment-user userinfo">Crs</span></div></div></div><div id="comment-tools-7596" class="comment-tools"></div><div class="clear"></div><div id="comment-7596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

