+++
type = "question"
title = "Get frame data and packet info from frame number?"
description = '''If I have the number of a frame, is it possible to then look up the actual frame/packet? I&#x27;m trying to make some enhancements to io_stat.c, and I&#x27;d like to show some information about the packet inside the graph window itself, when clicked on. The only context I have in that situation is the frame n...'''
date = "2011-07-02T01:10:00Z"
lastmod = "2011-07-04T02:08:00Z"
weight = 4891
keywords = [ "development", "frame" ]
aliases = [ "/questions/4891" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get frame data and packet info from frame number?](/questions/4891/get-frame-data-and-packet-info-from-frame-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4891-score" class="post-score" title="current number of votes">1</div><span id="post-4891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I have the number of a frame, is it possible to then look up the actual frame/packet?</p><p>I'm trying to make some enhancements to io_stat.c, and I'd like to show some information about the packet inside the graph window itself, when clicked on. The only context I have in that situation is the frame number.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '11, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/1e8ce1d540bf3e95d8b50c96a744124d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jackson%20Zhou&#39;s gravatar image" /><p><span>Jackson Zhou</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jackson Zhou has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>02 Jul '11, 02:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4891" class="comments-container"></div><div id="comment-tools-4891" class="comment-tools"></div><div class="clear"></div><div id="comment-4891-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4892"></span>

<div id="answer-container-4892" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4892-score" class="post-score" title="current number of votes">4</div><span id="post-4892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In 1.6 and later:</p><pre><code>frame_data *fd;
fd = frame_data_sequence_find(cfile.frames, frame_number);</code></pre><p>will get you the frame_data structure for the frame with the specified frame number. Whether that gives you all the information you need is another matter (and the frame_data structure will probably get things removed from it over time, to save memory - there's one of them for every packet in a capture).</p><p>The packet_info structure is another matter. <em>That</em> is generated when the packet is dissected, and is <em>not</em> saved (saving it would make Wireshark's memory usage even worse).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '11, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jul '11, 11:41</strong> </span></p></div></div><div id="comments-container-4892" class="comments-container"><span id="4893"></span><div id="comment-4893" class="comment"><div id="post-4893-score" class="comment-score"></div><div class="comment-text"><p>Thanks, That answer was really helpful.</p><p>How would I get the packet info, even in the most extreme case? Would I use cum_bytes and file_off to get the raw data and redissect it? I mean, the main wireshark window is able to offer packet info on any arbitrary row so that information must either be stored somewhere or recalculated right?</p></div><div id="comment-4893-info" class="comment-info"><span class="comment-age">(02 Jul '11, 12:55)</span> <span class="comment-user userinfo">Jackson Zhou</span></div></div><span id="4894"></span><div id="comment-4894" class="comment"><div id="post-4894-score" class="comment-score">1</div><div class="comment-text"><p>Yes, you'd have to get the raw data and redissect it. See, for example, cf_read_frame_r() in file.c, to read a packet from a capture given the frame_data structure, and new_packet_window() in gtk/packet_win.c, which, given a pseudo-header and pile of raw packet data (which you'd have read with cf_read_frame_r()), dissects the packet with epan_ calls and pops up a window with the packet details and hex dump.</p></div><div id="comment-4894-info" class="comment-info"><span class="comment-age">(02 Jul '11, 13:07)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="4898"></span><div id="comment-4898" class="comment"><div id="post-4898-score" class="comment-score"></div><div class="comment-text"><p>Mission accomplished. Thank you.</p></div><div id="comment-4898-info" class="comment-info"><span class="comment-age">(04 Jul '11, 02:08)</span> <span class="comment-user userinfo">Jackson Zhou</span></div></div></div><div id="comment-tools-4892" class="comment-tools"></div><div class="clear"></div><div id="comment-4892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

