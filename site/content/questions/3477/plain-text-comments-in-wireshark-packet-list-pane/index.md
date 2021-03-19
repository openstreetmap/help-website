+++
type = "question"
title = "plain text comments in Wireshark packet list pane"
description = '''I am relatively new to Wireshark. I am generating packets from our test platform. These are being correctly decoded by Wireshark. They happen to be &quot;mac-lte&quot; packets, but isn&#x27;t relevant for question I have... I would like to interleave the generated packets with comments/logs packets, with the Wires...'''
date = "2011-04-13T04:58:00Z"
lastmod = "2011-04-14T03:47:00Z"
weight = 3477
keywords = [ "comment", "protocol", "plain-text" ]
aliases = [ "/questions/3477" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [plain text comments in Wireshark packet list pane](/questions/3477/plain-text-comments-in-wireshark-packet-list-pane)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3477-score" class="post-score" title="current number of votes">0</div><span id="post-3477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am relatively new to Wireshark.</p><p>I am generating packets from our test platform. These are being correctly decoded by Wireshark. They happen to be "mac-lte" packets, but isn't relevant for question I have...</p><p>I would like to interleave the generated packets with comments/logs packets, with the Wireshark decoded comments being displayed in the packet list pane (the top pane in the Wireshark GUI, showing a summary of the packets decoded). Note, I don't want to have to dig into the packet to see the text. I would like the text displayed on the packet list pane.</p><p>I'd like to use the standard Wireshark product off the shelf, without having to add a non-standard dissector. Is there a 'protocol' dissector packaged with the standard Wireshark product to display plain text? Failing that, does anyone have a plain text dissector they can share?</p><p>Thanks in advance, Robert</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-comment" rel="tag" title="see questions tagged &#39;comment&#39;">comment</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-plain-text" rel="tag" title="see questions tagged &#39;plain-text&#39;">plain-text</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '11, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/628d14e973bb734dd865b38ce54aea76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobertA&#39;s gravatar image" /><p><span>RobertA</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobertA has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Apr '11, 05:00</strong> </span></p></div></div><div id="comments-container-3477" class="comments-container"></div><div id="comment-tools-3477" class="comment-tools"></div><div class="clear"></div><div id="comment-3477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3484"></span>

<div id="answer-container-3484" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3484-score" class="post-score" title="current number of votes">2</div><span id="post-3484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think the syslog dissector might be the closest thing to what you need and the easiest to use in your case.</p><p>You can use "nc" (netcat) to send the cleartext messages like this:</p><pre><code>$ echo &quot;&lt;181&gt;Hallo?&quot; | nc -w 1 -u 1.1.1.1 514
$</code></pre><p>Host 1.1.1.1 does not need to exist, as long as the route towards that host passes your capturing device :-)</p><p>Wireshark and tshark will now show you:</p><pre><code>  2.102943 192.168.1.22 -&gt; 194.1.2.3 TCP 51791 &gt; 443 [ACK] Seq=97 Ack=97 Win=65535 Len=0 TSval=999679650 TSecr=2322251460
  2.450229 192.168.1.22 -&gt; 1.1.1.1      Syslog LOCAL6.NOTICE: Hallo?\n
  3.103243 192.168.1.22 -&gt; 194.1.2.3 SSL Continuation Data</code></pre><p>The "&lt;xxx&gt;" at the beginning of the message signify the facility and the severity where xxx is an 8 bit value in decimal representation. The most significant 5 bits denote the facility (LOCAL6 in my case) and the least significant 3 bits denote the severity (EMERG..DEBUG).</p><p>(of course you can also use the logger command on a unix-like system, but then you have to make sure you have a rule in the configuration of the local syslog daemon that forwards the message to a remote host like 1.1.1.1)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '11, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3484" class="comments-container"><span id="3485"></span><div id="comment-3485" class="comment"><div id="post-3485-score" class="comment-score"></div><div class="comment-text"><p>Oh, I just tried without the facility/severity string and that works even better for your purpose:</p><p>echo "The following packets are interesting :-)" | nc -w 1 -u 1.1.1.1 514</p><p>results in:</p><p>26.143408 192.168.1.22 -&gt; 1.1.1.1 Syslog The following packets are interesting :-)\n</p></div><div id="comment-3485-info" class="comment-info"><span class="comment-age">(13 Apr '11, 08:32)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="3494"></span><div id="comment-3494" class="comment"><div id="post-3494-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Appears to use port to identify it is a syslog message.</p><p>If wanted to specify different port, could set up a filter via Wireshark-&gt;Analyse-&gt;DecodeAs-&gt;Transport, so could map another port to syslog protocol.</p><p>However want to send/receive "mac-lte" &amp; comment/log on same address&amp;port. To try to ensure network delays dont affect pkt order wrt the comment and mac-lte packets.</p><p>So think what want is to add a header in TCP/UDP payload to identify the packet as comment/trace text. i.e. a similar mechanim to how Wireshark uses a header to decode mac-lte packets.</p><p>Is there anything suitable?</p></div><div id="comment-3494-info" class="comment-info"><span class="comment-age">(14 Apr '11, 03:47)</span> <span class="comment-user userinfo">RobertA</span></div></div></div><div id="comment-tools-3484" class="comment-tools"></div><div class="clear"></div><div id="comment-3484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

