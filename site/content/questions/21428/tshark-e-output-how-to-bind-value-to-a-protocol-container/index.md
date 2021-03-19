+++
type = "question"
title = "tshark -e output - how to bind value to a protocol container?"
description = '''Hello, I&#x27;m using tshark to decode a protocol where I want to map the values of one attribute to the values of another by using the -T fields option and a -e flag for both attributes. The problem I have is that a single IP packet in this case can have multiple instances of this same protocol in the s...'''
date = "2013-05-23T21:00:00Z"
lastmod = "2016-07-11T02:22:00Z"
weight = 21428
keywords = [ "fields", "tshark" ]
aliases = [ "/questions/21428" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tshark -e output - how to bind value to a protocol container?](/questions/21428/tshark-e-output-how-to-bind-value-to-a-protocol-container)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21428-score" class="post-score" title="current number of votes">0</div><span id="post-21428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm using tshark to decode a protocol where I want to map the values of one attribute to the values of another by using the <code>-T fields</code> option and a <code>-e</code> flag for both attributes. The problem I have is that a single IP packet in this case can have multiple instances of this same protocol in the stack, and one of those two attributes doesn't have to be present in both messages in the single packet, so the output I get for some packets will be:</p><p><code>a,a b</code></p><p>My problem is that tshark's output seems to have no way to clarify if the first "a" attribute was in the same protocol container as b, or if it was the second "a" in the same protocol container as b.</p><p>The only solution I've been able to come up with so far for this is to use the pdml output option instead of -T fields, output the file and use XML parsing to map the protocol containers out. That got me out of a tight spot but it's extremely inefficient on resources and I'm thinking there's just got to be a better way. I'm not sure if I'd have to build a smarter script by experimenting with Lua or something but I'm hoping as much as possible that tshark has some way to accomplish this more easily as I'm just looking for the container mappings.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '13, 21:00</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-21428" class="comments-container"></div><div id="comment-tools-21428" class="comment-tools"></div><div class="clear"></div><div id="comment-21428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21436"></span>

<div id="answer-container-21436" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21436-score" class="post-score" title="current number of votes">0</div><span id="post-21436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My problem is that tshark's output seems to have <strong>no way</strong> to clarify if the first "a" attribute was in the same protocol container as b,</p></blockquote><p>Please you use a different <strong>aggregator</strong> character.</p><blockquote><p><code>tshark -nr input.pcap -T fields -e flag -e flag -E aggregator=; -E separator=,</code><br />
</p></blockquote><p>The output should then look similar to this:</p><blockquote><p>a;;,a;b</p></blockquote><p>You will be able to parse that, due to the empty field (;;).</p><p>See <strong><code>tshark -E ?</code></strong> for more options.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '13, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 May '13, 02:08</strong> </span></p></div></div><div id="comments-container-21436" class="comments-container"><span id="21437"></span><div id="comment-21437" class="comment"><div id="post-21437-score" class="comment-score"></div><div class="comment-text"><p>Kurt, that would only help if both fields are always present (and sometimes be empty). However, if one of the fields not present in one of the containers, you will still get:</p><pre><code>a,a;b</code></pre><p>Please also take a look at my answer to <a href="http://ask.wireshark.org/questions/20974/tshark-tfields-identify-ssl-record-types-accurately">this question</a></p></div><div id="comment-21437-info" class="comment-info"><span class="comment-age">(24 May '13, 02:38)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="21444"></span><div id="comment-21444" class="comment"><div id="post-21444-score" class="comment-score"></div><div class="comment-text"><p>Ah ... right. If the field does not <strong>exist</strong> (instead of being <strong>empty</strong>), it won't work that way. Sorry, I don't have a solution for that case.</p><p>Probably what you suggested in the other question (MATE, Lua or PDML parsing?)...</p></div><div id="comment-21444-info" class="comment-info"><span class="comment-age">(24 May '13, 05:40)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="21476"></span><div id="comment-21476" class="comment"><div id="post-21476-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the comments, but yes I think the only solution here will be for me to bite the bullet and recompile Wireshark with Lua, learn Lua, and write something that will match up those containers.</p></div><div id="comment-21476-info" class="comment-info"><span class="comment-age">(25 May '13, 13:51)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="21506"></span><div id="comment-21506" class="comment"><div id="post-21506-score" class="comment-score"></div><div class="comment-text"><p>Can you post a sample capture file with a packet where all fields are present and then one packet where some fields are not there?</p></div><div id="comment-21506-info" class="comment-info"><span class="comment-age">(27 May '13, 23:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="21687"></span><div id="comment-21687" class="comment"><div id="post-21687-score" class="comment-score"></div><div class="comment-text"><p>Sorry Kurt but I cannot as those packets are sensitive.</p></div><div id="comment-21687-info" class="comment-info"><span class="comment-age">(31 May '13, 20:20)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="21951"></span><div id="comment-21951" class="comment not_top_scorer"><div id="post-21951-score" class="comment-score"></div><div class="comment-text"><p>Just an update I thought I'd leave on this one. I found a slightly better solution to PDML - I just used the -O output of the protocol containers as input into a perl script that took care of the mappings. It's not perfect but it's far more efficient than PDML as it's quite a bit less text to print and parse.</p></div><div id="comment-21951-info" class="comment-info"><span class="comment-age">(11 Jun '13, 21:23)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-21436" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-21436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53976"></span>

<div id="answer-container-53976" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53976-score" class="post-score" title="current number of votes">0</div><span id="post-53976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>We have had the same problem. As a short answer, you can't! Using -T Fields there is no way to do this. With -T PDML you can achieve your goal, but that is not efficient.</p><p>We have worked on a solution, which preserves the protocol tree. It creates separate entries in output for each set.</p><p>In the following photo, you can see an example. In first photo there are two SCTP Chunks on top of IP layer. There are cases where there are 4 Chunks on top of IP layer (second photo)</p><p>Photo1: <img src="https://osqa-ask.wireshark.org/upfiles/protocol-tree_RXEMg5z.png" alt="alt text" /></p><p>in these cases, our solution returns 2 (4 for second example) datasets, one for the blue set and one for the red set consisting of the values from all protocols (frame;eth;ip;sctp;m3ua;SCCP;TCAP;GSM-MAP; x 2).</p><p>We believe, this feature is needed more often but is not mentioned in the community; would really appreciate it if you could submit an enhancement request in the bugzilla-thingy and if this feature is accepted, we can then submit our solution easier, as it is now not a wildly popular request and we are afraid it would be rejected.</p><p>Photo2: <img src="https://osqa-ask.wireshark.org/upfiles/protocol-tree-2.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '16, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/52d600a0425fd5e6a7306e84605b027d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arashdalir&#39;s gravatar image" /><p><span>arashdalir</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arashdalir has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jul '16, 02:23</strong> </span></p></div></div><div id="comments-container-53976" class="comments-container"></div><div id="comment-tools-53976" class="comment-tools"></div><div class="clear"></div><div id="comment-53976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

