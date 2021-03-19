+++
type = "question"
title = "Copy multiple URIs at once"
description = '''Hi, Is it possible to copy multiple URIs at once in Wireshark 1.6.5? Right now, when Wireshark displays an http GET command of interest, I select the packet, then right click on the Full Request URI under &quot;Hypertext Transfer Protocol&quot;, &quot;Copy&quot;, then &quot;Value&quot;. When there are hundreds of URIs to copy, i...'''
date = "2012-01-21T18:12:00Z"
lastmod = "2012-01-24T07:26:00Z"
weight = 8533
keywords = [ "multiple", "http", "uri", "copying" ]
aliases = [ "/questions/8533" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Copy multiple URIs at once](/questions/8533/copy-multiple-uris-at-once)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8533-score" class="post-score" title="current number of votes">0</div><span id="post-8533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is it possible to copy multiple URIs at once in Wireshark 1.6.5?</p><p>Right now, when Wireshark displays an http GET command of interest, I select the packet, then right click on the Full Request URI under "Hypertext Transfer Protocol", "Copy", then "Value". When there are hundreds of URIs to copy, it becomes maddening.</p><p>Ideally, I would like to select the packets with ctrl+click, shift+click or ctrl+A, then right click and copy Full URIs.</p><p>Is there any way to get the full URIs faster than how I'm doing now ?</p><p>Thank you very much for your help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-uri" rel="tag" title="see questions tagged &#39;uri&#39;">uri</span> <span class="post-tag tag-link-copying" rel="tag" title="see questions tagged &#39;copying&#39;">copying</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '12, 18:12</strong></p><img src="https://secure.gravatar.com/avatar/e3b051144e70a05eb06689bc312aaf90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arto65&#39;s gravatar image" /><p><span>Arto65</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arto65 has no accepted answers">0%</span></p></div></div><div id="comments-container-8533" class="comments-container"></div><div id="comment-tools-8533" class="comment-tools"></div><div class="clear"></div><div id="comment-8533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="8535"></span>

<div id="answer-container-8535" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8535-score" class="post-score" title="current number of votes">1</div><span id="post-8535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <a href="http://www.wireshark.org/docs/man-pages/tshark.html">TShark</a>, one of the <a href="http://www.wireshark.org/docs/man-pages/">Wireshark tools</a> to do the job:<br />
</p><pre><code>-T pdml|ps|psml|text|fields  format of text output (def: text)
-e &lt;field&gt;                   field to print if -Tfields selected (e.g. tcp.port);</code></pre>$ tshark -r clmt_04.pcap -T fields -e http.request.full_uri | sort | uniq &gt; http.request.full_uri.txt</div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '12, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jan '12, 01:08</strong> </span></p></div></div><div id="comments-container-8535" class="comments-container"><span id="8560"></span><div id="comment-8560" class="comment"><div id="post-8560-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, joke!</p><p>I got it working but using this: <code>tshark -i [mycaptureinterface] -e http.request.full_uri -Tfields -f capture.filter &gt; f:\captureoutput.txt</code></p><p>It's not as good as I'd hope, but at least it's working. Do you think it would be a worthy feature to implement in Wireshark? Being able to copy one type of information from multiple packets? I, for one, would love that.</p></div><div id="comment-8560-info" class="comment-info"><span class="comment-age">(23 Jan '12, 05:51)</span> <span class="comment-user userinfo">Arto65</span></div></div></div><div id="comment-tools-8535" class="comment-tools"></div><div class="clear"></div><div id="comment-8535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8559"></span>

<div id="answer-container-8559" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8559-score" class="post-score" title="current number of votes">0</div><span id="post-8559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you very much, joke!</p><p>I got it working but using this: <code>tshark -i [mycaptureinterface] -e http.request.full_uri -Tfields -f capture.filter &gt; f:\captureoutput.txt</code></p><p>It's not as good as I'd hope, but at least it's working. Do you think it would be a worthy feature to implement in Wireshark? Being able to copy one type of information from multiple packets? I, for one, would love that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '12, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/e3b051144e70a05eb06689bc312aaf90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arto65&#39;s gravatar image" /><p><span>Arto65</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arto65 has no accepted answers">0%</span></p></div></div><div id="comments-container-8559" class="comments-container"></div><div id="comment-tools-8559" class="comment-tools"></div><div class="clear"></div><div id="comment-8559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8568"></span>

