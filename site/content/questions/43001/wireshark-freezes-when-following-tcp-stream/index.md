+++
type = "question"
title = "Wireshark freezes when following tcp stream"
description = '''Hi NG, I trying to trace an iperf test with Wireshark v1.12.5 to see if we got issues on our network.  I started with a 10 seconds trace. After the 10 seconds I stopped the trace, looked for the senders/receivers communication and clicked &quot;follow tcp stream&quot;. Wireshark starts counting the packets wh...'''
date = "2015-06-09T02:30:00Z"
lastmod = "2015-06-09T03:29:00Z"
weight = 43001
keywords = [ "freez", "stream", "tcp" ]
aliases = [ "/questions/43001" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark freezes when following tcp stream](/questions/43001/wireshark-freezes-when-following-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43001-score" class="post-score" title="current number of votes">0</div><span id="post-43001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi NG,</p><p>I trying to trace an iperf test with Wireshark v1.12.5 to see if we got issues on our network.</p><p>I started with a 10 seconds trace. After the 10 seconds I stopped the trace, looked for the senders/receivers communication and clicked "follow tcp stream".</p><p>Wireshark starts counting the packets which are involved (128862 in my test) and then shows the list of packets. Once I want to scroll or click on any packet Wireshark freezes and will never return. I did a test and let Wireshark run for 15 minutes in this state to see if anything is happening but if keeps the freezed state.</p><p>To keep the Wireshark file small I limited the each packet to 128 bytes.</p><p>Any idea how I can get Wireshark to work?</p><p>Regards</p><p>Christian</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-freez" rel="tag" title="see questions tagged &#39;freez&#39;">freez</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '15, 02:30</strong></p><img src="https://secure.gravatar.com/avatar/3579dd1b852039ea5a4255c8548c9252?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JogDial&#39;s gravatar image" /><p><span>JogDial</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JogDial has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jun '15, 02:32</strong> </span></p></div></div><div id="comments-container-43001" class="comments-container"></div><div id="comment-tools-43001" class="comment-tools"></div><div class="clear"></div><div id="comment-43001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43002"></span>

<div id="answer-container-43002" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43002-score" class="post-score" title="current number of votes">1</div><span id="post-43002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like a processing issue to me. What I don't get is why you try to use "Follow TCP stream" if you cut the packets at 128 bytes anyway - following the TCP stream only makes sense if you want to take a look at the combined payload, and that's not relevant in your case if I understand your motivation correctly.</p><p>If you want to isolate a TCP connection, use the popup menu to filter on "Conversation Filter" -&gt; "TCP" instead. This avoids Wireshark trying to reassemble the payloads and should work every time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '15, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-43002" class="comments-container"><span id="43009"></span><div id="comment-43009" class="comment"><div id="post-43009-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>thanks for your fast reply.</p><p>2 observations:</p><p>1st: I guess you're right with your assumption. The conversation filter does work out fine for me.</p><p>2nd: I checked again at my Wireshark process I left behind an hour ago. It finally returned from freez state and displays the tcp stream I selected. I believe there was just too much data to reassemble in a quick manner.</p><p>Thanks again.</p><p>Christian</p></div><div id="comment-43009-info" class="comment-info"><span class="comment-age">(09 Jun '15, 03:09)</span> <span class="comment-user userinfo">JogDial</span></div></div><span id="43010"></span><div id="comment-43010" class="comment"><div id="post-43010-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-43010-info" class="comment-info"><span class="comment-age">(09 Jun '15, 03:29)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-43002" class="comment-tools"></div><div class="clear"></div><div id="comment-43002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

