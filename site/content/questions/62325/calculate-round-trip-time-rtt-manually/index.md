+++
type = "question"
title = "Calculate Round Trip Time (RTT) manually"
description = '''How can we calculate Round Trip Time (RTT) from a passive traffic manually using the formula? I can obtain RTT values using tcptrace but it takes ONLy discrete values as it is shown in the graph below. For example, using tcptrace, we can get RTT values as in the following (the first column is time i...'''
date = "2017-06-27T02:27:00Z"
lastmod = "2017-06-28T03:01:00Z"
weight = 62325
keywords = [ "rtt", "tcpdump", "tcp", "wireshark" ]
aliases = [ "/questions/62325" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Calculate Round Trip Time (RTT) manually](/questions/62325/calculate-round-trip-time-rtt-manually)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62325-score" class="post-score" title="current number of votes">0</div><span id="post-62325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can we calculate Round Trip Time (RTT) from a passive traffic manually using the formula? I can obtain RTT values using <em>tcptrace</em> but it takes ONLy discrete values as it is shown in the graph below. For example, using tcptrace, we can get RTT values as in the following (the first column is time in seconds and the second column is RTT in milli seconds (ms)).</p><pre><code>8.983596 4.000000
8.984129 3.000000
8.984829 4.00000</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/RTT_tcptrace.png" alt="alt text" /></p><p>It seems TCP takes only the real values for RTT. Is there any way to export the values returned from <strong>tcp.analysis.ack_rtt</strong> to a file and apply the formula for an RTT? I tried with <strong>statistics -&gt; RTT StreamGraph -&gt; RTT Graph</strong> where I can plot the RTT graph but i can't export the values (X and Y coordinates as in the previous format from <em>tcptrace</em>) to a file. When we plot RTT in Wireshark, it shows the values as continuous but it doesn't seem possible to export the values to a file. Or is there anyway to extract these values using tcpdump or any other tool?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtt" rel="tag" title="see questions tagged &#39;rtt&#39;">rtt</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '17, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p><span>armodes</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></img></div></div><div id="comments-container-62325" class="comments-container"></div><div id="comment-tools-62325" class="comment-tools"></div><div class="clear"></div><div id="comment-62325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62337"></span>

<div id="answer-container-62337" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62337-score" class="post-score" title="current number of votes">1</div><span id="post-62337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could probably use tshark to do something like that, printing relative time of each frame with the ACK_RTT as columns, e.g.</p><pre><code>[C:\]tshark -r &quot;Sample.pcapng&quot; -Tfields -e frame.time_relative -e tcp.analysis.ack_rtt
0.000000000
0.017430000     0.017430000
0.017456000     0.000026000
0.025576000
0.038697000     0.013121000
0.043810000
0.043818000     0.000008000
0.051572000
0.051960000
0.051966000     0.000006000
0.052220000
0.258296000     0.206076000
0.673018000
0.682172000     0.009154000
0.882325000     0.200153000
3.053319000
3.065140000     0.011821000
3.065235000
3.065239000     0.000004000</code></pre><p>redirecting that output to a file should be simple enough.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '17, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-62337" class="comments-container"><span id="62353"></span><div id="comment-62353" class="comment"><div id="post-62353-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much Jasper. How about if we want to calculate SRTT (Smoothed Round Trip Time) from this?</p></div><div id="comment-62353-info" class="comment-info"><span class="comment-age">(28 Jun '17, 03:01)</span> <span class="comment-user userinfo">armodes</span></div></div></div><div id="comment-tools-62337" class="comment-tools"></div><div class="clear"></div><div id="comment-62337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

