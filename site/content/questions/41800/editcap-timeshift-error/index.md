+++
type = "question"
title = "Editcap timeshift error"
description = '''I am trying to shift the time of a set of pcap files by -112934478 seconds. The thing is for some files it shifts the times correctly, but others its off by an hour. I&#x27;m wondering if this is a bug or if theres possibly something I&#x27;m doing wrong. Heres a few examples of what I&#x27;m talking about. The co...'''
date = "2015-04-24T12:59:00Z"
lastmod = "2015-04-28T11:25:00Z"
weight = 41800
keywords = [ "editcap", "time_shift", "wrong_timestamps" ]
aliases = [ "/questions/41800" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Editcap timeshift error](/questions/41800/editcap-timeshift-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41800-score" class="post-score" title="current number of votes">0</div><span id="post-41800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to shift the time of a set of pcap files by -112934478 seconds. The thing is for some files it shifts the times correctly, but others its off by an hour. I'm wondering if this is a bug or if theres possibly something I'm doing wrong. Heres a few examples of what I'm talking about.</p><p>The command I'm using: /usr/sbin/editcap -F pcap -t -112934478 &lt;inputfile.pcap&gt; &lt;outputfile.pcap&gt;</p><p><strong>Example 1- Fail</strong></p><p>Original Time: 2008-09-13 7:29:29</p><p>Expected Time: 2005-02-14 4:48:11</p><p>Result from Shift: 2005-02-14 3:48:11</p><p><strong>Example 2 - Success</strong></p><p>Original Time: 2013-04-16 13:10:11</p><p>Expected Time: 2009-09-17 10:28:53</p><p>Result from Shift: 2009-09-17 10:28:53</p><p><strong>Example 3 - Fail</strong></p><p>Original Time: 2007-12-11 8:58:25</p><p>Expected Time: 2004-05-13 6:17:7</p><p>Result from Shift: 2004-05-13 7:17:7</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-editcap" rel="tag" title="see questions tagged &#39;editcap&#39;">editcap</span> <span class="post-tag tag-link-time_shift" rel="tag" title="see questions tagged &#39;time_shift&#39;">time_shift</span> <span class="post-tag tag-link-wrong_timestamps" rel="tag" title="see questions tagged &#39;wrong_timestamps&#39;">wrong_timestamps</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '15, 12:59</strong></p><img src="https://secure.gravatar.com/avatar/25594de892cd971fe92f0391a57fd962?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="drowningincode&#39;s gravatar image" /><p><span>drowningincode</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="drowningincode has no accepted answers">0%</span></p></div></div><div id="comments-container-41800" class="comments-container"></div><div id="comment-tools-41800" class="comment-tools"></div><div class="clear"></div><div id="comment-41800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41828"></span>

<div id="answer-container-41828" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41828-score" class="post-score" title="current number of votes">2</div><span id="post-41828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="drowningincode has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In what timezone are you? It looks like example 1 is going from "Summer time" to "Winter time", example 2 is going from "Summer time" to "Summer time" and example 3 is going from "Winter time" to "Summer time".</p><p>Did you take daylight saving into account?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '15, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-41828" class="comments-container"><span id="41896"></span><div id="comment-41896" class="comment"><div id="post-41896-score" class="comment-score"></div><div class="comment-text"><p>I'm in the Eastern Time Zone. Is there a way to force editcap to deal with daylight savings time or do I have to deal with it on my end.</p></div><div id="comment-41896-info" class="comment-info"><span class="comment-age">(27 Apr '15, 11:26)</span> <span class="comment-user userinfo">drowningincode</span></div></div><span id="41913"></span><div id="comment-41913" class="comment"><div id="post-41913-score" class="comment-score"></div><div class="comment-text"><p>All timestamps in the pcap[-ng] files are stored in UTC format. This means the actual timestamps in the tracefiles are agnostic to daylight saving corrections. It is when displaying the timestamps that your local timezone is used to make sure the time displayed in wireshark is the same as the time on your wall-clock (at the time).</p><p>So, editcap really does not care about daylight savings, it just follows your instruction to add/substract a certain amount of seconds. If you need the result to be an exact wall-clock time for your timezone, you need to take the daylight saving into account yourself.</p></div><div id="comment-41913-info" class="comment-info"><span class="comment-age">(28 Apr '15, 04:13)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="41915"></span><div id="comment-41915" class="comment"><div id="post-41915-score" class="comment-score"></div><div class="comment-text"><p>I wrote a blog post about packet/frame time stamps here, if anyone is interested:</p><p><a href="https://blog.packet-foo.com/2015/04/deep-dive-frame-timestamps/">https://blog.packet-foo.com/2015/04/deep-dive-frame-timestamps/</a></p></div><div id="comment-41915-info" class="comment-info"><span class="comment-age">(28 Apr '15, 06:28)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="41927"></span><div id="comment-41927" class="comment"><div id="post-41927-score" class="comment-score"></div><div class="comment-text"><p>Thank You so much, I was convinced that the problem was in editcap but I know when to admit that I was wrong. Turns out I just needed capinfos to return times in seconds since epoch instead of how it was doing it.</p></div><div id="comment-41927-info" class="comment-info"><span class="comment-age">(28 Apr '15, 11:25)</span> <span class="comment-user userinfo">drowningincode</span></div></div></div><div id="comment-tools-41828" class="comment-tools"></div><div class="clear"></div><div id="comment-41828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41826"></span>

<div id="answer-container-41826" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41826-score" class="post-score" title="current number of votes">0</div><span id="post-41826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Although the usage is a bit odd, I guess this should work. It would be worth <a href="https://bugs.wireshark.org">a bug report</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '15, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41826" class="comments-container"><span id="41897"></span><div id="comment-41897" class="comment"><div id="post-41897-score" class="comment-score"></div><div class="comment-text"><p>What is odd about the usage?</p></div><div id="comment-41897-info" class="comment-info"><span class="comment-age">(27 Apr '15, 11:27)</span> <span class="comment-user userinfo">drowningincode</span></div></div><span id="41924"></span><div id="comment-41924" class="comment"><div id="post-41924-score" class="comment-score"></div><div class="comment-text"><p>Offsetting timestamps a few years(!). I could imagine a couple of minutes in case of comparing captures from platforms with misaligned clocks.</p><p>Anyway, Sake got you on the right track I think.</p></div><div id="comment-41924-info" class="comment-info"><span class="comment-age">(28 Apr '15, 09:12)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-41826" class="comment-tools"></div><div class="clear"></div><div id="comment-41826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

