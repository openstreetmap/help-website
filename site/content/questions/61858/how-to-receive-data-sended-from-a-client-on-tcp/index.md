+++
type = "question"
title = "How to receive data sended from a client on tcp"
description = '''Hi  I&#x27;m new to Wireshark so be easy with me, I have an exe application (TCP Client) that sends some source of data (packet I guess), What I want is to get this packet, in this case my TCP Server translate it like this: (in C#)  // On Receive fucntion  CryptHelper.XorData(base._bufferSegment.Buffer.A...'''
date = "2017-06-08T01:51:00Z"
lastmod = "2017-06-08T01:51:00Z"
weight = 61858
keywords = [ "c#", "#wireshark", "#packet", "#tcp", "#receiver" ]
aliases = [ "/questions/61858" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to receive data sended from a client on tcp](/questions/61858/how-to-receive-data-sended-from-a-client-on-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61858-score" class="post-score" title="current number of votes">0</div><span id="post-61858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I'm new to Wireshark so be easy with me, I have an <strong>exe application (TCP Client)</strong> that <strong>sends</strong> some source of <strong>data</strong> (packet I guess),</p><p>What I want is to <strong>get this packet</strong>, in this case my <strong>TCP Server translate</strong> it like this: (in <strong>C#</strong>)</p><pre><code>            // On Receive fucntion
            CryptHelper.XorData(base._bufferSegment.Buffer.Array, num + 3, (long) (num2 - 4), this.Locale, Locale.Any);
            PacketIn packet = new PacketIn(base._bufferSegment, 7, num2 - 8, this.IsGameServerConnection);
            PacketMgr.Instance.HandlePacket(this, packet);</code></pre><p>So how can I know <strong>what is and what type</strong> of (packet/other data) is my <strong>TCP client</strong> sending to my <strong>TCP server</strong> using <strong>Wireshark</strong> ?</p><p>Thanks in Advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-#wireshark" rel="tag" title="see questions tagged &#39;#wireshark&#39;">#wireshark</span> <span class="post-tag tag-link-#packet" rel="tag" title="see questions tagged &#39;#packet&#39;">#packet</span> <span class="post-tag tag-link-#tcp" rel="tag" title="see questions tagged &#39;#tcp&#39;">#tcp</span> <span class="post-tag tag-link-#receiver" rel="tag" title="see questions tagged &#39;#receiver&#39;">#receiver</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '17, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/94de119891699f2d75e0453019370652?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zuher%20Laith&#39;s gravatar image" /><p><span>Zuher Laith</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zuher Laith has no accepted answers">0%</span></p></div></div><div id="comments-container-61858" class="comments-container"></div><div id="comment-tools-61858" class="comment-tools"></div><div class="clear"></div><div id="comment-61858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

