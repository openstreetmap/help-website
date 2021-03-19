+++
type = "question"
title = "tshark follow TCP stream upon condition"
description = '''I want to dump in a one-liner all TCP traffic of a stream after a specific condition. In other words, I want to do something like: tshark -i wlan0 -s 0 -z follow,tcp,raw,x x=tshark -i wlan0 -s 0 -Y &#x27;http.request.full_uri contains &quot;blah-blah&quot; and http.request.method == GET&#x27; -n -Tfields -e tcp.stream ...'''
date = "2016-01-16T17:41:00Z"
lastmod = "2016-01-19T10:21:00Z"
weight = 49283
keywords = [ "follow", "follow.tcp.stream", "tshark", "condition" ]
aliases = [ "/questions/49283" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tshark follow TCP stream upon condition](/questions/49283/tshark-follow-tcp-stream-upon-condition)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49283-score" class="post-score" title="current number of votes">0</div><span id="post-49283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to dump in a one-liner all TCP traffic of a stream after a specific condition. In other words, I want to do something like:</p><p>tshark -i wlan0 -s 0 -z follow,tcp,raw,x</p><p>x=<code>tshark -i wlan0 -s 0 -Y 'http.request.full_uri contains "blah-blah" and http.request.method == GET' -n -Tfields -e tcp.stream</code></p><p>How can I do that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow" rel="tag" title="see questions tagged &#39;follow&#39;">follow</span> <span class="post-tag tag-link-follow.tcp.stream" rel="tag" title="see questions tagged &#39;follow.tcp.stream&#39;">follow.tcp.stream</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-condition" rel="tag" title="see questions tagged &#39;condition&#39;">condition</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '16, 17:41</strong></p><img src="https://secure.gravatar.com/avatar/2260f8170710660b45f279c37a04f401?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gregoireg&#39;s gravatar image" /><p><span>gregoireg</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gregoireg has no accepted answers">0%</span></p></div></div><div id="comments-container-49283" class="comments-container"></div><div id="comment-tools-49283" class="comment-tools"></div><div class="clear"></div><div id="comment-49283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49371"></span>

<div id="answer-container-49371" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49371-score" class="post-score" title="current number of votes">0</div><span id="post-49371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gregoireg has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can do that with scripting, see my answer to a very similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/14811/follow-tcp-stream-with-tshark-still-can-not-in-batch-mode">https://ask.wireshark.org/questions/14811/follow-tcp-stream-with-tshark-still-can-not-in-batch-mode</a><br />
</p></blockquote><p><strong>HOWEVER</strong> you can do that only for a pcap file, and not on-the-fly while capturing on an interface (wlan0), for obvious reasons.</p><p>So, if you need/want on-the-fly TCP stream extraction, you can't use tshark. ngrep is probably the better tool then.</p><p>ngrep</p><blockquote><p><a href="http://ngrep.sourceforge.net/">http://ngrep.sourceforge.net/</a></p></blockquote><p>Example:</p><blockquote><p>ngrep -d wlan0 -O /var/tmp/http.pcap '/someurl' 'port 80 and (host 10.0.0.1 or net 1.2.3.0/24)'</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '16, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-49371" class="comments-container"><span id="49384"></span><div id="comment-49384" class="comment"><div id="post-49384-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer. I'm already doing that:</p><ol><li>tcpdump to get pcap</li><li>first tshark pass to get the tcp stream id upon my http.request condition</li><li>second tshark pass to extract the relevant stream as hex</li><li>conversion of the stream from hex to bin</li></ol><p>But I would like to do the same on-the-fly. How could I do that? I start to lose confidence that I can do it in a bash command. I can do 1. and 2. at the same time, as well as 3. and 4. but linking 2. and 3. doesn't seem possible. Am I right? Would my only hope be to have an app using libpcap to achieve my goal?</p></div><div id="comment-49384-info" class="comment-info"><span class="comment-age">(19 Jan '16, 09:02)</span> <span class="comment-user userinfo">gregoireg</span></div></div><span id="49386"></span><div id="comment-49386" class="comment"><div id="post-49386-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But I would like to do the same on-the-fly.</p></blockquote><p>It depends on your definition of <strong>on-the-fly</strong>.</p><p>If that is: <strong>Extract TCP streams while tshark is capturing on an interface</strong>, then you can't! As you said yourself, you need <strong>two passes</strong>, which is impossible while tshark is capturing!</p><p>If it means <strong>only one bash command line</strong>, then the solution is in the answer I posted first.</p><blockquote><p>for stream in <code>tshark -r follow_tcp.pcap -R "ip.addr eq 127.0.0.1 and tcp.port eq 5678" -T fields -e tcp.stream | sort -n -u</code>; do echo Stream: $stream; tshark -r follow_tcp.pcap -q -z follow,tcp,raw,$stream; done</p></blockquote></div><div id="comment-49386-info" class="comment-info"><span class="comment-age">(19 Jan '16, 10:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-49371" class="comment-tools"></div><div class="clear"></div><div id="comment-49371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

