+++
type = "question"
title = "TCP checksum validation (off) doesn&#x27;t show my messages"
description = '''Hey, I wrote a dissector, Some of my messages are not seen by the wireshark, even though the information is inside the .pcap file, and I can see a specific message that doesn&#x27;t be dissected as my protocol, as &quot;[TCP segment of a reassembled PDU]&quot;. When I turn on the option in the TCP preferences &quot;Val...'''
date = "2013-02-26T23:10:00Z"
lastmod = "2013-02-26T23:10:00Z"
weight = 18909
keywords = [ "checksum", "dissector", "wireshark", "error" ]
aliases = [ "/questions/18909" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP checksum validation (off) doesn't show my messages](/questions/18909/tcp-checksum-validation-off-doesnt-show-my-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18909-score" class="post-score" title="current number of votes">0</div><span id="post-18909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, I wrote a dissector,</p><p>Some of my messages are not seen by the wireshark, even though the information is inside the .pcap file, and I can see a specific message that doesn't be dissected as my protocol, as "<code>[TCP segment of a reassembled PDU]</code>".</p><p>When I turn on the option in the TCP preferences "<code>Validate the TCP checksum if possible.</code>", I suddenly see the message of my protocol, as my protocol - but with an error of checksum:</p><pre><code>Checksum: 0xff30 [incorrect, should be 0x1a23 (maybe caused by &quot;TCP checksum offload&quot;?)]
[Bad Checksum: True]</code></pre><p>My question is, Why can't I see messages of my protocol before checking this option, and what is this error about?</p><p>Thanks ahead...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '13, 23:10</strong></p><img src="https://secure.gravatar.com/avatar/b7ccaef1113111fc5cb2bb2a0d866a4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hudac&#39;s gravatar image" /><p><span>hudac</span><br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hudac has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Feb '13, 01:14</strong> </span></p></div></div><div id="comments-container-18909" class="comments-container"></div><div id="comment-tools-18909" class="comment-tools"></div><div class="clear"></div><div id="comment-18909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

