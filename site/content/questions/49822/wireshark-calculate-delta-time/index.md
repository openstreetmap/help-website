+++
type = "question"
title = "Wireshark - Calculate Delta Time"
description = '''Hi Very new to wireshark. I am trying to find average timer between 2 messages in about 50-60 separate wireshark traces collected. The messages are (1) &quot;Get URL&quot; message and (2)the first packet with size &amp;gt;1400 Bytes. Is it possible to write a query or any other method to find this in single trace...'''
date = "2016-02-04T07:09:00Z"
lastmod = "2016-02-04T22:37:00Z"
weight = 49822
keywords = [ "query", "time", "delta" ]
aliases = [ "/questions/49822" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark - Calculate Delta Time](/questions/49822/wireshark-calculate-delta-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49822-score" class="post-score" title="current number of votes">0</div><span id="post-49822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Very new to wireshark. I am trying to find average timer between 2 messages in about 50-60 separate wireshark traces collected. The messages are (1) "Get URL" message and (2)the first packet with size &gt;1400 Bytes. Is it possible to write a query or any other method to find this in single trace or for all traces at once?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span> <span class="post-tag tag-link-delta" rel="tag" title="see questions tagged &#39;delta&#39;">delta</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '16, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/ec9937a07b241f678e89199167160b40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tanz_eel&#39;s gravatar image" /><p><span>tanz_eel</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tanz_eel has no accepted answers">0%</span></p></div></div><div id="comments-container-49822" class="comments-container"></div><div id="comment-tools-49822" class="comment-tools"></div><div class="clear"></div><div id="comment-49822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49880"></span>

<div id="answer-container-49880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49880-score" class="post-score" title="current number of votes">1</div><span id="post-49880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark, as well as tshark which may be more useful for you as you talk about handling multiple files, uses a "display filter" to limit the display of packets (frames) to those matching some conditions. The conditions compare real fields of the packets (such as <code>ip.dst</code>, fields of their metadata (such as <code>frame.time</code>), and pseudo-fields computed by some protocol dissectors (such as <code>tcp.stream</code>) to constant values or to other fields, but always only fields defined for a single packet are taken into account when evaluating the conditions for that packet. Only few dissectors keep track about other packets belonging to the same conversation and compute pseudo-fields allowing to see (and use in display filter conditions) e.g. the delay of a response after a request.</p><p>Lucky for you, this is the case for http: for the first packet of an http response, the dissector calculates a pseudo-field <code>http.time</code>. So a display filter <code>http.time</code> alone would show you only the response packets; a display filter <code>http.time and (http.content_length &gt; 1400)</code> would show you only the first packets of responses whose total (payload!) size is over 1400 bytes, and a display filter <code>http.time and (frame.len &gt; 1400)</code> would show you only first packets of responses where the size of such first frame, including all the headers starting from the Ethernet one, is over 1400 bytes.</p><p>Now for your purpose, you would probably use a script, calling a tshark with all your 60 files as parameters and calculating the average from the displayed values. The command for a single file looks as follows:</p><p><code>tshark -r your_capture_file_name -Y "http.time and (frame.len &gt; 1400)" -T fields -e http.time</code></p><p>This outputs only the http response times found in the file, one per line.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '16, 22:37</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49880" class="comments-container"></div><div id="comment-tools-49880" class="comment-tools"></div><div class="clear"></div><div id="comment-49880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

