+++
type = "question"
title = "How do I apply a capture filter to a file?"
description = '''Can I apply a capture filter to a file I&#x27;ve already saved? Whenever I try this with tshark, I get this: C:&#92;ws_data&amp;gt;tshark -f &quot;ip host 192.168.0.2&quot; -r input_data.pcap -w output_data.pcap tshark: Only read filters, not capture filters, can be specified when reading a capture file. I&#x27;m using TShark ...'''
date = "2014-01-29T11:32:00Z"
lastmod = "2014-01-30T05:32:00Z"
weight = 29279
keywords = [ "capture-filter", "tshark", "file" ]
aliases = [ "/questions/29279" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I apply a capture filter to a file?](/questions/29279/how-do-i-apply-a-capture-filter-to-a-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29279-score" class="post-score" title="current number of votes">0</div><span id="post-29279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I apply a capture filter to a file I've already saved? Whenever I try this with <code>tshark</code>, I get this:<br />
</p><pre><code>C:\ws_data&gt;tshark -f &quot;ip host 192.168.0.2&quot; -r input_data.pcap -w output_data.pcap
tshark: Only read filters, not capture filters, can be specified when reading a capture file.</code></pre>I'm using <code>TShark 1.8.12-custom-win64 (SVN Rev 53127 from /trunk-1.8)</code>. Is there another tool that will do what I want, or do I need to learn how to write an equivalent read filter for my capture filter?</div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '14, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span> </br></p></div></div><div id="comments-container-29279" class="comments-container"></div><div id="comment-tools-29279" class="comment-tools"></div><div class="clear"></div><div id="comment-29279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29281"></span>

<div id="answer-container-29281" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29281-score" class="post-score" title="current number of votes">0</div><span id="post-29281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="multipleinterfaces has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there another tool that will do what I want,</p></blockquote><p>tcpdump ;-)</p><p>For windows there is a tool called <a href="http://www.netresec.com/?page=SplitCap">SplitCap</a>, but the filter syntax is neither capture filter nor display filter.</p><p>If you prefer a scripted solution, take a look at <a href="http://www.badpenguin.co.uk/files/pcap-util2">pcap-util2</a>. It accepts tcpdump capture filters: <a href="http://www.badpenguin.co.uk/files/pcap-util2">http://www.badpenguin.co.uk/files/pcap-util2</a></p><blockquote><p>do I need to learn how to write an equivalent read filter for my capture filter?</p></blockquote><p>sure, you can also use 'display/read' filters, and the change in the syntax shouldn't be too complex, at least not for simple capture filters.</p><blockquote><p>tshark -nr input.pcap -Y "icmp" -w output.pcap<br />
tshark -nr input.pcap -Y "ip.addr eq 192.168.0.2" -w output.pcap<br />
</p></blockquote><p><strong>++ UPDATE ++</strong><br />
I totally forgot <a href="http://www.winpcap.org/windump/default.htm">WinDump</a>. It will work like tcpdump, meaning it accepts capture filters.</p><blockquote><p>windump -nr input.pcap -w output.pcap "icmp"<br />
windump -nr input.pcap -w output.pcap "ip host 192.168.0.2"<br />
</p></blockquote><p>Hint: currently it only supports libpcap files, <strong>not</strong> pcap-ng files! So, if you want to use WinDump for pcap-ng files, you need to convert them first</p><blockquote><p>editcap -F pcap input.pcapng ouput.pcap</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '14, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jan '14, 05:13</strong> </span></p></div></div><div id="comments-container-29281" class="comments-container"><span id="29282"></span><div id="comment-29282" class="comment"><div id="post-29282-score" class="comment-score"></div><div class="comment-text"><p>I think you meant <code>-R</code> in place of <code>-Y</code>, but this is exactly what I really needed. Not sure how many times I missed that in the <code>tshark -h</code> output. And also thank you for pointing out that <strong>read</strong> filters are the same as <strong>display</strong> filters; I thought I was going to have to learn a third filter syntax for Wireshark.</p></div><div id="comment-29282-info" class="comment-info"><span class="comment-age">(29 Jan '14, 12:19)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="29283"></span><div id="comment-29283" class="comment"><div id="post-29283-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I think you meant -R in place of -Y,</p></blockquote><p>I really meant -Y. There was a change regarding -Y and -R in one of the recent releases.</p></div><div id="comment-29283-info" class="comment-info"><span class="comment-age">(29 Jan '14, 12:24)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29284"></span><div id="comment-29284" class="comment"><div id="post-29284-score" class="comment-score"></div><div class="comment-text"><p>BTW: see my update in the answer regarding pcap-util2.</p></div><div id="comment-29284-info" class="comment-info"><span class="comment-age">(29 Jan '14, 12:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29293"></span><div id="comment-29293" class="comment"><div id="post-29293-score" class="comment-score"></div><div class="comment-text"><p>Hm, -Y is for display filters, but <span>@multipleinterfaces</span> specifically asked for read filters, so I think it IS in fact "-R".</p></div><div id="comment-29293-info" class="comment-info"><span class="comment-age">(29 Jan '14, 23:28)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="29294"></span><div id="comment-29294" class="comment"><div id="post-29294-score" class="comment-score"></div><div class="comment-text"><p>Afiak, 'read' filters are display filter syntax. See 'tshark -h'.</p></div><div id="comment-29294-info" class="comment-info"><span class="comment-age">(29 Jan '14, 23:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29308"></span><div id="comment-29308" class="comment not_top_scorer"><div id="post-29308-score" class="comment-score"></div><div class="comment-text"><p>From <code>tshark -h</code></p><pre><code>  -2                       perform a two-pass analysis
  -R &lt;read filter=&quot;&quot;&gt;         packet Read filter in Wireshark display filter syntax
  -Y &lt;display filter=&quot;&quot;&gt;      packet displaY filter in Wireshark display filter syntax</code></pre><p>From the code in tshark.c.</p><p>option -R sets the 'read filter'<br />
option -Y sets the 'display filter'<br />
</p><p>Now, if I run the following command (1.11.x):</p><blockquote><p>tshark -nr input.pcap -R "ip.addr eq 1.2.3.4"</p></blockquote><p>I get the following message.</p><blockquote><p><code>tshark: -R without -2 is deprecated. For single-pass filtering use -Y.</code></p></blockquote><p>So, -Y is single pass and -R -r is two-pass. In that respect, -Y should be called the 'read filter' as it is applied only once during the first/single pass, while the file is being read. And -R should be called the 'display filter', as that's the filter that is applied on both passes, which makes it more like a display filter.</p><p><strong>However</strong>, in the code it seems to be vice versa (-Y sets the filter for pass two and -R sets the filter for pass one), or maybe I don't understand the code correctly.</p><p>Hopefully someone with a better understanding of the code can shed some light on the difference between -Y and -R !?!</p></div><div id="comment-29308-info" class="comment-info"><span class="comment-age">(30 Jan '14, 05:32)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29281" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-29281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

