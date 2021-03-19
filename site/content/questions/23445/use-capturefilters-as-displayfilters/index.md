+++
type = "question"
title = "Use CaptureFilters as DisplayFilters"
description = '''I&#x27;m wondering if there&#x27;s a way in Wireshark to use Capture Filters in the Display Filters input box? I need this because I want to check a Capture Filter on a known PCAP before applying it somewhere else. Is this at all possible (even through a plugin) ?'''
date = "2013-07-30T06:32:00Z"
lastmod = "2013-07-31T10:40:00Z"
weight = 23445
keywords = [ "capture-filter" ]
aliases = [ "/questions/23445" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Use CaptureFilters as DisplayFilters](/questions/23445/use-capturefilters-as-displayfilters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23445-score" class="post-score" title="current number of votes">0</div><span id="post-23445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm wondering if there's a way in Wireshark to use Capture Filters in the Display Filters input box? I need this because I want to check a Capture Filter on a known PCAP before applying it somewhere else.</p><p>Is this at all possible (even through a plugin) ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '13, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/b0dde5c8166df4abcd25c45d6b47c5c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Astraa&#39;s gravatar image" /><p><span>Astraa</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Astraa has no accepted answers">0%</span></p></div></div><div id="comments-container-23445" class="comments-container"></div><div id="comment-tools-23445" class="comment-tools"></div><div class="clear"></div><div id="comment-23445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23450"></span>

<div id="answer-container-23450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23450-score" class="post-score" title="current number of votes">2</div><span id="post-23450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I want to check a Capture Filter on a known PCAP before applying it somewhere else</p></blockquote><p>If by "check" you mean "make sure it filters the packets I expect it to filter", try running tcpdump on it; tcpdump uses libpcap filters. You could do <code>tcpdump -r {input_file} {filter}</code> and see whether it prints the packets you want, or <code>tcpdump -r {input_file} -w {output_file} {filter}</code> and then read <code>{output_file}</code> with Wireshark.</p><p>There's no way to use capture filters as display filters in Wireshark, and there's no "plugin point" that would make it possible for a plugin to do so.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '13, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23450" class="comments-container"><span id="23465"></span><div id="comment-23465" class="comment"><div id="post-23465-score" class="comment-score"></div><div class="comment-text"><p>I often go the tcpdump route myself.</p><p>However, it would be a nice feature to be able to filter with a capture (BPF) filter in Wireshark, as there are some things a BPF filter can do that a display filter can't do.</p></div><div id="comment-23465-info" class="comment-info"><span class="comment-age">(31 Jul '13, 01:41)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="23487"></span><div id="comment-23487" class="comment"><div id="post-23487-score" class="comment-score"></div><div class="comment-text"><p>Or use <a href="http://www.winpcap.org/windump/default.htm">WinDump</a> if you're on Windows.</p><p>And if anyone ever decides to try to resolve <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1814">bug 1814</a>, then it might be possible in the future to do something like:</p><ul><li>Windows: <code>type file.pcap | tshark.exe -i - -f "capture filter"</code></li><li>*nix: <code>cat file.pcap | tshark -i - -f "capture filter"</code></li></ul></div><div id="comment-23487-info" class="comment-info"><span class="comment-age">(31 Jul '13, 10:40)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-23450" class="comment-tools"></div><div class="clear"></div><div id="comment-23450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

