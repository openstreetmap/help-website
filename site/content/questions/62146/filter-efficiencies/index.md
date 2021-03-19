+++
type = "question"
title = "filter efficiencies"
description = '''I was just wondering about how filters process and can I do things more efficiently with one filter vs another. Example: 1) tcp.flags.syn == 1 &amp;amp;&amp;amp; tcp.flags.rst == 1 2) tcp[13] == 12 Does one work better/same/worse than two? '''
date = "2017-06-19T18:43:00Z"
lastmod = "2017-06-22T11:19:00Z"
weight = 62146
keywords = [ "efficiencies" ]
aliases = [ "/questions/62146" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [filter efficiencies](/questions/62146/filter-efficiencies)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62146-score" class="post-score" title="current number of votes">0</div><span id="post-62146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was just wondering about how filters process and can I do things more efficiently with one filter vs another. Example:</p><p>1) tcp.flags.syn == 1 &amp;&amp; tcp.flags.rst == 1</p><p>2) tcp[13] == 12</p><p>Does one work better/same/worse than two?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-efficiencies" rel="tag" title="see questions tagged &#39;efficiencies&#39;">efficiencies</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '17, 18:43</strong></p><img src="https://secure.gravatar.com/avatar/be6efabca81a0dc1cc87c4722258ba03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Antacus&#39;s gravatar image" /><p><span>Antacus</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Antacus has no accepted answers">0%</span></p></div></div><div id="comments-container-62146" class="comments-container"></div><div id="comment-tools-62146" class="comment-tools"></div><div class="clear"></div><div id="comment-62146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62159"></span>

<div id="answer-container-62159" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62159-score" class="post-score" title="current number of votes">0</div><span id="post-62159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It depends:</p><ul><li><code>tcp.flags.rst == 1</code> is not valid. I guess you mean <code>tcp.flags.reset == 1</code>?</li><li>Your first filter will show packets where at least SYN AND RST are set. But other flags (e.g. Push, Fin) may also be set to 1</li><li>The second filter will only show packets where the value on TCP offset 13 is 12 (Only SYN AND ACK are set, all other flags are 0)</li></ul><p>Therefore it's hard to say if one of the filter is better/worse than the other. It depends for what your're looking for. But one thing is clear: Both filters are not the same.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '17, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-62159" class="comments-container"><span id="62165"></span><div id="comment-62165" class="comment"><div id="post-62165-score" class="comment-score"></div><div class="comment-text"><p>Guess I should not have written an off the hip question. My original was more of a concept question on how does the code of wireshark process filters. You got me on details, which I am usually a stickler on :) So let me rewrite my original question :)</p><p>A) (conditional test #1) &amp;&amp; (conditional test #2)</p><p>B) (conditional test #3) * where B) provides the same answer as A)</p><p>Not being a hard core coder it seems to me that logically test B) would be twice as fast as A) so where you can take the time to optimize filters. Think of a script which you have setup to pre-parse capture files and generate a report before you even open the capture file for the first time. Filters run inside repeating scripts which can be optimized to run faster should, imho.</p><p>I assume this question has been asked before but I am unable to locate an answer. There is a Performance page on the Wiki but it does not address this question.</p></div><div id="comment-62165-info" class="comment-info"><span class="comment-age">(20 Jun '17, 05:25)</span> <span class="comment-user userinfo">Antacus</span></div></div><span id="62186"></span><div id="comment-62186" class="comment"><div id="post-62186-score" class="comment-score">1</div><div class="comment-text"><p>I realize this question was geared more for Wireshark display filters, but for <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">capture filters</a>, you <strong>can</strong> directly compare them by having <a href="http://www.tcpdump.org/tcpdump_man.html"><code>tcpdump</code></a> or <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html"><code>dumpcap</code></a> generate the bpf code if you specify the <code>-d</code> option. For example, if you run these two commands, you can see that they produce the exact same resulting bpf code:</p><pre><code>dumpcap -i 2 -f &quot;tcp[13]==6&quot; -d
dumpcap -i 2 -f &quot;tcp[tcpflags]==tcp-syn|tcp-rst&quot; -d</code></pre><p>Here's the output in either case:</p><pre><code>(000) ldh      [12]
(001) jeq      #0x800           jt 2    jf 10
(002) ldb      [23]
(003) jeq      #0x6             jt 4    jf 10
(004) ldh      [20]
(005) jset     #0x1fff          jt 10   jf 6
(006) ldxb     4*([14]&amp;0xf)
(007) ldb      [x + 27]
(008) jeq      #0x6             jt 9    jf 10
(009) ret      #262144
(010) ret      #0</code></pre><p>If you generate the bfp code, it can help you determine if one capture filter is more efficient than another or if they differ in any way.</p></div><div id="comment-62186-info" class="comment-info"><span class="comment-age">(20 Jun '17, 12:05)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="62200"></span><div id="comment-62200" class="comment"><div id="post-62200-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Here's the output in either case</p></blockquote><p>Not surprising, given that, in effect, "tcpflags" is a macro for "13" , "tcp-syn" is a macro for "0x02", "tcp-rst" is a macro for "0x04", and libpcap's BPF compiler's optimizer evaluates some expressions at compile time.</p><p>For <em>display</em> filters, there's a program <code>dftest</code>, which is part of the Wireshark source, and may be installed if Wireshark is; if, for example, you run <code>dftest 'tcp.flags.syn == 1 &amp;&amp; tcp.flags.reset == 1'</code>, it prints</p><p>Filter: "tcp.flags.syn == 1 &amp;&amp; tcp.flags.reset == 1"</p><pre><code>Constants:
00000 PUT_FVALUE        1 &lt;FT_BOOLEAN&gt; -&gt; reg#2
00001 PUT_FVALUE        1 &lt;FT_BOOLEAN&gt; -&gt; reg#3

