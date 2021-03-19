+++
type = "question"
title = "export selected packet bytes / how to cut off the payload in a pcap file?"
description = '''The File menu option &quot;Export Selected Packet Bytes...&quot; is NOT enabled. What do I need to do to enable it?'''
date = "2014-02-11T06:31:00Z"
lastmod = "2014-02-11T07:21:00Z"
weight = 29693
keywords = [ "bytes", "selected", "export", "packet", "anonimization" ]
aliases = [ "/questions/29693" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [export selected packet bytes / how to cut off the payload in a pcap file?](/questions/29693/export-selected-packet-bytes-how-to-cut-off-the-payload-in-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29693-score" class="post-score" title="current number of votes">0</div><span id="post-29693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The File menu option "Export Selected Packet Bytes..." is NOT enabled. What do I need to do to enable it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bytes" rel="tag" title="see questions tagged &#39;bytes&#39;">bytes</span> <span class="post-tag tag-link-selected" rel="tag" title="see questions tagged &#39;selected&#39;">selected</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-anonimization" rel="tag" title="see questions tagged &#39;anonimization&#39;">anonimization</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/67fd1377da78e16e63d1e5c95dacab83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bundgaj&#39;s gravatar image" /><p><span>bundgaj</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bundgaj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '14, 07:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-29693" class="comments-container"><span id="29694"></span><div id="comment-29694" class="comment"><div id="post-29694-score" class="comment-score"></div><div class="comment-text"><p>This problem exists in both 1.10.5 and 1.11.2</p></div><div id="comment-29694-info" class="comment-info"><span class="comment-age">(11 Feb '14, 06:32)</span> <span class="comment-user userinfo">bundgaj</span></div></div></div><div id="comment-tools-29693" class="comment-tools"></div><div class="clear"></div><div id="comment-29693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29696"></span>

<div id="answer-container-29696" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29696-score" class="post-score" title="current number of votes">1</div><span id="post-29696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the manual: <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChIOExportSection.html">http://www.wireshark.org/docs/wsug_html_chunked/ChIOExportSection.html</a></p><pre><code>5.7.7. The &quot;Export selected packet bytes&quot; dialog box
Export the bytes selected in the &quot;Packet Bytes&quot; pane into a raw binary file. </code></pre><p>As soon as you select some bytes in the 'Packet Bytes' pane, the menu item will be enabled.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '14, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29696" class="comments-container"><span id="29699"></span><div id="comment-29699" class="comment"><div id="post-29699-score" class="comment-score"></div><div class="comment-text"><p>Thanks. What I really want to do is to export only the headers from the pcap file. How do I do that?</p></div><div id="comment-29699-info" class="comment-info"><span class="comment-age">(11 Feb '14, 06:56)</span> <span class="comment-user userinfo">bundgaj</span></div></div><span id="29701"></span><div id="comment-29701" class="comment"><div id="post-29701-score" class="comment-score"></div><div class="comment-text"><p>It depends on what you mean by "headers from the pcap file"...</p><p>I guess the following should be O.K. for you.</p><blockquote><p>File -&gt; Export Packet Dissections -&gt; as plain text file</p></blockquote><p>Then take a look at the "Packet Format" option.</p><p>Additionally, you can use <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a> to extract whatever 'protocol field' you need.</p><blockquote><p>tshark -nr input.pcap -T fields -e frame.number -e ip.src -e ip.dst -e tcp.port -e xxxxx</p></blockquote><p>See the <a href="http://www.wireshark.org/docs/dfref/">Display filter reference</a> for all available fields.</p></div><div id="comment-29701-info" class="comment-info"><span class="comment-age">(11 Feb '14, 07:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29702"></span><div id="comment-29702" class="comment"><div id="post-29702-score" class="comment-score"></div><div class="comment-text"><p>The pcap file has a variety of encapsulations: UDP, TCP, L3 only... I'd like to export the entire pcap file without any of the 'payload data'.</p></div><div id="comment-29702-info" class="comment-info"><span class="comment-age">(11 Feb '14, 07:06)</span> <span class="comment-user userinfo">bundgaj</span></div></div><span id="29703"></span><div id="comment-29703" class="comment"><div id="post-29703-score" class="comment-score"></div><div class="comment-text"><p>In what form do you want to export it? Do need a new pcap file, just without the payload (like for anonymization) or do you need a text representation of the dissected headers, just without the payload?</p></div><div id="comment-29703-info" class="comment-info"><span class="comment-age">(11 Feb '14, 07:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29704"></span><div id="comment-29704" class="comment"><div id="post-29704-score" class="comment-score"></div><div class="comment-text"><p>A new pcap file.</p></div><div id="comment-29704-info" class="comment-info"><span class="comment-age">(11 Feb '14, 07:20)</span> <span class="comment-user userinfo">bundgaj</span></div></div><span id="29705"></span><div id="comment-29705" class="comment not_top_scorer"><div id="post-29705-score" class="comment-score"></div><div class="comment-text"><p>Ah, then you need a tool to anonymize the file.</p><p>One of the best tools available is <a href="http://www.tracewrangler.com">TraceWrangler</a> from <span>@Jasper</span>.</p><p>There are other tools as well, just google for: 'pcap anonymizer' or 'pcap anonymization'</p><p>You can also use <a href="http://www.wireshark.org/docs/man-pages/editcap.html">editcap</a> to cut off the frames at a certain position.</p><blockquote><p>editcap -C 100 input.pcap output.pcap</p></blockquote></div><div id="comment-29705-info" class="comment-info"><span class="comment-age">(11 Feb '14, 07:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29696" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-29696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

