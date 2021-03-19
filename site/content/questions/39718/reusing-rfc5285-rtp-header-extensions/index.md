+++
type = "question"
title = "Reusing RFC5285 RTP header Extensions"
description = '''I have a similar issue - I&#x27;m trying to dissect an application that rides over RTP. The &quot;top-level&quot; dissector is registered to the &quot;udp.port&quot; dissector table for the specific ports in use. That dissector manually calls the RTP dissector. The payload dissector is registered to the &quot;rtp.pt&quot; dissector t...'''
date = "2015-02-09T10:53:00Z"
lastmod = "2015-02-09T10:53:00Z"
weight = 39718
keywords = [ "header", "rfc5285", "rtp", "extension" ]
aliases = [ "/questions/39718" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reusing RFC5285 RTP header Extensions](/questions/39718/reusing-rfc5285-rtp-header-extensions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39718-score" class="post-score" title="current number of votes">0</div><span id="post-39718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a similar issue - I'm trying to dissect an application that rides over RTP.</p><p>The "top-level" dissector is registered to the "udp.port" dissector table for the specific ports in use. That dissector manually calls the RTP dissector.</p><p>The payload dissector is registered to the "rtp.pt" dissector table for the specific payload types in use. This is automatically called by the RTP dissector.</p><p>However, my issue is with the header extensions.</p><p>It turns out that the specific header extensions (<code>rtp.ext.profile</code>) in use happen to overlap with the RFC 5285 2-byte range (i.e. 0x10.. - specifically, 0x1001, 0x1003, 0x1005, 0x1007, 0x1009, 0x100a, 0x100c, 0x100e).</p><p>Not sure if it is by luck or by design (the protocol definitely predates the RFC), but the extension payload matches the RFC 5825 format, so I was able to register an RTP extension dissector with the "rtp.ext.rfc5285.id" dissector table.</p><p>This mostly works. However, I would like to add some information to the tree about the RFC 5285 Application Bits (<code>rtp.ext.rfc5285.appbits</code>), which in my application are used as flags. Is there any way to do this? It would be great if I could register that information with the RTP dissector.</p><p>The first thing I tried was to register a dissector for each specific <code>rtp.ext.profile</code> with the "rtp.hdr_ext" table as suggested above, but the problem is that the RFC5285 dissector is called first. If the custom dissectors could be called first, that would address the issue.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-rfc5285" rel="tag" title="see questions tagged &#39;rfc5285&#39;">rfc5285</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-extension" rel="tag" title="see questions tagged &#39;extension&#39;">extension</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '15, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/c0e1d8fa360f3ed1d0eb32459c4eda98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chojiao&#39;s gravatar image" /><p><span>chojiao</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chojiao has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>10 Feb '15, 05:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-39718" class="comments-container"></div><div id="comment-tools-39718" class="comment-tools"></div><div class="clear"></div><div id="comment-39718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

