+++
type = "question"
title = "Special handling of an &#x27;FT_ABSOLUTE_TIME&#x27; field"
description = '''Hello guys, There is a question about FT_ABSOLUTE_TIME you know, from the README.developer file, the FT_ABSOLUTE_TIME described as below:   An absolute time from some fixed point in time, displayed as the date, followed by the time, as  hours, minutes, and seconds with 9 digits after the decimal poi...'''
date = "2011-10-09T07:42:00Z"
lastmod = "2011-10-11T17:40:00Z"
weight = 6811
keywords = [ "development", "ft_absolute_time" ]
aliases = [ "/questions/6811" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Special handling of an 'FT\_ABSOLUTE\_TIME' field](/questions/6811/special-handling-of-an-ft_absolute_time-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6811-score" class="post-score" title="current number of votes">0</div><span id="post-6811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys,</p><p>There is a question about <code>FT_ABSOLUTE_TIME</code> you know, from the README.developer file, the <code>FT_ABSOLUTE_TIME</code> described as below:</p><hr /><blockquote><p>An absolute time from some fixed point in time, displayed as the date, followed by the time, as hours, minutes, and seconds with 9 digits after the decimal point.</p></blockquote><hr /><p>But I just want only the last 30 bits of the last four bytes used for the nsecs, the first 2 bits of the last four bytes used for other purposes. Any ideas?</p><p>Best Regards! Sam</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-ft_absolute_time" rel="tag" title="see questions tagged &#39;ft_absolute_time&#39;">ft_absolute_time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '11, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/e9d668dd28830dd8f79d4dbb56e5f2bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sam&#39;s gravatar image" /><p><span>Sam</span><br />
<span class="score" title="51 reputation points">51</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Oct '11, 14:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-6811" class="comments-container"><span id="6818"></span><div id="comment-6818" class="comment"><div id="post-6818-score" class="comment-score">1</div><div class="comment-text"><p>What is the precise format, and interpretation, of the time stamp you're dealing with? Is it 32 bits or 64 bits of seconds since some epoch (such as the UN*X epoch), 30 bits of nanoseconds, and 2 bits of other information?</p></div><div id="comment-6818-info" class="comment-info"><span class="comment-age">(09 Oct '11, 14:32)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="6819"></span><div id="comment-6819" class="comment"><div id="post-6819-score" class="comment-score"></div><div class="comment-text"><p>Yes, it is 32bits for seconds, the following 2bit for other information, the last 30bits for nanoseconds.</p></div><div id="comment-6819-info" class="comment-info"><span class="comment-age">(09 Oct '11, 18:09)</span> <span class="comment-user userinfo">Sam</span></div></div><span id="6820"></span><div id="comment-6820" class="comment"><div id="post-6820-score" class="comment-score"></div><div class="comment-text"><p>The time stamp will be read from 8 bytes in nomal state, but now the first 2 bits of the fifth byte need to be defined for special purpose, such as an flag. so how to get the correct time from the rest 62bit? exactly, the first 32bits and the last 30bits of these 8 bytes is for time stamp. how do I get it?</p></div><div id="comment-6820-info" class="comment-info"><span class="comment-age">(09 Oct '11, 23:01)</span> <span class="comment-user userinfo">Sam</span></div></div></div><div id="comment-tools-6811" class="comment-tools"></div><div class="clear"></div><div id="comment-6811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6821"></span>

<div id="answer-container-6821" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6821-score" class="post-score" title="current number of votes">3</div><span id="post-6821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sam has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>(Note: questions are not guaranteed to be answered in <em>N</em> hours, for any value of <em>N</em>.)</p><p>What you need to do is to fetch the two 32-bit fields in the time stamp yourself, use them to fill in an <code>nstime_t</code> structure, and call <code>proto_tree_add_time()</code> to add it to the protocol tree. Put the first 32 bits - the seconds value - in the <code>secs</code> field of the <code>nstime_t</code>, extract the lower 30 bits of the second 32 bits (by ANDing with <code>0x3FFFFFFF</code>) and put it into the <code>nsecs</code> field of the <code>nstime_t</code>, and do whatever is appropriate with the remaining 2 bits.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '11, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6821" class="comments-container"><span id="6829"></span><div id="comment-6829" class="comment"><div id="post-6829-score" class="comment-score"></div><div class="comment-text"><p>Thank you, Harris.</p><p>But I'm sorry, stiil have two questions:</p><p>1) How to fill them into an nstime_t structure?</p><p>2) How to fetch the two 32-bit fields in the TIME STAMP? tvb_get_ptr or tvb_get_bits32 or others?</p><p>Note: the TIME STAMP is not the original time stamp, it is just the eight bytes inserted between the payload and CRCs by other tool.</p></div><div id="comment-6829-info" class="comment-info"><span class="comment-age">(10 Oct '11, 05:50)</span> <span class="comment-user userinfo">Sam</span></div></div><span id="6833"></span><div id="comment-6833" class="comment"><div id="post-6833-score" class="comment-score">1</div><div class="comment-text"><p>The answer to "how to fill them into an nstime_t structure?" is:</p><p>Put the first 32 bits - the seconds value - in the <code>secs</code> field of the <code>nstime_t</code>, extract the lower 30 bits of the second 32 bits (by ANDing with 0x3FFFFFFF) and put it into the <code>nsecs</code> field of the <code>nstime_t</code>, and do whatever is appropriate with the remaining 2 bits.</p><p>Seriously. You have two 32-bit quantities, and an <code>nstime_t</code> structure. If the <code>nstime_t</code> were named <code>ts</code>, and the two 32-bit quantities are <code>first</code> and <code>second</code>, do:</p><pre><code>ts.secs = first;
ts.nsecs = (second &amp; 0x3FFFFFFF);</code></pre></div><div id="comment-6833-info" class="comment-info"><span class="comment-age">(10 Oct '11, 10:58)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="6834"></span><div id="comment-6834" class="comment"><div id="post-6834-score" class="comment-score">1</div><div class="comment-text"><p>As for fetching the fields, use <code>tvb_get_ntohl()</code> if they're in big-endian format, and use <code>tvb_get_letohl()</code> if they're in little-endian format.</p></div><div id="comment-6834-info" class="comment-info"><span class="comment-age">(10 Oct '11, 10:59)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="6844"></span><div id="comment-6844" class="comment"><div id="post-6844-score" class="comment-score"></div><div class="comment-text"><p>It works fine. Thanks a lot for your patient help!! Harris.</p><p>BTW, I have another question. How to use these elements(ts.secs &amp; ts.nsecs) fetched from the packet for some further analysis? such as do some time analysis like 'IO Graphs' in Wireshark statistics menu.</p><p>I am a beginner on wireshark code, who can give me a thought? thanks.</p><p>--Sam</p></div><div id="comment-6844-info" class="comment-info"><span class="comment-age">(11 Oct '11, 04:04)</span> <span class="comment-user userinfo">Sam</span></div></div><span id="6857"></span><div id="comment-6857" class="comment"><div id="post-6857-score" class="comment-score"></div><div class="comment-text"><p>Anyone can give me a hand on this? or you need more information?</p></div><div id="comment-6857-info" class="comment-info"><span class="comment-age">(11 Oct '11, 17:40)</span> <span class="comment-user userinfo">Sam</span></div></div></div><div id="comment-tools-6821" class="comment-tools"></div><div class="clear"></div><div id="comment-6821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

