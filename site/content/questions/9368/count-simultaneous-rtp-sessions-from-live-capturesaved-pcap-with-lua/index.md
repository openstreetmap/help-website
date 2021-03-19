+++
type = "question"
title = "count simultaneous RTP sessions from live capture/saved pcap with Lua"
description = '''Currently, I&#x27;m looking for a Lua script that would count active RTP sessions on a live tshark capture or on saved pcap files.  Right now, the only way I found is to count RTP packets per second with tshark -qz io,stat and divide by 50 to get actual number of VOIP conversations. However, this require...'''
date = "2012-03-05T12:46:00Z"
lastmod = "2012-03-05T12:46:00Z"
weight = 9368
keywords = [ "lua", "rtp" ]
aliases = [ "/questions/9368" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [count simultaneous RTP sessions from live capture/saved pcap with Lua](/questions/9368/count-simultaneous-rtp-sessions-from-live-capturesaved-pcap-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9368-score" class="post-score" title="current number of votes">0</div><span id="post-9368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Currently, I'm looking for a Lua script that would count active RTP sessions on a live tshark capture or on saved pcap files.</p><p>Right now, the only way I found is to count RTP packets per second with <code>tshark -qz io,stat</code> and divide by 50 to get actual number of VOIP conversations. However, this requires way too many steps to be realistic on a regular basis other than to troubleshoot specific time ranges.</p><p>I was thinking about creating a table/list with SSRC id, where the line count would indicate number of active sessions. Not sure this is the best way though.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '12, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/e177d49ca6cc8f53ee58cb3de1c4fbaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yul_analyzer&#39;s gravatar image" /><p><span>yul_analyzer</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yul_analyzer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Mar '12, 14:58</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-9368" class="comments-container"></div><div id="comment-tools-9368" class="comment-tools"></div><div class="clear"></div><div id="comment-9368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

