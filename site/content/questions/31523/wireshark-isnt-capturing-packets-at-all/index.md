+++
type = "question"
title = "Wireshark isn&#x27;t capturing packets at all"
description = '''Wireshark isn&#x27;t capturing packets at all, I select my network and I see it is sending/receiving packets but I cant view them. They arn&#x27;t &quot;Displayed&quot;.  http://prntscr.com/36ymbr  http://prntscr.com/36ymig '''
date = "2014-04-04T10:54:00Z"
lastmod = "2014-04-05T14:33:00Z"
weight = 31523
keywords = [ "broken", "packet-display", "wireshark" ]
aliases = [ "/questions/31523" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark isn't capturing packets at all](/questions/31523/wireshark-isnt-capturing-packets-at-all)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31523-score" class="post-score" title="current number of votes">0</div><span id="post-31523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark isn't capturing packets at all, I select my network and I see it is sending/receiving packets but I cant view them. They arn't "Displayed". <a href="http://prntscr.com/36ymbr">http://prntscr.com/36ymbr</a><br />
<a href="http://prntscr.com/36ymig">http://prntscr.com/36ymig</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broken" rel="tag" title="see questions tagged &#39;broken&#39;">broken</span> <span class="post-tag tag-link-packet-display" rel="tag" title="see questions tagged &#39;packet-display&#39;">packet-display</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '14, 10:54</strong></p><img src="https://secure.gravatar.com/avatar/79a0461e1967b4768ed69f7271c45a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SMBAHB&#39;s gravatar image" /><p><span>SMBAHB</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SMBAHB has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-31523" class="comments-container"><span id="31543"></span><div id="comment-31543" class="comment"><div id="post-31543-score" class="comment-score"></div><div class="comment-text"><p>Did you enable promiscuous mode or monitor mode? Try again with both disabled.</p></div><div id="comment-31543-info" class="comment-info"><span class="comment-age">(05 Apr '14, 04:31)</span> <span class="comment-user userinfo">Roland</span></div></div><span id="31556"></span><div id="comment-31556" class="comment"><div id="post-31556-score" class="comment-score"></div><div class="comment-text"><p>Monitor mode can't even be <em>enabled</em> on Windows.</p><p>Promiscuous mode can, but often causes capture not to work <em>at all</em> on Wi-Fi interfaces; the second image indicates that the capture is being done on a Wi-Fi interface.</p><p>So, yes, they should turn off promiscuous mode. That means you will only see traffic going to and from your machine, but, with Wireshark on Windows, that's all you get on a Wi-Fi interface unless you have an AirPcap adapter.</p></div><div id="comment-31556-info" class="comment-info"><span class="comment-age">(05 Apr '14, 14:33)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-31523" class="comment-tools"></div><div class="clear"></div><div id="comment-31523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

