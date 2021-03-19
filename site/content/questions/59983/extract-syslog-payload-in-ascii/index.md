+++
type = "question"
title = "Extract syslog payload in ASCII"
description = '''Hi. I have a Wireshark capture of syslog data and I need to extract the raw data portion of the packet in ASCII. I can extract the data in the exact format I need by selecting a single packet and clicking &#x27;Export Packet Bytes&#x27; from the File menu. But I need to extract this data for every packet in t...'''
date = "2017-03-10T07:12:00Z"
lastmod = "2017-03-10T10:43:00Z"
weight = 59983
keywords = [ "data", "extract", "tshark" ]
aliases = [ "/questions/59983" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract syslog payload in ASCII](/questions/59983/extract-syslog-payload-in-ascii)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59983-score" class="post-score" title="current number of votes">0</div><span id="post-59983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I have a Wireshark capture of syslog data and I need to extract the raw data portion of the packet in ASCII. I can extract the data in the exact format I need by selecting a single packet and clicking 'Export Packet Bytes' from the File menu. But I need to extract this data for every packet in the trace, which isn't feasible in a trace containing thousands of packets. I've tried various permutations of the tshark command but I just can't seem to get it right. The closest I've come is this command, but the output is in hex:</p><p><strong>tshark -r syslog.pcap --disable-protocol syslog -T fields -e data.data</strong></p><p>What's the trick in getting this output in ASCII?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '17, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/1a70882b501f77b9706e5b3ad1808a4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="s_m_p&#39;s gravatar image" /><p><span>s_m_p</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="s_m_p has no accepted answers">0%</span></p></div></div><div id="comments-container-59983" class="comments-container"></div><div id="comment-tools-59983" class="comment-tools"></div><div class="clear"></div><div id="comment-59983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59984"></span>

<div id="answer-container-59984" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59984-score" class="post-score" title="current number of votes">1</div><span id="post-59984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could try:</p><pre><code>tshark -r syslog.pcap -T fields -e syslog.msg</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '17, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59984" class="comments-container"><span id="59985"></span><div id="comment-59985" class="comment"><div id="post-59985-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. That is close, but I need to include the raw facility and level bytes in the output. When I use this: 'tshark -r syslog.pcap -T fields -e syslog'</p><p>I get the translated data (i.e. "LOCAL7.INFO") instead of "&lt;190&gt;". I need the output in the "&lt;190&gt;" format.</p></div><div id="comment-59985-info" class="comment-info"><span class="comment-age">(10 Mar '17, 07:23)</span> <span class="comment-user userinfo">s_m_p</span></div></div><span id="59991"></span><div id="comment-59991" class="comment"><div id="post-59991-score" class="comment-score">1</div><div class="comment-text"><p>Well, you will probably have to convert the output using external tools. For example, the following <em>almost</em> works, except newlines are lost, so you will probably have to come up with something else.</p><pre><code>tshark -r syslog.pcap --disable-protocol syslog -Y &quot;udp.port eq 514&quot; -T fields -e data | xxd -r -p</code></pre></div><div id="comment-59991-info" class="comment-info"><span class="comment-age">(10 Mar '17, 09:50)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="59993"></span><div id="comment-59993" class="comment"><div id="post-59993-score" class="comment-score"></div><div class="comment-text"><p>OK, sure. I guess I just assumed that since Wireshark displays the data in ascii, tshark could output it in ascii too. But sure, I can run this output through an hex&gt;ascii tool. Thanks for the reply.</p></div><div id="comment-59993-info" class="comment-info"><span class="comment-age">(10 Mar '17, 10:43)</span> <span class="comment-user userinfo">s_m_p</span></div></div></div><div id="comment-tools-59984" class="comment-tools"></div><div class="clear"></div><div id="comment-59984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

