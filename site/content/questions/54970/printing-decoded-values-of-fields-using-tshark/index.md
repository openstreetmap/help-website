+++
type = "question"
title = "Printing decoded values of fields using Tshark"
description = '''I use tshark(in Windows) often to print some required fields from a pcap file for analysis. For example, i use this when i like to print the RAT type fields. C:&#92;Program Files&#92;Wireshark&amp;gt; ./tshark.exe -r &quot;C:&#92;Work&#92;GTP-diameter.cap&quot; -Y &quot;gtpv2 || diameter&quot; -T fields -e frame.number -e diameter.RAT-Typ...'''
date = "2016-08-19T01:42:00Z"
lastmod = "2016-08-19T01:42:00Z"
weight = 54970
keywords = [ "tshark", "decoding" ]
aliases = [ "/questions/54970" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Printing decoded values of fields using Tshark](/questions/54970/printing-decoded-values-of-fields-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54970-score" class="post-score" title="current number of votes">0</div><span id="post-54970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use tshark(in Windows) often to print some required fields from a pcap file for analysis. For example, i use this when i like to print the RAT type fields.</p><pre><code>C:\Program Files\Wireshark&gt; ./tshark.exe -r &quot;C:\Work\GTP-diameter.cap&quot; -Y &quot;gtpv2 || diameter&quot; -T fields -e frame.number -e diameter.RAT-Type -e gtp.ext_rat_type
1               1
2       1000
3
18      1000
29              2
30      1001</code></pre><p>However, this prints the value but not the decoded text. Is there any way to print the decoded text as we see in wireshark? The Wireshark GUI shows the values like the one below.</p><p>GTP:</p><pre><code>RAT Type: UTRAN (1)
RAT Type: GERAN (2)</code></pre><p>Diameter:</p><pre><code>RAT-Type: UTRAN (1000)
RAT-Type: GERAN (1001)</code></pre><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-decoding" rel="tag" title="see questions tagged &#39;decoding&#39;">decoding</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '16, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/dd095f051113eec930449223b3585971?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gouthamraj91&#39;s gravatar image" /><p><span>gouthamraj91</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gouthamraj91 has no accepted answers">0%</span></p></div></div><div id="comments-container-54970" class="comments-container"></div><div id="comment-tools-54970" class="comment-tools"></div><div class="clear"></div><div id="comment-54970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

