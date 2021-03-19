+++
type = "question"
title = "Export data from a range/marked packets only"
description = '''I have a pcap file, to which I have applied some filters (so, they are non-sequential) and have marked a subset of packets from which I would like to extract their protocol specific data fields from. How can I do this? File-&amp;gt;Export Specified Packets gives me whole frames. File-&amp;gt;Export Packet B...'''
date = "2016-04-30T05:52:00Z"
lastmod = "2016-05-01T08:11:00Z"
weight = 52111
keywords = [ "filter", "export", "mark" ]
aliases = [ "/questions/52111" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Export data from a range/marked packets only](/questions/52111/export-data-from-a-rangemarked-packets-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52111-score" class="post-score" title="current number of votes">0</div><span id="post-52111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap file, to which I have applied some filters (so, they are non-sequential) and have marked a subset of packets from which I would like to extract their protocol specific data fields from. How can I do this?</p><p>File-&gt;Export Specified Packets gives me whole frames. File-&gt;Export Packet Bytes is what I'm looking for, but that option only outputs the selected frame, not the range...</p><p>GUI or terminal solutions would be acceptable.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-mark" rel="tag" title="see questions tagged &#39;mark&#39;">mark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '16, 05:52</strong></p><img src="https://secure.gravatar.com/avatar/258d6c27080a538b2d68ac9142fa0ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J%20B&#39;s gravatar image" /><p><span>J B</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J B has no accepted answers">0%</span></p></div></div><div id="comments-container-52111" class="comments-container"></div><div id="comment-tools-52111" class="comment-tools"></div><div class="clear"></div><div id="comment-52111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52122"></span>

<div id="answer-container-52122" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52122-score" class="post-score" title="current number of votes">2</div><span id="post-52122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="J B has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>Export Packet Bytes</code> works on a single packet because in a raw data output, there is no way to separate the pieces of data coming from individual packets from each other. Your particular task may not require the separation (i.e. a continuous stream of raw data may be what you actually need), however that's how it works now.</p><p>If you don't mind that the contents of the protocol fields you are interested in is not always output as hex but sometimes as an ASCII string, then <code>tshark -r your_file_name -Y "your_display_filter_expression" -T fields -e field_1_name -e field_2_name</code> is your best friend; if not, try <code>-T pdml</code> instead, where you get <code>show</code> and <code>value</code> items for most (yet not all) fields, like in the following example:</p><pre><code>&lt; field name=&quot;usb.urb_ts_usec&quot; showname=&quot;URB usec: 948741&quot; size=&quot;4&quot; pos=&quot;24&quot; show=&quot;948741&quot; value=&quot;057a0e00&quot;/&gt;</code></pre><p>However, the <code>-e</code> option does not work together with <code>-T pdml</code>, so the output is really huge. And you'll have to post-process the pdml output with something grep- and sed-like to extract only the required data from it.</p><p>While you cannot mark packets in tshark, you can use the display filter to define ranges. <code>-Y "tcp and ((frame.number &gt;= 5 and frame.number &lt;= 10) or (frame.number &gt;= 100 and frame.number &lt;= 108))"</code> is an example of a filter which lets through all TCP packets which exist inside ranges 5-10 and 100-108.</p><p>Instead of (commandline) tshark, you may use <code>File -&gt; Export Packet Dissections -&gt; As PDML XML</code> in (GUI) Wireshark for the same purpose; in this case, you can specify the list of ranges directly in a dedicated form field (like <code>5-10,100-108</code> to match the above example), yet the need to post-process the pdml output remains.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '16, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 May '16, 05:50</strong> </span></p></div></div><div id="comments-container-52122" class="comments-container"><span id="52123"></span><div id="comment-52123" class="comment"><div id="post-52123-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, for a most detailed explanation! It's too bad that the Wireshark can't do this in itself, but exporting to XML and writing a Python script to post-process it should work well!</p></div><div id="comment-52123-info" class="comment-info"><span class="comment-age">(01 May '16, 08:11)</span> <span class="comment-user userinfo">J B</span></div></div></div><div id="comment-tools-52122" class="comment-tools"></div><div class="clear"></div><div id="comment-52122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

