+++
type = "question"
title = "My dissector is processing the first packet multiple times."
description = '''So I am reassembling fragments together into complete messages and I started to get a strange bug whenever I test my dissector on large pcap files. My dissector makes its initial pass though all the packets but when it makes its second pass it will randomly process the first packet again in the midd...'''
date = "2017-06-12T10:37:00Z"
lastmod = "2017-06-13T08:55:00Z"
weight = 61954
keywords = [ "reassembly", "fragmentation", "dissector", "reassemble", "dissection" ]
aliases = [ "/questions/61954" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [My dissector is processing the first packet multiple times.](/questions/61954/my-dissector-is-processing-the-first-packet-multiple-times)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61954-score" class="post-score" title="current number of votes">0</div><span id="post-61954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I am reassembling fragments together into complete messages and I started to get a strange bug whenever I test my dissector on large pcap files. My dissector makes its initial pass though all the packets but when it makes its second pass it will randomly process the first packet again in the middle of everything. It runs the first packet through the dissector in the middle of reassembling another message which throws off the reassembly of that message. Is it normal behavior for dissectors to do this?</p><p>Thank you, James</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-fragmentation" rel="tag" title="see questions tagged &#39;fragmentation&#39;">fragmentation</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-reassemble" rel="tag" title="see questions tagged &#39;reassemble&#39;">reassemble</span> <span class="post-tag tag-link-dissection" rel="tag" title="see questions tagged &#39;dissection&#39;">dissection</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '17, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/ec69e82648ca5a020df1522509212989?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jpetersen&#39;s gravatar image" /><p><span>jpetersen</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jpetersen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jun '17, 10:38</strong> </span></p></div></div><div id="comments-container-61954" class="comments-container"><span id="61956"></span><div id="comment-61956" class="comment"><div id="post-61956-score" class="comment-score"></div><div class="comment-text"><p>Hi,excuse me for this command.i have a question about reassembly in a dissector.can you take a look at my question,<a href="https://ask.wireshark.org/questions/61818/how-to-reassemble-fragments-in-a-dissector-by-fragment_add_seq_check-function.">https://ask.wireshark.org/questions/61818/how-to-reassemble-fragments-in-a-dissector-by-fragment_add_seq_check-function.</a> The function always return zero and dissector dosent Reassemble fragments.what is my problem</p></div><div id="comment-61956-info" class="comment-info"><span class="comment-age">(12 Jun '17, 11:52)</span> <span class="comment-user userinfo">hhw</span></div></div><span id="61957"></span><div id="comment-61957" class="comment"><div id="post-61957-score" class="comment-score">1</div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/28866/hhw">@hhw</a>, Please don't attempt to hijack other questions even if they do seem related.</p></div><div id="comment-61957-info" class="comment-info"><span class="comment-age">(12 Jun '17, 12:04)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-61954" class="comment-tools"></div><div class="clear"></div><div id="comment-61954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61961"></span>

<div id="answer-container-61961" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61961-score" class="post-score" title="current number of votes">0</div><span id="post-61961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's probably a relic of the UI. It may be redrawing your display which probably currently has frame 1 selected.</p><p>Note, however, that this isn't a bug--except possibly in your dissector. Your dissector needs to do any reassembly on the first pass (when <code>pinfo-&gt;fd-&gt;flags.visited</code> in 0).</p><p>(It also needs to be prepared to process the saved results of that reassembly in any order--the user may click on packets in any order thus causing redissection of (only) those selected packets.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '17, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-61961" class="comments-container"><span id="61964"></span><div id="comment-61964" class="comment"><div id="post-61964-score" class="comment-score">1</div><div class="comment-text"><p>Thank you JeffMorris for your reply, that makes a lot more sense now.</p><p>I see that I am not doing reassembly exactly correct, when I tried to put this (pseudocode):</p><p><code>if (pinfo-&gt;fd-&gt;flags.visited == 0)      reassemble();</code></p><p>it wouldn't return the reassembled_tvb but instead it just returned the tvb of the last packet. I believe that I can figure this one out on my own though unless you see that I am misunderstanding this.</p><p>However, to your last point, this is an issue I have been frustrated with about my dissector. After the initial pass through when a user is looking through the packets, it will only reassemble if the initial packet is selected first. I have been looking for a way to remedy this (suspecting that my code is not quite right..) Will reassembling it only in the first pass solve this? Or should I look into another option as well?</p><p>Thank you again</p></div><div id="comment-61964-info" class="comment-info"><span class="comment-age">(12 Jun '17, 15:35)</span> <span class="comment-user userinfo">jpetersen</span></div></div><span id="61988"></span><div id="comment-61988" class="comment"><div id="post-61988-score" class="comment-score"></div><div class="comment-text"><p>No problem - though now I worry I may have led you astray.</p><p>In fact Wireshark's reassembly routines (epan/reassemble.c) do check the <code>visited</code> flag for you--so if you're using them you actually don't need to check the flag yourself.</p><p>But, OTOH, if you're using them then they should "just work" even when frames are dissected (in the 2nd pass) out of order.</p><p>What reassembly API are you using?</p></div><div id="comment-61988-info" class="comment-info"><span class="comment-age">(13 Jun '17, 08:55)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-61961" class="comment-tools"></div><div class="clear"></div><div id="comment-61961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

