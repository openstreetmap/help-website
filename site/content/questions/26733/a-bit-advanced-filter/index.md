+++
type = "question"
title = "A bit advanced filter"
description = '''Hello, in the Wireshark filter I can display all packets destined to 10.0.0.1 address: ip.dst == 10.0.0.1 After that Wireshark will show a lot of packets with different IP source addresses. It is clear. But how can I display pakets with other IP destinations with exactly above IP sources (if there a...'''
date = "2013-11-07T14:49:00Z"
lastmod = "2013-11-07T18:08:00Z"
weight = 26733
keywords = [ "display-filter" ]
aliases = [ "/questions/26733" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [A bit advanced filter](/questions/26733/a-bit-advanced-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26733-score" class="post-score" title="current number of votes">0</div><span id="post-26733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, in the Wireshark filter I can display all packets destined to 10.0.0.1 address:</p><p>ip.dst == 10.0.0.1</p><p>After that Wireshark will show a lot of packets with different IP source addresses. It is clear.</p><p>But how can I display pakets with other IP destinations with exactly above IP sources (if there are)? I can check each IP source but it is long and time consuming process.</p><p>Simply: "display packets destined to 10.0.0.2, but only these having the same source addresses which we can find in another packets source addresses destined to 10.0.0.1"</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '13, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/28071bd7cf93e424c03dec9086ffa60f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net16&#39;s gravatar image" /><p><span>net16</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net16 has no accepted answers">0%</span></p></div></div><div id="comments-container-26733" class="comments-container"></div><div id="comment-tools-26733" class="comment-tools"></div><div class="clear"></div><div id="comment-26733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26735"></span>

<div id="answer-container-26735" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26735-score" class="post-score" title="current number of votes">1</div><span id="post-26735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="net16 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>so, you want to do this:</p><pre><code>100.100.100.100 -&gt; 10.0.0.1
200.200.200.200 -&gt; 10.0.0.1</code></pre><p>then create a filter that shows <strong>only</strong> frames from 100.100.100.100 and/or 200.200.200.200 to 10.0.0.2, like the marked frames below.</p><pre><code>100.100.100.100 -&gt; 10.0.0.2
1.2.3.4 -&gt; 10.0.0.2
10.1.1.1 -&gt; 10.0.0.2
200.200.200.200 -&gt; 10.0.0.2</code></pre><p>That is not possible with a simple display filter, as it would require a conditional filter, based on attributes of other frames.</p><p>What you can do:</p><p>Run tshark to find all source addresses. Then build a display filter with those list and apply that filter in Wireshark.</p><blockquote><p>Linux: <code>tshark -nr input.pcap -Y "ip.dst == 10.0.0.1" -T field -e ip.src | sort -u</code><br />
</p></blockquote><p>You will get the following list:</p><pre><code>100.100.100.100
200.200.200.200</code></pre><p>Now create the display filter</p><blockquote><p>(ip.addr eq 100.100.100.100 and ip.addr eq 10.0.0.2) or (ip.addr eq 200.200.200.200 and ip.addr eq 10.0.0.2)</p></blockquote><p>or</p><blockquote><p>ip.addr eq 10.0.0.2 and (ip.addr eq 100.100.100.100 or ip.addr eq 200.200.200.200)</p></blockquote><p>With a small script you should be able to automate this process.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '13, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Nov '13, 15:11</strong> </span></p></div></div><div id="comments-container-26735" class="comments-container"><span id="26744"></span><div id="comment-26744" class="comment"><div id="post-26744-score" class="comment-score"></div><div class="comment-text"><p>Kurt, thank you for your answer. I was doing exactly as you have written, but the IPs list I obtained by Conversation statistics manner (as Jasper wrote). I hoped that a conditional filter I can use by such manner. I have a quite a lot of similar problems and a conditional filter would be very useful. Regards.</p></div><div id="comment-26744-info" class="comment-info"><span class="comment-age">(07 Nov '13, 15:49)</span> <span class="comment-user userinfo">net16</span></div></div><span id="26746"></span><div id="comment-26746" class="comment"><div id="post-26746-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I have a quite a lot of similar problems and a conditional filter would be very useful.</p></blockquote><p>yes, but there is <strong>no conditional filter</strong></p><p>Your options are:</p><ul><li>file an enhancement bug at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> but don't expect too much, as that would be a rather though thing to implement</li><li>use tshark and some scripting to automate the process, as I have shown</li></ul></div><div id="comment-26746-info" class="comment-info"><span class="comment-age">(07 Nov '13, 15:54)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26754"></span><div id="comment-26754" class="comment"><div id="post-26754-score" class="comment-score"></div><div class="comment-text"><p>It is expectation rather than a bug ;) but perhaps I will try to report it. Thank you very much!</p></div><div id="comment-26754-info" class="comment-info"><span class="comment-age">(07 Nov '13, 16:55)</span> <span class="comment-user userinfo">net16</span></div></div><span id="26756"></span><div id="comment-26756" class="comment"><div id="post-26756-score" class="comment-score"></div><div class="comment-text"><p><strong>enhancement</strong> 'bug' ;-)</p></div><div id="comment-26756-info" class="comment-info"><span class="comment-age">(07 Nov '13, 17:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26735" class="comment-tools"></div><div class="clear"></div><div id="comment-26735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26734"></span>

<div id="answer-container-26734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26734-score" class="post-score" title="current number of votes">1</div><span id="post-26734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's what the conversation statistics is used for. Filter on either source or destination you want, and then use the conversation statistic with "Limit to display filter" checked. Go to the "IPv4" tab and you'll see all addresses the filtered address talks to. You can then either export that list, or filter from there on specific connections by using the popup menu.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '13, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-26734" class="comments-container"><span id="26742"></span><div id="comment-26742" class="comment"><div id="post-26742-score" class="comment-score"></div><div class="comment-text"><p>Jasper, thank you for your answer. I have tried Conversation statistics earlier, but I receive hundreds addresses destined to 10.0.0.1 on IPv4 list and it was not helpful. But what do you mean writing "filter from there on specific connections by using the popup menu"? I can only copy list of addresses and manually write filter rule as I was doing.</p></div><div id="comment-26742-info" class="comment-info"><span class="comment-age">(07 Nov '13, 15:39)</span> <span class="comment-user userinfo">net16</span></div></div><span id="26759"></span><div id="comment-26759" class="comment"><div id="post-26759-score" class="comment-score">1</div><div class="comment-text"><p>you can right click on any connection in the list in use the popup menu to filter on the connection. It will replace your existing display filter and modify your Conversation Statistics as well though.</p></div><div id="comment-26759-info" class="comment-info"><span class="comment-age">(07 Nov '13, 17:21)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="26763"></span><div id="comment-26763" class="comment"><div id="post-26763-score" class="comment-score"></div><div class="comment-text"><p>ok, thank you very much!</p></div><div id="comment-26763-info" class="comment-info"><span class="comment-age">(07 Nov '13, 18:08)</span> <span class="comment-user userinfo">net16</span></div></div></div><div id="comment-tools-26734" class="comment-tools"></div><div class="clear"></div><div id="comment-26734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

