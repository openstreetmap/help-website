+++
type = "question"
title = "tshark: extract rtp payload of the codec G.723"
description = '''In order to extract the RTP payload from a pcap file captured by wireshark, I&#x27;m using tshark with the command tshark -nr stream.pcap -R &#x27;rtp &amp;amp;&amp;amp; ip.dst==192.168.1.64&#x27; -T fields -e rtp.payload  this succeeded with the codecs g.729 and ilbc but with the codec g.723 it wasn&#x27;t the case. I think t...'''
date = "2013-09-01T10:27:00Z"
lastmod = "2013-09-02T02:44:00Z"
weight = 24268
keywords = [ "unix", "codec", "pcap", "tshark", "wireshark" ]
aliases = [ "/questions/24268" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: extract rtp payload of the codec G.723](/questions/24268/tshark-extract-rtp-payload-of-the-codec-g723)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24268-score" class="post-score" title="current number of votes">0</div><span id="post-24268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In order to extract the RTP payload from a pcap file captured by wireshark, I'm using tshark with the command</p><pre><code>tshark -nr stream.pcap -R &#39;rtp &amp;&amp; ip.dst==192.168.1.64&#39; -T fields -e rtp.payload</code></pre><p>this succeeded with the codecs g.729 and ilbc but with the codec g.723 it wasn't the case. I think that this problem is due to the fact that the field payload of the rtp protocol doesn't exist any more (when consulting the wireshark).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unix" rel="tag" title="see questions tagged &#39;unix&#39;">unix</span> <span class="post-tag tag-link-codec" rel="tag" title="see questions tagged &#39;codec&#39;">codec</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '13, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/50d6fd0a69c29833e828654aaa248e07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="basma&#39;s gravatar image" /><p><span>basma</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="basma has no accepted answers">0%</span></p></div></div><div id="comments-container-24268" class="comments-container"></div><div id="comment-tools-24268" class="comment-tools"></div><div class="clear"></div><div id="comment-24268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24277"></span>

<div id="answer-container-24277" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24277-score" class="post-score" title="current number of votes">0</div><span id="post-24277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>o solve this problem you have just to disable the protocol <strong>g723</strong> in wireshark in the item <strong>Enabled Protocols</strong> from the <strong>Analyze menu</strong> then the field "payload" will appear in the protocol rtp and the command</p><pre><code>tshark -nr stream.pcap -R &#39;rtp &amp;&amp; ip.dst==192.168.1.64&#39; -T fields -e rtp.payload</code></pre><p>will succeed!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '13, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/50d6fd0a69c29833e828654aaa248e07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="basma&#39;s gravatar image" /><p><span>basma</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="basma has no accepted answers">0%</span></p></div></div><div id="comments-container-24277" class="comments-container"></div><div id="comment-tools-24277" class="comment-tools"></div><div class="clear"></div><div id="comment-24277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

