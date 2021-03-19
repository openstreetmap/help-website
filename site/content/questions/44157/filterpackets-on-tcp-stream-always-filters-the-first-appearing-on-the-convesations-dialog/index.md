+++
type = "question"
title = "FilterPackets on TCP Stream always filters the first appearing on the Convesations dialog"
description = '''I have to filter single TCP streams out of the open capture file. Therefore I am programmatically applying display-filter &quot;tcp.stream eq TCP_STREAM_ID&quot;. The problem I have is that no matter the value of TCP_STREAM_ID, I always get the first stream shown in the Conversations dialog of the Statistics ...'''
date = "2015-07-14T15:12:00Z"
lastmod = "2015-07-14T15:12:00Z"
weight = 44157
keywords = [ "filter", "follow", "display-filter", "stream", "conversation" ]
aliases = [ "/questions/44157" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [FilterPackets on TCP Stream always filters the first appearing on the Convesations dialog](/questions/44157/filterpackets-on-tcp-stream-always-filters-the-first-appearing-on-the-convesations-dialog)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44157-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have to filter single TCP streams out of the open capture file. Therefore I am programmatically applying display-filter "tcp.stream eq TCP_STREAM_ID". The problem I have is that no matter the value of TCP_STREAM_ID, I always get the first stream shown in the Conversations dialog of the Statistics menu.</p><p>Please find a snapshot of my code below.</p><pre><code>gchar *data_out_filename;
QString follow_filter;
int tmp_fd;

follow_filter=QString(&quot;tcp.stream eq 5&quot;); //I am filtering tcp stream conversations.

reset_tcp_reassembly();
tmp_fd = create_tempfile(&amp;data_out_filename, &quot;follow&quot;);
data_out_file = fdopen(tmp_fd, &quot;w+b&quot;);

emit updateFilter(follow_filter, TRUE);</code></pre><p>What am I doing wrong? Am I missing anything?</p></div><div id="question-tags" class="tags-container tags">filter follow display-filter stream conversation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '15, 15:12</strong></p><img src="https://secure.gravatar.com/avatar/5df333830379ff009c6e2243920a5885?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CrazyL&#39;s gravatar image" /><p>CrazyL<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CrazyL has no accepted answers">0%</span></p></div></div><div id="comments-container-44157" class="comments-container"></div><div id="comment-tools-44157" class="comment-tools"></div><div class="clear"></div><div id="comment-44157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