Instructions:
00000 READ_TREE         tcp.flags.syn -&gt; reg#0
00001 IF-FALSE-GOTO     7
00002 ANY_EQ            reg#0 == reg#2
00003 IF-FALSE-GOTO     7
00004 READ_TREE         tcp.flags.reset -&gt; reg#1
00005 IF-FALSE-GOTO     7
00006 ANY_EQ            reg#1 == reg#3
00007 RETURN</code></pre><p>which is the code that's interpreted at run time by the display filter code. So you could use <code>dftest</code> on the two filter expressions to see what test instructions are generated.</p><p>Whether <code>(conditional test #3)</code> generates fewer instructions than <code>(conditional test #1) &amp;&amp; (conditional test #2)</code> and, if so, how <em>many</em> fewer instructions are generated, depends on what the three conditional tests are.</p></div><div id="comment-62200-info" class="comment-info"><span class="comment-age">(21 Jun '17, 00:50)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="62217"></span><div id="comment-62217" class="comment"><div id="post-62217-score" class="comment-score"></div><div class="comment-text"><p><em>Not surprising, given that, in effect, "tcpflags" is a macro for "13" , "tcp-syn" is a macro for "0x02", "tcp-rst" is a macro for "0x04",</em></p><p>Right, I was just illustrating the fact that tcp-syn|tcp-rst is equivalent to 6, and not 12, as Antacus originally wrote in the question. If the names are used instead of the number, then you can be assured of the correct value being used, so it's generally better to use the names.</p><p>And thanks for mentioning <code>dftest</code>. I sometimes forget about it because for some unknown reason, it has never been packaged with the Wireshark Windows installer, and Windows is the platform I generally use.</p><p>And to compare Guy's <code>dftest</code> output for the <code>"tcp.flags.syn == 1 &amp;&amp; tcp.flags.reset == 1"</code> filter, here's the <code>dftest</code> output for <code>tcp.flags == 6</code>:</p><p><code> Filter: "tcp.flags == 6"</code></p><p><code></code></p><pre><code>Constants:
00000 PUT_FVALUE        6 &lt;FT_UINT16&gt; -&gt; reg#1
Instructions:
00000 READ_TREE         tcp.flags -&gt; reg#0
00001 IF-FALSE-GOTO     3
00002 ANY_EQ            reg#0 == reg#1
00003 RETURN</code></pre><code></code><p><code></code></p><p>So clearly this filter is [slightly] more efficient.</p><p>I think Guy's <code>dftest</code> portion of his comment should be the answer to this question.</p></div><div id="comment-62217-info" class="comment-info"><span class="comment-age">(21 Jun '17, 11:16)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-62159" class="comment-tools"></div><div class="clear"></div><div id="comment-62159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62245"></span>

<div id="answer-container-62245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62245-score" class="post-score" title="current number of votes">0</div><span id="post-62245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Others have already pointed out <em>dftest</em> and dumping BPF code for comparisons, but I'll give an answer from a different perspective...</p><p>In my experience, I haven't seen much difference in efficiency...but I work in customer support, so I usually go with the <strong>most easily understood</strong> filter.</p><p>Obviously, <strong>tcp.flags.syn==1 &amp;&amp; tcp.flags.ack ==1</strong> requires much less explanation on my part than would any filter like <strong>tcp[offset]==value</strong>.</p><p>So, if I'm writing (say) a tshark script that I won't have to explain to others, I might use the offset test...but if I'm doing <strong>anything</strong> for public consumption, I go with what folks are more likely to understand at first glance.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '17, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-62245" class="comments-container"></div><div id="comment-tools-62245" class="comment-tools"></div><div class="clear"></div><div id="comment-62245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