<div id="answer-container-8568" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8568-score" class="post-score" title="current number of votes">0</div><span id="post-8568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You get a better result, when you use TShark together with sort and uniq:<br />
$ tshark -i 4 -T fields -e http.request.full_uri | sort | uniq &gt; http.request.full_uri4.txt.<br />
<br />
I run <a href="http://www.cygwin.com/">cygwin</a> on my Windows box.<br />
It took some time, but once I had learned how to use the <a href="http://www.wireshark.org/docs/man-pages/">command line tools</a>, I love to use them.<br />
Just some examples:<br />
</p><pre><code>$ tshark -r test.pcap -T fields -e frame.number -e eth.src -e eth.dst -e ip.src -e ip.dst -e frame.len &gt; test1.csv
$ tshark -r test.pcap -T fields -e frame.number -e eth.src -e eth.dst -e ip.src -e ip.dst -e frame.len -E header=y -E separator=, &gt; test2.csv
$ tshark -r test.pcap -R &quot;frame.number&lt;40&quot; -T fields -e frame.number -e frame.time -e frame.time_delta -e frame.time_delta_displayed -e frame.time_relative -E header=y &gt; test3.csv
$ tshark -r test.pcap -R &quot;wlan.fc.type_subtype == 0x08&quot; -T fields -e frame.number -e wlan.sa -e wlan.bssid &gt; test4.csv
$ tshark -r test.pcap -R &quot;ip.addr==192.168.1.6 &amp;&amp; tcp.port==1696 &amp;&amp; ip.addr==67.212.143.22 &amp;&amp; tcp.port==80&quot; -T fields -e frame.number -e tcp.analysis.ack_rtt -E header=y &gt; test5.csv
$ tshark -r test.pcap -T fields -e frame.number -e tcp.analysis.ack_rtt -E header=y &gt; test6.csv</code></pre><br />
BTW<br />
You can also file an enhancement bug at <a href="https://bugs.wireshark.org/bugzilla/">Bugzilla</a>.<br />
</div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '12, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-8568" class="comments-container"><span id="8577"></span><div id="comment-8577" class="comment"><div id="post-8577-score" class="comment-score"></div><div class="comment-text"><p>What are 'sort' and 'uniq' for ? I am not sure why I need them for this specific task: I just need the URL in the order they're coming, and there are never any dupes.</p><p>Why the need for cygwin? I use cygwin for rsync for example, but what are the benefits for Tshark?</p><p>I filed an enhancement request at Bugzilla, we'll see how it goes!</p><p>Thanks again for everything!</p></div><div id="comment-8577-info" class="comment-info"><span class="comment-age">(24 Jan '12, 01:17)</span> <span class="comment-user userinfo">Arto65</span></div></div><span id="8584"></span><div id="comment-8584" class="comment"><div id="post-8584-score" class="comment-score">1</div><div class="comment-text"><p>I converted your "answer" to a comment as that is how this site works. See the <a href="http://ask.wireshark.org/faq/">FAQ</a> for details.</p><p>The extra commands in the pipeline fairly obviously sort the output and remove duplicates, this may be useful for some folks.</p><p>For those that have embraced PowerShell the equivalent would be:</p><p><code>PS C:temp&gt; &amp; 'tshark.exe' -r test.pcap -T fields -e http.request.full_uri | Sort-Object | Get-Unique</code></p></div><div id="comment-8584-info" class="comment-info"><span class="comment-age">(24 Jan '12, 07:26)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-8568" class="comment-tools"></div><div class="clear"></div><div id="comment-8568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

