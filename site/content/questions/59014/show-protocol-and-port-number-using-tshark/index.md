+++
type = "question"
title = "Show protocol and port number using tshark"
description = '''Hi, I would like to export [protocol,source port ,destination port] from pcap file as csv file. Would it be possible to get results like [tcp,5423,22] [udp,9334,161].   I need something like if protocol column is tcp,print tcp.srcport in source port column and tcp.dstport in destination port column ...'''
date = "2017-01-24T10:25:00Z"
lastmod = "2017-01-24T13:01:00Z"
weight = 59014
keywords = [ "read-filter", "tshark", "display-filter" ]
aliases = [ "/questions/59014" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Show protocol and port number using tshark](/questions/59014/show-protocol-and-port-number-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59014-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I would like to export [protocol,source port ,destination port] from pcap file as csv file.</p><p>Would it be possible to get results like [tcp,5423,22] [udp,9334,161].<br />
</p><p>I need something like if protocol column is tcp,print tcp.srcport in source port column and tcp.dstport in destination port column and same for udp as well.</p><p>I do not want create seperate columns for tcp ports and udp ports.</p><p>Can I do it with tshark -R??</p></div><div id="question-tags" class="tags-container tags">read-filter tshark display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '17, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/95e9674b7a67d58ada813e0c6bc38d84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subinjp&#39;s gravatar image" /><p>subinjp<br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subinjp has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-59014" class="comments-container"></div><div id="comment-tools-59014" class="comment-tools"></div><div class="clear"></div><div id="comment-59014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59019"></span>

<div id="answer-container-59019" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59019-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You ought to be able to <em>mostly</em> achieve this with <a href="https://www.wireshark.org/docs/man-pages/tshark.html"><code>tshark</code></a> by specifying the columns you want as follows (run "<code>tshark -G column-formats</code>" to find these):</p><pre><code>tshark -r capture.pcap -Y &quot;udp or tcp&quot; -o &quot;gui.column.format:\&quot;Protocol\&quot;,\&quot;%p\&quot;,\&quot;SrcPort\&quot;,\&quot;%S\&quot;,\&quot;DstPort\&quot;,\&quot;%D\&quot;</code></pre><p>The "Protocol" column will indicate the most upper-layer protocol present in the packet though and not specifically "tcp" or "udp", and if you want the fields comma-separated and surrounded by those <code>[]</code> brackets, then you'll have to figure out how to do that some other way.</p><p>You can probably get a bit closer if you first add all the columns you want within Wireshark first+, and then run <code>tshark</code> as follows (assuming your Wireshark columns are named as mine are below):</p><pre><code>tshark -r capture.pcap -Y &quot;udp or tcp&quot; -T fields -e _ws.col.Protocol -e _ws.col.SrcPort -e _ws.col.DstPort -E separator=, &gt; ports.csv</code></pre><p>Again, the protocol name printed will be the most upper-layer protocol present in the packet. If you don't care about "udp" and "tcp" vs. their IP protocol numbers "17" and "6" respectively, then you could substitute "<code>-e ip.proto</code>" for "<code>-e _ws.col.Protocol</code>", but you should probably modify the filter to be "<code>-Y "ip and (udp or tcp)"</code> to be sure there's an IP header (as opposed to an IPv6 header, and you will still have to add the <code>[]</code> brackets somehow. If you have IPv6 traffic, then the field would be <code>-e ipv6.nxt</code> instead of <code>-e ip.proto</code> and the filter would be "<code>-Y ipv6 and (udp or tcp)</code>".</p><p>+Wireshark column preferences are added via <code>Edit -&gt; Preferences -&gt; Columns -&gt; Add</code>. The so-called <em>built-in</em> field types of "Source Port" and "Destination Port" are probably what you're looking for ... besides whatever other columns you're interested in.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '17, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59019" class="comments-container"><span id="59022"></span><div id="comment-59022" class="comment"><div id="post-59022-score" class="comment-score"></div><div class="comment-text"><p>@cmaynard Thank you very much for the answer.. The problem is packet capture is happening in a remote server. I have access to server only through command line(using ssh). So I am not able to add columns in to wireshark using gui. I am using only tshark to access the pcap file.</p><p>Can I change the format of columns or add columns using tshark itself?? or Is there any way to add columns in to wireshark without using gui.?</p></div><div id="comment-59022-info" class="comment-info"><span class="comment-age">(24 Jan '17, 13:18)</span> subinjp</div></div><span id="59024"></span><div id="comment-59024" class="comment"><div id="post-59024-score" class="comment-score"></div><div class="comment-text"><p>You can change the columns using <code>tshark</code> alone using the <code>-o "gui.column.format:...</code> method described above.</p><p>You could also directly edit the Wireshark "<em>preferences</em>" file found in the Wireshark personal configuration folder. Search for "gui.column.format" in the file and then add/modify columns as desired. Take heed when editing though, and I would suggest making a copy of the file first in case you make a mistake or to be able to restore the original preferences file later. Better would be to create a separate profile and edit the profile's preference file instead, thus leaving the original one alone. You can specify the profile to use with <code>tshark</code>'s <code>-C &lt;profile&gt;</code> option.</p></div><div id="comment-59024-info" class="comment-info"><span class="comment-age">(24 Jan '17, 13:31)</span> cmaynard ♦♦</div></div><span id="59036"></span><div id="comment-59036" class="comment"><div id="post-59036-score" class="comment-score"></div><div class="comment-text"><p>Thank you..:):)</p></div><div id="comment-59036-info" class="comment-info"><span class="comment-age">(24 Jan '17, 16:26)</span> subinjp</div></div></div><div id="comment-tools-59019" class="comment-tools"></div><div class="clear"></div><div id="comment-59019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

