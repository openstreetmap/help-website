+++
type = "question"
title = "&quot;Delta Time Displayed&quot; not showing &#x27;correct&#x27; values after re-sorting frames by clicking on any column"
description = '''I understand that the default order Wireshark is sorting frames is the frame number. Displaying either &quot;Delta Time Displayed&quot; or frame.delta_time_displayed will show the time difference between two frames based on the sorting by frame number. Unfortunately the &quot;Delta Time Displayed&quot; (∂t) is not bein...'''
date = "2012-05-29T06:22:00Z"
lastmod = "2012-06-01T01:55:00Z"
weight = 11440
keywords = [ "display-filter" ]
aliases = [ "/questions/11440" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# ["Delta Time Displayed" not showing 'correct' values after re-sorting frames by clicking on any column](/questions/11440/delta-time-displayed-not-showing-correct-values-after-re-sorting-frames-by-clicking-on-any-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11440-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I understand that the default order Wireshark is sorting frames is the frame number. Displaying either "Delta Time Displayed" or frame.delta_time_displayed will show the time difference between two frames based on the sorting by frame number.</p><p>Unfortunately the "Delta Time Displayed" (∂t) is not being calculated again after one changes the order by sorting by column.</p><p>I will give an example. I have to analyse a lot of captures with HTTP traffic and thus display the tcp.stream as a column and often sort by it to get the consecutive http.requests and http.responses. When filtering for a single stream for example with: tcp.stream == 1234 and (http.request or http.response) The value for ∂t are correctly displayed.</p><p>It starts to get problematic when not only a single stream is displayed but several. After having applied the filter: http.request or http.response with more then one stream available the frames will be displayed sorted by the frame number and ∂t will be calculated like wise. By clicking on my column tcp.stream the order of the frames will be changed but ∂t will not be calculated again based on what is shown now, thus all colouring rules based on ∂t will not work.</p><p>As far as I can see there are three possible workarounds for this:</p><ol><li>change the default sorting order to a custom value (tcp.stream) instead of frame number</li><li>somehow force ∂t to be calculated anew after one clicks on any other column for re-sorting</li><li>directly apply the sorting as a filter<br />
</li></ol><p>I haven't found any way how to do either of them and thus my question:</p><p>How can I get ∂t to show the correct values even after re-sorting the frames by clicking on any column?</p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '12, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/812f7dddfcfb20fc1990cfc3cba54c22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="teoh&#39;s gravatar image" /><p>teoh<br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="teoh has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-11440" class="comments-container"></div><div id="comment-tools-11440" class="comment-tools"></div><div class="clear"></div><div id="comment-11440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="11458"></span>

<div id="answer-container-11458" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11458-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><em>How can I get ∂t to show the correct values even after re-sorting the frames by clicking on any column?</em></p><p>Well, the delta times are showing the correct values, they're just not showing the values you want them to because currently the delta time computed is always from the previous displayed packet based on frame number, not from the previous frame based on sort order.</p><p>So, in order to have the delta time computed based on the current sort order, Wireshark would obviously need to be changed to handle this. However, there is at least one implication to this that would have to be resolved. For example, what happens to the delta times if you sort on the delta time column itself?</p><p>This feature request has been brought up before but was rejected, in part due to concerns I had about it; however, maybe it is worth implementing as long as the delta time column sort order problem can be ... um ... sorted out. Refer to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3481">bug 3481</a>, which you're free to reopen if you want.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '12, 19:38</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-11458" class="comments-container"><span id="11463"></span><div id="comment-11463" class="comment"><div id="post-11463-score" class="comment-score"></div><div class="comment-text"><p>I thanks for the answer. I am aware of the problem and agree that the bug mentioned is correctly marked as INVALID that's why I though it could be possible to implement a display-filter defining a custom sorting order and implement a change on how ∂t is computed according to that sorting order.</p></div><div id="comment-11463-info" class="comment-info"><span class="comment-age">(29 May '12, 23:03)</span> teoh</div></div><span id="11471"></span><div id="comment-11471" class="comment"><div id="post-11471-score" class="comment-score">1</div><div class="comment-text"><p>I don't think the current <code>"delta time (displayed)"</code> behavior should be changed. Rather, I was thinking that a new <code>"delta time (sorted)"</code> column could be added instead. And when sorting on the new <code>"delta time (sorted)"</code> column, it should revert to the same as how <code>"delta time (displayed)"</code> would sort ... or if possible, simply disallow sorting by that column.</p></div><div id="comment-11471-info" class="comment-info"><span class="comment-age">(30 May '12, 06:09)</span> cmaynard ♦♦</div></div><span id="11472"></span><div id="comment-11472" class="comment"><div id="post-11472-score" class="comment-score"></div><div class="comment-text"><p>sound would be perfect indeed ;)</p></div><div id="comment-11472-info" class="comment-info"><span class="comment-age">(30 May '12, 07:09)</span> teoh</div></div><span id="11479"></span><div id="comment-11479" class="comment"><div id="post-11479-score" class="comment-score"></div><div class="comment-text"><p>FYI, I reopened <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3481">bug 3481</a> ... now someone just needs to implement it. :)</p></div><div id="comment-11479-info" class="comment-info"><span class="comment-age">(30 May '12, 12:12)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-11458" class="comment-tools"></div><div class="clear"></div><div id="comment-11458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11485"></span>

<div id="answer-container-11485" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11485-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, as long as the traffic is TCP, as in your case, you can make use of "tcp.time_delta" and "tcp.time_relative" to get the timestamps for each specific TCP stream, without having to sort on tcp.stream. There i however no "tcp.time_delta_displayed" which you would need if you want to filter on http requests and responses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '12, 01:09</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-11485" class="comments-container"><span id="11518"></span><div id="comment-11518" class="comment"><div id="post-11518-score" class="comment-score"></div><div class="comment-text"><p>That's a good thought. I looked into that and found that using "tcp.time_delta" or "tcp.time_relative" won't do the trick. First of all because a server will send an [ACK] when receiving the http.request. Secondly a http.response (most likely) spans over several frames and Wireshark shows the http.response when the last frame is being received. Thus both "tcp.time_delta" and "tcp.time_relative" will not show the actual time between an http.request and an http.response but more likely between the frames in between.</p></div><div id="comment-11518-info" class="comment-info"><span class="comment-age">(01 Jun '12, 00:25)</span> teoh</div></div></div><div id="comment-tools-11485" class="comment-tools"></div><div class="clear"></div><div id="comment-11485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11521"></span>

<div id="answer-container-11521" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11521-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Secondly a http.response (most likely) spans over several frames and Wireshark shows the http.response when the last frame is being received.</p></blockquote><p>yes, that's correct. However you can circumvent this, by using the following display filter:</p><blockquote><p><code>tcp.port eq 80 and (tcp contains "GET /" or tcp contains "Server:")</code><br />
</p></blockquote><p>This will only show the packet with the GET request (or any other method you specify) and the packet of the HTTP response. It's not 100% reliable, but better than nothing ;-)</p><p>Alternatively you can filter on other HTTP request headers as well.</p><blockquote><p><code>tcp.port eq 80 and (tcp contains "Host:" or tcp contains "Server:")</code><br />
<code>tcp.port eq 80 and (tcp contains "User-Agent:" or tcp contains "Server:")</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '12, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jun '12, 01:56</p></div></div><div id="comments-container-11521" class="comments-container"></div><div id="comment-tools-11521" class="comment-tools"></div><div class="clear"></div><div id="comment-11521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

