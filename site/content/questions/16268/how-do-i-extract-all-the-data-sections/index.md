+++
type = "question"
title = "How do I extract all the &quot;data&quot; sections?"
description = '''I&#x27;m trying to analyse the protocol used to communicate with a device. The host computer just opens a connection to the device on port 9100, and leaves in open. It then communicates with the device very like a serial device (I suspect that the protocol is more or less unchanged from the old serial ve...'''
date = "2012-11-24T15:37:00Z"
lastmod = "2012-11-26T01:27:00Z"
weight = 16268
keywords = [ "serial", "analyze", "data" ]
aliases = [ "/questions/16268" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I extract all the "data" sections?](/questions/16268/how-do-i-extract-all-the-data-sections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16268-score" class="post-score" title="current number of votes">0</div><span id="post-16268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to analyse the protocol used to communicate with a device. The host computer just opens a connection to the device on port 9100, and leaves in open. It then communicates with the device very like a serial device (I suspect that the protocol is more or less unchanged from the old serial version of the device). To analyse the bytes sent and received, I need to capture them and ignore all the ethernet, tcp and ip "wrapping". I'd like to keep the timestamps if possible, because it's useful to see where the long breaks are (which usually mean the system was waiting for something external to happen).</p><p>How do I do this?</p><p>Thanks - Rowan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-serial" rel="tag" title="see questions tagged &#39;serial&#39;">serial</span> <span class="post-tag tag-link-analyze" rel="tag" title="see questions tagged &#39;analyze&#39;">analyze</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '12, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/fd3bc17dd17d9e0301f9329394be1539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rowan&#39;s gravatar image" /><p><span>Rowan</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rowan has no accepted answers">0%</span></p></div></div><div id="comments-container-16268" class="comments-container"></div><div id="comment-tools-16268" class="comment-tools"></div><div class="clear"></div><div id="comment-16268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16270"></span>

<div id="answer-container-16270" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16270-score" class="post-score" title="current number of votes">0</div><span id="post-16270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can try this:</p><blockquote><p><code>tshark -r input.cap -E separator=, -R "tcp.data" -T fields  -e frame.number -e frame.time -e ip.src -e ip.dst -e tcp.data</code><br />
</p></blockquote><p>It will output the hex representation of the tcp data plus some information about the frame. Instead of <code>-e frame.time</code> your can also use <code>-e frame.time_relative</code><br />
</p><p>If you need ASCII output, you can use <code>-e text</code> instead of <code>-e tcp.data</code><br />
</p><blockquote><p><code>tshark -r input.cap -E separator=, -R "tcp.data" -T fields  -e frame.number -e frame.time -e ip.src -e ip.dst -e text</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '12, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Nov '12, 02:44</strong> </span></p></div></div><div id="comments-container-16270" class="comments-container"><span id="16288"></span><div id="comment-16288" class="comment"><div id="post-16288-score" class="comment-score"></div><div class="comment-text"><p>Thanks. This looks just the job, but it doesn't seem to produce any output. Where does it write its output to? Do I have to add some more options to give it an output filename? I tried several (e.g. -w - or -F libpcap) without success. Here's my actual command: "C:\Program Files\Wireshark\tshark.exe" -r "C:\Users\rbradley.ADC\Documents\Customers\Dansk\DanskLogs121113\2201 overnight capture.pcap" -E separator=, -R "tcp.data" -T fields -e frame.number -e frame.time -e ip.src -e ip.dst -e text</p><p>Can I do the same thing using the GUI version?</p><p>Thanks - Rowan</p></div><div id="comment-16288-info" class="comment-info"><span class="comment-age">(25 Nov '12, 18:09)</span> <span class="comment-user userinfo">Rowan</span></div></div><span id="16296"></span><div id="comment-16296" class="comment"><div id="post-16296-score" class="comment-score"></div><div class="comment-text"><blockquote><p>This looks just the job, but it doesn't seem to produce any output.</p></blockquote><p>The above command works for tcp. If it does not output anything, your protocol might use UDP. Is that the case?</p></div><div id="comment-16296-info" class="comment-info"><span class="comment-age">(26 Nov '12, 01:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-16270" class="comment-tools"></div><div class="clear"></div><div id="comment-16270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16289"></span>

<div id="answer-container-16289" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16289-score" class="post-score" title="current number of votes">0</div><span id="post-16289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Could you just write a Wireshark dissector for the (serial) protocol that registers itself with "udp.port" with a value of 9100?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '12, 19:18</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-16289" class="comments-container"></div><div id="comment-tools-16289" class="comment-tools"></div><div class="clear"></div><div id="comment-16289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

