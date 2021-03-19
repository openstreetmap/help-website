+++
type = "question"
title = "invalid address:port pair"
description = '''I ran this script: file=man.pcap for stream in $(tshark -nlr $file -Y tcp.flags.syn==1 -T fields -e tcp.stream | sort -n | uniq) do  echo &quot;Processing stream $stream&quot;  tshark -nlr $file -qz &quot;follow,tcp,ascii,$stream&quot; &amp;gt; stream-$stream.log done  but I got this message for all streams: Processing str...'''
date = "2013-08-30T10:40:00Z"
lastmod = "2013-08-30T11:27:00Z"
weight = 24207
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/24207" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [invalid address:port pair](/questions/24207/invalid-addressport-pair)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24207-score" class="post-score" title="current number of votes">1</div><span id="post-24207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I ran this script:</p><pre><code>file=man.pcap
for stream in $(tshark -nlr $file -Y tcp.flags.syn==1 -T fields -e tcp.stream | sort -n | uniq)
do
  echo &quot;Processing stream $stream&quot;
  tshark -nlr $file -qz &quot;follow,tcp,ascii,$stream&quot; &gt; stream-$stream.log
done</code></pre><p>but I got this message for all streams:</p><pre><code>Processing stream 0 tshark: follow - Invalid address:port pair.

Processing stream 1 tshark: follow - Invalid address:port pair.

Processing stream 2 tshark: follow - Invalid address:port pair.</code></pre><p>. . .</p><p>what is the reason?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '13, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/372d4c266bc96a0ef9b71b291c582d2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Soroor&#39;s gravatar image" /><p><span>Soroor</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Soroor has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>30 Aug '13, 10:44</strong> </span></p></div></div><div id="comments-container-24207" class="comments-container"></div><div id="comment-tools-24207" class="comment-tools"></div><div class="clear"></div><div id="comment-24207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24210"></span>

<div id="answer-container-24210" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24210-score" class="post-score" title="current number of votes">2</div><span id="post-24210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Soroor has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><em>what is the reason?</em></p><p>There is a carriage return that needs to be removed. Try something like the following:</p><pre><code>file=man.pcap
for stream in $(tshark -nlr $file -Y tcp.flags.syn==1 -T fields -e tcp.stream | sort -n | uniq | sed &#39;s/\r//&#39;)
do
    echo &quot;Processing stream $stream&quot;
    tshark -nlr $file -qz &quot;follow,tcp,ascii,$stream&quot; &gt; stream-$stream.log
done</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '13, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24210" class="comments-container"></div><div id="comment-tools-24210" class="comment-tools"></div><div class="clear"></div><div id="comment-24210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

