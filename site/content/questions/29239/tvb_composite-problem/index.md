+++
type = "question"
title = "tvb_composite problem"
description = '''Hello, I have the following problem. My dissector needs to rebuild a new tvb. A better description would be, I need to cut out some data and send it to the next dissector. As Example.... 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 11 11 11 11 11 11...'''
date = "2014-01-28T07:45:00Z"
lastmod = "2014-02-04T08:29:00Z"
weight = 29239
keywords = [ "tvbuff_t", "subset", "tvb" ]
aliases = [ "/questions/29239" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tvb\_composite problem](/questions/29239/tvb_composite-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29239-score" class="post-score" title="current number of votes">0</div><span id="post-29239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have the following problem. My dissector needs to rebuild a new tvb. A better description would be, I need to cut out some data and send it to the next dissector.</p><p>As Example....</p><pre><code>02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02
02 02 02 02 02 02 02 02 02 02 02 02 02 02 02 02
11 11 11 11 11 11 22 22 22 22 22 22 33 33 44 44             I
10 01 00 00 00 aa c2 bc cd ef ed fe 15 18 1d d2
44 44 44 44 44 44 44 44 44 44 44 44 44 44 44 44            II
10 01 00 00 00 aa c2 bc cd ef ed fe 15 18 1d d3
....</code></pre><p>the first to lines are some other protocol data (my protocol) 11, 22 and 33 are the ethernet header 44 the ip header</p><p>what I now need to do is to cut out line I and II, reasamble it an send it to the next dissector (ethernet). I found the solution in building a composite buffer. The real code looks a little bit different but for the data above it would like this.</p><pre><code>tvbuff_t *new_tvb;
tvbuff_t *tvb_sub1;
tvbuff_t *tvb_sub2;

new_tvb = tvb_new_composite();

tvb_sub1 = tvb_new_subset(tvb, 32, 16, 16);
tvb_sub2 = tvb_new_subset(tvb, 64, 16, 16);

tvb_composite_append(new_tvb, tvb_sub1);
tvb_composite_append(new_tvb, tvb_sub2);

tvb_composite_finalize(new_tvb);

call_dissector(handle_eth, timing_tvb, pinfo, tree);</code></pre><p>The handle_eth is set with</p><pre><code>handle_eth = find_dissector(&quot;eth&quot;);</code></pre><p>No the problem.... With Ethernet everything is fine. Then the Ethernet dissector sends it to IP dies because of wrong data. When I look at the data IP gets I see that IP do not get the right data. It should be</p><pre><code>  44 44 44 44 44 44 44 44 44 .....</code></pre><p>but it is</p><pre><code> 44 10 01 00 00 00 aa c2 .....</code></pre><p>That shows me that the composite buffer is not working the right way. I found some old mailing lists entries (the newest was 2011) with composite buffer problems.</p><p>Do I miss something or they still problems with the composite buffer? Is there another way to do this that I missed?</p><p>Thanks Gatherer</p><p>EDIT1: fixed the code example after the first reply</p><p>EDIT2: I got it running today. But it's a little bit weared. I post the real code so I can discribe it better. First the code.</p><pre><code>  tvbuff_t *timing_tvb;
  timing_tvb = tvb_new_composite();

  // I need to calculate the amount of sub buffer I need
  // tvb size is calculated before
  tvbuff_t *tvb_sub[tvb_size/16/2];

  guint loopCounter;
  loopCounter = 0;
  while(tvb_size &gt; 0) {
     tvb_sub[loopCounter] = tvb_new_subset(tvb, payload_offset_save, 16, 32);
     tvb_size -= 32;
     tvb_composite_append(timing_tvb, tvb_sub[loopCounter]);
     // this output is just for testpurpose and shows me that I cut the right data
     proto_tree_add_item(tree_reportPayload, hf_proto_hsDebugProtocol_payload_data,          tvb_sub[loopCounter], 0, 16, ENC_BIG_ENDIAN);
     // check to see if I go trough the while loop right
     printf(&quot;loopCounter: %d\n&quot;, loopCounter);
     payload_offset_save += 32;
     loopCounter += 1;
  }
  tvb_composite_finalize(timing_tvb);
  // this line had a testpurpose too but here comes the weired part, I explaine this later
  // this is my &quot;special line&quot;
  proto_tree_add_item(tree_reportPayload, hf_proto_type_payload_data, timing_tvb, 0, -1, ENC_BIG_ENDIAN);
  // call Ethernet
  call_dissector(data_handle_eth, timing_tvb, pinfo, tree);</code></pre><ol><li>When I use the code above it works. I get some strange side effects in column names (e.g. ASSERT erorrs are shown) but its ok. The only problem is that the highligting is completly wrong. The highlighting shows the right amount of bytes but its shown as no cutting happend. E.g. IP shows the right source and destination IP, Port and so on. It's not pretty but I could live with it.</li><li>Now the weared part. If I comment out my special line. The Ethernet dissector works fine and calls the IP dissector but then IP dies and throws ASSERT errors and stop dissecting on different. There are some funny things shown like IP Version: 12 but the data is right (4). Any Ideas?</li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tvbuff_t" rel="tag" title="see questions tagged &#39;tvbuff_t&#39;">tvbuff_t</span> <span class="post-tag tag-link-subset" rel="tag" title="see questions tagged &#39;subset&#39;">subset</span> <span class="post-tag tag-link-tvb" rel="tag" title="see questions tagged &#39;tvb&#39;">tvb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '14, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/9b1dc01f2575b09d0852f7a4245a0318?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gatherer&#39;s gravatar image" /><p><span>Gatherer</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gatherer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jan '14, 13:16</strong> </span></p></div></div><div id="comments-container-29239" class="comments-container"><span id="29434"></span><div id="comment-29434" class="comment"><div id="post-29434-score" class="comment-score"></div><div class="comment-text"><p>Just two quick notes: (I hadn't noticed your update).</p><ol><li>I've no idea if packet bytes highlighting works properly for composite tvb's. I'll have to test that.</li></ol><p>Update: Highlighting of the packet bytes based upon a composite buffer doesn't work (as you noted)in GTK Wireshark. Feel free to file a bug at bugs.wireshark.org. I should note that it's very unlikely that it will be fixed in GTK Wireshark since the dev Wireshark is now using QT as the GUI library. However, the bug report can serve as a reminder to check if the same problem exists in QT Wireshark.</p><ol><li>tvb_new_subset(tvb, payload_offset_save, 16, 32); The '32' as reported length may cause problems; I would try using '16'.</li></ol></div><div id="comment-29434-info" class="comment-info"><span class="comment-age">(04 Feb '14, 08:29)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-29239" class="comment-tools"></div><div class="clear"></div><div id="comment-29239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29240"></span>

<div id="answer-container-29240" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29240-score" class="post-score" title="current number of votes">1</div><span id="post-29240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gatherer has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li><p>I fixed various problems in tvb_composite quite some time back, so it should work (if it hasn't somehow got broken again).</p></li><li><p>The code you show won't fetch the "I" and "II" as shown. The offsets should be 32 and 64 (not 16 and 48). (I'm assuming that each row has should have 16 bytes, not the 14 bytes shown).</p></li></ol><p>(Possibly your example doesn't match your actual code).</p><p>That being said, you can obviously just create a new tvb and then copy portions of the existing tvb to the new tvb.</p><p>ISTR tvb_composite goes through some gyrations (and may actually create a tvb with the components) so it may be no worse to just copy the sections into a new tvb.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '14, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-29240" class="comments-container"><span id="29241"></span><div id="comment-29241" class="comment"><div id="post-29241-score" class="comment-score"></div><div class="comment-text"><p>with the length you are right ... should be 16 byte per line</p><p>with the offset you are right too .. thats the problem with writing simple example code .. ;)</p><p>what do you mean with copy the code into a new tvb . just with memcpy? Do you have a small example?</p></div><div id="comment-29241-info" class="comment-info"><span class="comment-age">(28 Jan '14, 08:25)</span> <span class="comment-user userinfo">Gatherer</span></div></div><span id="29242"></span><div id="comment-29242" class="comment"><div id="post-29242-score" class="comment-score"></div><div class="comment-text"><p>I use wireshark 1.10.3 ... i can switch to the latest stable if needed</p></div><div id="comment-29242-info" class="comment-info"><span class="comment-age">(28 Jan '14, 08:34)</span> <span class="comment-user userinfo">Gatherer</span></div></div><span id="29243"></span><div id="comment-29243" class="comment"><div id="post-29243-score" class="comment-score">1</div><div class="comment-text"><p>I take that back :) not quite so "obviously".</p><pre><code>buf = &lt;allocate memory for a buf&gt;
tvb_memcpy(tvb, ...);  // copy some data from existing tvb to buf
tvb_memcpy(tvb, ...);  // copy some data from existing tvb to buf

tvb_new = tvb_new_child_real_data(tvb, buf, ...)
tvb_set_free_cb(tvb_new,...) // callback to free buf
                            //  when tvb is free&#39;d</code></pre><p>See epan/tvbuff.h for details (especially for tvb_new_child_real_data)</p><p>(The above was done quickly so it may not be quite correct).</p></div><div id="comment-29243-info" class="comment-info"><span class="comment-age">(28 Jan '14, 08:59)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="29244"></span><div id="comment-29244" class="comment"><div id="post-29244-score" class="comment-score">1</div><div class="comment-text"><p>P.S: I just re-ran the tvbtest diagnostic and it shows no problems with composite buffers; I don't think there's a need to update 1.10.3</p></div><div id="comment-29244-info" class="comment-info"><span class="comment-age">(28 Jan '14, 09:02)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="29332"></span><div id="comment-29332" class="comment"><div id="post-29332-score" class="comment-score"></div><div class="comment-text"><p>I updated my comment</p></div><div id="comment-29332-info" class="comment-info"><span class="comment-age">(30 Jan '14, 13:16)</span> <span class="comment-user userinfo">Gatherer</span></div></div></div><div id="comment-tools-29240" class="comment-tools"></div><div class="clear"></div><div id="comment-29240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

