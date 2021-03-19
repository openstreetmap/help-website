+++
type = "question"
title = "Find Delayed FIN packets in a large capture"
description = '''Im trying to track down an issue where sometimes a FIN arrives 3-6 seconds after an HTTP connection with a Connection:close header very intermittently. Is there any way to filter a caputure based on total TCP session time, or perhaps long Delta time of any two packets in a tcp stream?'''
date = "2017-02-25T08:57:00Z"
lastmod = "2017-02-27T01:42:00Z"
weight = 59682
keywords = [ "filter", "fin", "tcp" ]
aliases = [ "/questions/59682" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Find Delayed FIN packets in a large capture](/questions/59682/find-delayed-fin-packets-in-a-large-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59682-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im trying to track down an issue where sometimes a FIN arrives 3-6 seconds after an HTTP connection with a Connection:close header very intermittently. Is there any way to filter a caputure based on total TCP session time, or perhaps long Delta time of any two packets in a tcp stream?</p></div><div id="question-tags" class="tags-container tags">filter fin tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '17, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/41fbbf1b51272259a91502d2927a0100?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="psilent&#39;s gravatar image" /><p>psilent<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="psilent has no accepted answers">0%</span></p></div></div><div id="comments-container-59682" class="comments-container"></div><div id="comment-tools-59682" class="comment-tools"></div><div class="clear"></div><div id="comment-59682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59686"></span>

<div id="answer-container-59686" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59686-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can change the displayed time to delta between two displayed packets. Hint: Mark the two packets you want to compare and use the display filter frame.marked=true <img src="https://osqa-ask.wireshark.org/upfiles/2017-02-25_21-20-32.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '17, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></img></div></div><div id="comments-container-59686" class="comments-container"><span id="59687"></span><div id="comment-59687" class="comment"><div id="post-59687-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the response, but multiple tcp streams are occuring simultaneously. A display delta would show the next packet that arrived, not the next packet within the same tcp stream. I did find out how to do this though. Go to edit&gt;preferences&gt;protocol&gt;tcp and check the calculate conversation timestamps box. You can then use the tcp.time_delay filter to find the delays between packeta in the same stream.</p></div><div id="comment-59687-info" class="comment-info"><span class="comment-age">(25 Feb '17, 12:31)</span> psilent</div></div><span id="59688"></span><div id="comment-59688" class="comment"><div id="post-59688-score" class="comment-score"></div><div class="comment-text"><p>You are right! But your solution shows the delta between the first and the prev packet of a session. That is true. But the "Seconds since previous displayed packet" means the delta between the actually displayed frames. So it can be used for different kind of analysis and can also be used in a very variable way.</p><p>So if you mark two packets and use the display filter frame.marked=true it shows the delta between these packets.</p></div><div id="comment-59688-info" class="comment-info"><span class="comment-age">(25 Feb '17, 13:10)</span> Christian_R</div></div></div><div id="comment-tools-59686" class="comment-tools"></div><div class="clear"></div><div id="comment-59686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59701"></span>

<div id="answer-container-59701" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59701-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can enable "Calculate Conversation Timestamps" in the TCP protocol preferences. This will give you the two fields:</p><ul><li><strong>tcp.time_relative</strong>: Time since first frame in this TCP stream</li><li><strong>tcp.time_delta</strong>: Time since previous frame in this TCP stream</li></ul><p>You can then find (or filter) with "tcp.flags.fin==1 and tcp.time_delta&gt;=3 and tcp.time_delta&lt;=6". Of course it will not take into account whether or not there was a "Connection: close" header in the request, but since webserver timeouts are usually larger than 6 seconds (15 secs is seen often), you will get pretty close to what you try to accomplish.</p><p>If you want to make sure there was a "Connection: close" header first, you could either create a <a href="https://wiki.wireshark.org/Mate">MATE</a> script. Or use tshark with something like this:</p><pre><code>tshark -r &lt;file&gt; -Y &quot;tcp.flags.fin==1 and tcp.time_delta&gt;=3 and tcp.stream in {`
    tshark -r &lt;file&gt; -T fields -e tcp.stream -Y &quot;http.connection == close&quot; | 
        sort | uniq | awk &#39;{printf(&quot;%s &quot;,$1)}&#39;
    `}&quot;</code></pre><p>(I split up this one-liner into multiple lines to make it more readable, but please just copy it all to one line)</p><p>Which will first make a list of tcp stream numbers of all tcp streams that contain a "Connection: close" header and then combines that with the filter for the long tcp delay before the FIN packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '17, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-59701" class="comments-container"></div><div id="comment-tools-59701" class="comment-tools"></div><div class="clear"></div><div id="comment-59701-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

