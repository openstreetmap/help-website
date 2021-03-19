+++
type = "question"
title = "How to export or display capture traffic in this format? - Ethernet II excluded"
description = '''4500 0028 596c 4000 8006 d127 0a3b 00a3 36ef  8e6f c12f 0050 1817 84d1 7a9b 5b14 5011 0fc69 bb90 000'''
date = "2013-05-19T11:25:00Z"
lastmod = "2013-05-19T15:20:00Z"
weight = 21265
keywords = [ "was", "makfoc" ]
aliases = [ "/questions/21265" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to export or display capture traffic in this format? - Ethernet II excluded](/questions/21265/how-to-export-or-display-capture-traffic-in-this-format-ethernet-ii-excluded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21265-score" class="post-score" title="current number of votes">0</div><span id="post-21265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>4500 0028 596c 4000 8006 d127 0a3b 00a3 36ef 8e6f c12f 0050 1817 84d1 7a9b 5b14 5011 0fc69 bb90 000</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-was" rel="tag" title="see questions tagged &#39;was&#39;">was</span> <span class="post-tag tag-link-makfoc" rel="tag" title="see questions tagged &#39;makfoc&#39;">makfoc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '13, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/a6986d561af67e19ce035f5def1f242d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OMara&#39;s gravatar image" /><p><span>OMara</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OMara has no accepted answers">0%</span></p></div></div><div id="comments-container-21265" class="comments-container"></div><div id="comment-tools-21265" class="comment-tools"></div><div class="clear"></div><div id="comment-21265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21270"></span>

<div id="answer-container-21270" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21270-score" class="post-score" title="current number of votes">1</div><span id="post-21270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, wireshark (with &gt;2million lines of code) is a bit overkill for that, why not use a simple perl script:</p><pre><code>#!/opt/local/bin/perl -w

use strict;
use Net::PcapUtils;
use NetPacket::Ethernet;

Net::PcapUtils::loop(\&amp;process_pkt, FILTER =&gt; &#39;ip proto 1&#39;);

sub process_pkt {
  my ($user_data,$hdr,$pkt)=@_;
  my $eth=NetPacket::Ethernet-&gt;decode($pkt);
  if($eth-&gt;{type} == 2048){
    printf &quot;%s\n&quot;, unpack(&quot;H*&quot;, $eth-&gt;{data});
  }
}</code></pre><p>which gives the following output (for a ping to 8.8.8.8):</p><pre><code>450000544f3d00004001599fc0a801150808080808006e73b68e00005199293100006d3008090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637
45280054000000003201b6b408080808c0a8011500007673b68e00005199293100006d3008090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637
45000054e97400004001bf67c0a801150808080808006e28b68e00015199293200006d7908090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637
45280054000000003201b6b408080808c0a8011500007628b68e00015199293200006d7908090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637</code></pre><p>I'll leave the proper filtering and layout enhancements as an exercise for the reader :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '13, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21270" class="comments-container"></div><div id="comment-tools-21270" class="comment-tools"></div><div class="clear"></div><div id="comment-21270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21266"></span>

<div id="answer-container-21266" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21266-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21266-score" class="post-score" title="current number of votes">0</div><span id="post-21266-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I guess by going to File -&gt; Export Packet Dissections -&gt; as Plain Text File. Then on the "Packet Format" pane uncheck everything except "Packet Bytes".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '13, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21266" class="comments-container"><span id="21268"></span><div id="comment-21268" class="comment"><div id="post-21268-score" class="comment-score"></div><div class="comment-text"><p>But that doesn't exclude Ethernet II. Thanks.</p></div><div id="comment-21268-info" class="comment-info"><span class="comment-age">(19 May '13, 11:45)</span> <span class="comment-user userinfo">OMara</span></div></div><span id="21269"></span><div id="comment-21269" class="comment"><div id="post-21269-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I thought "Ethernet excluded" meant that you removed it from your quote due to sanitization purposes. I guess if you want to export packets without the Ethernet header Wireshark will not help you unless you find a way to edit each frame by script after exporting it.</p><p>May I ask why you need to remove the ethernet header? Maybe there's another solution I can think of.</p></div><div id="comment-21269-info" class="comment-info"><span class="comment-age">(19 May '13, 11:48)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="21271"></span><div id="comment-21271" class="comment"><div id="post-21271-score" class="comment-score"></div><div class="comment-text"><p>For testing purposes. I can copy each frame and edit it but it is tedious. I appreciate your help.</p></div><div id="comment-21271-info" class="comment-info"><span class="comment-age">(19 May '13, 12:37)</span> <span class="comment-user userinfo">OMara</span></div></div><span id="21276"></span><div id="comment-21276" class="comment"><div id="post-21276-score" class="comment-score"></div><div class="comment-text"><p>The new export PDU functionality could be made to do that.</p></div><div id="comment-21276-info" class="comment-info"><span class="comment-age">(19 May '13, 15:20)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-21266" class="comment-tools"></div><div class="clear"></div><div id="comment-21266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

