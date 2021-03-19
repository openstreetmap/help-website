+++
type = "question"
title = "Combining RTP streams for analysis"
description = '''I&#x27;ve run into a quirky RTP implementation that generates a new SSRC after 256 packets for any given flow, which causes Wireshark to treat each flow-&amp;gt;SSRC pair as a separate stream. i.e a 60 second call will show up as 12 unique streams under Telephony-&amp;gt;RTP-&amp;gt;Show All Streams.  This is fine f...'''
date = "2010-09-16T05:25:00Z"
lastmod = "2010-09-23T18:11:00Z"
weight = 146
keywords = [ "telephony", "audio", "export", "rtp", "voip" ]
aliases = [ "/questions/146" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Combining RTP streams for analysis](/questions/146/combining-rtp-streams-for-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-146-score" class="post-score" title="current number of votes">0</div><span id="post-146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've run into a quirky RTP implementation that generates a new SSRC after 256 packets for any given flow, which causes Wireshark to treat each flow-&gt;SSRC pair as a separate stream. i.e a 60 second call will show up as 12 unique streams under Telephony-&gt;RTP-&gt;Show All Streams.<br />
</p><p>This is fine for a quick scan of stats, but is a real pain when attempting to export a stream to .au or .raw format for audio playback. Is there a way to combine these streams into one in tshark or Wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-telephony" rel="tag" title="see questions tagged &#39;telephony&#39;">telephony</span> <span class="post-tag tag-link-audio" rel="tag" title="see questions tagged &#39;audio&#39;">audio</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '10, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/e458b44fd60b4064eb73fc42e67b3897?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grossman&#39;s gravatar image" /><p><span>grossman</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grossman has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-146" class="comments-container"></div><div id="comment-tools-146" class="comment-tools"></div><div class="clear"></div><div id="comment-146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="194"></span>

<div id="answer-container-194" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-194-score" class="post-score" title="current number of votes">2</div><span id="post-194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From RFC 1889:</p><blockquote><p>Synchronization source (SSRC): The source of a stream of RTP packets, identified by a 32-bit numeric SSRC identifier carried in the RTP header so as not to be dependent upon the network address. All packets from a synchronization source form part of the same timing and sequence number space, so a receiver groups packets by synchronization source for playback. Examples of synchronization sources include the sender of a stream of packets derived from a signal source such as a microphone or a camera, or an RTP mixer (see below). A synchronization source may change its data format, e.g., audio encoding, over time. The SSRC identifier is a randomly chosen value meant to be globally unique within a particular RTP session (see Section 8). A participant need not use the same SSRC identifier for all the RTP sessions in a multimedia session; the binding of the SSRC identifiers is provided through RTCP (see Section 6.4.1). If a participant generates multiple streams in one RTP session, for example from separate video cameras, each must be identified as a different SSRC.</p></blockquote><p>So I'd say that application isn't compliant to the RFC so in principle there is nothing to be done in Wireshark to cater for it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '10, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Sep '10, 12:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span></p></div></div><div id="comments-container-194" class="comments-container"><span id="238"></span><div id="comment-238" class="comment"><div id="post-238-score" class="comment-score"></div><div class="comment-text"><p>Believe me, I'm not going to argue that anyone or anything should bend to accommodate this RTP implementation. I was just hoping that there was some kind of clever work around that would make life a little easier.</p></div><div id="comment-238-info" class="comment-info"><span class="comment-age">(20 Sep '10, 11:04)</span> <span class="comment-user userinfo">grossman</span></div></div></div><div id="comment-tools-194" class="comment-tools"></div><div class="clear"></div><div id="comment-194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="164"></span>

<div id="answer-container-164" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-164-score" class="post-score" title="current number of votes">1</div><span id="post-164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark would need a mixer functionality to handle this properly. Currently it can't.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '10, 23:10</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-164" class="comments-container"></div><div id="comment-tools-164" class="comment-tools"></div><div class="clear"></div><div id="comment-164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="303"></span>

<div id="answer-container-303" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-303-score" class="post-score" title="current number of votes">0</div><span id="post-303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could export them all to separate files and then mix them in a program like <a href="http://www.audacity.com">Audacity</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '10, 18:11</strong></p><img src="https://secure.gravatar.com/avatar/c04f2b4fb0d88dc25e89378b9b0542b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hmmwhatsthisdo&#39;s gravatar image" /><p><span>hmmwhatsthisdo</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hmmwhatsthisdo has no accepted answers">0%</span></p></div></div><div id="comments-container-303" class="comments-container"></div><div id="comment-tools-303" class="comment-tools"></div><div class="clear"></div><div id="comment-303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

