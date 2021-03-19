+++
type = "question"
title = "tcpdump - capture packets"
description = '''When we use tcpdump, we see like the following at the end - is there any way to write only the packets captured to a file using the -w option (in this case save only 1310)? I want to do my analysis on the captured packets. I am using this command  &amp;gt; sudo tcpdump -vv -s0 -i enp0s8 tcp and port 520...'''
date = "2017-05-14T10:39:00Z"
lastmod = "2017-05-14T19:18:00Z"
weight = 61389
keywords = [ "packets", "tcpdump", "tcp", "wireshark" ]
aliases = [ "/questions/61389" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tcpdump - capture packets](/questions/61389/tcpdump-capture-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61389-score" class="post-score" title="current number of votes">0</div><span id="post-61389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When we use tcpdump, we see like the following at the end - is there any way to write only the packets captured to a file using the -w option (in this case save only 1310)? I want to do my analysis on the captured packets.</p><p>I am using this command</p><pre><code>&gt; sudo tcpdump -vv -s0 -i enp0s8 tcp and port 5201
1310 packets captured
133919 packets received by filter
132609 packets dropped by kernel</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '17, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p><span>armodes</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 May '17, 13:13</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-61389" class="comments-container"></div><div id="comment-tools-61389" class="comment-tools"></div><div class="clear"></div><div id="comment-61389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61390"></span>

<div id="answer-container-61390" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61390-score" class="post-score" title="current number of votes">0</div><span id="post-61390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="armodes has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That looks like your machine is simply too slow to write all packets to disk, or even get all of them from the network card into memory. You need a much much much faster capture machine :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '17, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61390" class="comments-container"><span id="61393"></span><div id="comment-61393" class="comment"><div id="post-61393-score" class="comment-score"></div><div class="comment-text"><p>OK, in that case i will change a machine.</p></div><div id="comment-61393-info" class="comment-info"><span class="comment-age">(14 May '17, 13:39)</span> <span class="comment-user userinfo">armodes</span></div></div><span id="61395"></span><div id="comment-61395" class="comment"><div id="post-61395-score" class="comment-score"></div><div class="comment-text"><p>Note also that, in that example, tcpdump ''isn't'' writing packets to disk; the <code>-w</code> flag isn't being used, and the standard output isn't being redirected to a file. (Presumably it ''did'' print all 1310 packets before printing the captured/received/dropped message.)</p><p>Furthermore, tcpdump is dissecting the packets (because it's being run without <code>-w</code>), and that takes additional CPU time - and you're not running it with <code>-n</code>, so it's also trying to look up the source and destination IP addresses for the packets and report them as domain names, which can slow things down further.</p></div><div id="comment-61395-info" class="comment-info"><span class="comment-age">(14 May '17, 19:18)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-61390" class="comment-tools"></div><div class="clear"></div><div id="comment-61390-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

