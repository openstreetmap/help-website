+++
type = "question"
title = "how to classify tcp.flags,udp and icmp?"
description = '''Hi,i am newbie to wireshark.I want export my pcap to csv. I need to export data in this format Date || Time || Src_IP || Dest_IP || Src_Port || Dest_Prt || Protocol || Classification(tcp flags,udp,icmp) I m using CLI to do this. tshark -r test.pcap -T fields -e frame.time -e eth.src -e eth.dst -e ip...'''
date = "2015-02-25T21:02:00Z"
lastmod = "2015-02-26T02:13:00Z"
weight = 40079
keywords = [ "timestamp", "tcpflags" ]
aliases = [ "/questions/40079" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to classify tcp.flags,udp and icmp?](/questions/40079/how-to-classify-tcpflagsudp-and-icmp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40079-score" class="post-score" title="current number of votes">0</div><span id="post-40079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,i am newbie to wireshark.I want export my pcap to csv. I need to export data in this format <strong>Date || Time || Src_IP || Dest_IP || Src_Port || Dest_Prt || Protocol || Classification(tcp flags,udp,icmp)</strong></p><p>I m using CLI to do this.</p><pre><code>tshark -r test.pcap -T fields -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e tcp.srcport -e udp.srcport -e tcp.dstport -e udp.dstport -e ip.proto -e tcp.flags -E header=y -E separator=, -E quote=d -E occurrence=f &gt; test.csv</code></pre><p>Questions:</p><ol><li>How to separate date and time ?</li><li>How to add logical or operation in <strong>-e tcp.srcport -e udp.srcport</strong> ? (I have tried many times but failed each time)</li><li>How to classify <strong>tcp flags,icmp,udp</strong>?</li></ol><p>I m using <strong>Tcp.flags</strong> and it results in decimal number and i dont know the value of tcp flags.</p><p>Example:tcp.flag=18</p><p>Need Help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-tcpflags" rel="tag" title="see questions tagged &#39;tcpflags&#39;">tcpflags</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '15, 21:02</strong></p><img src="https://secure.gravatar.com/avatar/0b74140125761d788022e30676af3b13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Viru&#39;s gravatar image" /><p><span>Viru</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Viru has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Feb '15, 01:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-40079" class="comments-container"></div><div id="comment-tools-40079" class="comment-tools"></div><div class="clear"></div><div id="comment-40079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40085"></span>

<div id="answer-container-40085" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40085-score" class="post-score" title="current number of votes">1</div><span id="post-40085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Answers:</p><ol><li>You can't, as there is no extra field for date and/or time. So, you'll have to split it yourself after the export with a script</li><li>There is no 'or' operator for commandline options. So, you either let tshark print both values and then ignore the empty one or you run tshark twice, once for UDP and once for TCP (-Y "udp" or -Y "tcp"), with the corresponing port options.</li><li>The encoding of the tcp.flags is the same as in the TCP header. 00=no flags, 01=FIN set, 02=SYN set, 04=RESET set, etc. It's binary arithemtic. Please see the TCP RFC or any other resource on the internet about the TCP header and the definition of the flags. Your example (tcp.flags = 18) is in binary noation: 10010, which means: SYN set (02), ACK set (0F = 16). 02 + 16 = 18.</li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '15, 02:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40085" class="comments-container"></div><div id="comment-tools-40085" class="comment-tools"></div><div class="clear"></div><div id="comment-40085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40087"></span>

<div id="answer-container-40087" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40087-score" class="post-score" title="current number of votes">1</div><span id="post-40087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Answers:</p><blockquote><p>1.How to separate date and time ?</p></blockquote><p>You'll have to pipe the output of tshark through a tool, such as a sed, AWK, or Perl script, that modifies the output to do that. The "time stamp" is actually a date/time stamp, so "frame.time" includes both date and time (the internal representation in Wireshark is "seconds and fractions of a second since January 1, 1970, 00:00:00 UTC", which does not separate date and time).</p><blockquote><p>2.How to add logical or operation in -e tcp.srcport -e udp.srcport ? (I have tried many times but failed each time)</p></blockquote><p>Presumably you mean "how do I show tcp.srcport and udp.srcport in the same field in the CSV output?" If that's what you mean, there is no mechanism that allows you to do that, so, again, you'd have to pipe the output through something that modifies the output of tshark.</p><blockquote><p>3.How to classify tcp flags,icmp,udp? I m using Tcp.flags and it results in decimal number and i dont know the value of tcp flags.</p></blockquote><p>For TCP flags, convert the value to hex, and then see <a href="http://tools.ietf.org/html/rfc793#section-3.1">RFC 793 section 3.1 "Header Format"</a> for the interpretation of that value.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '15, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-40087" class="comments-container"></div><div id="comment-tools-40087" class="comment-tools"></div><div class="clear"></div><div id="comment-40087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

