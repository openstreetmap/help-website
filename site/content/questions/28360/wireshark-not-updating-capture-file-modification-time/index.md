+++
type = "question"
title = "wireshark not updating capture file modification time"
description = '''I have just installed Wireshark 1.10.1 on Windows XP (Home) SP3. Previously I have been using Ethereal and during live capturing the capture file modification timestamp changed in every time the capture file was written to. This does not appear to happen with Wireshark. The size of the file changes,...'''
date = "2013-12-24T02:03:00Z"
lastmod = "2013-12-25T08:22:00Z"
weight = 28360
keywords = [ "capture-file", "wireshark" ]
aliases = [ "/questions/28360" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark not updating capture file modification time](/questions/28360/wireshark-not-updating-capture-file-modification-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28360-score" class="post-score" title="current number of votes">0</div><span id="post-28360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have just installed Wireshark 1.10.1 on Windows XP (Home) SP3. Previously I have been using Ethereal and during live capturing the capture file modification timestamp changed in every time the capture file was written to. This does not appear to happen with Wireshark. The size of the file changes, but not its modification timestamp, which I make reference to in a bespoke application to test that it hasn't frozen/aborted. Is there a way to force Wireshark to update the capture file modification timestamp?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-file" rel="tag" title="see questions tagged &#39;capture-file&#39;">capture-file</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Dec '13, 02:03</strong></p><img src="https://secure.gravatar.com/avatar/bf30570c015382d7f482135a7b40f0f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gargoil666uk&#39;s gravatar image" /><p><span>gargoil666uk</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gargoil666uk has no accepted answers">0%</span></p></div></div><div id="comments-container-28360" class="comments-container"></div><div id="comment-tools-28360" class="comment-tools"></div><div class="clear"></div><div id="comment-28360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28363"></span>

<div id="answer-container-28363" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28363-score" class="post-score" title="current number of votes">0</div><span id="post-28363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On my machine (Win7 Pro x64) it looks like the modified timestamp is only updated when the capture is stopped. It doesn't seem to update the modified timestamp while writing packets, which I agree could be useful. I'm just not sure if this is anything dumpcap can be made responsible for, because it might be an OS issue.</p><p>But if you say it worked with Ethereal on the same machine and the same OS then you could open a bug at <a href="http://bugs.wireshark.org"></a><a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a>, but please check the bug tracker for existing bug reports of the same kind first.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '13, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28363" class="comments-container"><span id="28368"></span><div id="comment-28368" class="comment"><div id="post-28368-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper.</p><p>I will look into it. In the mean time I shall monitor the size of capture files instead of the modification timstamps, then I will know if Wireshark is actively capturing to file.</p></div><div id="comment-28368-info" class="comment-info"><span class="comment-age">(24 Dec '13, 06:38)</span> <span class="comment-user userinfo">gargoil666uk</span></div></div></div><div id="comment-tools-28363" class="comment-tools"></div><div class="clear"></div><div id="comment-28363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28388"></span>

<div id="answer-container-28388" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28388-score" class="post-score" title="current number of votes">0</div><span id="post-28388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I <strong>can't confirm</strong> your findings on a Win XP SP3 system. On my system, the <strong>file written by dumpcap</strong> gets the new modification time every time dumpcap flushes the next couple of bytes.</p><p>Starting Powershell and 'monitoring' the last write access time stamp.</p><pre><code>PS C:\&gt; $filename = &quot;$env:TEMP\wireshark_pcap_A3940B42-C4FC-408A-992A-4950283AFE0D_20131225171845_a00628&quot;

PS C:\&gt; $ws_file = get-item $filename
PS C:\&gt; $ws_file.LastWriteTime

25. Dezember 2013 17:22:19

PS C:\&gt; $ws_file = get-item $filename
PS C:\&gt; $ws_file.LastWriteTime

25. Dezember 2013 17:22:28

PS C:\&gt; $ws_file = get-item $filename
PS C:\&gt; $ws_file.LastWriteTime

25. Dezember 2013 17:22:33</code></pre><p>Are you aware of the changes between ethereal and Wireshark? There is now a TEMP file written by dumpcap (the application that is actually capturing the packets). That TEMP file will be created in %TEMP%\ and named like in my example above. So, that's the file to monitor.</p><p>Having said that, I wonder how you started Wireshark and <strong>which</strong> file you were monitoring for changes, because the TEMP files time stamp <strong>does change</strong> on Win XP SP3, tested with Wireshark 1.11.0 and 1.10.1 !??!</p><p><strong>--UPDATE--</strong></p><p>O.K. if I start Wireshark directly with option -w (I did not in my first test), then I <strong>can confirm</strong> the described behavior. Sorry, for the confusion.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Dec '13, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Dec '13, 15:39</strong> </span></p></div></div><div id="comments-container-28388" class="comments-container"></div><div id="comment-tools-28388" class="comment-tools"></div><div class="clear"></div><div id="comment-28388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

