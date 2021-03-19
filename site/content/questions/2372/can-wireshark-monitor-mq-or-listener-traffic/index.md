+++
type = "question"
title = "Can Wireshark monitor MQ or Listener traffic?"
description = '''Can I use wireshark to validate proper functionality of MQ and/or listener traffic?'''
date = "2011-02-16T08:34:00Z"
lastmod = "2013-02-12T12:24:00Z"
weight = 2372
keywords = [ "listener", "mq" ]
aliases = [ "/questions/2372" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark monitor MQ or Listener traffic?](/questions/2372/can-wireshark-monitor-mq-or-listener-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2372-score" class="post-score" title="current number of votes">0</div><span id="post-2372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I use wireshark to validate proper functionality of MQ and/or listener traffic?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-listener" rel="tag" title="see questions tagged &#39;listener&#39;">listener</span> <span class="post-tag tag-link-mq" rel="tag" title="see questions tagged &#39;mq&#39;">mq</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '11, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/3c48d340bc126489e19e1b9ea47e3c5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="soccernut&#39;s gravatar image" /><p><span>soccernut</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="soccernut has no accepted answers">0%</span></p></div></div><div id="comments-container-2372" class="comments-container"></div><div id="comment-tools-2372" class="comment-tools"></div><div class="clear"></div><div id="comment-2372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2378"></span>

<div id="answer-container-2378" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2378-score" class="post-score" title="current number of votes">0</div><span id="post-2378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By "MQ" do you you mean "Websphere MQ" ?</p><p>If so, Wireshark can monitor (capture) and dissect MQ traffic.</p><p>However, Wireshark just dissects the bits.</p><p>Altho a particular dissector may provide some diagnostic information (e.g., about what appear to be incorrect fields in a message), Wireshark in general certainly doesn't "validate proper functionality" of a protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '11, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Feb '11, 09:48</strong> </span></p></div></div><div id="comments-container-2378" class="comments-container"><span id="2410"></span><div id="comment-2410" class="comment"><div id="post-2410-score" class="comment-score"></div><div class="comment-text"><p>I.e., Wireshark can capture the traffic, and can dissect it and show you the details of the packets, so that <em>you</em> can look at those packets and see whether the programs sending the packets or replying to them are doing the right thing - Wireshark doesn't include a lot of functionality to check them itself. It also doesn't include any software to, for example, send test packets.</p></div><div id="comment-2410-info" class="comment-info"><span class="comment-age">(17 Feb '11, 21:52)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-2378" class="comment-tools"></div><div class="clear"></div><div id="comment-2378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9996"></span>

<div id="answer-container-9996" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9996-score" class="post-score" title="current number of votes">0</div><span id="post-9996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The WebSphere MQ protocol V6 is extensively supported in Wireshark. However, the MQ protocol V7 introduced new protocol features, implementing full-duplex instead of half-duplex channels. This adds 2 new magic headers, on top of the existing TSH header :<br />
- TSHC for common channel commands (heartbeat, quiesce stop, …).<br />
- TSHM for multiplexed sessions (for each MQHCONN).<br />
Wireshark does not support yet the new TSHC and TSHM headers : they will be displayed as "[Malformed packet]".</p><p>In the meanwhile, it is possible to use a backward compatible mode, which uses the V6 protocol. It can be configured 2 ways :<br />
- CLI (runmqsc) : configure the SHARECNV parameter to 0 on the server connection channel<br />
- GUI (MQ Explorer) : go to Channel -&gt; Extended -&gt; Sharing conversations and enter 0.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '12, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/e9af7a3a2f83d3eca906f48503fbb58a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metatech&#39;s gravatar image" /><p><span>metatech</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metatech has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Mar '13, 12:34</strong> </span></p></div></div><div id="comments-container-9996" class="comments-container"><span id="10007"></span><div id="comment-10007" class="comment"><div id="post-10007-score" class="comment-score"></div><div class="comment-text"><p>Anyone who would like to see the v7 protocol in Wireshark should check the <a href="https://bugs.wireshark.org/bugzilla/">Bugs</a> database for an existing entry and if there isn't one create a new entry, marking it as an Enhancement and including a reference to the protocol specification and if possible adding a sample capture.</p></div><div id="comment-10007-info" class="comment-info"><span class="comment-age">(07 Apr '12, 01:31)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="18566"></span><div id="comment-18566" class="comment"><div id="post-18566-score" class="comment-score"></div><div class="comment-text"><p>WebSphere MQ protocol v7 is now supported by Wireshark (see bug 8322). It is included in Wireshark 1.9.0 with a build number higher than 47641.</p></div><div id="comment-18566-info" class="comment-info"><span class="comment-age">(12 Feb '13, 12:24)</span> <span class="comment-user userinfo">metatech</span></div></div></div><div id="comment-tools-9996" class="comment-tools"></div><div class="clear"></div><div id="comment-9996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

