+++
type = "question"
title = "display the first data packet of a HTTP request as HTTP instead of the last data packet of the request"
description = '''I just installed ubuntu 14.04 and immediately installed tshark on it (ver TShark 1.10.6 (v1.10.6 from master-1.10). The problem is, tshark doesn&#x27;t display the packet as HTTP request (packet 4). This works fine on another PC I have. Here is link to the pcap file. I know HTTP request span over multipl...'''
date = "2015-07-21T09:10:00Z"
lastmod = "2015-07-22T20:34:00Z"
weight = 44327
keywords = [ "tshark" ]
aliases = [ "/questions/44327" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [display the first data packet of a HTTP request as HTTP instead of the last data packet of the request](/questions/44327/display-the-first-data-packet-of-a-http-request-as-http-instead-of-the-last-data-packet-of-the-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44327-score" class="post-score" title="current number of votes">0</div><span id="post-44327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just installed ubuntu 14.04 and immediately installed tshark on it (ver TShark 1.10.6 (v1.10.6 from master-1.10).</p><p>The problem is, tshark doesn't display the packet as HTTP request (packet 4). This works fine on another PC I have. Here is link to the <a href="https://www.cloudshark.org/captures/e8eef18443ce">pcap file</a>. I know HTTP request span over multiple data packets, wonder if there is a way to make tshark display the first such data as the HTTP request (instead of the last such data packet)?</p><pre><code>$ tshark -nr pcaps/httpUpload.pcap | more
  1   0.000000    127.0.0.1 -&gt; 127.0.0.1    TCP 74 43098 &gt; 80 [SYN] Seq=0 Win=3
2792 Len=0 MSS=16396 SACK_PERM=1 TSval=234865924 TSecr=0 WS=128
  2   0.000042    127.0.0.1 -&gt; 127.0.0.1    TCP 74 80 &gt; 43098 [SYN, ACK] Seq=0 
Ack=1 Win=32768 Len=0 MSS=16396 SACK_PERM=1 TSval=234865924 TSecr=234865924 WS=
128
  3   0.000067    127.0.0.1 -&gt; 127.0.0.1    TCP 66 43098 &gt; 80 [ACK] Seq=1 Ack=1
 Win=32896 Len=0 TSval=234865924 TSecr=234865924
  4   0.000882    127.0.0.1 -&gt; 127.0.0.1    TCP 668 [TCP segment of a reassembl
ed PDU]
  5   0.000952    127.0.0.1 -&gt; 127.0.0.1    TCP 66 80 &gt; 43098 [ACK] Seq=1 Ack=6
03 Win=32768 Len=0 TSval=234865924 TSecr=234865924
  6   0.001189    127.0.0.1 -&gt; 127.0.0.1    TCP 16450 [TCP segment of a reassem
bled PDU]</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '15, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-44327" class="comments-container"></div><div id="comment-tools-44327" class="comment-tools"></div><div class="clear"></div><div id="comment-44327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="44330"></span>

<div id="answer-container-44330" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44330-score" class="post-score" title="current number of votes">3</div><span id="post-44330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Most likely, the other PC has the TCP preference to <em>"Allow subdissector to reassemble TCP streams"</em> turned off while your Ubuntu 14.04 PC's Wireshark has it turned on.</p><p>You can turn it off permanently in Wireshark via: <code>Edit -&gt; Preferences -&gt; Protocols -&gt; TCP -&gt; Allow subdissector to reassemble TCP streams -&gt; [deselect]</code>, or you can turn it off on the <code>tshark</code> command-line as follows:</p><pre><code>tshark -o tcp.desegment_tcp_streams:FALSE -nr pcaps/httpUpload.pcap</code></pre><p>All Wireshark (and tshark) preferences are located in your <code>preferences</code> file, which can be located from Wireshark via: <code>Help -&gt; About Wireshark -&gt; Folders -&gt; Personal configuration</code>. See also the "<strong>Files</strong>" section at the bottom of the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a> for more information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '15, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-44330" class="comments-container"><span id="44389"></span><div id="comment-44389" class="comment"><div id="post-44389-score" class="comment-score"></div><div class="comment-text"><p>Thanks Chris for the reply. I installed tshark on the server (not wireshark). Wonder if there is a way to turn off reassemble TCP streams on command line?</p></div><div id="comment-44389-info" class="comment-info"><span class="comment-age">(22 Jul '15, 14:38)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="44394"></span><div id="comment-44394" class="comment"><div id="post-44394-score" class="comment-score"></div><div class="comment-text"><p>Yes, I gave it above. Use <code>-o tcp.desegment_tcp_streams:FALSE</code>.</p></div><div id="comment-44394-info" class="comment-info"><span class="comment-age">(22 Jul '15, 15:27)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="44404"></span><div id="comment-44404" class="comment"><div id="post-44404-score" class="comment-score"></div><div class="comment-text"><p>Thanks Chris again. It works. Sorry didn't notice the tshark command you put there.</p></div><div id="comment-44404-info" class="comment-info"><span class="comment-age">(22 Jul '15, 20:33)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-44330" class="comment-tools"></div><div class="clear"></div><div id="comment-44330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44360"></span>

<div id="answer-container-44360" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44360-score" class="post-score" title="current number of votes">0</div><span id="post-44360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Chris Maynard says, the only way to do this currently is to turn off TCP reassembly.</p><p>It might be possible to enhance Wireshark and TShark to have an option to show the reassembly on the first packet, although such an option will only work in TShark, as opposed to Wireshark, if you use the <code>-2</code> option - it would be <em>impossible</em> to make it work without that option, as you <em>have</em> to see all the packets in order to do the reassembly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '15, 16:44</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-44360" class="comments-container"><span id="44390"></span><div id="comment-44390" class="comment"><div id="post-44390-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guy. I like your suggestion. I would be happy if I know what configure file to edit manually since I don't have a wireshark installation right now (target host is a server).</p></div><div id="comment-44390-info" class="comment-info"><span class="comment-age">(22 Jul '15, 14:39)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="44393"></span><div id="comment-44393" class="comment"><div id="post-44393-score" class="comment-score"></div><div class="comment-text"><p>If, as, and when we ever implement that enhancement, we'll document the name of the preference that would control that.</p><p>If you just mean "the option to turn off TCP reassembly", it's "tcp.desegment_tcp_streams", and you turn it off with the Wireshark/TShark command-line option <code>-o tcp.desegment_tcp_streams:false</code>.</p></div><div id="comment-44393-info" class="comment-info"><span class="comment-age">(22 Jul '15, 15:05)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="44405"></span><div id="comment-44405" class="comment"><div id="post-44405-score" class="comment-score"></div><div class="comment-text"><p>Thanks again. I didn't notice the tshark command Chris put there. Now it's working well for me.</p></div><div id="comment-44405-info" class="comment-info"><span class="comment-age">(22 Jul '15, 20:34)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-44360" class="comment-tools"></div><div class="clear"></div><div id="comment-44360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

