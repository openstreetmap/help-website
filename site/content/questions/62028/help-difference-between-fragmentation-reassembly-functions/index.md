+++
type = "question"
title = "[Help] difference between fragmentation reassembly functions"
description = '''Hi, i have a custom dissector is layered on top of UDP that splits up its own data stream.flag bytes that signals the presence of a multi-packet sequence and also the last packet, followed by an ID of the sequence and a packet sequence number. packet1:id=1,frag_number=0,more_frags=1 packet2:id=1,fra...'''
date = "2017-06-14T10:55:00Z"
lastmod = "2017-07-04T14:14:00Z"
weight = 62028
keywords = [ "reassembly", "fragmentation" ]
aliases = [ "/questions/62028" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[Help\] difference between fragmentation reassembly functions](/questions/62028/help-difference-between-fragmentation-reassembly-functions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62028-score" class="post-score" title="current number of votes">1</div><span id="post-62028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i have a custom dissector is layered on top of UDP that splits up its own data stream.flag bytes that signals the presence of a multi-packet sequence and also the last packet, followed by an ID of the sequence and a packet sequence number.</p><pre><code>packet1:id=1,frag_number=0,more_frags=1
packet2:id=1,frag_number=1,more_frags=1
packet3:id=1,frag_number=2,more_frags=0 (&lt;-- this should complete reassembly)
packet4:id=5,frag_number=11,more_frags=1
packet5:id=5,frag_number=12,more_frags=1
packet6:id=5,frag_number=13,more_frags=0 (&lt;-- this should complete reassembly)</code></pre><p>if I use <code>fragment_add_seq_check</code> function packets 1,2,3 reassembled correctly, but packets 4,5,6 aren't reassembled.</p><p>if i use <code>fragment_add_check</code> function packets 1,2,3 reassembled incorrectly and hf_msg_fragment_overlap fields is true, and packets 4,5,6 aren't reassembled.</p><p>what is my problem? please help me. thanks. my code is like in <a href="https://ask.wireshark.org/questions/61818/how-to-reassemble-fragments-in-a-dissector-by-fragment_add_seq_check-function">this question</a>.</p><p>the picture of result in the case of <code>fragment_add_check() function</code> is here <img src="https://osqa-ask.wireshark.org/upfiles/error_of_fragmentation.png" alt="output result" /></p><p>the picture of result in the case of <code>fragment_add_seq_check() function</code> is here <img src="https://osqa-ask.wireshark.org/upfiles/error_of_fragmentatione.png" alt="output2" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-fragmentation" rel="tag" title="see questions tagged &#39;fragmentation&#39;">fragmentation</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '17, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/0b6bdfea45d7093830a2a0638a758239?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hhw&#39;s gravatar image" /><p><span>hhw</span><br />
<span class="score" title="10 reputation points">10</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hhw has one accepted answer">100%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jul '17, 04:33</strong> </span></p></div></div><div id="comments-container-62028" class="comments-container"><span id="62043"></span><div id="comment-62043" class="comment"><div id="post-62043-score" class="comment-score">2</div><div class="comment-text"><p>Looking through <code>fragment_add_work()</code> it appears other interesting parameters for <code>fragment_add_check()</code> are:</p><ul><li>offset</li><li>frag_offset</li><li>frag_data_len</li></ul><p>Could you add the values of those for each packet (similar to the output in the question)?</p></div><div id="comment-62043-info" class="comment-info"><span class="comment-age">(15 Jun '17, 07:38)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="62047"></span><div id="comment-62047" class="comment"><div id="post-62047-score" class="comment-score">1</div><div class="comment-text"><p>in the case of using fragment_add_work(), how can i use frag_id in reassembling?</p></div><div id="comment-62047-info" class="comment-info"><span class="comment-age">(15 Jun '17, 10:33)</span> <span class="comment-user userinfo">hhw</span></div></div><span id="62052"></span><div id="comment-62052" class="comment"><div id="post-62052-score" class="comment-score">2</div><div class="comment-text"><p><code>fragment_add_work()</code> isn't an API you can use: it's the internal routine that does the work of <code>fragment_add()</code> and <code>fragment_add_check()</code>. But to debug your problem of course we need to figure out what that routine is doing with your fragments.</p></div><div id="comment-62052-info" class="comment-info"><span class="comment-age">(15 Jun '17, 12:55)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="62055"></span><div id="comment-62055" class="comment"><div id="post-62055-score" class="comment-score">1</div><div class="comment-text"><p>excuse me. i dont know how to ues fragment_add_work for adding of those for each packet. i upload my foo.pcap and my code. can you take a look at it. thank you very very much.</p><p>my pcak : <a href="https://ufile.io/cmxe1">https://ufile.io/cmxe1</a></p><p>my code :<a href="https://ufile.io/ic0er">https://ufile.io/ic0er</a></p></div><div id="comment-62055-info" class="comment-info"><span class="comment-age">(16 Jun '17, 03:12)</span> <span class="comment-user userinfo">hhw</span></div></div><span id="62489"></span><div id="comment-62489" class="comment"><div id="post-62489-score" class="comment-score">1</div><div class="comment-text"><p>You might want to join the Wireshark developer mailing list for this. I'm not sure how often Jeff and others are visiting this site.</p><p>The mailing lists are here: <a href="https://www.wireshark.org/lists/">https://www.wireshark.org/lists/</a></p></div><div id="comment-62489-info" class="comment-info"><span class="comment-age">(04 Jul '17, 04:58)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-62028" class="comment-tools"></div><div class="clear"></div><div id="comment-62028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62504"></span>

<div id="answer-container-62504" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62504-score" class="post-score" title="current number of votes">1</div><span id="post-62504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See my <a href="https://www.wireshark.org/lists/wireshark-dev/201707/msg00024.html">response on the wireshark-dev mailing list</a> explaining why the reassembly function is behaving as expected and what to change on your side.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '17, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></img></div></div><div id="comments-container-62504" class="comments-container"></div><div id="comment-tools-62504" class="comment-tools"></div><div class="clear"></div><div id="comment-62504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

