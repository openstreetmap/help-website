+++
type = "question"
title = "Mate with TShark on Wireshark 2.0"
description = '''Hi all, I&#x27;ve recently upgraded to Wireshark 2, and MATE is no longer behaving as expected with tshark When it does work, it only returns the replies, not the requests. Is this a known bug, or do I have to do something different. I&#x27;ve tried using both two-pass and single pass filters, and I&#x27;m trying ...'''
date = "2015-11-25T17:30:00Z"
lastmod = "2016-02-12T08:10:00Z"
weight = 47999
keywords = [ "mate", "tshark" ]
aliases = [ "/questions/47999" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mate with TShark on Wireshark 2.0](/questions/47999/mate-with-tshark-on-wireshark-20)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47999-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I've recently upgraded to Wireshark 2, and MATE is no longer behaving as expected with tshark When it does work, it only returns the replies, not the requests.</p><p>Is this a known bug, or do I have to do something different. I've tried using both two-pass and single pass filters, and I'm trying to return all GIOP traffic which has got a duration of greater than 1 second - which works fine in the GUI.</p><p>I'm updating my question with some more data:</p><p>Hi guys The mate file is here: <a href="https://gist.github.com/scottharman/9419ce2cc4657295f6e0">https://gist.github.com/scottharman/9419ce2cc4657295f6e0</a></p><p>And I've uploaded a copy of the capture file, and the example based on captures of over a second are here: <img src="http://i.imgur.com/wzI3td8.png" alt="alt text" /></p><p>I've uploaded a sample capture with 2 queries taking over a second for illustration purposes on dropbox: <a href="https://dl.dropboxusercontent.com/u/7916275/wiresharkgiop.pcapng">Dropbox Link</a></p><p>It's possible the batch file is now wrong, but I don't think so - the batch file I typically use is in the Gist as well.</p></div><div id="question-tags" class="tags-container tags">mate tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '15, 17:30</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p>Scott Harman<br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '15, 14:39</p></div></div><div id="comments-container-47999" class="comments-container"><span id="48001"></span><div id="comment-48001" class="comment"><div id="post-48001-score" class="comment-score"></div><div class="comment-text"><p>tshark and Wireshark use the same dissection engine and plugins, so should perform the same in this respect.</p><p>You may have to post a sample capture and mate code to let folks assist you any further.</p></div><div id="comment-48001-info" class="comment-info"><span class="comment-age">(26 Nov '15, 01:18)</span> grahamb ♦</div></div></div><div id="comment-tools-47999" class="comment-tools"></div><div class="clear"></div><div id="comment-47999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50158"></span>

<div id="answer-container-50158" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50158-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It seems to work if you use <code>-Y</code> instead of <code>-R</code> and drop <code>-2</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '16, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-50158" class="comments-container"><span id="50371"></span><div id="comment-50371" class="comment"><div id="post-50371-score" class="comment-score">1</div><div class="comment-text"><p>@cmaynard, I am afraid your suggestion to use <code>-Y &lt;expression&gt;</code> instead of <code>-2 -R &lt;expression&gt;</code> only improves the situation, but does not fully solve it (leaving aside that I would still use <code>-2 -Y &lt;expression&gt;</code> as I understand the meaning of <code>-R</code> to be different from that of <code>-Y</code>).</p><p>To see what I mean (and what @Scott Harman most probably also had in mind), please run (with the mate file from the Question loaded):</p><pre><code>tshark -r wiresharkgiop.pcapng -Y giop -T fields -e giop.type -e mate.giop_req.StartTime -e mate.giop_req.Time</code></pre><p>You'll see that for the GIOP requests, the the Gop start time is shown but Gop hold time is not. This is a difference to Wireshark (GUI) where the Gop hold time is shown in the dissection of all Pdus of each Gop for which both the request and response have been captured, and it seems quite logical that tshark does not show the hold time for request frames because at the time when tshark is processing the request, the response is not available yet so the hold time is not defined yet. However, while use of <code>-2</code> seems to be an obvious remedy to that, running the command above with <code>-2</code> appended actually prevents <em>any</em> mate field from being shown.</p><p>So assuming @Scott Harman has a previous experience allowing him to state that it <em>no longer</em> behaves as expected, I'd conclude it is a regression of the 2.0.1.</p><p>The consequence is that you cannot use any "forward filtering", as (using this particular case as example) <code>-Y giop.type == 0 and mate.giop_req.Time &gt; 1</code> never evaluates to true as <code>mate.giop_req.Time</code> is not defined yet when <code>giop.type == 0</code>.</p></div><div id="comment-50371-info" class="comment-info"><span class="comment-age">(20 Feb '16, 10:56)</span> sindy</div></div></div><div id="comment-tools-50158" class="comment-tools"></div><div class="clear"></div><div id="comment-50158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

