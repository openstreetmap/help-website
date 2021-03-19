+++
type = "question"
title = "How to filter TCP conversations without any error packet ?"
description = '''When investigating a large trace, it is easy to point an error packet filtering on tcp.analysis.flags and &quot;Follow TCP stream&quot; for some of them. Is there a way to get a summary of TCP Conversations for only TCP streams that contain no error packet ? I got the following idea but have no clue how to im...'''
date = "2015-10-30T05:02:00Z"
lastmod = "2015-11-02T04:32:00Z"
weight = 47087
keywords = [ "tcp.stream", "display-filter" ]
aliases = [ "/questions/47087" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter TCP conversations without any error packet ?](/questions/47087/how-to-filter-tcp-conversations-without-any-error-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47087-score" class="post-score" title="current number of votes">0</div><span id="post-47087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When investigating a large trace, it is easy to point an error packet filtering on <code>tcp.analysis.flags</code> and "Follow TCP stream" for some of them.</p><p>Is there a way to get a summary of TCP Conversations for only TCP streams that contain no error packet ?</p><p>I got the following idea but have no clue how to implement it:</p><ul><li>get the list of tcp.stream IDs for packets filtered on <code>tcp.analysis.flags</code></li><li>exclude all packets for that streams</li></ul></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp.stream" rel="tag" title="see questions tagged &#39;tcp.stream&#39;">tcp.stream</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '15, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/9baf701b5b4e92171f13b558514ceaef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ymartin&#39;s gravatar image" /><p><span>ymartin</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ymartin has no accepted answers">0%</span></p></div></div><div id="comments-container-47087" class="comments-container"></div><div id="comment-tools-47087" class="comment-tools"></div><div class="clear"></div><div id="comment-47087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47151"></span>

<div id="answer-container-47151" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47151-score" class="post-score" title="current number of votes">1</div><span id="post-47151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I got the following idea but have no clue how to implement it:</p></blockquote><p>Please take a look at the examples in the answers of the following questions.</p><blockquote><p><a href="https://ask.wireshark.org/questions/14811/follow-tcp-stream-with-tshark-still-can-not-in-batch-mode">https://ask.wireshark.org/questions/14811/follow-tcp-stream-with-tshark-still-can-not-in-batch-mode</a><br />
<a href="https://ask.wireshark.org/questions/4677/easy-way-to-save-tcp-streams">https://ask.wireshark.org/questions/4677/easy-way-to-save-tcp-streams</a><br />
</p></blockquote><p>Both examples wil work on Linux. You'll have to adapt it to your use case.</p><pre><code>for stream in `tshark -nr input.pcap -Y &quot;tcp.analysis.flags&quot; -T fields -e tcp.stream | sort -n | uniq`
do
    echo $stream
    tshark -r input.pcap -w stream-$stream.pcap -Y &quot;tcp.stream eq $stream&quot;
done</code></pre><p>Then merge all of the pcap files with <strong>mergecap</strong> and create the conversation statistics in Wireshark or tshark.</p><pre><code>tshark -nr merged.pcap -q -z conv,tcp &gt; output.txt</code></pre><p>You can also export the conversation stats in the loop</p><pre><code>for stream in `tshark -nr input.pcap -Y &quot;tcp.analysis.flags&quot; -T fields -e tcp.stream | sort -n | uniq`
do
    echo $stream
    tshark -nr input.pcap -Y &quot;tcp.stream eq $stream&quot; -q -z conv,tcp &gt;&gt; output.txt
done</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '15, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-47151" class="comments-container"></div><div id="comment-tools-47151" class="comment-tools"></div><div class="clear"></div><div id="comment-47151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47109"></span>

<div id="answer-container-47109" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47109-score" class="post-score" title="current number of votes">0</div><span id="post-47109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hm, you could just try to do it this way, using the standard Wireshark statistics functionality:</p><ol><li>filter for <code>not tcp.analysis.flags</code></li><li>open Statistics -&gt; Conversation</li><li>select "TCP"</li><li>check "Limit to display filter".</li></ol><p>You should end up with a list of all conversations that have no error packet (or, more exact, no packet that a TCP analysis was diagnosed for)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '15, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></p></div></div><div id="comments-container-47109" class="comments-container"><span id="47112"></span><div id="comment-47112" class="comment"><div id="post-47112-score" class="comment-score"></div><div class="comment-text"><p>Thought the same. But it hasn´t worked for me, at least in my try.<br />
Example: If I have a session where only one packet has the field <code>tcp.analysis.flags</code> (The other 100 have that field not) Then only this packet is not displayed in TCP conversation(with the limit to display...)<br />
At least in my try....</p><p>Now, I think this case, which I have described, could be solved with a small script.</p></div><div id="comment-47112-info" class="comment-info"><span class="comment-age">(31 Oct '15, 11:15)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="47135"></span><div id="comment-47135" class="comment"><div id="post-47135-score" class="comment-score"></div><div class="comment-text"><p>I agree. My two bullets idea would consist in almost two tshark commands invocation. Any proposal ?</p></div><div id="comment-47135-info" class="comment-info"><span class="comment-age">(01 Nov '15, 23:50)</span> <span class="comment-user userinfo">ymartin</span></div></div><span id="47137"></span><div id="comment-47137" class="comment"><div id="post-47137-score" class="comment-score"></div><div class="comment-text"><p>About what kind of OS do we talk?</p></div><div id="comment-47137-info" class="comment-info"><span class="comment-age">(02 Nov '15, 00:11)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-47109" class="comment-tools"></div><div class="clear"></div><div id="comment-47109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

