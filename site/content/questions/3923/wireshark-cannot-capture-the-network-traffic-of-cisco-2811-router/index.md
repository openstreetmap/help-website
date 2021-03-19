+++
type = "question"
title = "Wireshark cannot capture the network traffic of Cisco 2811 router"
description = '''On Cisco 2811 router, I type the following configuration: config t ip traffic-export profile newprofile  interface Fa0/1  bidirectional  mac-address {the MAC address of the PC with Wireshark installed}  incoming sample one-in-every 2  outgoing sample one-in-every 2  exit interface Fa0/0  ip traffic-...'''
date = "2011-05-04T08:55:00Z"
lastmod = "2011-05-04T09:16:00Z"
weight = 3923
keywords = [ "cisco" ]
aliases = [ "/questions/3923" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark cannot capture the network traffic of Cisco 2811 router](/questions/3923/wireshark-cannot-capture-the-network-traffic-of-cisco-2811-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3923-score" class="post-score" title="current number of votes">0</div><span id="post-3923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>On Cisco 2811 router, I type the following configuration:</p><pre><code>config t
ip traffic-export profile newprofile
  interface Fa0/1
  bidirectional
  mac-address {the MAC address of the PC with Wireshark installed}
  incoming sample one-in-every 2
  outgoing sample one-in-every 2
  exit
interface Fa0/0
  ip traffic-export
  apply newprofile</code></pre><p>I open Wireshark on the PC and try to capture the network traffic of the 2811 router I type the IP of the 2811 router as the "Remote" host IP and click "OK" But Wireshark claim that the 2811 router reject the connection</p><p>What else can I do for Wireshark capture the network traffic of the 2811 router ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 May '11, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/5744eec38f21af3f8f3ca9663d7c519e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andresbag&#39;s gravatar image" /><p><span>andresbag</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andresbag has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 May '11, 09:13</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-3923" class="comments-container"></div><div id="comment-tools-3923" class="comment-tools"></div><div class="clear"></div><div id="comment-3923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3925"></span>

<div id="answer-container-3925" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3925-score" class="post-score" title="current number of votes">1</div><span id="post-3925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The ip traffic-export functionality of the cisco is not related to the remote capture functionality in Wireshark. For remote capture functionality, you will need a second system with WinPcap running and rpcapd running.</p><p>The cisco ip traffic-export will send a copy of the selected traffic to the configured mac-address. If that mac-address is of the Wireshark PC and the WIreshark PC is directly connected to the listed interface, then you should be able to see the copied traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '11, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3925" class="comments-container"></div><div id="comment-tools-3925" class="comment-tools"></div><div class="clear"></div><div id="comment-3925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

