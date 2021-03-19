+++
type = "question"
title = "Best time format to analyze duration of flow"
description = '''I have to determine the duration of a flow of packets sent from the same IP source address (DDoS). My criteria is that the flow should be no less than 60 seconds. I am a bit confused about the different time formats available in tshark for display. What is the best time format to choose for this pur...'''
date = "2016-11-26T08:27:00Z"
lastmod = "2016-11-26T09:10:00Z"
weight = 57645
keywords = [ "duration", "ddos", "time", "flow", "format" ]
aliases = [ "/questions/57645" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Best time format to analyze duration of flow](/questions/57645/best-time-format-to-analyze-duration-of-flow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57645-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have to determine the duration of a flow of packets sent from the same IP source address (DDoS). My criteria is that the flow should be no less than 60 seconds. I am a bit confused about the different time formats available in tshark for display. What is the best time format to choose for this purpose, and how would the flow duration be determined. This is a sample of what I have so far, with the time in seconds. I can sort the time field and then subtract the last time minus the first time to obtain the flow duration. Is this a correct approach? Is there a command in tshark to do both tasks? Thank you for your help.</p><p><code>8950 1385856045.754978 94.102.63.238 TCP  9030 1385856046.165178 94.102.63.238 TCP  9042 1385856046.195650 94.102.63.238 TCP  9082 1385856046.348072 94.102.63.238 TCP  9093 1385856046.391306 94.102.63.238 TCP  9105 1385856046.441899 94.102.63.238 TCP  9129 1385856046.562191 94.102.63.238 TCP  9150 1385856046.681125 94.102.63.238 TCP  9171 1385856046.824253 94.102.63.238 TCP  9178 1385856046.850174 94.102.63.238 TCP  9198 1385856046.949589 94.102.63.238 TCP  9233 1385856047.107929 94.102.63.238 TCP  9234 1385856047.110825 94.102.63.238 TCP  9245 1385856047.181578 94.102.63.238 TCP  9269 1385856047.314578 94.102.63.238 TCP  9278 1385856047.341350 94.102.63.238 TCP</code></p></div><div id="question-tags" class="tags-container tags">duration ddos time flow format</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '16, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/b3f6579bb81c4e2875f9293da09b05c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MaryR&#39;s gravatar image" /><p>MaryR<br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MaryR has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '16, 08:43</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-57645" class="comments-container"></div><div id="comment-tools-57645" class="comment-tools"></div><div class="clear"></div><div id="comment-57645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57646"></span>

<div id="answer-container-57646" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57646-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sorting should normally not be necessary as the timestamps are monotonously growing, unless you use some reordering of the capture file.</p><p>I must say that as I observe your case from your other Questions, I'd pipe the textual output of tshark to a perl (or any other scripting language which can use associative arrays) script to deal with the task, and I would keep records of first timestamp, last timestamp and packet count for each source IP address, as you seem not to be interested in the actual contents.</p><p>As for the time format chosen (unix time in microseconds resolution), I'd probably use <code>frame.time_relative</code> because it has less significant digits so the float representation can be more precise as compared to unix time. But for your purpose it is not significant as a 1 second resolution seems to be sufficient.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '16, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-57646" class="comments-container"><span id="57650"></span><div id="comment-57650" class="comment"><div id="post-57650-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer Sindy. For some reason when I sorted the ip source address field, the time field turn out to be sorted also but only for some IP addresses. For example, for this IP address, time is not growing. I added the time field that you suggested to see the display. So basically, I could use either time format to calculate my time flow, right?</p><p>As for the script, would a bash script work? Sadly, I do not know Perl, neither bash script for that matter, but it seems to me that it would be easier to learn how to write a bash script.</p><p>So what I am trying to accomplish cannot be done by just CL advanced commands? Thanks so much for responding.</p><pre><code>        27.913075000    1385856027.924645   92.42.38.238,149.67.116.32  ICMP
8107    41.576163000    1385856041.587733   92.42.38.238,149.67.116.64  ICMP
2478    13.732778000    1385856013.744348   92.42.38.238,149.67.118.57  ICMP
822     4.681965000     1385856004.693535   92.42.38.238,149.67.137.127 ICMP
1592    8.926652000     1385856008.938222   92.42.38.238,149.67.139.8   ICMP
757     4.352003000     1385856004.363573   92.42.38.238,149.67.14.21   ICMP
899     5.162769000     1385856005.174339   92.42.38.238,149.67.141.21  ICMP
7106    36.355340000    1385856036.366910   92.42.38.238,149.67.154.103</code></pre><p>`</p></div><div id="comment-57650-info" class="comment-info"><span class="comment-age">(26 Nov '16, 12:09)</span> MaryR</div></div><span id="57654"></span><div id="comment-57654" class="comment"><div id="post-57654-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So what I am trying to accomplish cannot be done by just CL advanced commands?</p></blockquote><p>You can use statistic functions of tshark (from the <code>-z</code> universe) but that won't provide all you want for more than a single IP address, so you'd have to use multiple passes - first to identify the list of IP addresses which are worth deeper investigation, and then to make an individual statistics for each of them.</p><p>By piping a tshark output to a tailor-made script, you can get your result in a single pass. Bash scripts <a href="http://www.tldp.org/LDP/abs/html/arrays.html">do support arrays</a> but the index must be an integer number; what makes the mission possible is that not all array elements must be initialized. So for IPv4 addresses, you can convert the IP address to a 32-bit integer (which it actually is) and then use it as an index to the three arrays (count, first_ts, last_ts). For IPv6 addresses, I'm not sure whether your bash will understand 128-bit integers, while in perl you would simply use string forms of the IP addresses as index values.</p><blockquote><p>For some reason when I sorted the ip source address field, the time field turn out to be sorted also but only for some IP addresses.</p></blockquote><p>I would have to see the complete CLI command which has caused that. If you take a real capture file and let tshark print some fields of the frames, they will be printed in the order in which they have been captured.</p></div><div id="comment-57654-info" class="comment-info"><span class="comment-age">(26 Nov '16, 13:26)</span> sindy</div></div></div><div id="comment-tools-57646" class="comment-tools"></div><div class="clear"></div><div id="comment-57646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

