+++
type = "question"
title = "use capture filter or display filter ?"
description = '''i want to do live capture and extract specific fields like ip.src ip.dst , .. then save the result in multiple csv files using ring buffer i found that if i used this command  tshark -r 111.pcap -T fields -e frame.number -e frame.time -e ip.src -e ip.dst -e data.text -e tcp.analysis.duplicate_ack -e...'''
date = "2015-01-18T11:56:00Z"
lastmod = "2015-01-19T03:45:00Z"
weight = 39254
keywords = [ "capture", "capture-filter", "ringbuffer" ]
aliases = [ "/questions/39254" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [use capture filter or display filter ?](/questions/39254/use-capture-filter-or-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39254-score" class="post-score" title="current number of votes">0</div><span id="post-39254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i want to do live capture and extract specific fields like ip.src ip.dst , .. then save the result in multiple csv files using ring buffer</p><p>i found that if i used this command</p><p>tshark -r 111.pcap -T fields -e frame.number -e frame.time -e ip.src -e ip.dst -e data.text -e tcp.analysis.duplicate_ack -e tcp.analysis.out_of_order -e tcp.analysis.retransmission -e tcp.analysis.fast_retransmission -e tcp.analysis.spurious_retransmission -e tcp.analysis.zero_window -e tcp.stream -e tcp.srcport -e tcp.dstport -e data.len -E header=y -E separator=, -E quote=d &gt;out.csv</p><p>tshark will read from 111.pcap file and save mentioned fields in out.csv file</p><p>i want to apply the same but in live capture and save the result in multiple csv files using ring buffer</p><p>so i tried to use this command</p><p>tshark -i 3 -b files:5 -T fields -e frame.number -e frame.time -e ip.src -e ip.dst -e data.text -e tcp.analysis.duplicate_ack -e tcp.analysis.out_of_order -e tcp.analysis.retransmission -e tcp.analysis.fast_retransmission -e tcp.analysis.spurious_retransmission -e tcp.analysis.zero_window -e tcp.stream -e tcp.srcport -e tcp.dstport -e data.len -E header=y -E separator=, -E quote=d &gt;out.csv</p><p>it give me (( tshark :multiple capture files requested but the capture isn't being saved to file))</p><p>why?</p><p>i think it need capture filter but couldn't write one for all these fields ? thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-ringbuffer" rel="tag" title="see questions tagged &#39;ringbuffer&#39;">ringbuffer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '15, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/583f60448e616e6c6f8408eb6620006a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shady&#39;s gravatar image" /><p><span>shady</span><br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shady has no accepted answers">0%</span></p></div></div><div id="comments-container-39254" class="comments-container"></div><div id="comment-tools-39254" class="comment-tools"></div><div class="clear"></div><div id="comment-39254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39255"></span>

<div id="answer-container-39255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39255-score" class="post-score" title="current number of votes">2</div><span id="post-39255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The error means you gave a "<code>-b files:5</code>" option to write to 5 capture files in a ring, but didn't give a "<code>-w filename</code>" option to make tshark write the capture file and its file name. Note that the "<code>-b files:5</code>" applies to <strong>capture</strong> files tshark writes, <em>not</em> to "out.csv" which is where you were saving the output that would have been printed to the screen to a file instead. In other words, when you did "<code>&gt;out.csv</code>", you redirected the screen output to a file named "out.csv"... but tshark knows nothing about that and wasn't doing it - your shell/OS was doing that redirection.</p><p>Also, you were not using a "display filter" - you were just telling tshark to print out those specific fields instead of its normal output. It's just that what it was printing to the screen was being redirected to a file by your shell/OS.</p><pre><code>&gt; i want to apply the same but in live capture and save the result in multiple csv files using ring buffer</code></pre><p>I don't know a way to do that. You could just run tshark to save live to 5 capture files in a ring, and then separately run tshark again for each of those saved files to save the specific fields to a CSV file, as you did before.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '15, 14:18</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-39255" class="comments-container"><span id="39271"></span><div id="comment-39271" class="comment"><div id="post-39271-score" class="comment-score"></div><div class="comment-text"><p>thank you very much for explaining</p><p>i planning to create batch file to handle these 5 pcap files from live capture to covert them to csv file while live capture is running</p><p>any help here</p></div><div id="comment-39271-info" class="comment-info"><span class="comment-age">(19 Jan '15, 03:45)</span> <span class="comment-user userinfo">shady</span></div></div></div><div id="comment-tools-39255" class="comment-tools"></div><div class="clear"></div><div id="comment-39255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

