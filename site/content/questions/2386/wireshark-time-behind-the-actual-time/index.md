+++
type = "question"
title = "Wireshark time behind the actual time"
description = '''Tracing doesn&#x27;t matched the users experience in terms of watching the clock on the PC, but Wireshark is about 20 seconds behind the actual time. As the trace goes on the time of the Wireshark packets gets more behind the actual time so that by the end of a 5 minute trace it is over 60 seconds behind...'''
date = "2011-02-16T11:58:00Z"
lastmod = "2011-02-17T22:13:00Z"
weight = 2386
keywords = [ "timestamp" ]
aliases = [ "/questions/2386" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark time behind the actual time](/questions/2386/wireshark-time-behind-the-actual-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2386-score" class="post-score" title="current number of votes">0</div><span id="post-2386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Tracing doesn't matched the users experience in terms of watching the clock on the PC, but Wireshark is about 20 seconds behind the actual time. As the trace goes on the time of the Wireshark packets gets more behind the actual time so that by the end of a 5 minute trace it is over 60 seconds behind. Why is this and can this be corrected. My platform is XP pro.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '11, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/44ff40101896b0e561438995a1f1f846?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="30michael&#39;s gravatar image" /><p><span>30michael</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="30michael has no accepted answers">0%</span></p></div></div><div id="comments-container-2386" class="comments-container"><span id="2395"></span><div id="comment-2395" class="comment"><div id="post-2395-score" class="comment-score"></div><div class="comment-text"><p>What's the interface captured on?</p></div><div id="comment-2395-info" class="comment-info"><span class="comment-age">(16 Feb '11, 23:06)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="2411"></span><div id="comment-2411" class="comment"><div id="post-2411-score" class="comment-score"></div><div class="comment-text"><p>Can you confirm whether the problem is only real-time display or the actual timestamps on packets? The former might be if you have a very busy network and wireshark is trying to do name resolution on IP addresses and not keeping up. However this would not change the actually time stamp. The best way to check this is to look for NTP packets on the network which will of course have very-close to real timestamps. Also if you look inside HTTP headers of say HTTP 200 OK responses there will be Date: timestamp that can be compared with the libpcap (Wireshark) applied timestamp</p></div><div id="comment-2411-info" class="comment-info"><span class="comment-age">(17 Feb '11, 22:13)</span> <span class="comment-user userinfo">martyvis</span></div></div></div><div id="comment-tools-2386" class="comment-tools"></div><div class="clear"></div><div id="comment-2386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

