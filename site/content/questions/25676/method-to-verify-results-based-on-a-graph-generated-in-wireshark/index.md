+++
type = "question"
title = "Method to verify results based on a graph generated in wireshark"
description = '''I want to write a script where I need to verify the final result (pass/fail) based on a graph generated in wireshark.  Message rate is to be configured for e.g., 25000 and the same is to be verified from graphs. In wireshark, under &quot;Statistics&quot; menu, &quot;IO Graph&quot; is there. There I need to give differe...'''
date = "2013-10-06T10:49:00Z"
lastmod = "2013-10-07T07:57:00Z"
weight = 25676
keywords = [ "graph" ]
aliases = [ "/questions/25676" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Method to verify results based on a graph generated in wireshark](/questions/25676/method-to-verify-results-based-on-a-graph-generated-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25676-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to write a script where I need to verify the final result (pass/fail) based on a graph generated in wireshark.</p><ul><li>Message rate is to be configured for e.g., 25000 and the same is to be verified from graphs.</li><li>In wireshark, under "Statistics" menu, "IO Graph" is there. There I need to give different filters for "Graph 1", "Graph 2" and "Graph 3". Three graphs with different colors will be generated.</li><li>I need to verify that the rate is exactly same (here 25000) what was configured.</li></ul><p>Attaching reference screenshot :-</p><p><img src="https://osqa-ask.wireshark.org/upfiles/graph.jpg" alt="alt text" /></p><p>To write pcap before sending messages</p><p><strong>sudo /usr/sbin/tethereal -i eth2 -q -w Wm_FUN_010.pcap -R diameter</strong></p><p>To read pcap after message exchange is done</p><p><strong>sudo /usr/sbin/tethereal -r Wm_FUN_010.pcap -R "diameter.Auth-Request-Type == 2 &amp;&amp; diameter.cmd.code == 265 &amp;&amp; diameter.flags.request == 1"</strong></p><p>As of now, I know only Graph option to verify the rate, but I am looking for an automated script solution. Is there a way I can do this with Graph or any other method?</p><p>I searched for reference but couldn't get any information on this. It will be really helpful if someone can suggest a method or reference to achieve above requirement.</p><p>I tried following command which gives count based on time interval, but what I need is, count for a particular protocol message which is 6 for my case.</p><pre><code>-bash-3.2$ tshark -q -nr rad_fun_010.pcap -t ad -z io,stat,1,&quot;COUNT(frame.len)frame.len&quot;

===================================================================
IO Statistics
Interval: 1.000 secs
Column #0: COUNT(frame.len)frame.len
                |   Column #0
Time            |          COUNT
000.000-001.000                 2
001.000-002.000                 0
002.000-003.000                 9
003.000-004.000                 0
004.000-005.000                 0
005.000-006.000                 0
006.000-007.000                 0
007.000-008.000                 2
===============================================</code></pre><p>With "<strong>tshark io</strong>" related command, getting <strong>count</strong> might be possible, but couldn't get enough information on this. Can someone throw some light on how to achieve this?</p></div><div id="question-tags" class="tags-container tags">graph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '13, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/963f2abedc2aff60ceae201a8f231d42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="npatel&#39;s gravatar image" /><p>npatel<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="npatel has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 15 Sep '14, 22:38</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-25676" class="comments-container"></div><div id="comment-tools-25676" class="comment-tools"></div><div class="clear"></div><div id="comment-25676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25691"></span>

<div id="answer-container-25691" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25691-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use tshark's -z io,stat option. That command can take display filters as well to generate those types of stats as output which you can then return to the scripted process you're referring to.</p><p>Depending on the setup, another way is to use the 'tshark -T fields -e (display filter) -e (display filter)' command to print out columns that you want and pipe them into awk scripts (for example) to generate all the stats you want from them that way. diameter.resp_time would be one example value that you can make use of to calculate min/max/average Diameter response times.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '13, 21:56</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-25691" class="comments-container"><span id="25696"></span><div id="comment-25696" class="comment"><div id="post-25696-score" class="comment-score"></div><div class="comment-text"><p>@Quadratic, Thanks for your response. Will check and get back if there is any issue.</p></div><div id="comment-25696-info" class="comment-info"><span class="comment-age">(07 Oct '13, 00:26)</span> npatel</div></div></div><div id="comment-tools-25691" class="comment-tools"></div><div class="clear"></div><div id="comment-25691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25710"></span>

<div id="answer-container-25710" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25710-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Another option with tshark would be:</p><blockquote><p>tshark -r Wm_FUN_010.pcap -R "diameter.Auth-Request-Type == 2 &amp;&amp; diameter.cmd.code == 265 &amp;&amp; diameter.flags.request == 1" -T fields -e frame.time_relative -e frame.number -e ip.src -e ip.dst -E header=y -E separator=;</p></blockquote><p>or even</p><blockquote><p>tshark -r Wm_FUN_010.pcap -R "diameter.Auth-Request-Type == 2" -T fields -e frame.time_relative -e frame.number -e ip.src -e ip.dst -e diameter.cmd.code -E header=y -E separator=;</p></blockquote><p>Hint: You might need a more recent version of tshark than the tethereal you are currently using ;-)</p><p>Take the output of that command and feed it into a spreadsheet or a script and do the analysis yourself. You'll get the time, the frame number (if needed) and the IP addresses (to distinguish different conversations). With that information you can easily calculate the 'message rate'.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '13, 01:54</p></div></div><div id="comments-container-25710" class="comments-container"><span id="25788"></span><div id="comment-25788" class="comment"><div id="post-25788-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I tried following command which gives count based on time interval, but what I need is, count for a particular protocol message which is 6 for my case.</p></blockquote><p>Did you try my tshark command?</p></div><div id="comment-25788-info" class="comment-info"><span class="comment-age">(09 Oct '13, 01:53)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25710" class="comment-tools"></div><div class="clear"></div><div id="comment-25710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

