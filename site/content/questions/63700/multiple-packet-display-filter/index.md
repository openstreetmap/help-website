+++
type = "question"
title = "Multiple Packet Display Filter"
description = '''Hello, I have a trace of ~103K packets. I am trying to create a display filter to find TCP streams containing 4 particular packets (FIN-ACK, ACK, FIN-ACK, ACK). Is this possible? I need to do the opposite and find the streams, out of the 900+ in this trace, that don&#x27;t have those 4 packets at the end...'''
date = "2017-10-05T05:25:00Z"
lastmod = "2017-10-06T06:31:00Z"
weight = 63700
keywords = [ "multiple", "stream", "display-filter" ]
aliases = [ "/questions/63700" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple Packet Display Filter](/questions/63700/multiple-packet-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63700-score" class="post-score" title="current number of votes">0</div><span id="post-63700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have a trace of ~103K packets. I am trying to create a display filter to find TCP streams containing 4 particular packets (FIN-ACK, ACK, FIN-ACK, ACK). Is this possible? I need to do the opposite and find the streams, out of the 900+ in this trace, that <strong>don't</strong> have those 4 packets at the end of the conversation.</p><p>Any direction, YouTube, or other resource to answer this question is appreciated.</p><p>Thanks and God bless, Genesius</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '17, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/1447b9a5dfe43c55a0852ab5af967ffa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="genesiusj&#39;s gravatar image" /><p><span>genesiusj</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="genesiusj has no accepted answers">0%</span></p></div></div><div id="comments-container-63700" class="comments-container"></div><div id="comment-tools-63700" class="comment-tools"></div><div class="clear"></div><div id="comment-63700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63701"></span>

<div id="answer-container-63701" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63701-score" class="post-score" title="current number of votes">0</div><span id="post-63701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not directly as display filters are used as a match against each frame as to whether it's displayed or not and so do not have the capability to match or aggregate across frames.</p><p>I would use command line scripting to generate a list of streams with a FIN-ACK and subtract that from the list of all streams resulting in a list of those streams without a FIN-ACK.</p><p>This seems to work for me using PowerShell:</p><pre><code>$opts = @(&quot;-rpath\to\capture&quot;, &quot;-Tfields&quot;, &quot;-etcp.stream&quot;)
$allstreams = path\to\tshark.exe $opts | Select-Object -Unique
$finstreams = path\to\tshark.exe $opts tcp.flags.fin == 1 | Select-Object -Unique
Compare-Object $allstreams $finstreams -PassThru</code></pre><p>The above script first sets some options, including the capture file to use, then runs tshark, firstly with no filter get all the tcp stream indexes, then with a filter for the FIN flag to get the streams with a FIN, then generates the differences between those two results.</p><p>Note that the above quick test regards any FIN as a stream to include so it will only give streams with no FIN at all. Extending it to give the exact result you need is left as an exercise for the reader.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '17, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Oct '17, 14:09</strong> </span></p></div></div><div id="comments-container-63701" class="comments-container"><span id="63702"></span><div id="comment-63702" class="comment"><div id="post-63702-score" class="comment-score"></div><div class="comment-text"><p>so why not just use "not tcp.flags.fin==1"? ;-)</p></div><div id="comment-63702-info" class="comment-info"><span class="comment-age">(05 Oct '17, 11:59)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="63703"></span><div id="comment-63703" class="comment"><div id="post-63703-score" class="comment-score"></div><div class="comment-text"><p>Using a filter of <code>not tcp.flags.fin==1</code> will give a list of all streams that have at least one packet that doesn't have a FIN, which will be pretty much all streams unless you've managed to capture only one packet from a stream that has FIN set.</p></div><div id="comment-63703-info" class="comment-info"><span class="comment-age">(05 Oct '17, 14:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="63705"></span><div id="comment-63705" class="comment"><div id="post-63705-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a> Maybe it would be a nice topic for a Sharkfest session: powershell &amp; tshark :)</p></div><div id="comment-63705-info" class="comment-info"><span class="comment-age">(05 Oct '17, 23:11)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="63706"></span><div id="comment-63706" class="comment"><div id="post-63706-score" class="comment-score"></div><div class="comment-text"><p>Indeed, see presentation 33 at <a href="https://sharkfesteurope.wireshark.org/agenda">SharkFest Europe</a>.</p><p><a href="https://ask.wireshark.org/users/16160/christian_r">@Christian_R</a>, you may redeem your beer token at Estoril :-)</p></div><div id="comment-63706-info" class="comment-info"><span class="comment-age">(06 Oct '17, 01:05)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="63707"></span><div id="comment-63707" class="comment"><div id="post-63707-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a> yes, you're right, typing comments like that on my cellphone while completely tired seems like a bad idea :-D</p></div><div id="comment-63707-info" class="comment-info"><span class="comment-age">(06 Oct '17, 06:31)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-63701" class="comment-tools"></div><div class="clear"></div><div id="comment-63701-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

