+++
type = "question"
title = "Frame is too long"
description = '''if a send more than 255 bytes, wireshark showing frame too long. I have set max size of 65536 in my code. can any one rep;y this issue?'''
date = "2017-06-08T01:59:00Z"
lastmod = "2017-06-09T10:10:00Z"
weight = 61859
keywords = [ "frame", "too", "long" ]
aliases = [ "/questions/61859" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Frame is too long](/questions/61859/frame-is-too-long)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61859-score" class="post-score" title="current number of votes">0</div><span id="post-61859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>if a send more than 255 bytes, wireshark showing frame too long. I have set max size of 65536 in my code. can any one rep;y this issue?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-too" rel="tag" title="see questions tagged &#39;too&#39;">too</span> <span class="post-tag tag-link-long" rel="tag" title="see questions tagged &#39;long&#39;">long</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '17, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/991e984ef5fcba2247597eb46f6ffaa3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="san46&#39;s gravatar image" /><p><span>san46</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="san46 has no accepted answers">0%</span></p></div></div><div id="comments-container-61859" class="comments-container"><span id="61860"></span><div id="comment-61860" class="comment"><div id="post-61860-score" class="comment-score"></div><div class="comment-text"><p>My code? What's that?</p></div><div id="comment-61860-info" class="comment-info"><span class="comment-age">(08 Jun '17, 02:56)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="61864"></span><div id="comment-61864" class="comment"><div id="post-61864-score" class="comment-score"></div><div class="comment-text"><p>What capture device do you capture from? The pipe feed must produce correct PCAP format frames.</p></div><div id="comment-61864-info" class="comment-info"><span class="comment-age">(08 Jun '17, 04:57)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="61890"></span><div id="comment-61890" class="comment"><div id="post-61890-score" class="comment-score"></div><div class="comment-text"><p>PCAP format is correct. its</p><pre><code>        uint magic_num = 0xa1b2c3d4;    // used for endianness
        short version_major = 2;        // version
        short version_minor = 4;        // version
        int thiszone = 0;               // zone (unused)
        uint sigfigs = 0;               // significant figures (unused)
        // earlier uint snaplen = 65536;
        uint snaplen = 65535;           // snapshot length (max value)
        uint network = 195;</code></pre></div><div id="comment-61890-info" class="comment-info"><span class="comment-age">(09 Jun '17, 01:47)</span> <span class="comment-user userinfo">san46</span></div></div><span id="61892"></span><div id="comment-61892" class="comment"><div id="post-61892-score" class="comment-score"></div><div class="comment-text"><p>That is the file header, now you have to look at the individual frame headers. It must adhere to <a href="https://wiki.wireshark.org/Development/LibpcapFileFormat">this format</a></p></div><div id="comment-61892-info" class="comment-info"><span class="comment-age">(09 Jun '17, 02:12)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="61894"></span><div id="comment-61894" class="comment"><div id="post-61894-score" class="comment-score"></div><div class="comment-text"><p>packet header is also fine. I have attached my file to your email . pls check &amp; reply</p></div><div id="comment-61894-info" class="comment-info"><span class="comment-age">(09 Jun '17, 02:33)</span> <span class="comment-user userinfo">san46</span></div></div><span id="61898"></span><div id="comment-61898" class="comment not_top_scorer"><div id="post-61898-score" class="comment-score"></div><div class="comment-text"><p>Well, I don't C# so there's little point in sending me code. Post a link to a pcap file and we'll see what we can do.</p></div><div id="comment-61898-info" class="comment-info"><span class="comment-age">(09 Jun '17, 04:12)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="61908"></span><div id="comment-61908" class="comment not_top_scorer"><div id="post-61908-score" class="comment-score"></div><div class="comment-text"><p>Hi Jaap,</p><p>Thanks for reply. Bug fixed. it was issue in data type for a variable which i defined to compare with packet length.</p></div><div id="comment-61908-info" class="comment-info"><span class="comment-age">(09 Jun '17, 06:38)</span> <span class="comment-user userinfo">san46</span></div></div></div><div id="comment-tools-61859" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-61859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61916"></span>

<div id="answer-container-61916" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61916-score" class="post-score" title="current number of votes">0</div><span id="post-61916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In the end, buggy code generating the pcap stream triggered this defence in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '17, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61916" class="comments-container"></div><div id="comment-tools-61916" class="comment-tools"></div><div class="clear"></div><div id="comment-61916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

