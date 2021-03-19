+++
type = "question"
title = "How to filter out streams that contain multiple SYN packets"
description = '''I am troubleshooting communication problems that my micro web server is encountering. I may have found a clue to the problem that I mention in this post. To cut to the chase, I&#x27;m looking for a way to search/filter my Wireshark capture where I can quickly find ALL streams that contain more than one S...'''
date = "2013-01-21T15:47:00Z"
lastmod = "2013-01-21T22:18:00Z"
weight = 17833
keywords = [ "filter", "stream", "wireshark" ]
aliases = [ "/questions/17833" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter out streams that contain multiple SYN packets](/questions/17833/how-to-filter-out-streams-that-contain-multiple-syn-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17833-score" class="post-score" title="current number of votes">0</div><span id="post-17833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am troubleshooting communication problems that my micro web server is encountering.</p><p>I may have found a clue to the problem that I mention in <a href="http://ask.wireshark.org/questions/17831/what-can-cause-multiple-syn-packets-in-same-stream">this post</a>.</p><p>To cut to the chase, I'm looking for a way to search/filter my Wireshark capture where I can quickly find ALL streams that contain more than one SYN request/packet.</p><p>For example:</p><p>Take a <a href="http://cloudshark.org/captures/feaad26b1a89">look at this stream</a> and notice how it contains two SYN requests. The way I was able to filter this out was by filtering out each stream one-by-one (tcp.stream eq 53 then tcp.stream eq 54, etc) until I found a stream that contained multiple SYN's. It would be nice if Wireshark had an easier way for me to track down the streams that meet the criteria (multiple SYN).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '13, 15:47</strong></p><img src="https://secure.gravatar.com/avatar/1259897b9b42059302967b55c0dc2228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KTM&#39;s gravatar image" /><p><span>KTM</span><br />
<span class="score" title="76 reputation points">76</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KTM has one accepted answer">100%</span></p></div></div><div id="comments-container-17833" class="comments-container"></div><div id="comment-tools-17833" class="comment-tools"></div><div class="clear"></div><div id="comment-17833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17836"></span>

<div id="answer-container-17836" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17836-score" class="post-score" title="current number of votes">4</div><span id="post-17836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="KTM has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you enable "Calculate Conversation Timestamps" in the TCP protocol preferences, you can use:</p><pre><code>tcp.flags==2 and tcp.time_relative&gt;0</code></pre><p>This would show all SYN packets which were not the first packet in the TCP session.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '13, 16:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17836" class="comments-container"><span id="17838"></span><div id="comment-17838" class="comment"><div id="post-17838-score" class="comment-score"></div><div class="comment-text"><p>Good one, didn't think of that - or maybe I just gave up too soon :-)</p></div><div id="comment-17838-info" class="comment-info"><span class="comment-age">(21 Jan '13, 16:16)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="17840"></span><div id="comment-17840" class="comment not_top_scorer"><div id="post-17840-score" class="comment-score"></div><div class="comment-text"><p>Well, I have to admit it was inspired by your answer (we should work together more often :-))</p></div><div id="comment-17840-info" class="comment-info"><span class="comment-age">(21 Jan '13, 16:20)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="17841"></span><div id="comment-17841" class="comment not_top_scorer"><div id="post-17841-score" class="comment-score"></div><div class="comment-text"><p>For noobs like myself - You enable "Calculate Conversation Timestamps" by going to "Edit -&gt; Preferences -&gt; Protocols -&gt; TCP -&gt; Calculate conversation timestamps"</p></div><div id="comment-17841-info" class="comment-info"><span class="comment-age">(21 Jan '13, 16:32)</span> <span class="comment-user userinfo">KTM</span></div></div><span id="17842"></span><div id="comment-17842" class="comment"><div id="post-17842-score" class="comment-score">1</div><div class="comment-text"><p>That...</p><p>... or rightclick on the TCP line in the packet detail pane and select "Protocol Preferences" and then select "Calculate Conversation Timestamps"</p><p>:-)</p></div><div id="comment-17842-info" class="comment-info"><span class="comment-age">(21 Jan '13, 16:38)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="17843"></span><div id="comment-17843" class="comment not_top_scorer"><div id="post-17843-score" class="comment-score"></div><div class="comment-text"><p><span>@Syn-bit</span> - Can you explain what tcp.time_relative does?</p><p>I've searched around for an answer to no avail.</p></div><div id="comment-17843-info" class="comment-info"><span class="comment-age">(21 Jan '13, 16:39)</span> <span class="comment-user userinfo">KTM</span></div></div><span id="17844"></span><div id="comment-17844" class="comment"><div id="post-17844-score" class="comment-score">1</div><div class="comment-text"><ul><li>tcp.time_relative is the time of the packet relative to the first packet in the TCP session (tcp.stream)</li><li>tcp.time_delta is the time of the packet relative to the previous packet in the TCP session (tcp.stream)</li></ul></div><div id="comment-17844-info" class="comment-info"><span class="comment-age">(21 Jan '13, 17:11)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="17845"></span><div id="comment-17845" class="comment"><div id="post-17845-score" class="comment-score">1</div><div class="comment-text"><p>if you enable conversation timestamps Wireshark will keep track of the time of each tcp packet relative to the other packets in the <strong>same</strong> flow, and you can filter on that.</p></div><div id="comment-17845-info" class="comment-info"><span class="comment-age">(21 Jan '13, 17:12)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="17848"></span><div id="comment-17848" class="comment"><div id="post-17848-score" class="comment-score">1</div><div class="comment-text"><p>Damn...here I thought I was being cute by filtering on tcp.flags==02 and using the Statistics conversation, TCP and using the "Limit to display filter" and sorting by relative time.<br />
</p><p>figures..Sake would figure out a command line equivalent that's much quicker and relevant. I'll add it to my arsenal for sure! :)</p></div><div id="comment-17848-info" class="comment-info"><span class="comment-age">(21 Jan '13, 22:18)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-17836" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-17836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17834"></span>

<div id="answer-container-17834" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17834-score" class="post-score" title="current number of votes">1</div><span id="post-17834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That kind of filtering is pretty hard to do, because you would need to filter on packet relations, which normally can't be done, unless in some special cases. What you'd need to do is filter on SYN packets and find those, that have a delta time from the previous frame of more than, lets say, 1 second. For this, a filter like <code>tcp.flags==0x02 and frame.time_delta &gt; 1.0</code> could help (a flag byte of 0x02 means "only the SYN flag is set").</p><p>Now for the "but": <strong>But</strong> this filter will <em>only</em> work if the SYN packets are right next to each other, without anything in between, or otherwise the time part of the filter will not work. Unfortunately I don't think there is a way (yet) to do time based filtering on "same flow" packets - I tried tcp.time_delta, but it didn't help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '13, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></p></div></div><div id="comments-container-17834" class="comments-container"></div><div id="comment-tools-17834" class="comment-tools"></div><div class="clear"></div><div id="comment-17834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

