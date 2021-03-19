+++
type = "question"
title = "How can I get tshark to display data from Wireshark Parameterize column values as formatted text"
description = '''I am trying to use tshark to produce either a tab or comma delimited file with various fields from a pacap file that I have. I have tried 2 different methods and each has it&#x27;s own shortcoming. I am hoping that some one can help remedy my ignorance. I have been searching here, google, and a few other...'''
date = "2014-05-02T15:20:00Z"
lastmod = "2014-06-19T16:59:00Z"
weight = 32441
keywords = [ "output", "tshark", "formatted" ]
aliases = [ "/questions/32441" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can I get tshark to display data from Wireshark Parameterize column values as formatted text](/questions/32441/how-can-i-get-tshark-to-display-data-from-wireshark-parameterize-column-values-as-formatted-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32441-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to use tshark to produce either a tab or comma delimited file with various fields from a pacap file that I have. I have tried 2 different methods and each has it's own shortcoming. I am hoping that some one can help remedy my ignorance. I have been searching here, google, and a few other sites with no luck.<br />
</p><p>First method: tshark -r &lt;pcapfile.pcap&gt; -t ad -E header=y -E separator=/t -T fields -e frame.number -e frame.time -e tcp.stream -e ip.src -e ip.src_host -e ip.dst -e ip.dst_host -e Protocol</p><p>First Result: With this I get most of the data that I want. But I have not been able to to to get the contents of Wiresharks 'Protocol' Column. I have used both -e protocol and -e Protocol as the filed name, neither generates an error or provides data. But -e fred does the same. In Wireshark the column details are displayed as 'Protocol' (no 's), in the preferences file the protocol column is defined as %p. Using -e %p does generate and error.</p><p>Second method: tshark -r &lt;pcapfile.pcap&gt; -t ad -E header=y -E separator=/t -C &lt;profilename&gt;</p><p>Second Result: This does output all of the same data that I see in Wireshark. But, I seem to not be able to get column headers or field separators.</p><p>Now that I have went through all of this, It seems that what I want to know is 2 basic questions; 1) how can I get the 'paramterized' columns from Wireshark like 'Protocol(%p)', 'Cumulative Bytes(%B)',etc. list listed by tshark in formatted text?</p><p>2) how can I get tshark to display formatted text (headers and files separators) when using a configuration profile "-C" parameter.</p><p>Any help with this would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">output tshark formatted</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '14, 15:20</strong></p><img src="https://secure.gravatar.com/avatar/c89893c29e1be2a892a4bbce28d53a61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="astrader&#39;s gravatar image" /><p>astrader<br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="astrader has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-32441" class="comments-container"></div><div id="comment-tools-32441" class="comment-tools"></div><div class="clear"></div><div id="comment-32441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32442"></span>

<div id="answer-container-32442" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32442-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>In general, to display an arbitrary column, use <code>-e col.column name</code>, so in your case you could use <code>-e col.Protocol</code> to display the contents of the Protocol column.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '14, 16:18</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-32442" class="comments-container"><span id="32443"></span><div id="comment-32443" class="comment"><div id="post-32443-score" class="comment-score"></div><div class="comment-text"><p>That is exactly what I was looking for. That is exactly the bit of ignorance that was holding me up. I was not aware ot the col item.</p><p>Thanks!</p></div><div id="comment-32443-info" class="comment-info"><span class="comment-age">(02 May '14, 16:26)</span> astrader</div></div></div><div id="comment-tools-32442" class="comment-tools"></div><div class="clear"></div><div id="comment-32442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33971"></span>

<div id="answer-container-33971" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33971-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As of the 1.11.x and 1.12 versions of tshark, the field names are "_ws.col.Protocol" and "_ws.col.Info", instead of "col.Protocol" and "col.Info".</p><p>Example:</p><p><code>tshark -T fields -e _ws.col.Protocol -e _ws.col.Info</code></p><p>Source: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10201">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10201</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '14, 16:59</strong></p><img src="https://secure.gravatar.com/avatar/028a4be69999143f43a3ed2e97f42159?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CraigGarrett&#39;s gravatar image" /><p>CraigGarrett<br />
<span class="score" title="86 reputation points">86</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CraigGarrett has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jun '14, 10:20</p></div></div><div id="comments-container-33971" class="comments-container"><span id="33999"></span><div id="comment-33999" class="comment"><div id="post-33999-score" class="comment-score"></div><div class="comment-text"><p>thanks for the update. I will have to grab a newer version and give this a try.</p></div><div id="comment-33999-info" class="comment-info"><span class="comment-age">(20 Jun '14, 12:17)</span> astrader</div></div></div><div id="comment-tools-33971" class="comment-tools"></div><div class="clear"></div><div id="comment-33971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

