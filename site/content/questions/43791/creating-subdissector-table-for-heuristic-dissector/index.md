+++
type = "question"
title = "Creating subdissector table for Heuristic Dissector"
description = '''Hello, So I&#x27;m developing a tool right now that creates dissectors based on xml input. I have it working so that all the dissectors created(40+ as of now) are added simply as heuristic dissectors. The way I want it to work is that I have one Heuristic Dissector that determines if it is one of these m...'''
date = "2015-07-01T09:07:00Z"
lastmod = "2015-07-01T10:59:00Z"
weight = 43791
keywords = [ "dissectortable", "heuristic", "plugin", "subdissector", "wireshark" ]
aliases = [ "/questions/43791" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Creating subdissector table for Heuristic Dissector](/questions/43791/creating-subdissector-table-for-heuristic-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43791-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>So I'm developing a tool right now that creates dissectors based on xml input. I have it working so that all the dissectors created(40+ as of now) are added simply as heuristic dissectors. The way I want it to work is that I have one Heuristic Dissector that determines if it is one of these messages, and then try all the heuristic sub-dissectors in its table if it is.</p><p>I tried implementing this but couldn't find much documentation on it. What I have now crashes whenever it receives one of the messages I want it to dissect.</p><p>Heres where I register the subdissector list:</p><pre><code>void
    proto_reg_handoff_srcmsg(void) {
    srcmsg_handle = new_create_dissector_handle(dissect_heur_srcmsg, proto_srcmsg);

    /* register as a dissector for udp packets */
    heur_dissector_add(&quot;udp&quot;, dissect_heur_srcmsg, proto_srcmsg);

    register_heur_dissector_list(&quot;srcmsg&quot;, &amp;sub_dissectors);
}</code></pre><p>And here is where I call the subdissector, at the bottom of dissect_heur_srcmsg:</p><pre><code>    dissector_try_heuristic(sub_dissectors, tvb, pinfo, tree, NULL, NULL);

    return TRUE;
}</code></pre><p>Here is where the other dissectors register as subdissectors:</p><pre><code>void
proto_reg_handoff_srcmsg(void)
{
    srcmsg_handle = new_create_dissector_handle(dissect_heur_srcmsg, proto_srcmsg);

    heur_dissector_add(&quot;srcmsg&quot;, dissect_heur_srcmsg, proto_srcmsg);
}</code></pre><p>The reason I want to do this is so I can filter for all these messages, in addition to filtering for them specifically. Please let me know if there is a simpler way to accomplish this (there probably is).</p><p>Also, when I open the Dissector Tables window and look at Heuristic Dissectors, my protocol shows up, but without any subdissectors registered to it. If anyone has any tips on what I should change, or a better approach, please let me know.</p></div><div id="question-tags" class="tags-container tags">dissectortable heuristic plugin subdissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '15, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/059a334676449782e9d927f2f79351fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="broccollirob&#39;s gravatar image" /><p>broccollirob<br />
<span class="score" title="75 reputation points">75</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="broccollirob has no accepted answers">0%</span></p></div></div><div id="comments-container-43791" class="comments-container"></div><div id="comment-tools-43791" class="comment-tools"></div><div class="clear"></div><div id="comment-43791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43795"></span>

<div id="answer-container-43795" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43795-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Move the line</p><pre><code>register_heur_dissector_list(&quot;srcmsg&quot;, &amp;sub_dissectors);</code></pre><p>from proto_reg_handoff_srcmsg() to proto_register_srcmsg() function: the heuristic table must be created before the call to the various handoff functions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '15, 10:59</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-43795" class="comments-container"><span id="43797"></span><div id="comment-43797" class="comment"><div id="post-43797-score" class="comment-score"></div><div class="comment-text"><p>Thank you, this helped a lot. Now the protocols are registering correctly, I can check the heuristic tables and see them all there.</p><p>I am, however, still crashing when I call dissector_try_heuristic(). I'm going to mess around with it for a bit, but if you any ideas about whats happening or why, let me know.</p></div><div id="comment-43797-info" class="comment-info"><span class="comment-age">(01 Jul '15, 11:34)</span> broccollirob</div></div><span id="43798"></span><div id="comment-43798" class="comment"><div id="post-43798-score" class="comment-score">1</div><div class="comment-text"><p>You cannot use a NULL pointer for the heur_dtbl_entry pointer. So your call should be:</p><p>dissector_try_heuristic(sub_dissectors, tvb, pinfo, tree, &amp;hdtbl_entry, NULL);</p><p>PS: please consider accepting the answer, this will be useful for other users in case they perform a search on the same subject as yours.</p></div><div id="comment-43798-info" class="comment-info"><span class="comment-age">(01 Jul '15, 12:03)</span> Pascal Quantin</div></div><span id="43799"></span><div id="comment-43799" class="comment"><div id="post-43799-score" class="comment-score"></div><div class="comment-text"><p>Perfect, that got it working</p></div><div id="comment-43799-info" class="comment-info"><span class="comment-age">(01 Jul '15, 12:15)</span> broccollirob</div></div></div><div id="comment-tools-43795" class="comment-tools"></div><div class="clear"></div><div id="comment-43795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

