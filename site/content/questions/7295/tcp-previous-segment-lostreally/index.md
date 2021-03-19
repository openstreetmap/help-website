+++
type = "question"
title = "TCP previous segment lost...really?"
description = '''I have users that RDP to servers from remote offices through a VPN. I do not get complaints from users running terminal server but when running a capure I&#x27;m seeing a lot of (TCP previous segment lost) but not retransmitions or duplicate acknowledgements. Below is a small sample export:  No. Time Del...'''
date = "2011-11-08T14:15:00Z"
lastmod = "2015-02-09T05:44:00Z"
weight = 7295
keywords = [ "segment", "lost" ]
aliases = [ "/questions/7295" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP previous segment lost...really?](/questions/7295/tcp-previous-segment-lostreally)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7295-score" class="post-score" title="current number of votes">0</div><span id="post-7295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have users that RDP to servers from remote offices through a VPN. I do not get complaints from users running terminal server but when running a capure I'm seeing a lot of (TCP previous segment lost) but not retransmitions or duplicate acknowledgements. Below is a small sample export:</p><pre><code>  No.   Time        Delta       Source                Destination           Protocol Info                                                            TCP Win Size
  16594 35.668978   0.001375    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=133501 Win=65216 Len=0 65216
  21380 44.940581   0.003265    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  21532 45.198616   0.001418    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=134037 Win=64680 Len=0 64680
  25676 51.846655   0.000021    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  25740 52.120098   0.008579    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=134056 Win=64661 Len=0 64661
  33920 68.269875   0.018953    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  34014 68.470952   0.003303    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=134074 Win=64643 Len=0 64643
  39489 81.083668   0.004569    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  39591 81.310868   0.000169    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=134097 Win=64620 Len=0 64620
  40992 84.661456   0.002586    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  41086 84.922094   0.000270    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=134120 Win=64597 Len=0 64597
  46969 101.070159  0.004696    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  47039 101.272924  0.000401    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=134138 Win=64579 Len=0 64579
  53231 117.476833  0.005800    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  53321 117.724009  0.000914    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=134156 Win=64561 Len=0 64561
  59055 130.494564  0.005086    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  59093 130.552710  0.000426    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  59094 130.552827  0.000117    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  59095 130.552928  0.000101    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  59096 130.553154  0.000226    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  59128 130.628580  0.000313    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=136036 Win=65535 Len=0 65535
  59133 130.636297  0.000025    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=137393 Win=64178 Len=0 64178
  59142 130.650200  0.003315    10.11.0.34            10.11.4.151           TPKT     [TCP Previous segment lost] Continuation                        32760
  59143 130.650336  0.000136    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  59184 130.731314  0.001042    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=139458 Win=65535 Len=0 65535
  59186 130.733554  0.001918    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=139799 Win=65194 Len=0 65194
  59211 130.759843  0.002716    10.11.0.34            10.11.4.151           TPKT     [TCP Previous segment lost] Continuation                        32760
  59249 130.847533  0.004212    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=142084 Win=65535 Len=0 65535
  59269 130.869924  0.000606    10.11.0.34            10.11.4.151           TPKT     [TCP Previous segment lost] Continuation                        32760
  59315 130.956755  0.007208    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=144586 Win=65535 Len=0 65535
  59333 130.978730  0.001011    10.11.0.34            10.11.4.151           TPKT     [TCP Previous segment lost] Continuation                        32760
  59334 130.978762  0.000032    10.11.0.34            10.11.4.151           TPKT     Continuation                                                    32760
  59369 131.066828  0.000189    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=147019 Win=65535 Len=0 65535
  59383 131.089565  0.004658    10.11.0.34            10.11.4.151           TPKT     [TCP Previous segment lost] Continuation                        32760
  59413 131.170660  0.002069    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=148819 Win=65535 Len=0 65535
  59421 131.180857  0.002506    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=150383 Win=65535 Len=0 65535
  59434 131.200199  0.003550    10.11.0.34            10.11.4.151           TPKT     [TCP Previous segment lost] Continuation                        32760
  59469 131.291004  0.000367    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=153303 Win=65535 Len=0 65535
  59479 131.307596  0.002806    10.11.0.34            10.11.4.151           TPKT     [TCP Previous segment lost] Continuation                        32760
  59480 131.308106  0.000510    10.11.0.34            10.11.4.151           TPKT     [TCP Previous segment lost] Continuation                        32760
  59512 131.388760  0.001165    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=155567 Win=65535 Len=0 65535
  59519 131.401704  0.001452    10.11.4.151           10.11.0.34            TCP      hpvmmdata &gt; ms-wbt-server [ACK] Seq=7482 Ack=157916 Win=65535 Len=0 65535
  59530 131.416372  0.000762    10.11.0.34            10.11.4.151           TPKT     [TCP Previous segment lost] Continuation                        32760
  59531 131.416871  0.000499    10.11.0.34            10.11.4.151           TPKT     [TCP Previous segment lost] Continuation                        32760</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-segment" rel="tag" title="see questions tagged &#39;segment&#39;">segment</span> <span class="post-tag tag-link-lost" rel="tag" title="see questions tagged &#39;lost&#39;">lost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '11, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/a23a6d5fb104c527e199def8f954a0ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newb33&#39;s gravatar image" /><p><span>newb33</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newb33 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Nov '11, 14:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-7295" class="comments-container"><span id="7334"></span><div id="comment-7334" class="comment"><div id="post-7334-score" class="comment-score"></div><div class="comment-text"><p>How can wireshark specify "TCP Previous segment lost" but have no TCP Retransmission or TCP Fast Retransmission? Is that possible?</p></div><div id="comment-7334-info" class="comment-info"><span class="comment-age">(09 Nov '11, 13:25)</span> <span class="comment-user userinfo">newb33</span></div></div><span id="39713"></span><div id="comment-39713" class="comment"><div id="post-39713-score" class="comment-score"></div><div class="comment-text"><p>Hello newb33,</p><p>Any update regarding this issue? I am also experiencing a similar issue. I got "TCP Previous Segment Not Captured" but no TCP retransmissions. Afterwards, the client send [FIN, ACK] packet to the server due to no response from server.</p><p>Thank you.</p></div><div id="comment-39713-info" class="comment-info"><span class="comment-age">(09 Feb '15, 05:44)</span> <span class="comment-user userinfo">chwijaya</span></div></div></div><div id="comment-tools-7295" class="comment-tools"></div><div class="clear"></div><div id="comment-7295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7335"></span>

