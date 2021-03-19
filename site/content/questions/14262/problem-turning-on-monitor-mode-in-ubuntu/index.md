+++
type = "question"
title = "Problem turning on monitor mode in Ubuntu"
description = '''Hi all, I am trying to turn on monitor mode in Ubuntu 12.04 and wireshark 1.6.7 I have 2 wireless  adapters 1. Ralink 2870/3070 instaled and working  2: Intel 5100 internal  ok both have white field turn on monitor mode but both gives me error ---The capabilities of the capture device &quot;ra0&quot; could no...'''
date = "2012-09-14T03:03:00Z"
lastmod = "2013-05-11T23:35:00Z"
weight = 14262
keywords = [ "3070", "mode", "2870", "ralink", "monitor" ]
aliases = [ "/questions/14262" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem turning on monitor mode in Ubuntu](/questions/14262/problem-turning-on-monitor-mode-in-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14262-score" class="post-score" title="current number of votes">2</div><span id="post-14262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I am trying to turn on monitor mode in Ubuntu 12.04 and wireshark 1.6.7 I have 2 wireless adapters 1. Ralink 2870/3070 instaled and working 2: Intel 5100 internal ok both have white field turn on monitor mode but both gives me error ---The capabilities of the capture device "ra0" could not be obtained (pcap_activate() failed: ra0: SIOCGIWPRIV: Argument list too long). Please check to make sure you have sufficient permissions, and that you have the proper interface or pipe specified.--- I think at least Ralink can be able to turn to monitor mode. Where to look for problems? I read wireshark wiki and I am more confused. Where to look for solution?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-3070" rel="tag" title="see questions tagged &#39;3070&#39;">3070</span> <span class="post-tag tag-link-mode" rel="tag" title="see questions tagged &#39;mode&#39;">mode</span> <span class="post-tag tag-link-2870" rel="tag" title="see questions tagged &#39;2870&#39;">2870</span> <span class="post-tag tag-link-ralink" rel="tag" title="see questions tagged &#39;ralink&#39;">ralink</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '12, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/f6a5ce3b4e6c75e5fb962e6d0b32700f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jarda&#39;s gravatar image" /><p><span>Jarda</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jarda has no accepted answers">0%</span></p></div></div><div id="comments-container-14262" class="comments-container"><span id="14317"></span><div id="comment-14317" class="comment"><div id="post-14317-score" class="comment-score"></div><div class="comment-text"><p>I have the exact same issue with the same version of Ubuntu and wireshark. However I am using a Netgear N300 USB wireless adapter.</p></div><div id="comment-14317-info" class="comment-info"><span class="comment-age">(17 Sep '12, 01:30)</span> <span class="comment-user userinfo">JWinTX</span></div></div><span id="21095"></span><div id="comment-21095" class="comment"><div id="post-21095-score" class="comment-score"></div><div class="comment-text"><p>I am also having the same problem with Ubuntu 12.04, wireshark and a Netgear N900 (using rt3573sta driver). pcap_activate() failed: ra0: SIOCGIWPRIV: Argument list too long. The rt3573sta driver is loaded fine and monitor mode works as well. I also already have updated my wireless-tools to the latest (29) and can send iwpriv (set and stat) from the terminal.</p></div><div id="comment-21095-info" class="comment-info"><span class="comment-age">(11 May '13, 23:35)</span> <span class="comment-user userinfo">hickup</span></div></div></div><div id="comment-tools-14262" class="comment-tools"></div><div class="clear"></div><div id="comment-14262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

