+++
type = "question"
title = "calling another dissector"
description = '''hey, I am writing a dissector for netscaler core to core messages. Now this protocol works on top of the Net Scaler Trace layer(nstrace), which is introduced by the netscaler for debugging purposes.  So when I am writing the dissector for core to core, I want to be able to call (nstrace) after that....'''
date = "2011-02-14T20:26:00Z"
lastmod = "2012-11-28T05:58:00Z"
weight = 2334
keywords = [ "dissector" ]
aliases = [ "/questions/2334" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [calling another dissector](/questions/2334/calling-another-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2334-score" class="post-score" title="current number of votes">0</div><span id="post-2334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>hey,</p><p>I am writing a dissector for netscaler core to core messages. Now this protocol works on top of the Net Scaler Trace layer(nstrace), which is introduced by the netscaler for debugging purposes.</p><p>So when I am writing the dissector for core to core, I want to be able to call (nstrace) after that. So how should I code for that??</p><p>PLEASE HELP, ANYONE??</p><p>Thanks,</p><p>Sid</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '11, 20:26</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p><span>sid</span><br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-2334" class="comments-container"></div><div id="comment-tools-2334" class="comment-tools"></div><div class="clear"></div><div id="comment-2334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2335"></span>

<div id="answer-container-2335" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2335-score" class="post-score" title="current number of votes">1</div><span id="post-2335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Simple enough:</p><p>To call dissector "foo":</p><ol><li>Define a global variable</li></ol><p><code>static dissector_handle_t foo_handle;</code><br />
</p><ol><li><p>In your <code>proto_reg_handoff()</code> fcn:</p><p><code>foo_handle = find_dissector("foo");</code></p></li><li><p>To actually call the dissector:</p><p><code>foo_tvb = tvb_new_subset(tvb, offset, length, reported_length);</code></p><p><code>call_dissector(foo_handle, foo_tvb, pinfo, subtree);</code></p></li></ol><p>Look at any one of the many dissectors which use <code>call_dissector()</code> for examples.</p><p>In fact, if you look at packet-nstrace.c you'll see that it calls the <code>"eth_withoutfcs"</code> dissector.</p><hr /><p>Oops:</p><p>Actually: the above won't work. - nstrace isn't a "public" (registered dissector) (so it's not available to be found by <code>find_dissector</code>).</p><ul><li>From the code, it looks like nstrace is expected to be and is processed as a thin outer layer which encapsulates ethernet.</li></ul><p>So: I'm puzzled when you say the core-to-core protocol runs "on top of" nstrace.</p><p>What is the actual sequence of protocols in a frame ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '11, 22:06</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Feb '11, 22:26</strong> </span></p></div></div><div id="comments-container-2335" class="comments-container"><span id="2338"></span><div id="comment-2338" class="comment"><div id="post-2338-score" class="comment-score"></div><div class="comment-text"><p>Yes, I was mistaken. I am just told that core to core does not work on top of the nstrace.</p><p>So core to core too is expected to be processed as a thin layer outer layer i guess. I am waiting for a sound word about core to core. Meanwhile tell me one thing. core to core definitely does not work on top of nstrace. But it can not work independently right? It has to work on top of some protocol. Ethernet or anyone??</p><p>Is that right?? Can a dissector be written which does not work on top of any protocol?? Can core to core be something like that??</p></div><div id="comment-2338-info" class="comment-info"><span class="comment-age">(15 Feb '11, 00:37)</span> <span class="comment-user userinfo">sid</span></div></div><span id="2347"></span><div id="comment-2347" class="comment"><div id="post-2347-score" class="comment-score"></div><div class="comment-text"><p>Please see my comment in <a href="http://ask.wireshark.org/questions/2341/dissector-for-core-to-core-messages-ie-shared-memory-messages">your other question</a>.</p></div><div id="comment-2347-info" class="comment-info"><span class="comment-age">(15 Feb '11, 07:42)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="4198"></span><div id="comment-4198" class="comment"><div id="post-4198-score" class="comment-score"></div><div class="comment-text"><p>I am trying to do the same thing, however can you elaborate on how a dissector gets to become public. I have two dissectors I have written both work individually but when I try to call one from the other the find_dissector call returns NULL.</p></div><div id="comment-4198-info" class="comment-info"><span class="comment-age">(24 May '11, 08:14)</span> <span class="comment-user userinfo">spotthemaniac</span></div></div><span id="16384"></span><div id="comment-16384" class="comment"><div id="post-16384-score" class="comment-score"></div><div class="comment-text"><p>For the record (much after the fact):</p><p>Use:</p><pre><code>register_dissector(...)   /* (see doc/README.developer for details) */</code></pre></div><div id="comment-16384-info" class="comment-info"><span class="comment-age">(28 Nov '12, 05:58)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-2335" class="comment-tools"></div><div class="clear"></div><div id="comment-2335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