<div id="answer-container-7335" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7335-score" class="post-score" title="current number of votes">0</div><span id="post-7335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The first packet number is 16,594; the last packet number is 59,531. From 16,594 to 59,531 is 42,938 packets. Your sample shows only 44 packets, so obviously a display filter was in place. What filter was used? Is it possible that you accidentally filtered out the retransmissions and duplicate ACKs?</p><p>This would be easier to troubleshoot if you would post the actual capture file somewhere so that we could download it and open it in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '11, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-7335" class="comments-container"><span id="7336"></span><div id="comment-7336" class="comment"><div id="post-7336-score" class="comment-score"></div><div class="comment-text"><p>I filtered the exact communication between the 2 systems. My filter was ip.addr==10.11.4.151</p><p>I did not want to post the entire dump. Just a sample that had good traffic and then the supposed lost segments...</p></div><div id="comment-7336-info" class="comment-info"><span class="comment-age">(09 Nov '11, 13:52)</span> <span class="comment-user userinfo">newb33</span></div></div><span id="7337"></span><div id="comment-7337" class="comment"><div id="post-7337-score" class="comment-score"></div><div class="comment-text"><p>When I run the Expert Info Composite for the entire capture of 10 minutes I have <strong>2323</strong> Previous Segment lost and <strong>1</strong> ACKed Lost segment</p></div><div id="comment-7337-info" class="comment-info"><span class="comment-age">(09 Nov '11, 13:55)</span> <span class="comment-user userinfo">newb33</span></div></div></div><div id="comment-tools-7335" class="comment-tools"></div><div class="clear"></div><div id="comment-7335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

