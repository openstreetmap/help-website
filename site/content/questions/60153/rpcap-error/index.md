+++
type = "question"
title = "RPCAP error"
description = '''During a normal TCP capture, some TCP frames are captured as RPCAP protocol, with these error details: Remote Packet Capture, Error  Version: 0  Message type: Error (1)  Error value: Network error (1)  Payload length: 32  Error: &#92;357&#92;277&#92;275&#92;0360  [Expert Info (Note/Sequence): Error: &#92;310&#92;0360&#92;000&#92;0...'''
date = "2017-03-17T07:49:00Z"
lastmod = "2017-03-19T22:08:00Z"
weight = 60153
keywords = [ "captureerror", "rpcap" ]
aliases = [ "/questions/60153" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RPCAP error](/questions/60153/rpcap-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60153-score" class="post-score" title="current number of votes">0</div><span id="post-60153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>During a normal TCP capture, some TCP frames are captured as RPCAP protocol, with these error details:</p><pre><code>Remote Packet Capture, Error
    Version: 0
    Message type: Error (1)
    Error value: Network error (1)
    Payload length: 32
    Error: \357\277\275\0360
        [Expert Info (Note/Sequence): Error: \310\0360\000\000\000\0013%CF\236\232ee\2721\002\346\326a\264\035\276\262\216\364 ^\326\346\236]
            [Error: \310\0360\000\000\000\0013%CF\236\232ee\2721\002\346\326a\264\035\276\262\216\364 ^\326\346\236]
            [Severity level: Note]
            [Group: Sequence]</code></pre><p>What's the meaning of this info? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-captureerror" rel="tag" title="see questions tagged &#39;captureerror&#39;">captureerror</span> <span class="post-tag tag-link-rpcap" rel="tag" title="see questions tagged &#39;rpcap&#39;">rpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '17, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/5cc60dc9bdb003c47d244e00ed1293f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PversusNP&#39;s gravatar image" /><p><span>PversusNP</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PversusNP has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Mar '17, 07:59</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-60153" class="comments-container"><span id="60186"></span><div id="comment-60186" class="comment"><div id="post-60186-score" class="comment-score"></div><div class="comment-text"><p>It probably means that something on the network sent a packet that looks enough like an RPCAP packet that Wireshark tried to decode it as an RPCAP packet, but that it <em>isn't</em> an RPCAP packet, and Wireshark got confused trying to interpret it as one. Unfortunately, the technique Wireshark uses to determine whether a packet is an RPCAP packet or not are relatively weak and can treat non-RPCAP packets as RPCAP packets.</p><p>Try disabling the RPCAP dissector - go to "Enabled Protocols...' In the "Analyze" menu, and turn "RPCAP" off.</p></div><div id="comment-60186-info" class="comment-info"><span class="comment-age">(19 Mar '17, 22:08)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-60153" class="comment-tools"></div><div class="clear"></div><div id="comment-60153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

