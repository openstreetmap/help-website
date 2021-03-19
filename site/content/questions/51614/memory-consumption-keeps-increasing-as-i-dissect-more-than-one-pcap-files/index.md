+++
type = "question"
title = "Memory consumption keeps increasing as I dissect more than one pcap files"
description = '''This might be a trivial question - My program is making use of libwireshark API, notably epan related calls to dissect pcap files. I notice that as I process one file and another, the memory consumption keeps increasing. I have code similar to the following: for each pcap file {  init_dissection(); ...'''
date = "2016-04-12T15:18:00Z"
lastmod = "2016-04-13T10:57:00Z"
weight = 51614
keywords = [ "dissector", "epan", "memory" ]
aliases = [ "/questions/51614" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Memory consumption keeps increasing as I dissect more than one pcap files](/questions/51614/memory-consumption-keeps-increasing-as-i-dissect-more-than-one-pcap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51614-score" class="post-score" title="current number of votes">0</div><span id="post-51614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This might be a trivial question - My program is making use of libwireshark API, notably epan related calls to dissect pcap files. I notice that as I process one file and another, the memory consumption keeps increasing. I have code similar to the following:</p><pre><code>for each pcap file {
    init_dissection();

    for each packet {
        frame_data_init()
        epan_dissect_init()

        frame_data_set_before_dissect()
        epan_dissect_run()
        frame_data_set_after_dissect()

        epan_dissect_cleanup()
        frame_data_cleanup()
    }

    cleanup_dissection();
}</code></pre><p>While I understand the two cleanup functions don't free up all processed data related to the current packet as future packet dissection within the same file might make use of the data, these data, however, are completely useless when I move on to the next pcap file. I can't seem to identify the function that would free these data up after I am done with a file, and I come to speculate that libwireshark is meant to process one file and exit, like tshark does - Am I right?</p><p>My current workaround is to restart my program for each pcap file to free up all used memory - ugly, however, as my program is supposed to run as a daemon... Wonder if there is a better approach..</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-epan" rel="tag" title="see questions tagged &#39;epan&#39;">epan</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '16, 15:18</strong></p><img src="https://secure.gravatar.com/avatar/29079e3047011676d290d7aeeaad3670?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="linzhao115&#39;s gravatar image" /><p><span>linzhao115</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="linzhao115 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Apr '16, 20:38</strong> </span></p></div></div><div id="comments-container-51614" class="comments-container"></div><div id="comment-tools-51614" class="comment-tools"></div><div class="clear"></div><div id="comment-51614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51616"></span>

<div id="answer-container-51616" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51616-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51616-score" class="post-score" title="current number of votes">0</div><span id="post-51616-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I come to speculate that libwireshark is meant to process one file and exit, like tshark does - Am I right?</p></blockquote><p>No. libwireshark is meant to be used by Wireshark, which lets you close files and open new files.</p><p>What you want is something such as</p><pre><code>for each pcap file {
    epan_t *epan = epan_new();
    initialize the epan in question;
    for each packet {
        frame_data_init();
        epan_dissect_init();
        frame_data_set_before_dissect();
        epan_dissect_run();
        frame_data_set_after_dissect();
        epan_dissect_cleanup();
        frame_data_cleanup();
    }
    epan_free(epan);
}</code></pre><p><code>epan_free()</code> is important here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '16, 18:20</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Apr '16, 21:37</strong> </span></p></div></div><div id="comments-container-51616" class="comments-container"><span id="51617"></span><div id="comment-51617" class="comment"><div id="post-51617-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info! But at the moment I am stuck with wireshark-1.8.12, in which epan_new()/epan_free() API aren't available yet. And I looked at the source code, epan_new() is no much more than calling init_dissection(), accordingly, epan_free() calls cleanup_dissection(), and I have already made sure to call these functions for each new file (Updated the code snippet in the question). So huh...</p></div><div id="comment-51617-info" class="comment-info"><span class="comment-age">(12 Apr '16, 20:33)</span> <span class="comment-user userinfo">linzhao115</span></div></div><span id="51619"></span><div id="comment-51619" class="comment"><div id="post-51619-score" class="comment-score"></div><div class="comment-text"><p>Then you're also stuck with whatever memory leaks wireshark 1.8.12 has. <code>init_dissection()</code> and <code>cleanup_dissection()</code> are the routines that are supposed to free up all data for the current capture file; there's nothing more you can do.</p></div><div id="comment-51619-info" class="comment-info"><span class="comment-age">(12 Apr '16, 21:43)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="51644"></span><div id="comment-51644" class="comment"><div id="post-51644-score" class="comment-score"></div><div class="comment-text"><p>Okay. Thanks!</p></div><div id="comment-51644-info" class="comment-info"><span class="comment-age">(13 Apr '16, 10:57)</span> <span class="comment-user userinfo">linzhao115</span></div></div></div><div id="comment-tools-51616" class="comment-tools"></div><div class="clear"></div><div id="comment-51616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

