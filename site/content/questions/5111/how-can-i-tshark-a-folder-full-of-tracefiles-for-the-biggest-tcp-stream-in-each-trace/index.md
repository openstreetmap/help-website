+++
type = "question"
title = "How can i tshark a folder full of tracefiles for the biggest tcp stream in each trace?"
description = '''I&#x27;m tracing issues with Window Scaling from client to server, after a batch testfile (with copy commands for file transfers) i want to analyse all tracefiles for throughput, window sizes, application read requests and so on, but..... from every trace i only need the biggest tcp stream. Most of the t...'''
date = "2011-07-18T23:55:00Z"
lastmod = "2011-07-26T05:03:00Z"
weight = 5111
keywords = [ "tcp.stream", "command", "tshark", "windowscaling" ]
aliases = [ "/questions/5111" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can i tshark a folder full of tracefiles for the biggest tcp stream in each trace?](/questions/5111/how-can-i-tshark-a-folder-full-of-tracefiles-for-the-biggest-tcp-stream-in-each-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5111-score" class="post-score" title="current number of votes">0</div><span id="post-5111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm tracing issues with Window Scaling from client to server, after a batch testfile (with copy commands for file transfers) i want to analyse all tracefiles for throughput, window sizes, application read requests and so on, but..... from every trace i only need the biggest tcp stream. Most of the time it's "tcp.stream eq 0" but sometimes not.. How to tshark a folder full of traces for the biggest tcp stream in each trace?</p><p>As always, all answers are highly appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp.stream" rel="tag" title="see questions tagged &#39;tcp.stream&#39;">tcp.stream</span> <span class="post-tag tag-link-command" rel="tag" title="see questions tagged &#39;command&#39;">command</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-windowscaling" rel="tag" title="see questions tagged &#39;windowscaling&#39;">windowscaling</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '11, 23:55</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p><span>Marc</span><br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jul '11, 23:56</strong> </span></p></div></div><div id="comments-container-5111" class="comments-container"></div><div id="comment-tools-5111" class="comment-tools"></div><div class="clear"></div><div id="comment-5111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5237"></span>

<div id="answer-container-5237" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5237-score" class="post-score" title="current number of votes">3</div><span id="post-5237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Marc has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So the "koel" stuff you're looking for might be looking something like this?</p><pre><code>for file in *.pcap
do 
  tshark -r $file -w largest-stream-from-$file \
     -R `tshark -nlr $file -R &quot;tcp.flags.fin==1 or tcp.flags.reset==1&quot; -T fields -e tcp.seq -e tcp.ack -e tcp.stream | \
           awk &#39;BEGIN {max=1} {sum=$1+$2;if(sum&gt;max) {max=sum;stream=$3}} END {printf(&quot;tcp.stream==%d&quot;,stream)}&#39;`
done</code></pre><p>(only works with relative sequence numbering on and for streams in which the sequence number does not wrap)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '11, 17:12</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5237" class="comments-container"><span id="5252"></span><div id="comment-5252" class="comment"><div id="post-5252-score" class="comment-score"></div><div class="comment-text"><p>Many,many thanks! I'll let the script work down my dir meanwhile i'll try get my head around everybit of that long line you wrote here, amazing stuff mr Blok!</p></div><div id="comment-5252-info" class="comment-info"><span class="comment-age">(26 Jul '11, 05:03)</span> <span class="comment-user userinfo">Marc</span></div></div></div><div id="comment-tools-5237" class="comment-tools"></div><div class="clear"></div><div id="comment-5237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5225"></span>

<div id="answer-container-5225" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5225-score" class="post-score" title="current number of votes">2</div><span id="post-5225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>You can use tshark statistics to create a table of all tcp conversations:
$ tshark -r test.pcap -q -z conv,tcp
================================================================================
TCP Conversations
Filter:&lt;no filter=&quot;&quot;&gt;
                                               |       &lt;-      | |       -&gt;      | |     Total     |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |
192.168.108.2:2720     &lt;-&gt; 147.234.1.253:21          28      2306      18      1047      46      3353
147.234.1.253:58999    &lt;-&gt; 192.168.108.2:2721         3       170       2       122       5       292
192.168.108.2:2718     &lt;-&gt; 147.137.21.94:139          0         0       3       186       3       186
192.168.108.2:2717     &lt;-&gt; 147.137.21.94:445          0         0       3       186       3       186
================================================================================

Or use this little script:

for file in `ls -1 *.pcap`
do
   tshark -r $file -q -z conv,tcp &gt; $file.txt
done
</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '11, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span></p></div></div><div id="comments-container-5225" class="comments-container"><span id="5228"></span><div id="comment-5228" class="comment"><div id="post-5228-score" class="comment-score"></div><div class="comment-text"><p>Ah Joke! Thanks for the answer! but this is only partly what i ment, i would need the biggest trace in the file eg a new .pcap file with only the biggest trace, so dropping everything else</p></div><div id="comment-5228-info" class="comment-info"><span class="comment-age">(25 Jul '11, 12:12)</span> <span class="comment-user userinfo">Marc</span></div></div><span id="5229"></span><div id="comment-5229" class="comment"><div id="post-5229-score" class="comment-score"></div><div class="comment-text"><pre><code>So next step is (but I only know the hard way:))
tshark -r test.pcap -R &quot;ip.addr==192.168.108.2 &amp;&amp; tcp.port==2720 &amp;&amp; ip.addr==147.234.1.253 &amp;&amp; tcp.port==21&quot; -w test.tcp.pcap

$ tshark -r test.tcp.pcap -q -z conv,tcp
TCP Conversations
Filter:&lt;no filter=&quot;&quot;&gt;
                                               |       &lt;-      | |       -&gt;      | |     Total     |
                                               | Frames  Bytes | | Frames  Bytes | | Frames  Bytes |
192.168.108.2:2720     &lt;-&gt; 147.234.1.253:21       28      2306      18      1047      46      3353</code></pre></div><div id="comment-5229-info" class="comment-info"><span class="comment-age">(25 Jul '11, 12:34)</span> <span class="comment-user userinfo">joke</span></div></div><span id="5230"></span><div id="comment-5230" class="comment"><div id="post-5230-score" class="comment-score"></div><div class="comment-text"><p>Exactly, and this is where it gets hard because doing this for every tracefile in a folder is as much trouble as clicking through the GUI... i was hoping for something (i'm using my fantasy here...)along the lines of: tshark -r test.tcp.pcap -q -z conv,tcp | awk "first lines of previous output" then put in new tshark cmd... wouldn't that be "koel"?</p></div><div id="comment-5230-info" class="comment-info"><span class="comment-age">(25 Jul '11, 12:44)</span> <span class="comment-user userinfo">Marc</span></div></div></div><div id="comment-tools-5225" class="comment-tools"></div><div class="clear"></div><div id="comment-5225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

